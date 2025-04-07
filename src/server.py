import os
from typing import Any
from helpers import make_api_request, compose_query_term
from dto import SearchRequest

from mcp.server.fastmcp import FastMCP

server = FastMCP("Demo")

BASE_URL = os.environ.get("CORTEX_BASE_URL")
TOKEN = os.environ.get("CORTEX_TOKEN")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@server.tool()
async def get_list_criteria() -> list[dict]:
    """Return the list of criteria"""
    url = f"{BASE_URL}/api/Search/v3.0/ListCriteria?format=JSON"
    criteria = await make_api_request(url, TOKEN)

    return criteria

@server.tool()
async def search_with_criteria(request: SearchRequest) -> dict[str, Any]:
    """Search for documents based on multiple criteria"""
    # Compose query term
    query_term = compose_query_term(request.criteria)

    # Compose fields term
    fields = set(["RecordID", "Doctype"])
    for field in request.returned_fields:
        fields.add(field)
    fields_term = "&".join([f"fields={x}" for x in fields])

    url = f"{BASE_URL}/api/Search/v3.0/Search?{query_term}&{fields_term}&format=JSON"
    result = await make_api_request(url, TOKEN)

    return result
    