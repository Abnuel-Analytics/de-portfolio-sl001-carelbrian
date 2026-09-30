"""Validation test - required pydantic (installed iva `uv sync`)."""

from apisync.models import Product, validate_records


def test_valid_product_coerces_types():
    p = Product(id="1", title="Bag", price="10.5", category="bags")
    assert p.id == 1 and p.price == 10.5


def test_negative_price_rejected():
    import pytest

    with pytest.raises(Exception):
        Product(id=1, title="Bag", price=-1, category="bags")


def test_validate_records_counts_invalid():
    raw = [
        {"id": 1, "title": "Bag", "price": 10.0, "category": "bags"},
        {"id": 2, "title": " ", "price": 5.0, "category": "bags"},  # blank title
        {"id": 3, "title": "Hat", "price": -2.0, "category": "hats"},  # negative price
    ]
    valid, invalid = validate_records(raw)
    assert len(valid) == 1 and invalid == 2
