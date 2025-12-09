"""
Market Phase Score - Final Clean Charts
========================================
Creates clean visualization of market phase scores without cycle analysis.
Generates two versions:
- All available data
- 850-day window (for focused recent analysis)
"""

import pandas as pd
import numpy as np
import logging
from pathlib import Path
from datetime import timedelta
import plotly.graph_objects as go

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_market_phase_data(window_size: str = "all") -> pd.DataFrame:
    """Load market phase score data from CSV."""
    logger.info(f"\n{'='*60}")
    logger.info(f"LOADING MARKET PHASE SCORE DATA ({window_size})")
    logger.info(f"{'='*60}")

    csv_path = Path("plots/market_phase_score.csv")
    if not csv_path.exists():
        raise FileNotFoundError(f"Market phase score CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp').sort_index()

    # Apply window if specified
    if window_size == "850":
        df = df.tail(850)
        logger.info(f"✓ Loaded 850-day window: {df.index[0]} to {df.index[-1]}")
    else:
        logger.info(f"✓ Loaded all data: {df.index[0]} to {df.index[-1]}")

    logger.info(f"  Total points: {len(df)}")

    return df


def create_clean_chart(df: pd.DataFrame, btc_price: pd.Series, window_size: str) -> go.Figure:
    """Create clean chart with dual y-axes and phase zones."""
    fig = go.Figure()

    # BTC Price on left y-axis
    fig.add_trace(
        go.Scatter(
            x=btc_price.index,
            y=btc_price.values,
            name='BTC Price',
            line=dict(color='white', width=2.5),
            yaxis='y1'
        )
    )

    # Market Phase Score on right y-axis
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['value'],
            name='Phase Score',
            line=dict(color='rgba(0, 255, 150, 1.0)', width=3),
            yaxis='y2'
        )
    )

    # Phase zones
    zones = [
        (0, 20, 'Supply Retention', 'rgba(0, 255, 0, 0.2)', 'green'),
        (80, 100, 'Supply Distribution', 'rgba(255, 0, 0, 0.2)', 'red')
    ]

    for y0, y1, label, fill_color, line_color in zones:
        # Add zone shading
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

        # Add threshold lines
        for threshold in [y0, y1]:
            if threshold == 0 or threshold == 100:
                continue
            fig.add_shape(
                type="line",
                xref="paper",
                yref="y2",
                x0=0,
                x1=1,
                y0=threshold,
                y1=threshold,
                line=dict(color=line_color, width=1.5, dash="dot"),
                opacity=0.6
            )

        # Add label
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

    # Determine current signal
    current_score = df['value'].iloc[-1]
    if current_score < 20:
        signal = "🟢 Supply Retention"
    elif current_score > 80:
        signal = "🔴 Supply Distribution"
    else:
        signal = "⚪ Mid-Cycle"

    # Extend x-axis for clean presentation
    last_date = df.index[-1]
    extended_date = last_date + timedelta(days=60)

    # Layout
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
        margin=dict(r=150),
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


def main():
    """Main execution."""
    logger.info("\n" + "="*60)
    logger.info("MARKET PHASE SCORE - FINAL CLEAN CHARTS")
    logger.info("="*60)

    # Load BTC price data
    from market_phase_score import fetch_chartinspect_data

    logger.info("\nFetching BTC price data...")
    mvrv_df = fetch_chartinspect_data(
        "https://chartinspect.com/api/charts/onchain/lth-mvrv?timeframe=all",
        "LTH-MVRV"
    )
    btc_price = mvrv_df['btc_price'].copy() if 'btc_price' in mvrv_df.columns else None

    if btc_price is None:
        logger.error("✗ Could not load BTC price data")
        return

    # Process both versions
    for window in ["all", "850"]:
        logger.info(f"\n\n{'#'*60}")
        logger.info(f"# PROCESSING {window.upper()} DATA")
        logger.info(f"{'#'*60}")

        try:
            # Load market phase data
            df = load_market_phase_data(window_size=window)

            # Create chart
            fig = create_clean_chart(df, btc_price, window)

            # Save
            output_file = f"plots/market_phase_clean_{window}.html"
            fig.write_html(
                output_file,
                config={'displayModeBar': True, 'displaylogo': False}
            )
            logger.info(f"\n✓ Chart saved: {output_file}")

            # Print current status
            current_score = df['value'].iloc[-1]
            logger.info(f"\nCurrent Score: {current_score:.1f}/100")

            if current_score < 20:
                logger.info("  🟢 SUPPLY RETENTION - LTHs holding supply")
            elif current_score > 80:
                logger.info("  🔴 SUPPLY DISTRIBUTION - LTHs distributing")
            else:
                logger.info("  ⚪ MID-CYCLE - Balanced behavior")

        except Exception as e:
            logger.error(f"✗ Error processing {window}: {e}")
            import traceback
            traceback.print_exc()

    logger.info("\n" + "="*60)
    logger.info("COMPLETE")
    logger.info("="*60)


if __name__ == "__main__":
    main()
