# Project Scoping & Phased Development

## MVP Strategy & Philosophy

**MVP Approach: Revenue Validation with Platform Foundation**

Public_plots follows a **disciplined revenue-first validation strategy** where each phase must prove value before scaling investment. This is not a "build everything and hope" approach - it's systematic validation of product-market fit with clear go/no-go gates at each phase transition.

The MVP philosophy combines four strategic elements:

1. **Revenue Generation**: Launch with paying customers from day one ($750-1,500 MRR target by month 6)
2. **Value Validation**: Prove proprietary timing signals + interactive validation creates measurable confidence and systematic decision-making
3. **Platform Foundation**: Build reusable architecture (80% shared code, 20% per-chart customization) enabling rapid Phase 2 expansion
4. **Learning-Driven**: Each phase teaches what the next phase should be - no speculative development

**Why This Approach:**

- **De-risks expansion**: Retail proof required before institutional or education bets
- **Preserves optionality**: Multiple growth paths available based on what Phase 1-2 validates
- **Sustainable growth**: Revenue funds expansion rather than speculative investment
- **Disciplined execution**: Solve "how to get 50 happy members" before "how to get 500"

**Resource Requirements:**

**MVP (Phase 1):**
- **Solo operator** (analyst + developer) - you
- **Time commitment**: 40-60 hours development + 5-10 hours/week maintenance
- **Skills needed**: Python (data pipeline), JavaScript (TradingView charts), Netlify deployment, Notion configuration
- **Infrastructure costs**: <$50/month (Netlify, data APIs, monitoring)

**Growth (Phase 1.5-2):**
- Same solo operator model proven in MVP
- 20-40 hours per new chart (reusable architecture validated)
- Potential contractor for educational content creation (Phase 1.5)

**Expansion (Phase 3):**
- Contingent on Phase 2 learnings
- May require additional resources based on chosen path (retail scale vs institutional vs education)

## MVP Feature Set (Phase 1: Marcus Segment Only)

**Timeline: Months 0-6**

**Core User Journey Supported:**
Marcus Chen's journey from decision paralysis to systematic confidence - experienced crypto investor with 6-figure portfolio seeking systematic timing framework to replace emotional decision-making.

**Must-Have Capabilities:**

**1. Python Data Pipeline**
- Daily automated Bitcoin market phase calculations
- LTH SOPR smoothing and LTH MVRV transformations
- Proprietary phase scoring (0-100 scale)
- Supply retention (0-20) and distribution (80-100) zone identification
- Automated daily updates to chart data JSON

**2. TradingView Lightweight Charts Implementation**
- Professional-grade interactive visualization
- BTC price (log scale) as baseline reference series
- Phase score dynamically rescaled to visible BTC price range
- Supply zone overlays with inline labels
- Zoom/pan with crosshair and tooltips (60 FPS, <2s load time)
- Dark mode, rounded borders, modern polish

**3. Netlify Hosting + Access Control**
- Single HTML file deployment with daily automated updates
- Edge Function referer validation (Notion-only access)
- Token parameter support (built-in but not enforced in Phase 1)
- Scalable infrastructure ready for Phase 2 expansion

**4. Single Notion Page Experience**
- Embedded interactive chart (above the fold, primary focus)
- Concise methodology explainer: How phase score is calculated
- Historical track record section: 2021 top and 2022 bottom timing validation
- "Last updated: X hours ago" timestamp prominently displayed
- Visual cue pointing to chart: "👈 Zoom into 2021 peak to see how we called the top"
- Disclaimer: "Not financial advice - data visualization tool for research purposes"

**5. Marcus-Only Experience (Streamlined Access)**
- Direct access to chart and methodology
- No educational tutorials or guided onboarding
- Assumes familiarity with on-chain terminology (SOPR, MVRV, distribution phases)
- Focus on independent validation and historical pattern verification

**6. Informal Feedback Channels**
- Email/DM for chart requests and member feedback
- No formal Notion database forms or Discord integration infrastructure
- Direct communication enables rapid iteration based on early user input

**7. Pipeline Monitoring System**
- Daily pipeline success/failure notifications to Discord webhook
- Simple alerts: "✅ Phase score updated" or "⚠️ Pipeline failed"
- SMS/email escalation during critical market conditions (Phase Score <20 or >80)
- Prominent "Last updated: X hours ago" timestamp on Notion page

