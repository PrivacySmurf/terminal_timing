# Functional Requirements

## Data Pipeline & Calculation

- FR1: System can execute proprietary Bitcoin phase score calculations daily using LTH SOPR smoothing and LTH MVRV transformations
- FR2: System can output phase scores on a 0-100 scale with supply retention zone (0-20) and distribution zone (80-100) identification
- FR3: System can generate chart data in JSON format with BTC price and phase score time series
- FR4: System can automatically deploy updated chart data to hosting platform on successful pipeline execution
- FR5: System can fall back to alternate data sources when primary data provider is unavailable
- FR6: System can validate calculation correctness against manual verification within ±0.3 phase score points
- FR7: System can maintain historical data consistency for backtested period (2020-present)

## Interactive Chart Visualization

- FR8: Users can view interactive Bitcoin price chart with overlaid phase score using professional-grade charting library
- FR9: Users can zoom into specific time periods using mouse/touch gestures
- FR10: Users can pan across historical data from 2020 to present
- FR11: Users can view crosshair tooltips showing exact BTC price and phase score values at specific dates
- FR12: Users can see phase score dynamically rescaled to visible BTC price range for readability
- FR13: Users can see supply zone overlays with inline labels marking retention (0-20) and distribution (80-100) zones
- FR14: Users can view chart in dark mode with rounded borders and modern visual polish
- FR15: Users can interact with chart immediately without requiring focus click (iframe interaction handling)

## Content Presentation & Access

- FR16: Users can access chart embedded in Notion page with chart displayed above the fold
- FR17: Users can view single-sentence value proposition above chart distinguishing service from competitors
- FR18: Users can view methodology explainer positioned below chart describing calculation approach
- FR19: Users can view historical track record section showing 2021 top and 2022 bottom timing validation with specific dates and phase scores
- FR20: Users can see "Last updated: X hours ago" timestamp prominently displayed
- FR21: Users can see visual cue pointing to chart encouraging historical exploration
- FR22: Users can view disclaimer stating "Not financial advice - data visualization tool for research purposes"
- FR23: Users can access persistent bookmark-friendly chart URL

## Access Control & Security

- FR24: System can validate referer headers to restrict chart access to Notion-only embedding
- FR25: System can support token parameter for per-member access control (built but not enforced in Phase 1)
- FR26: System can grant Notion page access based on subscription status via payment provider webhooks
- FR27: System can revoke Notion page access when subscription is canceled or payment fails

## Monitoring & Reliability

- FR28: System can notify admin via Discord webhook on successful daily pipeline execution with current BTC price and phase score
- FR29: System can alert admin via Discord webhook when pipeline fails with error indication
- FR30: System can escalate to SMS/email alert when pipeline fails during critical market conditions (Phase Score <20 or >80)
- FR31: System can track pipeline uptime separately for normal conditions (Phase Score 20-80) vs critical conditions (Phase Score <20 or >80)
- FR32: System can log pipeline errors with timestamps and failure mode categorization
- FR33: Admin can access manual calculation runbook documentation for emergency backup calculations
- FR34: Admin can post manual phase score updates to emergency communication channels when automated pipeline fails

## Member Engagement & Feedback

- FR35: Members can submit chart requests via email or direct message
- FR36: Admin can log chart requests in tracking system with request description, date, member name, and category
- FR37: Admin can categorize chart requests by type (exchange flows, valuation, supply, derivatives, cross-asset)
- FR38: Admin can identify recurring request patterns when 3+ members request same chart type
- FR39: Admin can communicate Phase 2 roadmap decisions to members with rationale based on request patterns
- FR40: Admin can respond to out-of-scope requests with realistic timeline expectations and transparency about tracking

## Educational Experience (Phase 1.5 - Deferred)

- FR41: First-cycle investors can access educational onboarding path separate from experienced investor flow
- FR42: Users can complete guided historical explorations through interactive tutorials covering 2021 peak, 2022 bottom, and current cycle
- FR43: Users can view tooltip overlays explaining on-chain terminology in plain English
- FR44: Users can see tutorial progress indicators showing current step position
- FR45: Users can resume tutorials from where they left off via state management
- FR46: Users can receive email reminders to complete started but unfinished tutorials within 24 hours
- FR47: Users can toggle between educational mode (with tooltips) and advanced mode (streamlined)
- FR48: Users can see success messaging when graduating to advanced mode
- FR49: Users can access $5 trial subscription offering before converting to $20/month standard pricing

## Performance & Compatibility

- FR50: Chart can load in under 2 seconds on 10 Mbps broadband connection
- FR51: Chart can render zoom/pan interactions at 60 FPS without lag or stuttering
- FR52: Chart can display tooltip responses within 50ms of hover action
- FR53: Chart can function correctly on Chrome 90+, Firefox 88+, Safari 14+, and Edge 90+
- FR54: Chart can render properly on desktop (1920x1080) and tablet (1024x768) viewports
- FR55: System can support 50-100 concurrent users without performance degradation
- FR56: System can serve chart globally with CDN latency under 100ms

## Analytics & Measurement (Phase 2 - Tracking Deferred)

- FR57: System can track member check frequency and time-on-chart duration
- FR58: System can identify correlation between hub usage and phase score transitions
- FR59: System can measure first-session zoom rate as aha moment indicator
- FR60: System can track tutorial completion rates for educational path users
- FR61: System can measure tooltip usage declining over time as learning progression indicator
- FR62: Admin can view Phase 2 gate criteria dashboard showing member count, retention percentage, and chart request patterns

---
