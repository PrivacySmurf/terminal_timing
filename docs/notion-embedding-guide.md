# Notion Embedding Guide for Timing Terminal Chart

This guide explains how to embed the Netlify-hosted Timing Terminal chart into a Notion page, keep it above the fold with supporting copy, and update it in the future.

## 1. Prerequisites

- Netlify production URL for the chart page from Story 2.1 / 2.2, e.g.
  - `https://<site-name>.netlify.app` or your custom domain
- Access to the Timing Terminal Notion workspace/teamspace

> Recommendation: **Always use the stable production URL** (or custom domain) as the canonical embed target. Avoid deploy previews or branch-specific URLs for the main Notion embed.

## 2. Creating / Selecting the Notion Host Page

1. Open Notion and navigate to the workspace/teamspace where the Timing Terminal content lives.
2. Either:
   - Create a new page (e.g., **“Timing Terminal – Bitcoin Phase Score”**), or
   - Reuse an existing landing page designated in the PRD.
3. Ensure this page is where you want both **onboarding content** and the **chart** to live.

## 3. Structuring the Page (Above-the-Fold Layout)

Goal: chart visible above the fold on a typical desktop, with nearby context.

1. At the top of the page, add:
   - A concise title (e.g., “Bitcoin Phase Score – Interactive Chart”).
   - A short 1–2 sentence value proposition.
2. Immediately under that, reserve space for the **chart embed block**.
3. Under the chart embed, add supporting sections:
   - **Methodology (brief)** – 2–4 sentences explaining what the chart shows.
   - **Track record / validation pointer** – a link or reference to deeper analysis or backtests.
   - Longer narrative or deep-dive sections can go **below the fold**.

## 4. Embedding the Netlify Chart URL in Notion

1. Copy the production Netlify URL for the chart page, for example:
   - `https://<site-name>.netlify.app`
2. In the Notion page, position your cursor where the chart should appear.
3. Paste the URL directly and wait for Notion’s embed options to appear.
4. Choose **“Create embed”** (preferred) or **“Create bookmark”** if embed is not available.
5. Once the embed block is created:
   - Drag to adjust height so the chart is clearly visible.
   - Optionally adjust width (e.g., full-width page layout or wide column) to avoid horizontal scrollbars.

## 5. Copy and Context Around the Embed

Near the chart (above or immediately below), include:

1. **What the chart shows**
   - Example: “This chart shows Bitcoin price over time with our proprietary phase score, which summarizes market regime into a single line.”
2. **How to explore**
   - Example bullet points:
     - “Zoom into the 2021 peak to see how the phase score behaved near cycle tops.”
     - “Compare the 2022 bottom to the current phase score level.”
     - “Use the crosshair/tooltip to align BTC price and phase score on specific dates.”
3. **Disclaimer**
   - A minimal statement such as: “This is not financial advice. For educational and informational purposes only.”

## 6. Validating Layout and Interaction

On desktop:

1. Confirm the chart is visible **without scrolling** on a typical desktop viewport (e.g., 1080p / 1440p width).
2. Interact with the chart inside the embed:
   - Zoom / pan.
   - Hover to see tooltips / crosshair.
3. Verify there are **no awkward horizontal scrollbars**.

On narrower widths (optional but recommended):

1. Resize the browser window or open the Notion page on a tablet-sized viewport.
2. Confirm the chart remains usable (even if less optimal):
   - No completely broken layout.
   - Tooltips/zoom still function.

## 7. Updating the Embed if the Netlify URL Changes

If the production URL changes (e.g., new domain, renamed Netlify site):

1. Obtain the new canonical production URL.
2. In the Notion page:
   - Hover over the existing embed block.
   - Use the block menu (`…`) and choose **Replace** or **Edit** (depending on Notion’s UI at the time).
3. Paste the new URL and re-confirm:
   - The chart loads correctly.
   - Layout and interactions remain acceptable.
4. Optionally keep a small **“Implementation notes”** toggle on the page recording the current URL and last update date.

## 8. Known / Potential Limitations

When working with Notion embeds:

- **Mobile app behavior**
  - Some mobile clients may render iframes in a more constrained way; chart may feel cramped.
  - If the chart feels unusable on mobile, capture this as a known limitation rather than blocking the story.
- **Caching / refresh**
  - Notion may cache previews; if a new deploy changes styling, a hard refresh or reopen of the page may be needed.
- **Network / referer constraints**
  - Access control and referer validation are explicitly **out of scope for Story 2.3** and handled in later stories.

## 9. Quick Checklist for Story 2.3 Tasks

Use this as a fast pass when implementing or reviewing:

1. Host Notion page chosen/created for the MVP chart.
2. Chart embed block added using the production Netlify URL.
3. Chart visible above the fold on desktop; no awkward horizontal scrolling.
4. Copy around the chart explains what it is, how to explore, and includes a simple disclaimer.
5. Basic responsiveness manually validated on at least one narrower viewport.
6. This guide (or equivalent) referenced from story/dev notes so future changes are straightforward.
