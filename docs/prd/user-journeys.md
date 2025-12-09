# User Journeys

## Journey 1: Marcus Chen - From Decision Paralysis to Systematic Confidence

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

## Journey 2: Sarah Martinez - From FOMO to Framework Thinking (Phase 1.5)

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

## Journey 3: David Kim - The Convinced But Confused Non-Converter

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

## Journey 4: The Analyst (You) - Maintaining Trust Through Reliability

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

## Journey Requirements Summary

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
