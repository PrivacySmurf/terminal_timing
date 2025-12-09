# Non-Functional Requirements

## Performance

- NFR1: Chart initial load completes in <2 seconds on 10 Mbps broadband connection (target: 1.5s)
- NFR1a: Load time validated on 5 Mbps throttled connection (worst case) before launch
- NFR2: Chart reaches interactive state (zoom/pan functional) within 2.5 seconds of page load
- NFR3: Zoom and pan operations render at 60 FPS minimum without visible lag or stuttering
- NFR4: Crosshair tooltips display within 50ms of hover action
- NFR5: Chart page weight remains under 400kb (HTML + library + data combined)
- NFR6: Chart maintains 60 FPS performance when rendering 500-700 data points maximum
- NFR6a: Chart decimates daily data to <700 points when viewing full historical range (5+ years)
- NFR7: CDN serves chart HTML globally with <100ms latency from edge servers

## Security

- NFR8: Chart access restricted to Notion referer headers via edge function validation
- NFR9: Payment processing handled by PCI-compliant third-party providers (Stripe/Gumroad)
- NFR10: User authentication and access management delegated to Notion platform (no custom auth)
- NFR11: Token parameter signatures validated to prevent forgery when per-member access control enabled (Phase 2)
- NFR12: All data transmission occurs over HTTPS/TLS encryption
- NFR13: No sensitive user data (passwords, payment info) stored in custom infrastructure
- NFR13a: Code review confirms no PII/payment data persisted to logs or storage

## Scalability

- NFR14: System supports 50-100 concurrent users without performance degradation at launch
- NFR15: Infrastructure costs remain under $50/month at 100-user scale
- NFR16: CDN architecture supports scaling to 200-300 users (Phase 2) without application redesign
- NFR17: Static HTML deployment model eliminates backend scaling concerns
- NFR18: Chart data generation pipeline scales linearly with additional chart types (Phase 2)
- NFR18a: Chart data JSON files remain under 300kb per chart type for CDN efficiency

## Reliability

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

## Integration

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

## Compliance & Transparency

- NFR33: Notion page displays disclaimer "Not financial advice - data visualization tool for research purposes" prominently
- NFR34: Methodology documentation enables independent verification of calculation logic
- NFR35: "Last updated: X hours ago" timestamp displayed prominently on all chart views
- NFR36: Data source attribution documented (Glassnode, CryptoQuant) for transparency
- NFR37: Calculation methodology explanation published (LTH SOPR smoothing, LTH MVRV transformations)

## Browser Compatibility

- NFR38: Chart functions correctly on Chrome 90+, Firefox 88+, Safari 14+, Edge 90+ (latest 2 versions)
- NFR39: Chart renders properly on desktop viewports (1920x1080 optimal, 1280x720 minimum)
- NFR40: Chart supports tablet viewports (1024x768 landscape orientation)
- NFR41: Mobile viewports (<768px) display explicit "desktop experience recommended" message
- NFR42: Internet Explorer explicitly unsupported (no polyfills or degraded experience)

## Development & Deployment

- NFR45: Staging environment mirrors production for pre-launch validation

---
