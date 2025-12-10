"""Sync chart embeds from the ⚡ Timing Terminal 2 (Source) database into their pages.

For each row in the database:
- Reads the Chart URL property
- Appends an Embed block with that URL to the page (if Chart URL is present)

Usage (from repo root):

    python scripts/notion_sync_chart_embeds.py

The script expects environment variables defined in `.env` or your shell:

    NOTION_API_KEY    - Notion integration secret
    TT2_DATABASE_ID   - The database ID of ⚡ Timing Terminal 2 (Source)
"""

from __future__ import annotations

import os
from typing import Any, Dict, List

from dotenv import load_dotenv
from notion_client import Client


def get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def fetch_all_rows(notion: Client, database_id: str) -> List[Dict[str, Any]]:
    """Fetch all rows from the database (single-page query for now)."""
    resp = notion.databases.query(database_id=database_id)
    return resp.get("results", [])


def extract_chart_url(properties: Dict[str, Any]) -> str | None:
    """Extract Chart URL from a page properties dict.

    For a URL property, the Notion API returns an object like:

        "Chart URL": {"id": "...", "type": "url", "url": "https://..."}

    We only care about the `url` field.
    """

    chart_prop = properties.get("Chart URL")
    if not isinstance(chart_prop, dict):
        return None
    url = chart_prop.get("url")
    if isinstance(url, str) and url:
        return url
    return None


def extract_name(properties: Dict[str, Any]) -> str:
    name_prop = properties.get("Name")
    if isinstance(name_prop, dict):
        title = name_prop.get("title") or []
        if title and isinstance(title[0], dict):
            return title[0].get("plain_text", "Untitled")
    return "Untitled"


def sync_embeds() -> None:
    load_dotenv()

    api_key = get_env("NOTION_API_KEY")
    db_id = get_env("TT2_DATABASE_ID")

    notion = Client(auth=api_key)

    rows = fetch_all_rows(notion, db_id)
    print(f"Found {len(rows)} rows in Timing Terminal 2 (Source)")

    for row in rows:
        page_id = row["id"]
        props = row.get("properties", {})

        name = extract_name(props)
        chart_url = extract_chart_url(props)

        if not chart_url:
            print(f"- Skipping {name} ({page_id}): no Chart URL set")
            continue

        print(f"- Adding embed for {name} ({page_id}): {chart_url}")

        notion.blocks.children.append(
            block_id=page_id,
            children=[
                {
                    "object": "block",
                    "type": "embed",
                    "embed": {"url": chart_url},
                }
            ],
        )

    print("Done syncing embeds.")


if __name__ == "__main__":
    sync_embeds()
