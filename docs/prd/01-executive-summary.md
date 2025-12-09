# Executive Summary

### Product Vision

Public Plots is a premium interactive data visualization hub that transforms proprietary Bitcoin market analysis into explorable, actionable insights for crypto investors seeking systematic timing decisions. The product addresses a fundamental limitation in how crypto analysts share insights: static images in newsletters and Discord channels prevent readers from independently validating timing signals, exploring historical patterns, or building conviction through data interaction.

The full platform vision (Phase 2+) expands to a multi-chart hub supporting diverse proprietary analyses with reusable architecture, saved view functionality, advanced member tiers, and potential expansion into institutional API access or education offerings based on validated retail demand.

**Target Market:** 1,400+ existing newsletter subscribers, focusing initially on experienced crypto investors (Marcus segment) seeking systematic frameworks to replace emotional decision-making. Phase 1.5 adds educational onboarding for first-cycle investors (Sarah segment).

**Business Model:** Premium subscription ($15-25/month) competing with Glassnode ($30-800/mo) and CryptoQuant ($49-799/mo) on signal quality and timing precision rather than metric quantity.

### MVP Scope (Phase 1)

The MVP delivers a **single Bitcoin Market Phase Chart** as proof of concept, featuring:

- **Custom phase scoring methodology** (0-100 scale) with proven track record calling major cycle inflection points (2021 top within 2 weeks at score 85, 2022 bottom at score 12)
- **Daily-automated Python data pipeline** calculating proprietary phase scores from LTH SOPR smoothing and LTH MVRV transformations
- **TradingView Lightweight Charts** for professional interactive visualization (zoom/pan, tooltips, historical exploration)
- **Netlify hosting** with edge function referer validation for Notion-only access
- **Single Notion page** with embedded chart, methodology explainer, and historical track record validation
- **Marcus-only experience** (streamlined, no educational scaffolding)
- **Informal feedback channels** (email/DM for chart requests)
- **Pipeline monitoring** (Discord notifications for daily updates/failures)

**MVP Success Criteria (3 months):**
- 50-100 paying members ($750-1,000 MRR sustainable)
- 75%+ retention after month 3
- 5-7%+ newsletter → paid conversion
- 10+ chart requests with 2+ recurring patterns

**Phase 2 Gate:** All three criteria must be met before expanding to multi-chart platform.

### What Makes This Special

**Proprietary Timing Advantage:**
Custom phase score methodology proven to call cycle inflection points that competitors miss. Historical track record demonstrates timing precision - 2021 peak called within 2 weeks at phase score 85, 2022 bottom marked at phase score 12. Bespoke index combinations (LTH SOPR smoothing, LTH MVRV transformations) unavailable on any other platform provide actionable "when to act" signals vs overwhelming metric dashboards.

**Interactive Validation Creates Trust:**
Static images require readers to trust analyst conclusions. Interactive charts enable readers to VERIFY methodology independently by exploring historical patterns themselves. This reader-driven discovery builds conviction through active exploration - readers zoom into 2021 peak, validate phase score hit 85 before top, compare to current trajectory, and generate confidence in systematic decisions vs emotional reactions.

**Technical Moat:**
Unique combination difficult to replicate: proprietary Python calculation pipelines + daily automation + TradingView professional polish + Notion publishing integration + access control infrastructure. Reusable architecture (80% shared code, 20% per-chart customization) enables rapid Phase 2 expansion while maintaining quality.

**Retail-First Validation with Expansion Optionality:**
Disciplined approach proves value with Marcus segment (months 0-6, 50-100 members), expands to Sarah segment if retention validates (months 6-18, 200-300 members), then explores strategic paths (retail scale, institutional API, education) based on organic demand signals and validated product-market fit. Revenue funds expansion rather than speculative development.
