"""
Market Phase Score - Smoothed LTH Top/Bottom Identifier

Focused implementation with noise reduction for cleaner signals.
"""

import pandas as pd
import numpy as np
import logging
from datetime import datetime, timezone
from pathlib import Path
import json
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import time
from data_cache import get_cache

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================
# DATA FETCHING
# ============================================================

def fetch_chartinspect_data(url: str, metric_name: str) -> pd.DataFrame:
    """Fetch data from ChartInspect API with caching."""
    cache = get_cache()

    # Check cache first
    cached_data = cache.get_api_data(url, ttl_hours=24)
    if cached_data is not None:
        logger.info(f"Using cached data for {metric_name}")
        if isinstance(cached_data, dict) and 'data' in cached_data:
            df = pd.DataFrame(cached_data['data'])
            # Try timestamp first, fall back to date string
            try:
                df['date'] = pd.to_datetime(df['date'], unit='ms')
            except:
                df['date'] = pd.to_datetime(df['date'])
            df.set_index('date', inplace=True)
            df.sort_index(inplace=True)
            return df

    logger.info(f"Fetching {metric_name} from ChartInspect...")

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()

            # Cache the response
            cache.set_api_data(url, data, data_type=f"chartinspect_{metric_name}", ttl_hours=24)

            if 'data' in data and isinstance(data['data'], list):
                df = pd.DataFrame(data['data'])
                # Try timestamp first, fall back to date string
                try:
                    df['date'] = pd.to_datetime(df['date'], unit='ms')
                except:
                    df['date'] = pd.to_datetime(df['date'])
                df.set_index('date', inplace=True)
                df.sort_index(inplace=True)
                logger.info(f"✓ Fetched {len(df)} records for {metric_name}")
                return df
            else:
                raise ValueError(f"Unexpected data format from {url}")

        except Exception as e:
            logger.warning(f"Attempt {attempt + 1}/{max_retries} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise

# ============================================================
# SMOOTHING FUNCTIONS
# ============================================================

def simple_moving_average(series: pd.Series, window: int) -> pd.Series:
    """Simple Moving Average smoothing."""
    return series.rolling(window=window, min_periods=1).mean()

def exponential_moving_average(series: pd.Series, span: int) -> pd.Series:
    """Exponential Moving Average smoothing (more responsive to recent changes)."""
    return series.ewm(span=span, min_periods=1).mean()

def double_exponential_smoothing(series: pd.Series, span: int) -> pd.Series:
    """Double EMA for even smoother result."""
    ema1 = series.ewm(span=span, min_periods=1).mean()
    ema2 = ema1.ewm(span=span, min_periods=1).mean()
    return ema2

def savitzky_golay_smooth(series: pd.Series, window: int = 21, poly_order: int = 3) -> pd.Series:
    """
    Savitzky-Golay filter - preserves peaks/troughs better than moving averages.
    Good for identifying extremes while smoothing noise.
    """
    from scipy.signal import savgol_filter

    # Ensure window is odd
    if window % 2 == 0:
        window += 1

    # Need at least window length of data
    if len(series) < window:
        return series

    # Handle NaN values
    valid_mask = ~series.isna()
    if valid_mask.sum() < window:
        return series

    smoothed = series.copy()
    smoothed[valid_mask] = savgol_filter(series[valid_mask], window, poly_order)

    return smoothed

# ============================================================
# MARKET PHASE SCORE
# ============================================================

def percentile_rank(series: pd.Series, window: int) -> pd.Series:
    """Calculate rolling percentile rank (0-100)."""
    def rank_pct(x):
        if len(x) < 2 or pd.isna(x.iloc[-1]):
            return np.nan
        return (x < x.iloc[-1]).sum() / len(x) * 100

    return series.rolling(window=window, min_periods=window//2).apply(rank_pct, raw=False)

def market_phase_score(
    lth_sopr: pd.Series,
    lth_mvrv: pd.Series,
    lookback_window: int = 365 * 2,
    mvrv_weight: float = 0.6,
    sopr_weight: float = 0.4,
    capitulation_threshold: float = 0.95,
    euphoria_threshold: float = 4.0
) -> pd.Series:
    """
    Market Phase Score (0-100): Actionable buy/sell signal.

    Uses percentile ranking with multipliers for extreme conditions.
    """
    # Calculate percentile ranks
    mvrv_pct = percentile_rank(lth_mvrv, lookback_window)
    sopr_pct = percentile_rank(lth_sopr, lookback_window)

    # Weighted combination
    base_score = (mvrv_pct * mvrv_weight) + (sopr_pct * sopr_weight)

    # Apply multipliers for extreme conditions
    score = base_score.copy()

    # Capitulation multiplier (reduce score during panic)
    capitulation_mask = lth_sopr < capitulation_threshold
    score[capitulation_mask] *= 0.5

    # Euphoria multiplier (amplify score during extreme greed)
    euphoria_mask = lth_mvrv > euphoria_threshold
    score[euphoria_mask] *= 1.2

    # Clip to 0-100 range
    score = score.clip(0, 100)

    return score

# ============================================================
# VISUALIZATION
# ============================================================

def create_comparison_chart(
    df: pd.DataFrame,
    btc_price: pd.Series,
    smoothing_windows: dict
) -> go.Figure:
    """
    Create multi-panel comparison chart showing:
    1. Raw vs Smoothed Market Phase Score
    2. BTC Price with phase zones
    """
    from datetime import timedelta

    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.08,
        row_heights=[0.4, 0.4, 0.2],
        subplot_titles=[
            'Market Phase Score - Smoothing Comparison',
            'Bitcoin Price (Log Scale) with Phase Zones',
            'LTH Metrics (SOPR & MVRV)'
        ]
    )

    # Color scheme for different smoothing methods
    colors = {
        'raw': 'rgba(255, 255, 255, 0.3)',
        'sma': 'rgba(0, 200, 255, 0.8)',
        'ema': 'rgba(255, 100, 255, 0.8)',
        'savgol': 'rgba(0, 255, 150, 1.0)'
    }

    # Row 1: Market Phase Score comparison
    # Raw signal (thin, transparent)
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['market_phase_raw'],
            name='Raw Signal',
            line=dict(color=colors['raw'], width=1),
            opacity=0.4
        ),
        row=1, col=1
    )

    # SMA smoothed
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['market_phase_sma'],
            name=f"SMA ({smoothing_windows['sma']}d)",
            line=dict(color=colors['sma'], width=2)
        ),
        row=1, col=1
    )

    # EMA smoothed
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['market_phase_ema'],
            name=f"EMA ({smoothing_windows['ema']}d)",
            line=dict(color=colors['ema'], width=2)
        ),
        row=1, col=1
    )

    # Savitzky-Golay (best for peaks/troughs)
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['market_phase_savgol'],
            name=f"Savitzky-Golay ({smoothing_windows['savgol']}d)",
            line=dict(color=colors['savgol'], width=2.5)
        ),
        row=1, col=1
    )

    # Phase zone lines - only extremes
    zones = [
        (0, 20, 'Supply Retention', 'green'),
        (80, 100, 'Supply Distribution', 'red')
    ]

    for lower, upper, label, color in zones:
        fig.add_hrect(
            y0=lower, y1=upper,
            fillcolor=color, opacity=0.15,
            layer="below", line_width=0,
            row=1, col=1
        )
        # Add threshold lines
        fig.add_hline(
            y=upper, line_dash="dot", line_color=color,
            opacity=0.4, row=1, col=1
        )

    # Row 2: BTC Price with colored background based on smoothed signal
    fig.add_trace(
        go.Scatter(
            x=btc_price.index,
            y=btc_price.values,
            name='BTC Price',
            line=dict(color='white', width=2),
            fill='tozeroy',
            fillcolor='rgba(255, 255, 255, 0.1)'
        ),
        row=2, col=1
    )

    # Add threshold lines to indicate zones (simpler than per-point shading)
    # This is much faster than adding 5000+ vrect shapes
    pass

    # Row 3: LTH Metrics for context
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['lth_sopr'],
            name='LTH SOPR',
            line=dict(color='cyan', width=1.5)
        ),
        row=3, col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['lth_mvrv'],
            name='LTH MVRV',
            line=dict(color='magenta', width=1.5)
        ),
        row=3, col=1
    )

    # Add SOPR=1 line
    fig.add_hline(
        y=1.0, line_dash="dash", line_color="white",
        opacity=0.3, row=3, col=1
    )

    # Layout
    fig.update_layout(
        title=dict(
            text='Market Phase Score: Smoothing Methods Comparison<br><sub>Finding the optimal signal for tops and bottoms</sub>',
            x=0.5,
            xanchor='center'
        ),
        template='plotly_dark',
        height=1200,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        ),
        hovermode='x unified'
    )

    # Update y-axes
    fig.update_yaxes(title_text="Phase Score (0-100)", row=1, col=1, gridcolor='rgba(128,128,128,0.2)')
    fig.update_yaxes(title_text="BTC Price (USD)", type="log", row=2, col=1, gridcolor='rgba(128,128,128,0.2)')
    fig.update_yaxes(title_text="LTH Metrics", row=3, col=1, gridcolor='rgba(128,128,128,0.2)')

    # Extend x-axis to add empty space on the right
    last_date = df.index[-1]
    extended_date = last_date + timedelta(days=60)

    fig.update_xaxes(
        title_text="Date",
        row=3, col=1,
        gridcolor='rgba(128,128,128,0.2)',
        range=[df.index[0], extended_date]
    )

    return fig

