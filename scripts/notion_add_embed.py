"""Utilities to add an Embed block for the BTC Phase chart page in Notion.

Usage (from repo root):

    uv run python scripts/notion_add_embed.py

Required environment variables (set in .env or your shell):

    NOTION_API_KEY       - Notion integration secret
    BTC_PHASE_PAGE_ID    - Page ID of the BTC Phase Score (MVP) page
    BTC_PHASE_URL        - Netlify URL of the BTC Phase chart
"""

import os

from dotenv import load_dotenv
from notion_client import Client


def get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def add_btc_phase_embed() -> None:
    """Append a real Embed block for the BTC Phase chart to the configured page."""

    load_dotenv()

    api_key = get_env("NOTION_API_KEY")
    page_id = get_env("BTC_PHASE_PAGE_ID")
    embed_url = get_env("BTC_PHASE_URL")

    notion = Client(auth=api_key)

    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "embed",
                "embed": {"url": embed_url},
            }
        ],
    )

    print(f"Added embed block for {embed_url} to page {page_id}")


if __name__ == "__main__":
    add_btc_phase_embed()
