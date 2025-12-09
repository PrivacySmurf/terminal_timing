

## Executive Summary

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

## Project Classification

**Technical Type:** Web App
**Domain:** Fintech (Cryptocurrency/Trading)
**Complexity:** Medium

**Classification Rationale:**

This is classified as a **web app** based on browser-based interactive visualization architecture, TradingView Lightweight Charts implementation, single HTML deployment to Netlify, and primary user interaction through web interface. While embedded in Notion, the core product is a standalone web application accessed via browser.

The **fintech (cryptocurrency/trading)** domain classification derives from the product's core function: providing timing signals for Bitcoin investment decisions, portfolio management guidance, and systematic trading framework. Users make financial decisions based on proprietary phase scoring data.

**Medium complexity** is assigned for MVP based on:

**Integration Complexity:**
- Multi-system architecture: Python pipeline → Netlify hosting → Notion embedding → Email/payment providers
- Daily automation reliability requirements with monitoring and error handling
- Four infrastructure layers that must work together: data generation, chart hosting, content platform, subscription management
- Failure mode dependencies: Pipeline failure → stale data → user trust impact

**Technical Requirements:**
- Browser compatibility matrix (Chrome, Firefox, Safari, Edge)
- Responsive design for desktop/tablet viewing
- Performance targets for chart interactivity (smooth zoom/pan)
- Data accuracy validation and error handling
- Monitoring infrastructure for daily pipeline execution

**Reduced Regulatory Burden (vs typical fintech):**
MVP leverages existing infrastructure for regulatory-heavy functions:
- **Payment processing**: Stripe/Gumroad handles PCI compliance, not built in-house
- **User authentication**: Notion manages access control, not custom auth system
- **Financial advice**: Product positioned as data visualization tool, not investment advice platform
- **Compliance focus**: Disclaimer clarity ("not financial advice"), data source transparency, calculation methodology documentation

**Future Complexity Considerations (Phase 2+):**
- Regional cryptocurrency regulations (marketing, disclaimers vary by jurisdiction)
- Data accuracy liability as user base scales
- Potential institutional access requires different compliance considerations
- Education expansion may trigger content regulation review

---

## Success Criteria

### User Success

User success for public_plots is measured through observable behavioral patterns that indicate confidence-building and systematic decision-making rather than direct portfolio performance (which we cannot measure).

**Marcus Segment (Experienced Investors) - Confidence Through Validation:**

**Primary Success Indicator:** Marcus uses the hub to make systematic timing decisions with confidence, replacing emotional reactions with data-driven execution.

**Path to Aha Moment - Leading Indicators:**

The first 60 seconds after landing on the Notion page are critical - this is where the aha moment happens or the user bounces.

- **Chart interaction within 30 seconds** of landing (indicates clear value prop and low friction)
- **Zoom action within first 2 minutes** (indicates exploration behavior activated)
- **Historical period exploration** (2020-2022 range) in first session (indicates validation seeking)
- **2021 peak examination** in first session (indicates methodology verification behavior)

**Early Warning Signal:** If <50% of users zoom within first session, there's onboarding friction preventing aha moment discovery.

**Measurable Behaviors (Post-Aha Moment):**
- **Historical pattern exploration**: Time spent examining 2021 peak and 2022 bottom periods indicates methodology validation (first-week activity)
- **Critical phase monitoring**: Increased check frequency when Phase Score approaches decision zones (75-85+) vs baseline usage
- **Strategic visit patterns**: 3-5 hub checks per week during phase transitions (not random daily checks showing anxiety)
- **Deep engagement signals**: Average time-on-chart 90+ seconds with active zoom/pan usage (not passive 10-second glances)

**"Aha Moment" Definition:** First instance of zooming into 2021 peak, validating phase score hit 85 before top, and comparing to current trajectory - realization "I can verify this methodology myself"

**Success Milestone:** Marcus makes his first systematic position adjustment (reduces 40% at Phase Score 80+) based on chart exploration rather than Twitter sentiment.

**Sarah Segment (First-Cycle Investors) - Learning Progression (Phase 1.5):**

**Primary Success Indicator:** Sarah develops systematic decision framework, moving from FOMO/panic to confidence in phase-based timing.

**Path to Aha Moment - Leading Indicators:**
- **Tutorial start within 5 minutes** of landing (indicates education path engaged)
- **Completion of Tutorial 1** (2021 peak exploration) in first session (indicates aha moment reached)
- **Return visit within 48 hours** after completing Tutorial 1 (indicates value recognized)

**Early Warning Signal:** If <60% complete Tutorial 1 in first session, educational scaffolding isn't working.

**Measurable Behaviors (Post-Aha Moment):**
- **Tutorial completion**: 70%+ complete all 3 guided historical explorations within first week
- **Tooltip usage declining**: Decreasing reliance on educational overlays over 2-3 months (learning curve)
- **Educational → Advanced toggle**: Switching to streamlined view marks confidence milestone (typically month 2-3)
- **Exploration depth evolution**: Surface-level checks initially → deeper historical pattern analysis over time
- **Time-on-chart increasing**: Early quick glances (30 seconds) → sustained analytical sessions (90+ seconds) as skills develop

**"Aha Moment" Definition:** Completing guided tutorial exploring 2021 peak, seeing phase score hit 85 before top, realizing "there WAS a signal - I can see when smart money exits"

**Success Milestone:** Sarah takes her first profit (50% position at Phase Score 80+) based on framework understanding rather than fear or hype.

**Cross-Segment Engagement Quality Indicators:**
- **Interactive feature usage**: 50%+ of paid members use zoom/pan/historical exploration monthly (separates active users from passive subscribers)
- **Time-aligned engagement**: Hub checks correlating with phase transitions (strategic usage) not random anxiety-driven checks
- **Chart request activity**: Members requesting new analyses (15-20 requests in 6 months from 50-100 members)
- **Community feedback**: Discord mentions of trading decisions influenced by phase scores
- **Referral behavior**: Users telling friends = demonstrated value worth protecting/sharing
- **Trial conversion** (Sarah): 65%+ of $5 trials convert to $20/month after experiencing value

### Business Success

**3-Month Success Criteria:**

**Conversion Performance:**
- **Overall (Marcus-only MVP)**: 10-12% newsletter → paid conversion
  - MVP targets experienced investors exclusively, so overall = Marcus conversion rate
  - Note: Some Sarah-type users may convert despite no educational scaffolding (self-motivated learners)
  - Below 7% = concerning, indicates value prop not resonating with target segment
  - Above 15% = exceptional, validates premium positioning and track record credibility

**Engagement Quality:**
- **Active user rate**: 60%+ of paid members check hub 2+ times per week
  - Below 40% = paying but not using (warning sign)
  - Above 70% = exceptional product stickiness
- **Interactive feature usage**: 50%+ use zoom/pan/historical exploration monthly
  - Below 30% = treating as static image, missing core value (onboarding friction)
- **Average time-on-chart**: 90+ seconds per session (mix of quick checks + deep exploration)
  - Below 30 seconds = passive glancing, not analytical engagement
- **First session zoom rate**: 60%+ zoom within first session (path to aha moment working)

**Retention Validation:**
- **Month 3 retention**: 60%+ (stabilized after initial 20-30% month 1→2 churn)
  - Below 60% = ongoing value not demonstrated
  - This becomes the baseline for evaluating Phase 2 readiness

**Community Validation:**
- Chart requests emerging organically via email/DM (baseline: 5+ requests in first 3 months)
- Unsolicited testimonials about decision confidence and systematic execution
- Discord activity showing members discussing timing decisions influenced by phase scores

**Revenue Momentum:**
- Trajectory toward 50+ members and $750-1,000 MRR by month 6
- Mix of monthly ($20) and annual ($180) subscriptions
- Lifetime purchases ($500) providing development cash cushion

**12-Month Success Vision:**

**Sustainable Revenue Model:**
- 75%+ retention demonstrating ongoing value creation (not one-time curiosity)
- 50-100 paying members generating $750-1,500 MRR
- Annual renewal rates: 75-80% (proves indispensable decision-support tool)

**Community-Driven Roadmap:**
- 15-20 chart requests in first 6 months proving expansion demand
- Pattern validation: 3+ requests for same chart type (not just single power user)
- Segment diversity: Requests from both Marcus AND Sarah segments

**Platform Readiness:**
- Both user segments showing value realization through behavioral metrics
- Proven engagement patterns during phase transitions (validates core value prop)
- Infrastructure tested at 50-100 user scale, ready for Phase 2 expansion

**Phase 1 → Phase 2 Gate (Minimum Viable Success):**

**Core Criteria (ALL must be true):**
1. **Revenue threshold**: 50+ paying members at $15-20/month average = $750-1,000 MRR sustainable
2. **Retention proof**: 75%+ retention after month 3 = proven ongoing value, not one-time purchase
3. **Demand validation**: 10+ chart requests with 2+ recurring patterns = community-driven roadmap justified

**Go/No-Go Decision Framework:**

**PROCEED TO PHASE 2 if:**
- All 3 core criteria met → Strong green light
- 2 of 3 criteria met with 3rd showing strong trajectory (>80% of target) → Conditional green light, set 30-day checkpoint

**PAUSE AND DIAGNOSE if:**
- 2 of 3 criteria met but 3rd stalled (<50% of target) → Identify root cause before proceeding
  - Example: 55 members + 78% retention, but only 3 chart requests → Demand unclear, survey users
- 1 of 3 criteria met → Deep diagnosis required, likely 60-90 day extension before decision

**PIVOT OR ADJUST if:**
- 0 of 3 criteria met after 6 months → Fundamental product-market fit issue
- Red flags dominating (see below) → Core value proposition not working

**Red Flags (Pivot or Adjust):**
- **Poor conversion**: <7% newsletter → paid after 3 months despite promotion (Marcus value prop not resonating)
- **Low retention**: <60% month 3 retention (users not finding ongoing value)
- **No engagement**: Members signing up but rarely checking hub (passive subscribers)
- **Low aha moment rate**: <40% zoom in first session (onboarding friction killing discovery)
- **Zero demand signals**: No chart requests or feature feedback after 90 days (no expansion appetite)
- **Wrong behavior**: Usage patterns show passive viewing, not active exploration

### Technical Success

Technical success focuses on reliable delivery of the core value proposition: daily-updated interactive charts with proprietary timing signals. Technical failures directly impact user trust and business success.

**Pipeline Reliability (Tiered by Market Criticality):**

**Normal Market Conditions (Phase Score 20-80):**
- **Uptime target**: 95% daily successful pipeline executions (~18 failures allowed per year)
- **Recovery SLA**: Failed pipelines debugged and resolved within 24 hours
- **User communication**: "Last updated: X hours ago" prominently displayed on Notion page
- **Rationale**: Most users check occasionally during neutral phases; 24-hour staleness acceptable

