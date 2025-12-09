# Product Scope

## MVP - Minimum Viable Product (Phase 1: Marcus Segment Only)

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

## Growth Features (Post-MVP)

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

## Vision (Future - 18+ Months)

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
