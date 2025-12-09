"""
Quick analysis: Phase Score vs BTC Price correlation
Shows how phase score extremes align with cycle tops/bottoms
"""

import pandas as pd
from datetime import datetime

# Load phase score data
phase_df = pd.read_csv('/Users/privacysmurf/warp/cohorts/plots/market_phase_score.csv')
phase_df['timestamp'] = pd.to_datetime(phase_df['timestamp'])
phase_df = phase_df.dropna()
phase_df.columns = ['date', 'phase_score']

# Load BTC price data
btc_df = pd.read_csv("/Users/privacysmurf/Library/Mobile Documents/com~apple~CloudDocs/Snagit/INDEX_BTCUSD, 1D_cc426.csv")
btc_df['date'] = pd.to_datetime(btc_df['time'], unit='s')
btc_df = btc_df[['date', 'close']]
btc_df.columns = ['date', 'btc_price']

# Merge on date
df = pd.merge(phase_df, btc_df, on='date', how='inner')
df = df.sort_values('date')

print("="*80)
print("PHASE SCORE vs BTC PRICE CORRELATION ANALYSIS")
print("="*80)

# Find top 10 highest phase scores (Distribution zones)
print("\n🔴 TOP 10 HIGHEST PHASE SCORES (Distribution/Tops):")
print("-" * 80)
top_scores = df.nlargest(10, 'phase_score')[['date', 'phase_score', 'btc_price']]
for idx, row in top_scores.iterrows():
    print(f"{row['date'].strftime('%Y-%m-%d')}  |  Phase: {row['phase_score']:6.2f}  |  BTC: ${row['btc_price']:>10,.2f}")

# Find top 10 lowest phase scores (Retention/Bottoms)
print("\n🟢 TOP 10 LOWEST PHASE SCORES (Retention/Bottoms):")
print("-" * 80)
bottom_scores = df.nsmallest(10, 'phase_score')[['date', 'phase_score', 'btc_price']]
for idx, row in bottom_scores.iterrows():
    print(f"{row['date'].strftime('%Y-%m-%d')}  |  Phase: {row['phase_score']:6.2f}  |  BTC: ${row['btc_price']:>10,.2f}")

# Key cycle analysis - find local maxima/minima
print("\n" + "="*80)
print("CYCLE TOP/BOTTOM ANALYSIS")
print("="*80)

# Known cycle dates to check
key_dates = {
    '2013-11-30': 'Nov 2013 Peak',
    '2015-01-14': 'Jan 2015 Bottom',
    '2017-12-17': 'Dec 2017 Peak',
    '2018-12-15': 'Dec 2018 Bottom',
    '2021-11-10': 'Nov 2021 Peak',
    '2022-11-21': 'Nov 2022 Bottom',
    '2025-01-20': 'Jan 2025 Peak (Recent)',
}

print("\nKNOWN CYCLE EXTREMES:")
print("-" * 80)
for date_str, label in key_dates.items():
    try:
        date_obj = pd.to_datetime(date_str)
        # Find closest date in data
        closest_idx = (df['date'] - date_obj).abs().idxmin()
        row = df.loc[closest_idx]
        days_diff = (row['date'] - date_obj).days

        print(f"{label:25} | {row['date'].strftime('%Y-%m-%d')} | Phase: {row['phase_score']:6.2f} | BTC: ${row['btc_price']:>10,.2f} | (±{abs(days_diff)}d)")
    except:
        print(f"{label:25} | Data not available")

# Phase score zones
print("\n" + "="*80)
print("PHASE SCORE ZONE STATISTICS")
print("="*80)

retention = df[df['phase_score'] < 20]
distribution = df[df['phase_score'] > 80]
neutral = df[(df['phase_score'] >= 20) & (df['phase_score'] <= 80)]

print(f"\n🟢 RETENTION ZONE (<20): {len(retention)} days ({len(retention)/len(df)*100:.1f}%)")
if len(retention) > 0:
    print(f"   Avg BTC Price: ${retention['btc_price'].mean():,.2f}")
    print(f"   Median BTC Price: ${retention['btc_price'].median():,.2f}")
    print(f"   Price Range: ${retention['btc_price'].min():,.2f} - ${retention['btc_price'].max():,.2f}")

print(f"\n🔴 DISTRIBUTION ZONE (>80): {len(distribution)} days ({len(distribution)/len(df)*100:.1f}%)")
if len(distribution) > 0:
    print(f"   Avg BTC Price: ${distribution['btc_price'].mean():,.2f}")
    print(f"   Median BTC Price: ${distribution['btc_price'].median():,.2f}")
    print(f"   Price Range: ${distribution['btc_price'].min():,.2f} - ${distribution['btc_price'].max():,.2f}")

print(f"\n⚪ NEUTRAL ZONE (20-80): {len(neutral)} days ({len(neutral)/len(df)*100:.1f}%)")

# Forward returns analysis
print("\n" + "="*80)
print("PREDICTIVE POWER: Forward Returns After Zone Entry")
print("="*80)

def analyze_forward_returns(zone_df, zone_name, forward_days=[90, 180, 365]):
    """Calculate forward returns after entering a zone"""
    if len(zone_df) == 0:
        print(f"\n{zone_name}: No data")
        return

    print(f"\n{zone_name}:")
    results = []

    for days in forward_days:
        returns = []
        for idx, row in zone_df.iterrows():
            entry_date = row['date']
            entry_price = row['btc_price']

            # Find price X days later
            future_date = entry_date + pd.Timedelta(days=days)
            future_data = df[df['date'] >= future_date]

            if len(future_data) > 0:
                exit_price = future_data.iloc[0]['btc_price']
                ret = ((exit_price - entry_price) / entry_price) * 100
                returns.append(ret)

        if returns:
            avg_return = sum(returns) / len(returns)
            median_return = sorted(returns)[len(returns)//2]
            positive_pct = (sum(1 for r in returns if r > 0) / len(returns)) * 100

            print(f"   {days}d forward: Avg {avg_return:+.1f}% | Median {median_return:+.1f}% | Win Rate {positive_pct:.0f}%")

# Analyze forward returns from retention zone entries
retention_entries = retention.drop_duplicates(subset=['date']).head(20)  # Sample first 20 entries
distribution_entries = distribution.drop_duplicates(subset=['date']).head(20)

analyze_forward_returns(retention_entries, "🟢 RETENTION ZONE Entry")
analyze_forward_returns(distribution_entries, "🔴 DISTRIBUTION ZONE Entry")

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
