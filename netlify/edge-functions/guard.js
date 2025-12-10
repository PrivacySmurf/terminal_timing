export default async (request, context) => {
  const url = new URL(request.url);

  // Basic 403 helper
  const denied = (reason) => {
    // Do not leak internals; keep message simple
    const body = `<!doctype html><html><head><title>Access restricted</title></head><body><h1>Access restricted</h1><p>This chart is only available from the authorized Timing Terminal context.</p></body></html>`;
    return new Response(body, {
      status: 403,
      headers: {
        'content-type': 'text/html; charset=utf-8',
        'x-access-denied-reason': reason,
      },
    });
  };

  // 1) Referer allowlist
  const referer = request.headers.get('referer');
  const allowedHosts = [
    'notion.so',
    'www.notion.so',
    'notion.site',
  ];

  if (!referer) {
    return denied('missing-referer');
  }

  let refererHost;
  try {
    const refererUrl = new URL(referer);
    refererHost = refererUrl.hostname;
  } catch {
    return denied('invalid-referer');
  }

  const refererAllowed = allowedHosts.some((host) => refererHost === host || refererHost.endsWith(`.${host}`));
  if (!refererAllowed) {
    return denied('referer-not-allowed');
  }

  // 2) Static token check
  const token = url.searchParams.get('token');
  const expectedToken = Deno.env.get('PUBLIC_EMBED_TOKEN');

  if (!expectedToken) {
    // Misconfiguration: fail closed rather than open
    return denied('token-not-configured');
  }

  if (!token || token !== expectedToken) {
    return denied('invalid-token');
  }

  // All checks passed: continue to underlying site
  return context.next();
};
