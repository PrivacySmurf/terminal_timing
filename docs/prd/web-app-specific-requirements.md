# Web App Specific Requirements

## Project-Type Overview

Public_plots is a **static HTML web application** with embedded interactive JavaScript components. The architecture centers on a single, self-contained HTML file that embeds TradingView Lightweight Charts for interactive data visualization. This is not a Single Page Application (SPA) with client-side routing - it's a focused, static page optimized for one purpose: interactive chart exploration with professional-grade performance.

The deployment model leverages **Netlify's edge network** for global CDN distribution, with **Edge Functions** handling access control via referer validation. Daily automated Python pipeline updates generate new chart data, which triggers Netlify redeployment of the updated HTML file. Users access the chart through **Notion embedding** - the Notion page acts as the content wrapper (methodology explainer, track record, educational context) while the embedded chart provides the interactive experience.

This architecture choice prioritizes:
- **Simplicity**: No complex build process, state management, or routing frameworks
- **Performance**: Static HTML served from CDN with minimal JavaScript overhead
- **Reliability**: No backend dependencies at request time (chart data pre-generated)
- **Scalability**: CDN handles 50-100 concurrent users without application-level scaling concerns

## Technical Architecture Considerations

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

## Performance Targets & Validation

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

## Data Pipeline Contract & Error Handling

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

## Notion Iframe Embedding Considerations

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

## SEO & Discovery Strategy

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
- Users find timing_terminal via **newsletter**, not search engines
- Chart access is **gated content** delivered after payment
- SEO irrelevant for MVP - growth via newsletter audience, not organic search

## Accessibility Compliance

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

## Implementation Considerations

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
