# Epic 2: Frontend Chart Delivery – TradingView + Netlify + Notion

## Epic Goal

Deliver a production-ready frontend experience that renders the Bitcoin phase chart from `chart-data.json` using TradingView Lightweight Charts, hosts it on Netlify, and embeds it into Notion with basic access control and UX aligned to the MVP PRD.

The pipeline from Epic 1 produces reliable `chart-data.json`. Epic 2 focuses on everything from that JSON file to the user’s browser, ensuring the chart is fast, readable, and easy to access from Notion.

## Story List (High-Level)

- **Story 2.1 – Minimal TradingView Chart Page**  
  Build a static HTML + TypeScript page that consumes a local `chart-data.json` file and renders a combined BTC price + phase score chart using TradingView Lightweight Charts.

- **Story 2.2 – Netlify Build & Static Asset Wiring**  
  Wire the chart page into a minimal frontend build/deploy setup (Netlify) so that `chart-data.json` and the HTML/JS/CSS bundle are deployed and served from a stable public URL.

- **Story 2.3 – Notion Embedding & Layout Integration**  
  Embed the Netlify-hosted chart into a Notion page, validate sizing and interaction behavior, and ensure the above-the-fold layout matches the MVP PRD expectations for Marcus.

- **Story 2.4 – Basic Access Control & Referer Guard (Edge Function)**  
  Implement a minimal Netlify Edge Function (or equivalent) that restricts chart asset access to requests originating from approved Notion pages, laying the groundwork for member-only access.

- **Story 2.5 – UX Polish & A11y Baseline**  
  Apply basic visual polish (dark theme, labels, legends) and ensure keyboard focus and basic accessibility are reasonable for the initial MVP experience.

> Detailed, fully fleshed-out story documents (e.g., `2.1`, `2.2`, etc.) will be created just-in-time for each story, using this epic outline plus the PRD and architecture docs.