def create_single_smoothed_chart(
    df: pd.DataFrame,
    btc_price: pd.Series,
    smoothed_col: str,
    method_name: str
) -> go.Figure:
    """Create a clean single-view chart with dual y-axes."""
    from datetime import timedelta

    fig = go.Figure()

    # BTC Price on left y-axis (primary)
    fig.add_trace(
        go.Scatter(
            x=btc_price.index,
            y=btc_price.values,
            name='BTC Price',
            line=dict(color='white', width=2.5),
            yaxis='y1'
        )
    )

    # Market Phase Score on right y-axis (secondary)
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df[smoothed_col],
            name='Phase Score',
            line=dict(color='rgba(0, 255, 150, 1.0)', width=3),
            yaxis='y2'
        )
    )

    # Phase zone lines on right y-axis - only extremes
    zones = [
        (0, 20, 'Accumulation', 'rgba(0, 255, 0, 0.2)', 'green'),
        (80, 100, 'Distribution', 'rgba(255, 0, 0, 0.2)', 'red')
    ]

    for y0, y1, label, fill_color, line_color in [(0, 20, 'Accumulation', 'rgba(0, 255, 0, 0.2)', 'green'),
                                                     (80, 100, 'Distribution', 'rgba(255, 0, 0, 0.2)', 'red')]:
        # Add horizontal zone shading
        fig.add_shape(
            type="rect",
            xref="paper",
            yref="y2",
            x0=0,
            x1=1,
            y0=y0,
            y1=y1,
            fillcolor=fill_color,
            layer="below",
            line_width=0
        )

        # Add threshold lines at boundaries
        for threshold in [y0, y1]:
            if threshold == 0 or threshold == 100:
                continue  # Skip outer bounds
            fig.add_shape(
                type="line",
                xref="paper",
                yref="y2",
                x0=0,
                x1=1,
                y0=threshold,
                y1=threshold,
                line=dict(
                    color=line_color,
                    width=1.5,
                    dash="dot"
                ),
                opacity=0.6
            )

        # Add label annotation at midpoint
        label_y = (y0 + y1) / 2
        fig.add_annotation(
            text=label,
            xref="paper",
            yref="y2",
            x=1.01,
            y=label_y,
            showarrow=False,
            xanchor="left",
            font=dict(size=11, color=line_color, weight='bold')
        )

    # Layout
    current_score = df[smoothed_col].iloc[-1]
    if current_score < 20:
        signal = "🟢 Supply Retention"
    elif current_score > 80:
        signal = "🔴 Supply Distribution"
    else:
        signal = "⚪ Mid-Cycle"

    # Extend x-axis to add empty space on the right
    last_date = df.index[-1]
    extended_date = last_date + timedelta(days=60)

    fig.update_layout(
        title=dict(
            text=f'LTH Supply Dynamics: {current_score:.1f}/100 - {signal}',
            x=0.5,
            xanchor='center'
        ),
        template='plotly_dark',
        height=700,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.1,
            xanchor="center",
            x=0.5
        ),
        hovermode='x unified',
        margin=dict(r=150),  # Add right margin for labels
        xaxis=dict(
            title="Date",
            gridcolor='rgba(128,128,128,0.2)',
            range=[df.index[0], extended_date]
        ),
        yaxis=dict(
            title="BTC Price (USD)",
            type="log",
            side="left",
            gridcolor='rgba(128,128,128,0.2)'
        ),
        yaxis2=dict(
            side="right",
            overlaying="y",
            range=[0, 100],
            gridcolor='rgba(128,128,128,0.1)',
            showticklabels=False,
            showgrid=False,
            title=""
        )
    )

    return fig

# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    logger.info("=== Market Phase Score Analysis ===")

    # Ensure plots directory exists for all outputs
    plots_dir = Path("plots")
    plots_dir.mkdir(parents=True, exist_ok=True)

    # Fetch data
    sopr_df = fetch_chartinspect_data(
        "https://chartinspect.com/api/charts/onchain/lth-sopr",
        "LTH-SOPR"
    )

    mvrv_df = fetch_chartinspect_data(
        "https://chartinspect.com/api/charts/onchain/lth-mvrv?timeframe=all",
        "LTH-MVRV"
    )

    # Extract BTC price from MVRV data (more complete) or SOPR data
    btc_price = mvrv_df['btc_price'].copy() if 'btc_price' in mvrv_df.columns else (
        sopr_df['btc_price'].copy() if 'btc_price' in sopr_df.columns else None
    )

    if btc_price is None:
        logger.error("BTC price series not found in ChartInspect responses; cannot export phase series with price")
    else:
        # Ensure price is sorted and aligned by date index
        btc_price = btc_price.sort_index()

    # Prepare data - align on date index
    df = pd.DataFrame({
        'lth_sopr': sopr_df['lth_sopr'],
        'lth_mvrv': mvrv_df['lth_mvrv'].reindex(sopr_df.index)
    })

    # Drop rows where either metric is missing
    df = df.dropna()

    # Attach BTC price to the working DataFrame if available
    if btc_price is not None:
        df['btc_price'] = btc_price.reindex(df.index)

    logger.info(f"Data range: {df.index[0]} to {df.index[-1]}")
    logger.info(f"Total records: {len(df)}")

    # Calculate raw Market Phase Score
    logger.info("\n=== Computing Market Phase Score ===")
    df['market_phase_raw'] = market_phase_score(
        df['lth_sopr'],
        df['lth_mvrv'],
        lookback_window=365 * 2
    )

    # Apply different smoothing methods
    smoothing_windows = {
        'sma': 14,      # Simple moving average
        'ema': 14,      # Exponential moving average
        'savgol': 21    # Savitzky-Golay filter
    }

    logger.info("\n=== Applying Smoothing Methods ===")
    df['market_phase_sma'] = simple_moving_average(df['market_phase_raw'], smoothing_windows['sma'])
    df['market_phase_ema'] = exponential_moving_average(df['market_phase_raw'], smoothing_windows['ema'])
    df['market_phase_savgol'] = savitzky_golay_smooth(df['market_phase_raw'], smoothing_windows['savgol'])

    logger.info(f"✓ SMA ({smoothing_windows['sma']}d)")
    logger.info(f"✓ EMA ({smoothing_windows['ema']}d)")
    logger.info(f"✓ Savitzky-Golay ({smoothing_windows['savgol']}d)")

    # Current values
    latest = df.iloc[-1]
    logger.info("\n=== Current Values ===")
    logger.info(f"Date: {df.index[-1].strftime('%Y-%m-%d')}")
    logger.info(f"LTH SOPR: {latest['lth_sopr']:.4f}")
    logger.info(f"LTH MVRV: {latest['lth_mvrv']:.4f}")
    logger.info(f"Raw Score: {latest['market_phase_raw']:.1f}/100")
    logger.info(f"SMA Score: {latest['market_phase_sma']:.1f}/100")
    logger.info(f"EMA Score: {latest['market_phase_ema']:.1f}/100")
    logger.info(f"Savgol Score: {latest['market_phase_savgol']:.1f}/100")

    # Create visualizations
    logger.info("\n=== Creating Visualizations ===")

    # Comparison chart
    fig_comparison = create_comparison_chart(df, btc_price, smoothing_windows)
    fig_comparison.write_html(
        str(plots_dir / "market_phase_smoothing_comparison.html"),
        config={'displayModeBar': True, 'displaylogo': False}
    )
    logger.info("✓ Saved: plots/market_phase_smoothing_comparison.html")

    # Single clean chart with Savitzky-Golay (best for peaks/troughs)
    fig_clean = create_single_smoothed_chart(
        df, btc_price,
        'market_phase_savgol',
        'Savitzky-Golay'
    )
    fig_clean.write_html(
        str(plots_dir / "market_phase_clean.html"),
        config={'displayModeBar': True, 'displaylogo': False}
    )
    logger.info("✓ Saved: plots/market_phase_clean.html")

    # Print recommendation
    savgol_score = latest['market_phase_savgol']
    logger.info("\n" + "="*60)
    logger.info("RECOMMENDED SIGNAL (Savitzky-Golay Smoothed)")
    logger.info("="*60)
    logger.info(f"\nMarket Phase Score: {savgol_score:.1f}/100")

    if savgol_score < 20:
        logger.info("  🟢 SUPPLY RETENTION")
        logger.info("      → LTHs holding supply - DCA aggressively")
    elif savgol_score > 80:
        logger.info("  🔴 SUPPLY DISTRIBUTION")
        logger.info("      → LTHs distributing supply - Exit positions")
    else:
        logger.info("  ⚪ MID-CYCLE")
        logger.info("      → LTH behavior balanced - Monitor position")

    logger.info("\n" + "="*60)

    # Export CSV + JSON artifacts for frontend consumption
    logger.info("\n=== Exporting Data ===")

    plots_dir = Path("plots")
    plots_dir.mkdir(parents=True, exist_ok=True)

    # Enriched CSV: timestamp, phase_score, btc_price
    export_df = pd.DataFrame({
        'timestamp': df.index,
        'phase_score': df['market_phase_savgol']
    })

    if 'btc_price' in df.columns:
        export_df['btc_price'] = df['btc_price']
    else:
        logger.warning("btc_price column missing on df; CSV will not include price column")

    csv_path = plots_dir / 'market_phase_score.csv'
    export_df.to_csv(csv_path, index=False)
    logger.info(f"✓ Saved: {csv_path} ({len(export_df)} records)")

    # JSON phase series artifact for TradingView frontend
    try:
        logger.info("Exporting phase_series.json for frontend")

        # Format timestamps as ISO date strings with Z suffix (assume daily candles at 00:00Z)
        iso_timestamps = export_df['timestamp'].dt.strftime("%Y-%m-%dT00:00:00Z")
        series_records = export_df.copy()
        series_records['timestamp'] = iso_timestamps

        # Build current snapshot
        latest_row = series_records.iloc[-1]
        phase_score = float(latest_row['phase_score'])

        if phase_score < 20:
            zone = "retention"
        elif phase_score > 80:
            zone = "distribution"
        else:
            zone = "mid_cycle"

        current = {
            'timestamp': latest_row['timestamp'],
            'phase_score': phase_score,
            'btc_price': float(latest_row['btc_price']) if 'btc_price' in latest_row else None,
            'zone': zone,
        }

        phase_series = {
            'last_updated': datetime.now(timezone.utc).isoformat(),
            'current': current,
            'series': series_records.to_dict(orient='records'),
        }

        json_path = plots_dir / 'phase_series.json'
        with json_path.open('w') as f:
            json.dump(phase_series, f)

        logger.info(f"✓ Saved: {json_path}")
    except Exception as e:
        logger.error(f"Failed to export phase_series.json: {e}")

    logger.info("\n" + "="*60)
    logger.info("Analysis complete!")