**Critical Market Conditions (Phase Score <20 or >80):**
- **Uptime target**: 99% daily successful pipeline executions (~4 failures allowed per year)
- **Recovery SLA**: Failed pipelines debugged and resolved within 4 hours
- **Escalation**: SMS/email alert (not just Discord) for immediate awareness
- **Manual backup**: If pipeline fails, post current phase score manually to Discord/Twitter within 2 hours
- **Rationale**: Users check frequently during decision zones; failures destroy trust at critical moments

**Absolute Limit:**
- **No more than 2 consecutive days** of failed updates during critical market conditions
- 3+ consecutive failures = emergency manual intervention required regardless of time of day

**Data Freshness & Transparency:**
- Phase score calculations updated within 24 hours when source data available
- When pipeline fails: "Last updated: X hours ago" prominently displayed, no hiding staleness
- Expectation-setting commentary: "Calculations updated daily when data available (typically within 24 hours)"

**Monitoring & Alerting:**
- Discord webhook notification for all pipeline executions: "✅ Phase score updated - BTC: $X, Score: Y"
- Discord alert on failure: "⚠️ Pipeline failed - check logs"
- SMS/email escalation if Phase Score in critical zone (<20 or >80)
- Weekly uptime report tracking normal vs critical period reliability separately

**Chart Performance:**
- **Load time**: Chart renders in <2 seconds on standard broadband (10 Mbps)
- **Interaction smoothness**: Zoom/pan operations at 60fps (no lag or stuttering)
- **Browser compatibility**: Chart functions correctly on Chrome, Firefox, Safari, Edge (latest 2 versions)
- **Responsive design**: Chart displays properly on desktop (1920x1080) and tablet (1024x768) viewports
- **Data visualization accuracy**: BTC price and phase score overlay with correct dynamic rescaling

**Data Accuracy & Validation:**
- **Calculation correctness**: Phase score calculations match manual validation 100% when spot-checked
- **Source data integrity**: LTH SOPR and LTH MVRV source data validated against Glassnode/CryptoQuant baselines monthly
- **Historical consistency**: Backtested phase scores for 2021 peak (85 at Nov 2021) and 2022 bottom (12 at Nov 2022) remain stable
- **Transparency**: Methodology documentation allows independent verification of calculation logic

**Access Control & Security:**
- **Referer validation**: Netlify edge function correctly blocks non-Notion referers (prevents public chart exposure)
- **Token infrastructure**: Token parameter support built and tested (ready for Phase 2 enforcement)
- **Notion embedding**: Chart embeds correctly in Notion pages without rendering issues
- **Payment integration**: Stripe/Gumroad subscription webhooks correctly grant/revoke Notion access

**Infrastructure Scalability:**
- **Single HTML deployment**: Daily automated updates to Netlify deploy successfully
- **CDN performance**: Netlify CDN serves chart HTML globally with <100ms latency
- **Concurrent user capacity**: Chart supports 50-100 concurrent users without performance degradation
- **Cost efficiency**: Infrastructure costs remain <$50/month at 100-user scale

**Success Milestone:** 30 consecutive days of successful pipeline execution during normal conditions with zero user-reported chart rendering issues.

### Success Interdependencies

Success dimensions are interconnected - technical excellence enables user aha moments, which drive business metrics. Understanding these causal paths helps diagnose problems faster.

**Critical Success Paths:**

**Path 1: Technical Performance → User Aha Moment → Business Conversion**
- Chart loads in <2 seconds (technical) →
- Marcus explores immediately, not bouncing (user engagement) →
- Marcus zooms into 2021 peak within 2 minutes (user aha moment) →
- Marcus converts and subscribes (business metric: 10-12% conversion)

**Failure Mode:** If chart takes 5+ seconds to load, Marcus bounces before reaching aha moment → <5% conversion → Miss Phase 2 gate

**Path 2: Pipeline Reliability → User Trust → Business Retention**
- Pipeline runs daily during critical periods (technical: 99% uptime in decision zones) →
- Marcus checks during Phase Score 78→82 transition and sees fresh data (user trust building) →
- Marcus makes systematic decision based on current score (user value realization) →
- Marcus renews subscription (business metric: 75%+ retention)

**Failure Mode:** Pipeline fails when Phase Score crosses 80 → Marcus sees stale data during decision moment → Loses trust in "real-time" positioning → Churns → <60% retention → Pivot required

**Path 3: User Onboarding → Engagement → Retention**
- Notion page clearly invites chart interaction (user onboarding) →
- 60%+ zoom within first session (user aha moment rate) →
- Users return 3-5x per week during phase transitions (user engagement pattern) →
- 60%+ active rate sustained (business metric) →
- 75%+ retention after month 3 (business metric)

**Failure Mode:** Methodology explainer overwhelms users before chart interaction → <40% zoom in first session → Users don't reach aha moment → 40% active rate → 50% retention → Miss Phase 2 gate

**Path 4: Chart Requests → Product Expansion → Revenue Growth**
- Users explore chart and think "I wish I could see [X metric]" (user engagement depth) →
- 15-20 chart requests via email/DM in 6 months (business metric: demand validation) →
- 3+ requests for same chart type (business metric: pattern validation) →
- Phase 2 expansion justified (strategic decision) →
- 3-5 new charts launched (product growth) →
- 200-300 members engaging with multi-chart platform (revenue growth)

**Failure Mode:** Users treat chart passively, no exploration depth → Zero chart requests after 90 days → No demand signal for expansion → Phase 2 not justified → Platform remains single-chart, limited growth potential

**Diagnostic Questions Using Interdependencies:**

**If at month 3 you see:**
- ✅ 95% pipeline uptime (technical)
- ❌ 45% active engagement rate (business)
- ❌ 50% retention (business)

**Trace the failure path:**
→ Pipeline uptime isn't the bottleneck
→ Check: Are users reaching aha moments? (% who zoom in first session)
→ If <50% zoom rate: **Onboarding friction issue** - Notion page needs redesign
→ If 60%+ zoom rate: **Value delivery issue** - Chart insights not actionable enough

**If at month 3 you see:**
- ✅ 65% zoom rate in first session (user aha moment)
- ✅ 70% active engagement (business)
- ❌ Pipeline failed 3 times during critical periods (technical)

**Trace the risk:**
→ Users ARE reaching aha moments and engaging
→ But pipeline failures during decision zones will erode trust
→ **Fix technical reliability BEFORE it tanks retention**
→ Implement tiered SLA and manual backup for critical periods

This causal modeling enables proactive intervention rather than reactive firefighting.

### Measurable Outcomes

**At 3 Months Post-Launch:**
- 50-75 paying members (10-12% conversion from ~600 Marcus-type newsletter subscribers)
- $1,000-1,500 MRR (mix of $20 monthly, $180 annual)
- 60%+ retention (40% who join month 1 still subscribed month 3)
- 60%+ active engagement rate (members checking 2+ times per week)
- 60%+ first-session zoom rate (onboarding working, users reaching aha moments)
- 5-10 chart requests received via email/DM
- 95%+ pipeline uptime during normal conditions, 99%+ during critical conditions
- Zero pipeline failures lasting >2 consecutive days during critical market conditions

**At 6 Months Post-Launch:**
- 50-100 paying members (Phase 2 gate threshold met or approaching)
- $750-1,500 MRR sustainable
- 70-75% retention (early adopters stabilized)
- 10-15 chart requests with 2-3 recurring patterns identified
- Ready to evaluate Phase 2 expansion using Go/No-Go framework

**At 12 Months (If Phase 2 Approved):**
- 150-250 paying members (Sarah segment added via Phase 1.5)
- $2,250-4,500 MRR from multi-segment subscription base
- 3-5 additional charts launched based on validated demand
- 75-80% annual renewal rate proving long-term value
- Infrastructure scaled to support 200+ concurrent users

## Product Scope

### MVP - Minimum Viable Product (Phase 1: Marcus Segment Only)

**Core Value Delivered:** Prove that interactive exploration of proprietary timing signals creates measurable confidence and systematic decision-making for experienced crypto investors.

**What's Included in MVP:**

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
- Supply zone overlays with inline labels ("Retention Zone 0-20", "Distribution Zone 80-100")
- Zoom/pan with crosshair and tooltips
- Dark mode, rounded borders, modern polish

**3. Netlify Hosting + Access Control**
- Single HTML file deployment with daily automated updates
- Edge Function referer validation (Notion-only access)
- Token parameter support (built-in but not enforced in Phase 1)
- Scalable infrastructure ready for Phase 2 expansion

**4. Single Notion Page Experience**
- Embedded interactive chart (above the fold, primary focus)
- Concise methodology explainer: How phase score is calculated (LTH SOPR + LTH MVRV formula)
- Historical track record section: 2021 top and 2022 bottom timing validation with specific dates/scores
- "Last updated: X hours ago" timestamp prominently displayed
- Visual cue pointing to chart: "👈 Zoom into 2021 peak to see how we called the top"
- Direct link to chart (no separate dashboard/hub structure)
- Disclaimer: "Not financial advice - data visualization tool for research purposes"

**5. Marcus-Only Experience (Streamlined Access)**
- Direct access to chart and methodology
- No educational tutorials or guided onboarding
- Assumes familiarity with on-chain terminology (SOPR, MVRV, distribution phases, long-term holders)
- Focus on independent validation and historical pattern verification

**6. Informal Feedback Channels**
- Email/DM for chart requests and member feedback
- No formal Notion database forms or Discord integration infrastructure
- Direct communication enables rapid iteration based on early user input

**7. Pipeline Monitoring System**
- Daily pipeline success/failure notifications to Discord webhook
- Simple alerts: "✅ Phase score updated - BTC: $X, Score: Y" or "⚠️ Pipeline failed - check logs"
- SMS/email escalation during critical market conditions (Phase Score <20 or >80)
- Prominent "Last updated: X hours ago" timestamp on Notion page
- Expectation-setting commentary: "Calculations updated daily when data available (typically within 24 hours)"
- Manual backup plan: Post current phase score to Discord/Twitter if automated pipeline fails during critical periods

**What's Explicitly NOT in MVP:**

