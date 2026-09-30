"""I/O boundary: fetch raw records. Keep logic out of here."""

import requests

API_URL = "https://fakestoreapi.com/products"


def fetch_products(limit: int, url: str = API_URL, timeout: int = 30) -> list[dict]:
    response = requests.get(
        url,
        params={"limit": limit},
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()
