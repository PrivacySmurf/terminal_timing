# User Journeys

This shard captures the key user journeys that drive requirements for the system. The full narrative detail remains in `docs/prd.md`; here we focus on the main flows and extracted requirements.

### Journey 1: Marcus Chen – From Decision Paralysis to Systematic Confidence

Marcus is a 38-year-old experienced investor with a six-figure BTC position and high emotional load (including family capital). He is overwhelmed by conflicting analyst opinions and past drawdown trauma.

He lands on the Notion page and, within seconds:
- Sees the interactive BTC + Phase Score chart **above the fold**
- Sees a single-sentence value prop: "Glassnode shows you the raw data (WHAT). We show you when to act (WHEN)."
- Is guided by a cue: "👈 Zoom into the 2021 peak to see how we called the top."

He zooms into November 2021, verifies Phase Score behavior around the peak (mid-80s before the top), and later repeats the same for the 2022 bottom (~12). Over time, he:
- Monitors Phase Score approaching distribution zones (75–85+)
- Systematically reduces exposure (e.g., sell 40% at ~82) based on the chart, not Twitter

**Key requirements revealed:**
- Daily Python pipeline computing Phase Score with historical data back to 2020
- TradingView Lightweight Charts with smooth zoom/pan (<2s load, 60fps)
- Single Notion page with the chart embedded above the fold
- Clear zone overlays and labels (0–20 retention, 80–100 distribution)
- Methodology explainer and historical track record section **below** the chart
- Prominent "Last updated" timestamp for trust
- Netlify hosting and access control to protect premium content

### Journey 2: Sarah Martinez – From FOMO to Framework Thinking (Phase 1.5)

Sarah is a 29-year-old first-cycle investor with limited technical background and high susceptibility to FOMO/panic.

She enters via a **$5 trial** and a guided onboarding path:
- Tutorial 1: The 2021 Peak – guided zoom, overlays, and plain-English explanations
- Tutorial 2: The 2022 Bottom – understanding retention zones and accumulation
- Tutorial 3: Current cycle – applying the framework

She uses:
- Tooltips that explain SOPR, MVRV, retention, distribution in non-jargon language
- A progress indicator (e.g., "step 3 of 8")
- Email prompts to return and finish tutorials

Eventually she graduates to the **Advanced** view, same as Marcus, and makes her first systematic profit-taking decision around Phase Score ~80.

**Key requirements (Phase 1.5+):**
- Educational overlay layer on top of the base chart (guided tours, tooltips)
- Tutorial state management (resume in place)
- Email triggers based on tutorial progress (e.g., "complete Tutorial 1")
- Toggle between Educational and Advanced modes

### Journey 3: David Kim – The Convinced But Confused Non-Converter

David, a 42-year-old financial analyst, already pays for Glassnode and reads many newsletters. He is intellectually convinced by the Phase Score methodology but is unsure whether this product is redundant with his existing tools.

He needs:
- Clear competitive positioning: "Glassnode/CryptoQuant show WHAT; timing_terminal shows WHEN"
- A succinct explanation of how this complements, not replaces, his existing stack
- Easy re-access: bookmarkable link and simple URL structure

This journey highlights the need for:
- Strong above-the-fold positioning copy
- A brief competitive context section
- Good linkability and low-friction re-entry to the chart

### Journey 4: The Analyst (You) – Maintaining Trust Through Reliability

You, as the analyst/operator, must:
- Respond quickly when the pipeline fails, especially in critical zones
- Have a manual fallback runbook (backup data source, manual Phase Score calculation, communication plan)
- Track chart requests and use them to prioritize Phase 2 charts

**System requirements from this journey:**
- Tiered uptime targets (95% neutral, 99% critical)
- Discord + SMS/email alerts on pipeline failures
- Manual runbook and backup data strategy
- Chart request tracking (simple Notion DB or equivalent)

---

These journeys drive the architecture decisions already captured elsewhere: a robust Python pipeline, TV chart front-end, Netlify/Notion integration, and strong monitoring/alerting behavior.