**User Experience:**
- ❌ Educational onboarding for first-cycle investors (Sarah's tutorials, tooltips)
- ❌ Multi-segment user routing (Marcus vs Sarah paths)
- ❌ Guided historical explorations or progressive learning features
- ❌ Mobile-optimized preset zoom buttons
- ❌ Saved view functionality (bookmark timeframes/zoom levels)

**Product Features:**
- ❌ Multiple chart types or cryptocurrencies (ONLY Bitcoin Market Phase Chart)
- ❌ Portfolio tracking or integration
- ❌ Trade execution capabilities
- ❌ Price alerts or notifications
- ❌ Real-time alerts when Phase Score crosses thresholds
- ❌ Export functionality (download data, share views)
- ❌ Historical annotation features (mark personal trades on chart)
- ❌ Community features (leaderboards, commenting, social sharing)

**Infrastructure:**
- ❌ Token-enforced access control per member (built but not enforced)
- ❌ Multi-page Notion hub structure (separate dashboard, individual chart pages)
- ❌ Formal chart request infrastructure (Notion database forms, Discord integration)
- ❌ Usage analytics per chart for roadmap prioritization
- ❌ Advanced member tiers with differential chart access
- ❌ Custom indicator combinations beyond phase score
- ❌ Mobile native apps (iOS/Android)

**Success Threshold:** MVP is successful if it hits 3-month criteria (50+ members, 60%+ retention, 10-12% conversion) proving the core value proposition works.

### Growth Features (Post-MVP)

**Phase 1.5: Sarah Segment Addition (Months 3-6, contingent on MVP success)**

**What's Added:**
- Educational onboarding path for first-cycle investors
- Guided historical explorations: 3 interactive tutorials walking through 2021 peak, 2022 bottom, current cycle
- Tooltip system explaining on-chain terminology (SOPR, MVRV, distribution, long-term holders)
- Educational → Advanced toggle allowing Sarah to graduate to Marcus's streamlined view
- Progressive learning features and success milestones
- $5 trial offering to reduce commitment barrier for Sarah segment

**What's Still Deferred:**
- Multiple chart types (still single Bitcoin chart)
- Formal chart request infrastructure (still informal email/DM)
- Saved views, advanced features

**Success Threshold:** 65%+ trial → paid conversion, 70%+ tutorial completion, combined 200-300 members across both segments.

**Phase 2: Multi-Chart Platform (Months 6-18, contingent on Phase 1 success meeting gate criteria)**

**What's Added:**
- 3-5 additional chart types based on validated chart request patterns from Phase 1
- Multi-page Notion hub structure (dashboard, individual chart pages, educational content)
- Formal chart request infrastructure (Notion database forms, Discord channel integration)
- Saved view functionality (bookmark timeframes/zoom levels for quick access)
- Mobile-optimized preset zoom buttons (1W, 1M, 3M, 1Y, ALL)
- Usage analytics per chart for roadmap prioritization
- Token-enforced access control per member (tighten security)
- Advanced member tiers with differential chart access (Basic: 3-5 charts, Pro: 10-15 charts, Elite: full access)

**What's Still Deferred:**
- Export functionality (download data, CSV export)
- Real-time alerts/notifications
- Portfolio tracking integration
- Mobile native apps

**Success Threshold:** 200-300 paying members, 75%+ retention, multi-chart engagement (users accessing 3+ different charts monthly).

### Vision (Future - 18+ Months)

**Strategic Expansion Vectors (CONTINGENT on Phase 1-2 learnings):**

**Path A: Retail Scale (IF referrals + newsletter growth strong)**
- Expand member base through proven acquisition channels to 400-500+ premium members
- Add advanced features: detailed usage analytics, mobile optimization, sophisticated member tiers
- Revenue target: $6,000-10,000+ MRR from diversified retail subscription base
- Mature multi-chart platform with 10-20 proprietary analyses

**Path B: Institutional Pilot (IF sophisticated users request API access)**
- Exploratory outreach to crypto hedge funds and trading firms
- Validate demand for programmatic access to phase scoring methodology
- Pilot: API endpoints for real-time phase scores and historical data
- Potential: $500-2,000/month institutional tier OR revenue share partnerships
- Validation required: Track record credibility, data reliability standards, competitive differentiation

**Path C: Education Expansion (IF teaching demand emerges organically)**
- Develop courses around systematic crypto timing and on-chain analysis
- Integrate education with interactive tool access (learn → apply → community)
- Potential offerings: "Reading Market Phases" course ($200-500), live cohorts, analyst Q&A
- Revenue: Education tier bundled with chart access ($40-50/month) OR one-time course sales
- Community growth: Private Discord for course graduates, member case studies

**Vision Philosophy:**
Rather than committing to all three paths simultaneously, pursue retail validation first (Phase 1-2), then walk through whichever door(s) make sense based on:
- Organic demand signals (what are members asking for?)
- Proven acquisition channels (what's actually working for growth?)
- Resource constraints (what can be executed well vs stretched thin?)
- Market validation (what will institutions/students actually pay for?)

**Why This Approach:**
- **Disciplined execution**: Solve "how to get 50 happy members" before "how to get 500"
- **Learning-driven**: Each phase validates assumptions before scaling investment
- **Optionality preservation**: Multiple growth paths available based on what Phase 1-2 teaches
- **Risk mitigation**: Retail proof required before institutional or education bets
- **Sustainable growth**: Revenue funds expansion rather than speculative development

---

## User Journeys

### Journey 1: Marcus Chen - From Decision Paralysis to Systematic Confidence

Marcus is a 38-year-old software architect who's been in Bitcoin since 2017. His six-figure portfolio includes family wealth he manages for his parents, which adds pressure to every decision. It's Tuesday evening, and he's staring at his screens again: Analyst A says "distribution zone imminent," Analyst B says "still room to run," Analyst C's last post was three days ago. His BTC position is up 60%, but memories of riding the 2021 peak down 80% haunt him. He has 5-10 hours per week max for portfolio decisions, and right now he's paralyzed.

That night, his newsletter arrives: "Access your interactive Bitcoin Phase Score hub - verify our methodology yourself." He clicks through, slightly skeptical. The Notion page loads in under 2 seconds. **First 30 seconds are critical:** The interactive chart dominates the screen above the fold - no dense text blocking it. A simple visual cue points at the chart: "👈 Zoom into the 2021 peak to see how we called the top." Below the chart, a single-sentence value prop: "Glassnode shows you the raw data (WHAT). We show you when to act (WHEN)." Clean. Direct. He immediately understands this isn't another metrics dashboard.

Marcus clicks the chart and drags left - it zooms smoothly. No confusion, no 15-second friction. He explores November 2021: Phase Score hit 85 two weeks before the top, then 88 at the absolute peak. He pans to the 2022 bottom where it marked 12. For the first time, he's not trusting someone else's call - he's VERIFYING the methodology himself with historical data that doesn't lie. Below the chart, a concise methodology explainer waits (he reads it AFTER exploring, not before - his curiosity is already hooked).

The breakthrough comes three weeks later. BTC hits $72K and Marcus checks the hub - Phase Score reads 78, approaching his decision zone. He remembers the 2021 pattern: distribution started at 80, peaked at 88. Over the next week, he checks 4 times as the score climbs: 78... 80... 82... 84. Unlike 2021 when he ignored all signals and held through greed, this time he systematically reduces 40% of his position at Phase Score 82. Not because Twitter said so. Not out of panic. Because the data he personally validated told him "smart money is exiting."

Six months later, Marcus tells his brother: "I'm not guessing anymore. I have a system." His portfolio didn't catch the absolute top - he exited too early by two weeks - but he locked in 65% gains instead of riding another brutal drawdown. His parents' wealth is protected. His stress is manageable. He checks the hub 3-4 times per week during phase transitions, no longer drowning in conflicting analyst noise. The interactive chart turned passive consumption into active conviction.

**This journey reveals requirements for:**
- Python pipeline calculating proprietary phase scores daily
- TradingView Lightweight Charts with smooth zoom/pan interaction (<2 second load, 60fps)
- Chart captures mouse events immediately without requiring focus click (iframe interaction handling)
- Historical data back to 2020 for methodology validation
- Single Notion page with embedded chart **above the fold** (primary visual focus)
- Visual cue pointing to chart: "👈 Zoom into the 2021 peak to see how we called the top"
- **Single-sentence value prop above chart**: "Glassnode shows you the raw data (WHAT). We show you when to act (WHEN)."
- Methodology explainer positioned BELOW chart (users explore first, read explanation second)
- Historical track record section: 2021 top and 2022 bottom timing validation with specific dates/scores
- "Last updated: X hours ago" timestamp for data freshness confidence
- Supply zone overlays (0-20 retention, 80-100 distribution) with clear labels
- Phase score dynamically rescaled to BTC price range for readability
- Browser performance: <2 second load, 60fps interactions (no friction to aha moment)
- Netlify hosting with access control (premium content protection)
- Disclaimer: "Not financial advice - data visualization tool for research purposes"

---

### Journey 2: Sarah Martinez - From FOMO to Framework Thinking (Phase 1.5)

Sarah is a 29-year-old marketing manager who entered crypto in late 2023 after watching her friends make money. Her $8,500 portfolio (75% BTC, 25% ETH) represents 15% of her liquid savings - enough to hurt if she loses it. She follows 8-10 Twitter crypto influencers and watches YouTube videos, but every bull run post triggers FOMO and every correction triggers panic. She's heard terms like "on-chain analysis" and "SOPR" but has no idea what they actually mean. Her imposter syndrome is maxing out.

**Trial Day 1 - Saturday Morning:**

She sees a newsletter offer: "$5 trial - learn to read market phases like experienced investors." Five dollars she can afford. She signs up expecting another generic "BTC price prediction" service.

She lands on a welcome page: "Start your learning journey - Tutorial 1: The 2021 Peak." She clicks. The chart loads with an overlay: "Welcome! This guided exploration will show you what experienced investors saw in November 2021 while everyone else was buying the top. Ready? Let's zoom in together."

She follows the prompts: zoom to November 2021, watch Phase Score climb from 75 to 85 to 88. A tooltip explains in plain English: "Distribution phase = when experienced investors take profits while retail buys the top." Not jargon - just clear language she understands.

After 8 minutes, she's halfway through Tutorial 1 when her partner calls her for lunch. She closes the tab thinking "Okay, this is actually interesting - I can see the pattern they're talking about." The hook is set, but she hasn't completed the tutorial yet.

**Return Visit - Sunday Evening:**

She receives an email: "Complete your Tutorial 1 - the 2021 peak pattern is waiting." She clicks through (the link brings her right back to where she left off). She finishes Tutorial 1 in another 7 minutes. The aha moment hits during Tutorial 2: "The 2022 Bottom - Recognizing Accumulation." She's exploring the chart herself now, seeing Phase Score at 12, understanding "retention zone means long-term holders are absorbing supply, not selling."

For the first time, she realizes: there WAS a signal. It wasn't invisible. She just didn't know how to see it. The tooltip hovers help when she forgets terms, but by Tutorial 3 (which she starts immediately after Tutorial 2 - she's hooked now), she's clicking them less. She's learning the language.

**Two Months Later - The Framework Test:**

BTC hits $78K and crypto Twitter is screaming "NEW ATH INCOMING 🚀🚀🚀." Sarah's old instinct: FOMO buy more. But she checks her hub first. Phase Score: 81. She remembers the tutorials - distribution zone starts at 80. Instead of buying the euphoria, she takes 50% profit on her position. Not because she's suddenly a technical expert. Because she has a framework that replaces emotional reactions with systematic thinking.

Six months after her $5 trial, Sarah converts to the $20/month subscription. She's switched from "educational mode" with tooltips to "advanced mode" - the same streamlined view Marcus uses. She still checks Twitter, but now it's entertainment, not her decision framework. Her $8,500 portfolio became $11,200 through one good phase-based exit, and more importantly, she stopped feeling like an imposter. She has a system now. She's building conviction through understanding, not just following hype.

**This journey reveals requirements for:**
- Educational onboarding path separate from experienced investor flow
- Guided historical explorations: 3 interactive tutorials (2021 peak, 2022 bottom, current cycle)
- **Tutorial technical approach**: Interactive guided tour with overlay tooltips/highlights (not just text instructions)
- Tutorial state management: saves progress, allows resume from where user left off
- Tutorial progress tracking: "You're on step 3 of 8" visual indicators
- Email trigger: "Complete Tutorial 1" sent within 24 hours if user starts but doesn't finish
- Tooltip system explaining on-chain terminology (SOPR, MVRV, LTH, distribution, retention)
- Plain English explanations avoiding institutional jargon
- Educational → Advanced toggle for graduation to streamlined experience
- Progressive learning features showing milestone achievements
- $5 trial offering to reduce commitment barrier (price anchoring for budget-conscious)
- Tutorial completion tracking (70%+ complete all 3 = success indicator)
- Return visit within 48 hours after Tutorial 1 partial completion (email reminder critical)
- Tooltip usage analytics declining over time (learning curve validation)
- Trial → paid conversion mechanism with Stripe/Gumroad webhooks
- Success messaging when switching to advanced mode ("You're ready for the full experience!")
- Realistic expectation: Tutorial 1 split across 2 sessions (8-10 minutes Day 1, 7-10 minutes return visit)

---

### Journey 3: David Kim - The Convinced But Confused Non-Converter

David is a 42-year-old financial analyst who's been reading your free newsletter for 8 months. He loves the market phase insights - your 2021 top call is legendary in his circles - but he's subscribed to 12 different crypto newsletters and already pays for Glassnode ($39/month). When he sees your premium hub announcement ("Interactive charts - $20/month"), his immediate thought: "Another subscription I don't need."

He clicks through to the Notion page out of curiosity. **First impression matters:** The chart loads cleanly above the fold. He immediately sees the positioning statement: "Glassnode shows you the raw data (WHAT). We show you when to act (WHEN)." He thinks: "Okay, interesting angle - but prove it."

The chart interaction is smooth - no 15-second confusion about how to zoom (the iframe captures his mouse events immediately). He explores November 2021, sees the Phase Score progression (75→85→88), validates the methodology against his own memory of that period. He checks the methodology explainer below the chart: "LTH SOPR smoothing via 365-day EMA, LTH MVRV Z-score transformation..." It's legit. This isn't some random Twitter chart - there's real methodology here.

**The "Convinced But Confused" Moment:**

David sits back. He's convinced the methodology is sound. He's convinced the track record is real (2021 top, 2022 bottom calls). He's even convinced the interactive experience is better than static newsletter images.

But here's his mental block: "I already pay $39/month for Glassnode. I can see MVRV Z-score there. Why do I need to pay another $20 for... essentially a different visualization of similar on-chain data?"

He can't articulate the answer himself. The positioning statement said "Glassnode shows WHAT, we show WHEN" - but what does that MEAN operationally? Does he cancel Glassnode and switch to this? Does he keep both? He's paralyzed by decision confusion, not convinced by product value.

He closes the tab. Two weeks later, another newsletter arrives: "BTC Phase Score approaching distribution zone (78)." David thinks, "I should check that chart again." But he didn't bookmark it. He searches his email, can't find the link quickly, and gives up. His Glassnode subscription auto-renews. Your subscription opportunity passes.

Three months later, BTC tops at Phase Score 86, and David rides it back down 30% before selling in panic. He vaguely remembers that interactive chart with phase scores. Maybe he should have subscribed. But by then, the moment's passed. He tells his colleague: "There was this interesting phase score thing, but I couldn't figure out if it was worth another subscription on top of Glassnode."

**This journey reveals requirements for:**
- **MVP positioning clarity on Notion page**: Single sentence above chart: "Glassnode shows you the raw data (WHAT). We show you when to act (WHEN)."
- Competitive positioning section (can be brief): "Already subscribe to on-chain services? Glassnode/CryptoQuant provide comprehensive metrics. We provide timing signals derived from those metrics. Complementary, not redundant."
- Chart interaction design ensuring immediate responsiveness (iframe focus handled automatically)
- Bookmark-friendly persistent link with clear URL structure (easy to find again)
- Email reminder campaigns: "Phase Score entering decision zone (78+) - check your hub" with direct link
- **Phase 2 conversion optimization** (deferred from MVP):
  - Social proof testimonials: "I have Glassnode AND public_plots - here's why"
  - Use case examples: "Glassnode for research, public_plots for execution timing"
  - Cart abandonment recovery: Email sequence for users who explore but don't subscribe
  - Objection handling: "Why both subscriptions?" FAQ section
- Conversion friction analytics: Track % newsletter subscribers who click through but don't convert (informs Phase 2 optimization)

---

### Journey 4: The Analyst (You) - Maintaining Trust Through Reliability

**Scene 1: The 3:47 AM Emergency**

Your phone buzzes - not the gentle Discord notification you expected, but an SMS alert: "⚠️ CRITICAL: Pipeline failed - Phase Score 82 (decision zone)." You bolt awake. BTC is at $81K, Phase Score crossed 80 yesterday (distribution zone), and your 63 paying members are making systematic decisions based on daily-updated data. But Glassnode's API threw a 503 error at 2:15 AM, and now your pipeline hasn't run for 6 hours. This is exactly the scenario you designed the tiered SLA for - but it's still terrifying when it happens.

You grab your laptop and open the **Manual Calculation Runbook** you documented during MVP setup:

**Step 1:** Check backup data source - CryptoQuant API is online (Glassnode down, but you have fallback)
**Step 2:** Pull LTH SOPR and LTH MVRV raw data from CryptoQuant for last 3 days
**Step 3:** Run backup calculation spreadsheet with 365-day EMA smoothing formula
**Step 4:** Verify calculation against last known good automated result (yesterday's 80.1)
**Step 5:** Calculate current Phase Score manually: 82.3 (±0.3 margin of error acceptable)

By 4:30 AM, you've verified the calculation three times and posted to Discord: "Phase Score 82.3 as of 4:15 AM (manual calculation) - automated pipeline experiencing API issues, investigating now. CryptoQuant backup data confirms score within ±0.3 margin." Three members reply immediately: "Thanks for the backup!" and "This is why I trust this service." You've bought yourself time, but the pipeline needs fixing before market open when check volume will spike.

By 8:00 AM, you've implemented a data source fallback in the pipeline code and it runs successfully: "✅ Phase score updated - BTC: $81,240, Score: 82.3." The Discord notification goes out. Crisis averted. But this incident taught you something: your 99% uptime SLA during critical periods (Phase Score >80) isn't just a number - it's a trust contract. Marcus checks the hub 5 times that day during the Phase Score 82→85 climb, making his exit decision at 84. If he'd seen stale data from 12 hours ago showing 80, he would have missed his window. Trust destroyed.

**Scene 2: Month 3 - Handling the Impossible Request**

Two weeks later, you receive an email: "Love the Bitcoin phase score! Any plans to add Ethereum? Would pay extra for ETH analysis."

You sit back. This is the moment you knew was coming. Your Phase 1 scope is explicitly Bitcoin-only - you need to validate the model with one asset before expanding. But this member is engaged, paying $20/month, and asking for reasonable expansion.

**Your response framework:**
"Thanks for the feedback! Ethereum phase scoring is on our radar for Phase 2 expansion (6-12 months). Right now, we're focused on perfecting the Bitcoin model - your continued engagement and feedback helps us validate the methodology before expanding to other assets.

I'm tracking all chart requests in a roadmap database. You're the 2nd person to request ETH analysis - if we get 3+ requests for the same feature, it becomes a priority candidate for Phase 2. Want to share any specific ETH metrics you'd find valuable when we expand?"

**What this does:**
- Sets realistic expectations (Phase 2, 6-12 months)
- Validates their request without over-promising
- Shows transparency (tracking requests, need 3+ for priority)
- Invites deeper engagement (what specific ETH metrics?)
- Turns "no" into "not yet, and here's why"

You log the request in your Notion database: "ETH Phase Score - Request #2 - Date: [today] - Member: David K." The pattern tracking begins.

**Scene 3: Month 6 - Chart Roadmap Decision**

It's Saturday afternoon, and you're reviewing your chart request database. Six months in, 67 paying members, 18 total chart requests logged:

**Request Categories:**
- **Exchange netflows** (5 requests) - clear pattern, highest demand
- **MVRV Z-score divergences** (4 requests) - strong pattern
- **Supply dynamics (holder cohorts)** (3 requests) - solid pattern
- **Ethereum phase scoring** (3 requests) - cross-asset, bigger scope
- **Funding rates** (2 requests) - derivatives focus
- **One-off requests** (1 each): Correlation to gold, open interest, hash ribbons

**Phase 2 Decision Framework:**

You've hit your gate criteria: 10+ chart requests with 2+ recurring patterns (you have 18 requests, 4 clear patterns). Time to decide which 3-5 charts to build for Phase 2.

**Analysis:**
1. **Exchange netflows** (5 requests): Top priority - directly complements phase score (accumulation/distribution signals)
2. **MVRV Z-score** (4 requests): High value - adds valuation context to timing signals
3. **Supply dynamics** (3 requests): Strong fit - deepens understanding of holder behavior during phases
4. **Ethereum phase scoring** (3 requests): Defer to Phase 3 - requires validating methodology on new asset, bigger scope

**Your communication strategy:**
Draft Phase 2 announcement for members: "Based on your chart requests over the past 6 months, Phase 2 (launching Q2) will add:
1. Exchange Netflow Analysis (5 requests)
2. MVRV Z-Score Divergences (4 requests)
3. Supply Dynamics by Holder Cohort (3 requests)

**Ethereum phase scoring** (3 requests) is planned for Phase 3 once we validate multi-asset methodology. Funding rates and derivatives metrics are on the backlog - if you'd like to see these prioritized, let us know!"

This shows: You listened. You're data-driven (request count matters). You're transparent about roadmap logic. Phase 2 planning is member-driven, not ego-driven.

**This journey reveals requirements for:**
- **Manual Calculation Runbook documentation:**
  - Backup data sources (CryptoQuant API when Glassnode fails)
  - Step-by-step calculation verification process (365-day EMA smoothing, Z-score transforms)
  - Acceptable error margin (±0.3 phase score points for manual calculations)
  - Backup spreadsheet with formulas documented and tested
- Pipeline monitoring with tiered alerting (Discord normal, SMS/email critical)
- Tiered SLA enforcement: 95% uptime (Phase Score 20-80), 99% uptime (Phase Score <20 or >80)
- Data source fallback strategy built into pipeline code (automatic failover)
- Absolute limit: No more than 2 consecutive days of failed updates during critical periods
- "Last updated: X hours ago" timestamp prominently displayed (transparency)
- Weekly uptime reports tracking normal vs critical period reliability separately
- Pipeline error logging with timestamps and failure mode categorization
- Emergency communication channels (Discord webhook, Twitter backup announcements)
- **Chart request tracking system:**
  - Notion database logging: Request description, date, member name, category
  - Request categorization (exchange flows, valuation, supply, derivatives, cross-asset)
  - Pattern identification (track recurring requests, 3+ = priority candidate)
- **Out-of-scope request response framework:**
  - "Phase 2 timeline" setting realistic expectations (6-12 months)
  - "Tracking your feedback" transparency (request logged, pattern threshold explained)
  - "Invite deeper input" engagement (what specific metrics would you want?)
  - Turn "no" into "not yet, and here's why" to maintain trust
- **Phase 2 roadmap decision process:**
  - Analyze all chart requests by category and frequency
  - Prioritize top 3-5 based on: request volume, strategic fit, technical feasibility
  - Communicate roadmap decisions transparently to members with rationale
  - Defer complex/large-scope requests (multi-asset) to later phases
- Member activity analytics (check frequency, time-on-chart, phase transition correlation)
- Subscription webhook automation for Notion access grant/revoke
- Phase 2 gate criteria dashboard (50+ members, 75%+ retention, 10+ chart requests with patterns)

---

### Journey Requirements Summary

The four user journeys reveal distinct capability areas required for public_plots to deliver value across all user types:

**Core Interactive Experience (Marcus & Sarah):**
- Daily-automated Python data pipeline with proprietary phase score calculations
- TradingView Lightweight Charts with professional zoom/pan interaction (<2s load, 60fps)
- **Iframe interaction handling**: Chart captures mouse events immediately without requiring focus click first
- Historical Bitcoin data back to 2020 for methodology validation
- Phase score (0-100 scale) dynamically rescaled to visible BTC price range
- Supply zone overlays with inline labels (Retention 0-20, Distribution 80-100)
- Dark mode, rounded borders, modern polish (professional aesthetics)
- Browser compatibility: Chrome, Firefox, Safari, Edge (latest 2 versions)
- Responsive design: desktop (1920x1080) and tablet (1024x768) viewports

**Onboarding & Conversion (Marcus vs Sarah vs David):**
- **Marcus path**: Direct access, streamlined experience, chart above the fold
- **Positioning clarity for David types**: Single sentence above chart: "Glassnode shows you the raw data (WHAT). We show you when to act (WHEN)."
- **Competitive context**: Brief section explaining complementary vs redundant positioning with existing services
- **Sarah path** (Phase 1.5): Guided tutorials (3 explorations), tooltip system, educational mode
- Single Notion page with embedded chart **above the fold** (primary visual focus)
- Visual cue pointing to chart: "👈 Zoom into the 2021 peak to see how we called the top"
- Methodology explainer positioned **BELOW chart** (users explore first, read explanation second)
- Historical track record section: 2021 top and 2022 bottom timing validation with specific dates/scores
- Disclaimer: "Not financial advice - data visualization tool for research purposes"
- $5 trial offering for budget-conscious first-cycle investors (Phase 1.5)
- Bookmark-friendly persistent links (easy to return after first visit)

**Educational Scaffolding (Sarah, Phase 1.5):**
- **Tutorial technical approach**: Interactive guided tour with overlay tooltips/highlights (not just text-based instructions)
- Tutorial state management: saves progress, allows resume from where user left off
- Tutorial progress tracking: "You're on step 3 of 8" visual indicators
- 3 guided historical explorations (2021 peak, 2022 bottom, current cycle analysis)
- Email trigger: "Complete Tutorial 1" sent within 24 hours if user starts but doesn't finish
- Realistic tutorial pacing: Tutorial 1 split across 2 sessions (8-10 min initial, 7-10 min return)
- Tooltip system explaining on-chain terminology (SOPR, MVRV, LTH, distribution, retention)
- Plain English explanations avoiding institutional jargon
- Tutorial completion tracking (70%+ target for all 3 explorations)
- Tooltip usage analytics to measure learning curve (declining usage = growing understanding)
- Educational → Advanced toggle for graduation to streamlined experience
- Progressive learning milestones and success messaging
- Return visit trigger: Tutorial 1 partial completion drives email within 24 hours

**Infrastructure & Reliability (Analyst/Admin):**
- **Manual Calculation Runbook**: Documented procedure for emergency 3AM scenarios
  - Backup data sources (CryptoQuant when Glassnode fails)
  - Step-by-step calculation verification (365-day EMA, Z-score transforms)
  - Acceptable error margin (±0.3 phase score points for manual calculations)
  - Backup spreadsheet with formulas tested and ready
- Pipeline monitoring with tiered alerting (Discord normal, SMS/email critical)
- Tiered SLA enforcement: 95% uptime (Phase Score 20-80), 99% uptime (Phase Score <20 or >80)
- Data source fallback strategy built into pipeline code (automatic CryptoQuant failover)
- Absolute limit: No more than 2 consecutive days of failed updates during critical periods
- "Last updated: X hours ago" timestamp prominently displayed (transparency)
- Weekly uptime reports tracking normal vs critical period reliability separately
- Pipeline error logging with timestamps and failure mode categorization
- Emergency communication channels (Discord webhook, Twitter backup announcements)

**Chart Request Management & Phase 2 Planning (Analyst/Admin):**
- **Chart request tracking system:**
  - Notion database: Request description, date, member name, category tag
  - Request categorization (exchange flows, valuation, supply, derivatives, cross-asset)
  - Pattern identification tracking (3+ requests = priority candidate)
- **Out-of-scope request response framework:**
  - Set realistic timeline expectations (Phase 2: 6-12 months, Phase 3: multi-asset)
  - Transparency about tracking and pattern thresholds ("You're request #2 for ETH")
  - Invite deeper engagement ("What specific ETH metrics would you want?")
  - Turn "no" into "not yet, and here's why" to maintain member trust
- **Phase 2 roadmap decision process:**
  - Analyze all chart requests by category and frequency at 6-month mark
  - Prioritize top 3-5 charts based on: request volume, strategic fit, technical scope
  - Communicate roadmap decisions transparently with rationale ("Based on your 18 requests...")
  - Defer complex requests (multi-asset, derivatives) to appropriate phase

**Subscription Management (Analyst/Admin):**
- Netlify hosting with edge function referer validation (Notion-only access)
- Token parameter support built (Phase 1: not enforced, Phase 2: per-member access control)
- Stripe/Gumroad integration for payment processing (not building in-house)
- Subscription webhook automation for Notion access grant/revoke
- Member activity analytics (check frequency, time-on-chart, phase transition correlation)
- Phase 2 gate criteria dashboard (50+ members, 75%+ retention, 10+ chart requests with patterns)

**Conversion Optimization (David's journey - MVP + Phase 2):**
- **MVP (minimal addressing)**: Positioning statement above chart, competitive context section
- **Phase 2 deferred features**:
  - Social proof: Testimonials from users who have both Glassnode AND public_plots
  - Use case examples: "Glassnode for research, public_plots for execution timing"
  - Email reminder campaigns with direct chart links during phase transitions (78+ = decision zone)
  - Conversion friction analytics: % newsletter subscribers who explore but don't convert
  - Cart abandonment recovery: Email sequence for users who interact but don't subscribe
  - Objection handling FAQ: "Why both subscriptions? Here's how they complement"

**Data & Performance Requirements (All users):**
- Data freshness: Phase scores updated within 24 hours when source data available
- Calculation correctness: Phase scores match manual validation 100% when spot-checked
- Source data integrity: LTH SOPR and LTH MVRV validated monthly against baseline providers
- Historical consistency: 2021 peak (85 at Nov 2021) and 2022 bottom (12 at Nov 2022) remain stable
- Chart performance: <2 second load time, 60fps zoom/pan on 10 Mbps broadband
- Concurrent capacity: 50-100 simultaneous users without performance degradation
- CDN delivery: <100ms latency globally via Netlify CDN
- Cost efficiency: Infrastructure <$50/month at 100-user scale

These requirements span the complete user experience from discovery (David) through onboarding (Marcus streamlined with positioning clarity, Sarah educational with realistic tutorial pacing) to sustained engagement (Marcus decision-making, Sarah learning progression) and operational sustainability (Analyst maintaining trust through reliability, prioritizing roadmap based on validated demand). Each journey validates specific capabilities needed to deliver the core value proposition while ensuring the product remains operationally maintainable by a solo operator.

---

## Innovation & Novel Patterns

### Core Innovation: Proprietary Timing Signals with Interactive Validation

Public_plots delivers a novel trust architecture that combines four interdependent layers - proprietary calculation methodology, proven historical track record, interactive validation mechanism, and curated single-signal focus - to create systematic timing confidence unavailable on comprehensive metric platforms.

**The Innovation System:**

Unlike competitors who provide either raw data access (Glassnode's 800+ metrics) or analyst curation alone (Ben Cowen's video analysis), public_plots delivers all four layers working together:

1. **Proprietary Signal Foundation:** Custom Phase Score (0-100) combining LTH SOPR smoothing and LTH MVRV transformations - calculation methodology unavailable on any other platform
2. **Proven Track Record Layer:** Historical validation calling 2021 top within 2 weeks (Phase Score 85) and 2022 bottom (Phase Score 12)
3. **Interactive Validation Mechanism:** TradingView Lightweight Charts enabling users to zoom into historical periods and verify methodology themselves
4. **Curated Focus Layer:** Single proven signal with clear action zones (0-20 accumulate, 80-100 distribute) vs overwhelming metric dashboards

**Each layer is necessary. None alone is sufficient.** Glassnode has data but no proprietary timing signals. Ben Cowen has analyst curation but no interactive validation. TradingView has charts but no proven methodology. The combination creates defensible differentiation - competitors can copy 2 layers (interactive charts, curated focus) but cannot replicate the proprietary methodology or historical proof without the domain expertise and track record.

### Innovation Positioning vs Market Assumptions

**Prevailing Market Model (Comprehensive Data Access):**
- Glassnode: 800+ on-chain metrics, $30-800/month
- CryptoQuant: Hundreds of metrics, professional institutional focus  
- Assumption: More comprehensive data = better insights = better decisions

**Public_plots Innovation Challenge:**
"More metrics create analysis paralysis for time-constrained investors. Information overload is the problem, not information scarcity."

**Evidence Supporting Innovation:**
- Marcus (experienced investor): Follows 4-5 analysts, multiple services, still paralyzed by conflicting signals - subscribing to more data sources didn't improve decisions
- Sarah (first-cycle investor): Overwhelmed by 8-10 Twitter influencers despite abundant "free alpha" - information abundance created confusion, not clarity
- Both segments demonstrate: The bottleneck isn't data access, it's **signal curation with trust validation**

**Unique Value Proposition:**
"The only premium crypto analysis platform where you verify our timing track record yourself through interactive data exploration - one proven signal that called major cycle inflections vs 800 metrics you'll never use."

### Market Context & Competitive Landscape

**Competitive Positioning Matrix:**

| Platform | Model | Strength | Gap public_plots Fills |
|----------|-------|----------|------------------------|
| **Glassnode** ($30-800/mo) | Comprehensive metrics | 800+ on-chain indicators, enterprise infrastructure | No proprietary timing signals, overwhelming metric count, no clear "when to act" guidance |
| **CryptoQuant** ($49-799/mo) | Professional analytics | Exchange flow data, institutional tools | Broad data without interpretation, missing actionable timing framework |
| **Ben Cowen** (~$20/mo) | Analyst + education | Personal methodology, educational content | Static charts in videos, less precise timing signals, no interactive validation |

**Public_plots Differentiation:**
- **vs Glassnode:** Proven timing signals with curated focus vs comprehensive data overload
- **vs CryptoQuant:** Actionable "when to act" framework vs "what's happening" raw data
- **vs Ben Cowen:** Interactive historical validation vs passive video consumption

**Defensibility Analysis:**

**Hard to Replicate (2 layers):**
- Proprietary phase scoring methodology (requires domain expertise, custom calculations)
- Historical track record with dated proof (can't fake 2021/2022 calls retroactively)

**Easy to Replicate (2 layers):**
- Interactive charts (TradingView Lightweight Charts available to anyone)
- Curated single-signal focus (philosophical choice, not technical barrier)

**System Defensibility:** Copying 2 out of 4 layers doesn't deliver equivalent value. Competitors need ALL FOUR working together to match the trust architecture. The proprietary methodology + proven track record create the core moat, while interactive validation + curation amplify trust and usability.

### Validation Approach

**Innovation Hypothesis:**
"Proprietary signals + interactive validation + curated focus creates more confidence and systematic decision-making than comprehensive metric access."

**Evidence Framework - Behavioral Validation:**

Each innovation layer maps to measurable user behaviors:

**Layer 1 - Proprietary Signal (Proven Track Record):**
- **Metric:** 10-12% newsletter → paid conversion despite $20/mo premium pricing
- **Validation:** Track record credibility drives conversion - users pay for proven methodology
- **Failure Signal:** <7% conversion = track record not compelling enough

**Layer 2 - Interactive Validation:**
- **Metric:** 60%+ zoom within first session (aha moment rate)
- **Validation:** Users actively verifying methodology by exploring historical data
- **Failure Signal:** <40% zoom rate = interactive validation not driving discovery

**Layer 3 - Curated Focus:**
- **Metric:** Chart requests stay at 15-20 total in first 6 months, asking for 3-5 additional signals
- **Validation:** Users want more curated signals, not metric explosion (comprehensiveness validated as unnecessary)
- **Failure Signal:** Dozens of diverse metric requests = users want comprehensive dashboards after all

**Layer 4 - Systematic Decision Confidence:**
- **Metric:** 75%+ retention with single chart after month 3, time-on-chart 90+ seconds with active exploration
- **Validation:** Proven signal value sustained, deep analytical engagement not passive viewing
- **Failure Signal:** <60% retention or passive usage patterns = ongoing value not demonstrated

**Business Validation:**

**Success Indicators:**
- Members maintain public_plots subscriptions while reducing/canceling Glassnode (curated beats comprehensive)
- Testimonials mentioning "clarity," "confidence," "systematic decisions" vs "comprehensive" or "more data"
- Strategic usage patterns: Hub checks correlating with phase transitions (78+ decision zones) not random anxiety checks

**Comparative Benchmarks:**
- If 75%+ retention achieved with 1 chart vs Glassnode's hundreds = innovation validated
- If chart request volume stays low (15-20 total, 3-5 patterns) = curation philosophy proven
- If conversion matches/exceeds Ben Cowen's ~$20/mo tier despite fewer charts = proven signals + validation working

### Risk Mitigation

**Innovation Risk:** Users expect comprehensive metric access despite stated preference for curation. "Less is more" philosophy doesn't resonate beyond early adopters.

**Mitigation Strategies:**

**1. Segment-First Validation (Phase 1 - Marcus):**
- Target experienced investors who've already tried metric overload (Glassnode subscriptions) and found it overwhelming
- This segment has context to appreciate curation over comprehensiveness
- Validates innovation with users most likely to value the approach

**2. Behavioral Early Warning System:**
- Month 1-3: Monitor chart request patterns and sentiment
- If requests explode to dozens of diverse metrics → Users want comprehensiveness, not curation
- If engagement remains passive (<40% zoom rate) → Interactive validation not compelling
- Enables pivot before 6-month gate decision

**3. Hybrid Model Fallback:**
- If Phase 2 validation shows demand for breadth: Introduce tiered system
  - Basic: 5 curated charts (maintains philosophy)
  - Pro: 15-20 charts (acknowledges some users want more)
- Tests whether curation is universal value or segment-specific

**4. Positioning Pivot Options:**
- **If curation doesn't resonate:** Lead with proprietary methodology + track record, downplay "less is more" messaging
- **If interactive validation weak:** Emphasize analyst expertise and proven calls, reduce validation positioning
- **If system works but messaging unclear:** A/B test positioning statements to find resonant framing

**5. Validation Timeline with Circuit Breakers:**
- **Month 3:** Evaluate zoom rates, chart request patterns, early retention
  - Circuit breaker: <5% conversion + <40% zoom rate = fundamental hypothesis issue
- **Month 6:** Gate decision using full criteria (50+ members, 75% retention, 10+ requests with patterns)
  - Circuit breaker: 0 of 3 criteria met = innovation not validated, pivot required

**Success Validation Example:**
Marcus cancels Glassnode ($39/mo), keeps public_plots ($20/mo), tells friends: "I only need these 3-5 signals, not 800 metrics I never check. The track record speaks for itself, and I can verify everything myself."

**Pivot Validation Example:**
Month 3 shows 32 chart requests spanning 20+ diverse topics, members asking "when will you add more comprehensive coverage?" → Curation hypothesis failing, users want breadth despite stated preferences → Evaluate comprehensive expansion or repositioning.

---

## Web App Specific Requirements

### Project-Type Overview

Public_plots is a **static HTML web application** with embedded interactive JavaScript components. The architecture centers on a single, self-contained HTML file that embeds TradingView Lightweight Charts for interactive data visualization. This is not a Single Page Application (SPA) with client-side routing - it's a focused, static page optimized for one purpose: interactive chart exploration with professional-grade performance.

The deployment model leverages **Netlify's edge network** for global CDN distribution, with **Edge Functions** handling access control via referer validation. Daily automated Python pipeline updates generate new chart data, which triggers Netlify redeployment of the updated HTML file. Users access the chart through **Notion embedding** - the Notion page acts as the content wrapper (methodology explainer, track record, educational context) while the embedded chart provides the interactive experience.

This architecture choice prioritizes:
- **Simplicity**: No complex build process, state management, or routing frameworks
- **Performance**: Static HTML served from CDN with minimal JavaScript overhead
- **Reliability**: No backend dependencies at request time (chart data pre-generated)
- **Scalability**: CDN handles 50-100 concurrent users without application-level scaling concerns

### Technical Architecture Considerations

**Hosting & Deployment:**
- **Platform**: Netlify (static site hosting + edge functions)
- **Deployment Method**: Single HTML file with embedded JavaScript and chart data
- **Update Mechanism**: Daily automated redeployment triggered by Python pipeline
- **CDN Strategy**: Global edge distribution for <100ms latency worldwide
- **Access Control**: Edge Function validates Notion referer, blocks direct access
- **Token Infrastructure**: Built-in token parameter support for Phase 2 per-member access control (Note: Notion's coarse-grained access control sufficient for MVP; per-member tokens deferred unless usage patterns demand earlier implementation)

**Browser Compatibility Matrix:**

| Browser | Minimum Version | Priority | Notes |
|---------|----------------|----------|-------|
| Chrome | 90+ (May 2021) | P0 | Primary browser for crypto investors |
| Firefox | 88+ (April 2021) | P0 | Secondary desktop browser |
| Safari | 14+ (Sept 2020) | P1 | macOS users, WebKit rendering quirks |
| Edge | 90+ (May 2021) | P1 | Chromium-based, similar to Chrome |

**Rationale for Version Minimums:**
- TradingView Lightweight Charts requires modern ES6+ JavaScript features
- 2021+ versions ensure Canvas API performance for smooth chart rendering
- Covers 95%+ of target user base (tech-savvy crypto investors)

**Browser Testing Protocol:**
- **Primary validation**: Chrome + Firefox on macOS/Windows
- **Safari-specific testing**: Canvas rendering and touch events (Safari WebKit has different performance characteristics)
- **iPad hardware testing**: Touch-based zoom/pan on actual iPad hardware (1024x768 landscape orientation)
- **Cross-browser validation**: Test chart initialization, zoom/pan smoothness, tooltip responsiveness on all supported browsers before launch

**Unsupported Browsers:**
- Internet Explorer (all versions) - explicitly not supported, no polyfills
- Mobile browsers (<768px viewports) - may render but broken interaction model (tap targets too small, labels unreadable) - explicitly documented as non-functional

**Responsive Design Strategy:**

**Desktop-First Optimization (Primary Experience):**
- **Target Resolution**: 1920x1080 (Full HD) - most common desktop resolution
- **Minimum Resolution**: 1280x720 (HD) - chart remains usable, some label condensing
- **Chart Dimensions**: Full-width within Notion embed, minimum 800px wide for readability
- **Interaction Model**: Mouse-based zoom/pan, hover tooltips, click-drag for timeframe selection

**Tablet Support (Secondary Experience):**
- **Target Resolution**: 1024x768 (iPad landscape)
- **Chart Usability**: Touch-based zoom/pan functional, tooltips on tap
- **Testing Requirement**: Must validate on actual iPad hardware (Notion app and mobile Safari browser)
- **No Mobile Optimization**: Preset zoom buttons, touch gesture refinements deferred to Phase 2
- **Expectation**: 10-15% of usage, primarily for quick checks not deep analysis

**Mobile Phone (Out of Scope for MVP):**
- Chart renders but explicitly non-functional on <768px viewports
- Specific breakages: tap targets <44px (too small for fingers), labels overlapping, zoom gestures unreliable
- Phase 2 consideration based on usage analytics showing demand

### Performance Targets & Validation

**Chart Load Performance:**
- **Initial Load Time**: <2 seconds on 10 Mbps broadband (target: 1.5s)
  - TradingView Lightweight Charts library: ~100kb minified + gzipped
  - HTML + chart initialization code: ~50kb
  - Chart data JSON (2020-present): ~200-250kb (4+ years daily data)
  - **Total realistic page weight**: 350-400kb (revised from initial 150kb estimate)
- **Time to Interactive**: <2.5 seconds (chart fully functional, zoom/pan responsive)
- **Critical for Aha Moment**: If chart takes >5 seconds to load, users bounce before reaching validation experience

**Performance Measurement Approach:**
- **Pre-launch validation**: Lighthouse CI testing on staging deployment (Target: Performance score 90+)
- **Connection throttling tests**: Validate <2s load on 5 Mbps connections (not just 10 Mbps optimal case)
- **Real User Monitoring (Phase 2)**: Netlify Analytics tracks actual user load times; custom instrumentation for time-to-interactive if MVP shows performance issues

**Interaction Performance:**
- **Zoom/Pan Operations**: 60 FPS minimum (no visible lag or stuttering)
  - Canvas rendering optimized for smooth interaction
  - Data decimation strategy: Show every daily data point when zoomed to <6 months, decimate to weekly when viewing full 4-year history
  - Maximum data points rendered: ~500-700 points (TradingView performance threshold)
- **Tooltip Response**: <50ms hover → tooltip display (feels instant)
- **Crosshair Tracking**: Smooth cursor following at 60 FPS

**Data Freshness vs Performance Trade-off:**
- Daily batch updates mean chart data is static between deployments
- No WebSocket/polling overhead, no real-time update performance concerns
- "Last updated: X hours ago" timestamp manages user expectations

**Load Testing Requirements:**
- **Pre-launch stress test**: Validate Netlify CDN handles 50-100 concurrent requests during simulated phase transition moment
- **Expected behavior**: CDN serves static HTML instantly without origin server load
- **Monitoring**: Track Netlify bandwidth and response times during first real phase transition (Phase Score 78-82 window)

### Data Pipeline Contract & Error Handling

**Pipeline Implementation:**
- **Active pipeline**: `market_phase_score_with_cycles.py` (primary implementation)
- **Deprecated pipeline**: `market_phase_score.py` (legacy version, retained for reference)
- **Output format**: `chart-data.json` with specific schema (documented below)

**Chart Data Schema (JSON):**

```json
{
  "btcPrice": [
    {"time": 1609459200, "value": 29000.50},  // Unix timestamp (seconds), BTC price (float)
    ...
  ],
  "phaseScore": [
    {"time": 1609459200, "value": 45.2},  // Unix timestamp (seconds), Phase score 0-100 (float)
    ...
  ],
  "lastUpdated": "2025-12-05T08:15:00Z",  // ISO 8601 timestamp
  "dataQuality": "complete"  // "complete" | "partial" | "stale"
}
```

**Data Format Specifications:**
- **Timestamps**: Unix epoch seconds (NOT milliseconds) - TradingView Lightweight Charts expects seconds
- **Timezone**: All timestamps in UTC (pipeline converts, chart displays in user's local timezone)
- **Data alignment**: BTC price and phase score arrays must have matching timestamps for accurate overlay
- **Missing data handling**: If source data unavailable for specific days, interpolate or mark as null (chart skips null values)

**Chart Initialization Sequence:**

```javascript
// 1. Wait for DOM ready
document.addEventListener('DOMContentLoaded', function() {
  // 2. Initialize chart container
  const chart = LightweightCharts.createChart(container, config);

  // 3. Load embedded JSON data
  const chartData = JSON.parse(document.getElementById('chart-data').textContent);

  // 4. Create series (BTC price baseline + phase score overlay)
  const btcSeries = chart.addLineSeries({...});
  const phaseSeries = chart.addLineSeries({...});

  // 5. Set data and configure dynamic rescaling
  btcSeries.setData(chartData.btcPrice);
  phaseSeries.setData(chartData.phaseScore);

  // 6. Handle iframe resize events (Notion embedding)
  window.addEventListener('resize', () => chart.resize());
});
```

**Error State Handling:**

| Error Condition | User-Visible Message | Technical Handling |
|----------------|---------------------|-------------------|
| **Pipeline failed (JSON missing)** | "Chart temporarily unavailable. Last successful update: [timestamp]. Check back in 2-4 hours." | Show fallback message div, hide chart container, log error to console for debugging |
| **JSON parsing error (corrupt data)** | "Chart data error detected. Our team has been notified. Last known good data: [timestamp]." | Catch JSON.parse() exception, display error state, attempt to load cached previous version |
| **Stale data (>48 hours old)** | "⚠️ Data is stale (last updated [X hours] ago). Phase Score may not reflect current conditions." | Check `lastUpdated` timestamp, display warning banner above chart, chart still functional |
| **Chart initialization failure** | "Chart failed to load. Try refreshing the page or contact support if issue persists." | Catch initialization exceptions, display error message, provide refresh button |

**Graceful Degradation Philosophy:**
- **No static image fallback**: Interactive chart is core value proposition; if chart fails, show error message (don't fake functionality)
- **Stale data is better than no data**: Display chart with warning if data is 24-48 hours old (macro indicator tolerance)
- **Absolute failure threshold**: If data >72 hours old, treat as pipeline failure (macro indicator too stale to be useful)

### Notion Iframe Embedding Considerations

**Embedding Architecture:**
- Notion page embeds chart HTML via `<iframe>` element
- Iframe source: `https://public-plots.netlify.app/chart.html?referer=notion`
- Edge Function validates `Referer` header matches Notion domain pattern

**Iframe-Specific Challenges:**

1. **Cookie & Storage Limitations:**
   - Third-party cookie restrictions in Safari/Firefox may block localStorage
   - Chart state (zoom level, scroll position) cannot be persisted client-side in MVP
   - Phase 2 saved views require backend state storage, not browser localStorage

2. **Resize Handling:**
   - Notion iframe resizes dynamically based on content
   - Chart must listen for `window.resize` events and call `chart.resize()`
   - Initial height must be set via Notion embed settings (manual configuration)

3. **Interaction Capture:**
   - Iframe must capture mouse/touch events immediately (no focus-click required)
   - TradingView charts handle this natively, but requires testing in Notion context

4. **Mobile Notion App Behavior:**
   - Notion mobile app (iOS/Android) renders iframes differently than mobile Safari
   - Requires separate testing on Notion mobile app, not just mobile browsers
   - May have different touch event handling and performance characteristics

**Pre-Launch Validation Checklist:**
- [ ] Chart loads and renders correctly in Notion desktop browser (Chrome, Firefox, Safari)
- [ ] Zoom/pan interactions work without requiring iframe focus click
- [ ] Referer validation correctly blocks direct URL access outside Notion
- [ ] Chart resizes properly when Notion page window is resized
- [ ] Tooltips display correctly within iframe boundaries (not clipped by Notion)
- [ ] iPad Notion app renders chart with functional touch interactions
- [ ] "Last updated" timestamp displays correctly in user's local timezone

### SEO & Discovery Strategy

**Intentionally Not Indexed Approach:**

The chart HTML is **explicitly not designed for search engine indexing**:
- **Access Control**: Edge Function referer validation blocks non-Notion access, including search engine crawlers
- **No robots.txt allowance**: Chart page should not be discoverable via Google/Bing
- **No meta tags for SEO**: No Open Graph, Twitter Card, or schema.org markup on chart HTML
- **Premium Content Protection**: Indexing would leak proprietary chart access to non-paying users

**Notion Page SEO (Separate Consideration):**

The Notion hub page containing the chart embed operates under **Notion's SEO rules**, not our control:
- Notion pages can be indexed if sharing settings allow (private pages not indexed)
- Premium hub page should be **private, members-only** - not publicly indexed
- Free newsletter landing page may be indexed for discovery, but not premium hub

**Discovery Model:**
- Users find public_plots via **newsletter**, not search engines
- Chart access is **gated content** delivered after payment
- SEO irrelevant for MVP - growth via newsletter audience, not organic search

### Accessibility Compliance

**MVP Accessibility Stance: Explicitly Deferred**

Accessibility features are **not required for MVP** and explicitly scoped out:
- No WCAG 2.1 compliance target
- No screen reader optimization for chart interactions
- No keyboard-only navigation support
- No ARIA labels on chart data points
- Color contrast not validated against accessibility standards

**Rationale for Deferral:**
- Target users (Marcus, Sarah) are sighted investors analyzing visual chart patterns
- Interactive chart exploration is inherently visual (zoom into 2021 peak, see distribution patterns)
- MVP validates core value proposition with primary user segment first
- Accessibility can be layered in Phase 2 if demand emerges from users with accessibility needs

**Phase 2 Reconsideration Triggers:**
- User feedback requesting screen reader support
- Legal/compliance requirement for financial tools
- Market expansion to users with visual impairments

**Minimum Baseline (Unintentional Accessibility):**
- Modern browsers provide some baseline accessibility (browser zoom, text scaling)
- Notion wrapper page may have accessibility features (platform-provided)
- Chart tooltips use high-contrast text for readability (not WCAG validated but pragmatically readable)

### Implementation Considerations

**Technology Stack:**
- **Core Library**: TradingView Lightweight Charts (v4.x)
- **JavaScript**: Vanilla ES6+ (no framework - React/Vue/Svelte not needed)
- **Styling**: Inline CSS or embedded `<style>` block (no external stylesheet for single-file deployment)
- **Build Process**: Python script generates HTML with embedded JSON data
- **Deployment**: Netlify CLI for automated deployments from pipeline

**Data Pipeline → Chart Flow:**
1. Python pipeline (`market_phase_score_with_cycles.py`) calculates phase scores daily
2. Script generates `chart-data.json` with BTC price + phase score time series (schema above)
3. Python script injects JSON into HTML template as inline JavaScript variable
4. Single `index.html` file deployed to Netlify via CLI
5. Edge Function validates referer on request
6. Browser loads HTML, renders chart using embedded data

**Chart Configuration:**
- Dark mode theme (professional aesthetic)
- Rounded borders, modern polish
- BTC price on log scale (left Y-axis)
- Phase score dynamically rescaled to visible BTC price range (right Y-axis)
- Supply zone overlays (0-20 green retention zone, 80-100 red distribution zone) with inline labels
- Crosshair with tooltip showing: date, BTC price, phase score

**Browser Storage:**
- **No localStorage or sessionStorage usage in MVP**: Safari/Firefox third-party cookie restrictions block iframe storage
- Saved views (bookmark zoom levels) deferred to Phase 2 with backend state storage
- No user-specific state persisted client-side

**Security Considerations:**
- **Referer validation**: Edge Function blocks non-Notion referers (prevents direct chart access)
- **No authentication in MVP**: Notion manages user access to premium hub page
- **Token infrastructure ready**: URL supports `?token=xxx` parameter for Phase 2 per-member access control
- **XSS protection**: No user-generated content in chart; JSON data is trusted pipeline output

---

## Project Scoping & Phased Development

### MVP Strategy & Philosophy

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

### MVP Feature Set (Phase 1: Marcus Segment Only)

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

### Post-MVP Features

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

### Risk Mitigation Strategy

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

## Functional Requirements

### Data Pipeline & Calculation

- FR1: System can execute proprietary Bitcoin phase score calculations daily using LTH SOPR smoothing and LTH MVRV transformations
- FR2: System can output phase scores on a 0-100 scale with supply retention zone (0-20) and distribution zone (80-100) identification
- FR3: System can generate chart data in JSON format with BTC price and phase score time series
- FR4: System can automatically deploy updated chart data to hosting platform on successful pipeline execution
- FR5: System can fall back to alternate data sources when primary data provider is unavailable
- FR6: System can validate calculation correctness against manual verification within ±0.3 phase score points
- FR7: System can maintain historical data consistency for backtested period (2020-present)

### Interactive Chart Visualization

- FR8: Users can view interactive Bitcoin price chart with overlaid phase score using professional-grade charting library
- FR9: Users can zoom into specific time periods using mouse/touch gestures
- FR10: Users can pan across historical data from 2020 to present
- FR11: Users can view crosshair tooltips showing exact BTC price and phase score values at specific dates
- FR12: Users can see phase score dynamically rescaled to visible BTC price range for readability
- FR13: Users can see supply zone overlays with inline labels marking retention (0-20) and distribution (80-100) zones
- FR14: Users can view chart in dark mode with rounded borders and modern visual polish
- FR15: Users can interact with chart immediately without requiring focus click (iframe interaction handling)

### Content Presentation & Access

- FR16: Users can access chart embedded in Notion page with chart displayed above the fold
- FR17: Users can view single-sentence value proposition above chart distinguishing service from competitors
- FR18: Users can view methodology explainer positioned below chart describing calculation approach
- FR19: Users can view historical track record section showing 2021 top and 2022 bottom timing validation with specific dates and phase scores
- FR20: Users can see "Last updated: X hours ago" timestamp prominently displayed
- FR21: Users can see visual cue pointing to chart encouraging historical exploration
- FR22: Users can view disclaimer stating "Not financial advice - data visualization tool for research purposes"
- FR23: Users can access persistent bookmark-friendly chart URL

### Access Control & Security

- FR24: System can validate referer headers to restrict chart access to Notion-only embedding
- FR25: System can support token parameter for per-member access control (built but not enforced in Phase 1)
- FR26: System can grant Notion page access based on subscription status via payment provider webhooks
- FR27: System can revoke Notion page access when subscription is canceled or payment fails

### Monitoring & Reliability

- FR28: System can notify admin via Discord webhook on successful daily pipeline execution with current BTC price and phase score
- FR29: System can alert admin via Discord webhook when pipeline fails with error indication
- FR30: System can escalate to SMS/email alert when pipeline fails during critical market conditions (Phase Score <20 or >80)
- FR31: System can track pipeline uptime separately for normal conditions (Phase Score 20-80) vs critical conditions (Phase Score <20 or >80)
- FR32: System can log pipeline errors with timestamps and failure mode categorization
- FR33: Admin can access manual calculation runbook documentation for emergency backup calculations
- FR34: Admin can post manual phase score updates to emergency communication channels when automated pipeline fails

### Member Engagement & Feedback

- FR35: Members can submit chart requests via email or direct message
- FR36: Admin can log chart requests in tracking system with request description, date, member name, and category
- FR37: Admin can categorize chart requests by type (exchange flows, valuation, supply, derivatives, cross-asset)
- FR38: Admin can identify recurring request patterns when 3+ members request same chart type
- FR39: Admin can communicate Phase 2 roadmap decisions to members with rationale based on request patterns
- FR40: Admin can respond to out-of-scope requests with realistic timeline expectations and transparency about tracking

### Educational Experience (Phase 1.5 - Deferred)

- FR41: First-cycle investors can access educational onboarding path separate from experienced investor flow
- FR42: Users can complete guided historical explorations through interactive tutorials covering 2021 peak, 2022 bottom, and current cycle
- FR43: Users can view tooltip overlays explaining on-chain terminology in plain English
- FR44: Users can see tutorial progress indicators showing current step position
- FR45: Users can resume tutorials from where they left off via state management
- FR46: Users can receive email reminders to complete started but unfinished tutorials within 24 hours
- FR47: Users can toggle between educational mode (with tooltips) and advanced mode (streamlined)
- FR48: Users can see success messaging when graduating to advanced mode
- FR49: Users can access $5 trial subscription offering before converting to $20/month standard pricing

### Performance & Compatibility

- FR50: Chart can load in under 2 seconds on 10 Mbps broadband connection
- FR51: Chart can render zoom/pan interactions at 60 FPS without lag or stuttering
- FR52: Chart can display tooltip responses within 50ms of hover action
- FR53: Chart can function correctly on Chrome 90+, Firefox 88+, Safari 14+, and Edge 90+
- FR54: Chart can render properly on desktop (1920x1080) and tablet (1024x768) viewports
- FR55: System can support 50-100 concurrent users without performance degradation
- FR56: System can serve chart globally with CDN latency under 100ms

### Analytics & Measurement (Phase 2 - Tracking Deferred)

- FR57: System can track member check frequency and time-on-chart duration
- FR58: System can identify correlation between hub usage and phase score transitions
- FR59: System can measure first-session zoom rate as aha moment indicator
- FR60: System can track tutorial completion rates for educational path users
- FR61: System can measure tooltip usage declining over time as learning progression indicator
- FR62: Admin can view Phase 2 gate criteria dashboard showing member count, retention percentage, and chart request patterns

---

## Non-Functional Requirements

### Performance

- NFR1: Chart initial load completes in <2 seconds on 10 Mbps broadband connection (target: 1.5s)
- NFR1a: Load time validated on 5 Mbps throttled connection (worst case) before launch
- NFR2: Chart reaches interactive state (zoom/pan functional) within 2.5 seconds of page load
- NFR3: Zoom and pan operations render at 60 FPS minimum without visible lag or stuttering
- NFR4: Crosshair tooltips display within 50ms of hover action
- NFR5: Chart page weight remains under 400kb (HTML + library + data combined)
- NFR6: Chart maintains 60 FPS performance when rendering 500-700 data points maximum
- NFR6a: Chart decimates daily data to <700 points when viewing full historical range (5+ years)
- NFR7: CDN serves chart HTML globally with <100ms latency from edge servers

### Security

- NFR8: Chart access restricted to Notion referer headers via edge function validation
- NFR9: Payment processing handled by PCI-compliant third-party providers (Stripe/Gumroad)
- NFR10: User authentication and access management delegated to Notion platform (no custom auth)
- NFR11: Token parameter signatures validated to prevent forgery when per-member access control enabled (Phase 2)
- NFR12: All data transmission occurs over HTTPS/TLS encryption
- NFR13: No sensitive user data (passwords, payment info) stored in custom infrastructure
- NFR13a: Code review confirms no PII/payment data persisted to logs or storage

### Scalability

- NFR14: System supports 50-100 concurrent users without performance degradation at launch
- NFR15: Infrastructure costs remain under $50/month at 100-user scale
- NFR16: CDN architecture supports scaling to 200-300 users (Phase 2) without application redesign
- NFR17: Static HTML deployment model eliminates backend scaling concerns
- NFR18: Chart data generation pipeline scales linearly with additional chart types (Phase 2)
- NFR18a: Chart data JSON files remain under 300kb per chart type for CDN efficiency

### Reliability

- NFR19: Pipeline achieves 95% uptime during normal market conditions (Phase Score 20-80)
- NFR20: Pipeline achieves 99% uptime during critical market conditions (Phase Score <20 or >80) OR manual backup calculation posted within 4 hours
- NFR21: No more than 2 consecutive days of failed pipeline updates during critical market conditions
- NFR21a: Manual calculation runbook enables recovery during business hours (8 AM - 10 PM ET)
- NFR22: Pipeline failures trigger automated Discord alerts within 5 minutes
- NFR23: Critical market condition failures escalate to SMS/email within 15 minutes
- NFR24: Manual backup calculation runbook enables 4-hour recovery during business hours, 8-hour recovery outside business hours
- NFR25: Chart data calculations match manual validation within ±0.3 phase score points when spot-checked
- NFR26: Historical data consistency maintained (2021 peak score 85, 2022 bottom score 12 remain stable)
- NFR43: Source data validated monthly against independent provider baselines (Glassnode vs CryptoQuant reconciliation)
- NFR44: All critical NFRs (performance, uptime, integration) have automated monitoring with alert thresholds
- NFR46: Pipeline failures preserve last known good data (no broken/empty charts served)

### Integration

- NFR27: Pipeline successfully pulls data from Glassnode API with 95%+ reliability
- NFR28: Pipeline falls back to CryptoQuant API when primary source unavailable
- NFR29: Chart embeds correctly in Notion pages without rendering issues across desktop browsers
- NFR29a: Chart renders with correct dimensions, captures mouse interactions, displays tooltips in Notion iframe
- NFR30: Subscription webhooks from Stripe/Gumroad grant Notion access within 60 seconds of payment
- NFR30a: Failed webhook processing retries every 5 minutes for 24 hours before manual intervention
- NFR31: Subscription cancellation webhooks revoke Notion access within 24 hours
- NFR32: Daily pipeline completion triggers Netlify redeployment within 15 minutes
- NFR32a: Failed deployments automatically rollback to previous working version
- NFR47: Chart HTML validates successfully before Netlify deployment goes live

### Compliance & Transparency

- NFR33: Notion page displays disclaimer "Not financial advice - data visualization tool for research purposes" prominently
- NFR34: Methodology documentation enables independent verification of calculation logic
- NFR35: "Last updated: X hours ago" timestamp displayed prominently on all chart views
- NFR36: Data source attribution documented (Glassnode, CryptoQuant) for transparency
- NFR37: Calculation methodology explanation published (LTH SOPR smoothing, LTH MVRV transformations)

### Browser Compatibility

- NFR38: Chart functions correctly on Chrome 90+, Firefox 88+, Safari 14+, Edge 90+ (latest 2 versions)
- NFR39: Chart renders properly on desktop viewports (1920x1080 optimal, 1280x720 minimum)
- NFR40: Chart supports tablet viewports (1024x768 landscape orientation)
- NFR41: Mobile viewports (<768px) display explicit "desktop experience recommended" message
- NFR42: Internet Explorer explicitly unsupported (no polyfills or degraded experience)

### Development & Deployment

- NFR45: Staging environment mirrors production for pre-launch validation

---
