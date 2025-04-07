from typing import Any
import httpx

from dto import Criterion

async def make_api_request(url: str, token: str) -> dict[str, Any] | None:
    """Make an HTTP request to the API endpoint with proper error handling."""
    headers = {
        "Token": token
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            response_body = response.json()        
            return response_body.get("APIResponse")
        except Exception:
            return None
        
def compose_query_term(criteria: list[Criterion]) -> str:
    """Compose the query term based on the given criteria."""
    query_parts = []

    for criterion in criteria:
        field = criterion.field
        value = criterion.value
        operator = criterion.operator.value

        query_part = f"{field}{operator}{value}"
        query_parts.append(query_part)

    query_term = " AND ".join(query_parts)
    query_term = f"query={query_term}"
    return query_term