**Explicitly Out of Scope for MVP:**
- ❌ Educational onboarding (Sarah's tutorials, tooltips) - Phase 1.5
- ❌ Multiple chart types - Phase 2
- ❌ Multi-page Notion hub structure - Phase 2
- ❌ Saved view functionality - Phase 2
- ❌ Token-enforced per-member access - Phase 2
- ❌ Export functionality, real-time alerts, portfolio tracking - Future

**MVP Success Criteria (3-Month Evaluation):**
- 50-75 paying members (10-12% conversion from Marcus-type subscribers)
- 60%+ retention after month 3
- 60%+ active engagement rate (2+ hub checks per week)
- 60%+ first-session zoom rate (aha moment working)
- 5-10 chart requests received
- 95%+ pipeline uptime (normal conditions), 99%+ (critical conditions)

**Phase 1 → Phase 1.5 Decision:**
If MVP hits success criteria at month 3, proceed to add Sarah's educational experience. If not, diagnose and adjust before expansion.

## Post-MVP Features

**Phase 1.5: Sarah Segment Addition (Months 3-6)**

**Contingent on:** MVP success criteria met (50+ members, 60%+ retention, chart requests emerging)

**What's Added:**
- Educational onboarding path for first-cycle investors
- Guided historical explorations: 3 interactive tutorials (2021 peak, 2022 bottom, current cycle)
- Tooltip system explaining on-chain terminology (SOPR, MVRV, distribution, retention)
- Educational → Advanced toggle allowing Sarah to graduate to Marcus's streamlined view
- Progressive learning features and success milestones
- $5 trial offering to reduce commitment barrier

**Resource Requirements:**
- 30-40 hours tutorial development
- Email automation setup (trial reminders, completion triggers)
- Potential contractor for educational content writing

**Success Criteria:**
- 65%+ trial → paid conversion
- 70%+ tutorial completion rate
- Combined 200-300 members across both segments
- 70%+ overall retention maintained

**What's Still Deferred:**
- Multiple chart types (still single Bitcoin chart)
- Formal chart request infrastructure
- Saved views, advanced features

---

**Phase 2: Multi-Chart Platform (Months 6-18)**

**Phase 1 → Phase 2 Gate (ALL must be true):**
1. **Revenue threshold**: 50+ paying members = $750-1,000 MRR sustainable
2. **Retention proof**: 75%+ retention after month 3 = proven ongoing value
3. **Demand validation**: 10+ chart requests with 2+ recurring patterns = community-driven roadmap justified

**What's Added:**

**Multi-Chart Expansion:**
- 3-5 additional chart types based on validated chart request patterns from Phase 1
  - Priority determined by request volume, strategic fit, technical feasibility
  - Example candidates: Exchange netflows, MVRV Z-score divergences, Supply dynamics
- Reusable chart architecture validated (80% shared code, 20% customization per chart)

**Infrastructure Enhancements:**
- Multi-page Notion hub structure (dashboard, individual chart pages, educational content)
- Formal chart request infrastructure (Notion database forms, Discord channel integration)
- Saved view functionality (bookmark timeframes/zoom levels for quick access)
- Mobile-optimized preset zoom buttons (1W, 1M, 3M, 1Y, ALL)
- Usage analytics per chart for roadmap prioritization
- Token-enforced access control per member (tighten security)

**Advanced Member Tiers:**
- Basic: 3-5 charts access
- Pro: 10-15 charts access
- Elite: Full access to all charts
- Differential pricing validated based on usage patterns from Phase 1

**Success Criteria:**
- 200-300 paying members
- 75%+ retention maintained
- Multi-chart engagement (users accessing 3+ different charts monthly)
- Chart request patterns validating roadmap prioritization approach

**What's Still Deferred:**
- Export functionality (download data, CSV export)
- Real-time alerts/notifications
- Portfolio tracking integration
- Mobile native apps

---

**Phase 3: Strategic Expansion (18+ Months)**

**Contingent on:** Phase 1-2 learnings validate one or more expansion paths

**Path A: Retail Scale**
**Trigger:** Strong referrals + newsletter growth demonstrating organic acquisition channel

- Expand member base to 400-500+ premium members
- Add advanced features: detailed usage analytics, mobile optimization, sophisticated member tiers
- Revenue target: $6,000-10,000+ MRR from diversified retail subscription base
- Mature multi-chart platform with 10-20 proprietary analyses

**Path B: Institutional Pilot**
**Trigger:** Sophisticated users requesting API access + track record credibility validation

- Exploratory outreach to crypto hedge funds and trading firms
- Validate demand for programmatic access to phase scoring methodology
- Pilot: API endpoints for real-time phase scores and historical data
- Potential: $500-2,000/month institutional tier OR revenue share partnerships
- Validation required: Track record credibility, data reliability standards, competitive differentiation

**Path C: Education Expansion**
**Trigger:** Teaching demand emerging organically (members asking "how did you build this methodology?")

- Develop courses around systematic crypto timing and on-chain analysis
- Integrate education with interactive tool access (learn → apply → community)
- Potential offerings: "Reading Market Phases" course ($200-500), live cohorts, analyst Q&A
- Revenue: Education tier bundled with chart access ($40-50/month) OR one-time course sales
- Community growth: Private Discord for course graduates, member case studies

**Vision Philosophy:**
Rather than committing to all three paths simultaneously, walk through whichever door(s) make sense based on:
- Organic demand signals (what are members asking for?)
- Proven acquisition channels (what's actually working for growth?)
- Resource constraints (what can be executed well vs stretched thin?)
- Market validation (what will institutions/students actually pay for?)

## Risk Mitigation Strategy

**Technical Risks**

**Risk 1: TradingView chart performance degradation with 4+ years of data**
- **Likelihood:** Medium (500-700 data points is library threshold)
- **Impact:** High (kills aha moment if chart lags)
- **Mitigation:** Data decimation strategy (daily data when zoomed <6 months, weekly when viewing full history); pre-launch load testing with full historical dataset
- **Contingency:** If performance issues persist, limit historical data to 2-3 years and provide "download full historical data" option

**Risk 2: Notion iframe embedding compatibility issues**
- **Likelihood:** Medium (iframe behavior varies across browsers/devices)
- **Impact:** High (chart must work in Notion context)
- **Mitigation:** Pre-launch validation checklist testing all target browsers/devices; separate testing on iPad Notion app vs mobile Safari; referer validation testing
- **Contingency:** If Notion embedding fails, pivot to standalone web app with Notion linking (loses embedded experience but maintains functionality)

**Risk 3: Pipeline reliability during critical market conditions**
- **Likelihood:** Low-Medium (API failures, data source issues)
- **Impact:** Critical (trust destroyed if Phase Score stale during decision moments)
- **Mitigation:** Manual calculation runbook with backup data sources (CryptoQuant); tiered SLA enforcement (99% uptime during Phase Score >80 or <20); absolute limit of 2 consecutive days failed updates
- **Contingency:** Manual phase score posting to Discord/Twitter if automated pipeline fails during critical periods

---

**Market Risks**

**Risk 1: Curation hypothesis fails - users want comprehensive metrics, not single curated signal**
- **Likelihood:** Medium (challenges prevailing "more data = better" market assumption)
- **Impact:** High (invalidates core value proposition)
- **Validation:** Month 3 chart request patterns - if 30+ diverse metric requests vs 10-15 focused requests, hypothesis failing
- **Mitigation:** Target Marcus segment first (experienced investors who've tried metric overload); behavioral early warning system (monitor request patterns and sentiment)
- **Contingency:** Hybrid model - Basic tier (5 curated charts), Pro tier (15-20 charts) acknowledging some users want more breadth

**Risk 2: Interactive validation doesn't drive aha moments (users treat chart passively)**
- **Likelihood:** Low-Medium (requires effective onboarding design)
- **Impact:** Critical (interactive validation is core innovation layer)
- **Validation:** First-session zoom rate - target 60%+, red flag if <40%
- **Mitigation:** Visual cue pointing to chart; single-sentence value prop above chart; methodology explainer positioned BELOW chart (users explore first)
- **Contingency:** A/B test onboarding variations; add 30-second video demo showing how to validate 2021 peak pattern

**Risk 3: Poor conversion (<7% newsletter → paid) despite track record**
- **Likelihood:** Low-Medium (depends on positioning clarity)
- **Impact:** High (misses Phase 2 gate criteria)
- **Validation:** Month 1-3 conversion tracking; David's journey highlights "convinced but confused" friction
- **Mitigation:** Clear positioning ("Glassnode shows WHAT, we show WHEN"); competitive context section; bookmark-friendly persistent links
- **Contingency:** Phase 1.5 trial offering ($5 first month) to reduce commitment barrier; testimonial collection from early adopters

---

**Resource Risks**

**Risk 1: Solo operator bandwidth constraints (pipeline maintenance + member support + chart expansion)**
- **Likelihood:** Medium-High (as member base scales to 100+)
- **Impact:** Medium (delays Phase 2 expansion, member satisfaction issues)
- **Mitigation:** Informal feedback channels in MVP (email/DM vs formal systems); automated pipeline monitoring with clear alerts; Phase 2 expansion only after retention validates sustainable model
- **Contingency:** Hire part-time contractor for: educational content creation (Phase 1.5), member support (Phase 2), or chart development (Phase 2)

**Risk 2: Infrastructure costs exceed projections as user base scales**
- **Likelihood:** Low (Netlify CDN pricing predictable, static HTML efficient)
- **Impact:** Low (eats into margin but unlikely to kill economics)
- **Mitigation:** Cost monitoring dashboard; infrastructure costs <$50/month at 100-user scale target; CDN efficiency from static HTML delivery
- **Contingency:** If costs spike unexpectedly, optimize chart data size (reduce historical range, increase decimation) or pass costs to users via slight price increase

**Risk 3: Faster-than-expected growth (200+ members in first 6 months) strains manual processes**
- **Likelihood:** Low (would be great problem to have)
- **Impact:** Medium (manual onboarding, chart requests, support don't scale)
- **Mitigation:** Phase 2 formal infrastructure (Notion database forms, Discord integration, saved views) designed to handle 200-300 members
- **Contingency:** Accelerate Phase 2 infrastructure development; hire contractor for member support; automate common support queries

---
