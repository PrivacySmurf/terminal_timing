# Project Classification

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
