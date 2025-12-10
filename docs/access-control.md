# Access Control Overview

This document describes the current "soft gate" in front of the Timing Terminal chart, and how it can evolve into a stricter, membership-aware system.

## Current Gate: Referer + Token (Story 2.4)

Story 2.4 introduces a **minimal access-control layer** implemented as a Netlify Edge Function. The goals are:

- Prevent the chart from being trivially public.
- Ensure the primary access path is via the Notion landing page.
- Establish a clear hook for future membership enforcement without changing the basic request shape.

### What the Edge Function Does

The `guard` Edge Function runs on the chart route (root `/`) and enforces **two checks** before allowing the request through:

1. **Referer allowlist**
   - Reads the `Referer` header from the incoming request.
   - Extracts the hostname (e.g. `www.notion.so`).
   - Allows the request only if the hostname is in an explicit allowlist (currently `notion.so` / `www.notion.so` and their subdomains).
   - If the referer is missing, invalid, or not allowed, it returns a `403 Access restricted` HTML response.

2. **Static token query parameter**
   - Reads the `token` query parameter from the URL.
   - Compares it against the `PUBLIC_EMBED_TOKEN` environment variable configured in Netlify.
   - If the token is missing, does not match, or the env var is not configured, the function returns the same `403 Access restricted` response.

If **both** checks pass, the function calls `context.next()` so the underlying chart page (`web/index.html`) and its assets behave exactly as before.

### Configuration

- **Netlify publish directory:** `web`
- **Edge Functions directory:** `netlify/edge-functions`
- **Active function:** `guard` on path `/` (root)
- **Environment variable:** `PUBLIC_EMBED_TOKEN`
- **Expected Notion embed URL shape:**
  - `https://<site-name>.netlify.app/?token=PUBLIC_EMBED_TOKEN`

### Security Model (Soft Gate)

This setup is intentionally a **soft barrier**, not a full security boundary:

- A motivated attacker could spoof `Referer` or exfiltrate the static token.
- For the MVP, this is acceptable: it blocks casual public sharing and keeps the main access path within Notion.
- Future stories will be responsible for turning this into a proper membership-aware gate.

## Future Membership Path (Planned Evolution)

This section sketches how the current scheme can be upgraded in later stories without breaking the embedding pattern.

### 1. Replace Static Token with Signed Tokens (e.g., JWT)

- Instead of a single shared `PUBLIC_EMBED_TOKEN`, issue a **per-session or per-member signed token**.
- The token could encode:
  - Member ID or subscription ID.
  - Expiration time.
  - Permissions or plan level.
- The Edge Function would:
  - Verify the token signature (using a shared secret or public key).
  - Check expiry and any embedded claims.
  - Deny access if invalid/expired.

The embed URL shape can stay the same (`?token=...`), but the token becomes a **short-lived signed credential** instead of a shared string.

### 2. Integrate with Billing / Membership System

Future stories can connect the Edge Function to a source of truth for membership:

- Stripe / Gumroad / Lemon Squeezy subscriptions.
- Notion database of members.
- Custom backend that issues tokens after login.

Typical flow:

1. Member completes purchase or login.
2. Backend issues a signed token with membership claims.
3. Notion (or another frontend) embeds the chart with `?token=<signed_token>`.
4. Edge Function validates token and member status on each request.

### 3. Hardening the Gate

When moving from soft gate to hard gate, consider:

- **More precise referer rules** (e.g., specific Notion page URLs or custom domain).
- **Rate limiting / anomaly detection** at the edge.
- **Better error responses** that differentiate user-facing copy from diagnostic logging.

## Non-Goals of Story 2.4

For clarity, Story 2.4 explicitly does **not**:

- Implement per-member auth or billing integration.
- Provide a login UI or account management.
- Guarantee that the chart cannot be accessed by a determined attacker.

It only establishes a small, clear layer at the edge that future stories can extend.
