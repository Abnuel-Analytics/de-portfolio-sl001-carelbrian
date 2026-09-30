"""Data contract for a product. Fill in the validation"""

from pydantic import BaseModel, field_validator  # noqa: F401


class Product(BaseModel):
    id: int
    title: str
    price: float
    category: str

    # TODO:  add a validator rejecting a negative price.
    @field_validator("price")
    @classmethod
    def price_must_be_non_negative(cls, value: float) -> float:
        if value < 0:
            raise ValueError("price must be non-negative")
        return value

    # TODO: add a validator rejecting a blank title.
    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("titre must not be blank")


def validate_records(raw: list[dict]) -> tuple[list[dict], int]:
    """Return (valid records as dicts, invalid count). Drop bad ones, don't raise"""
    # TODO: loop over raw; try Product(**item).model_dump(); count failures.
    valid_records: list[dict] = []
    invalid_count = 0

    for item in raw:
        try:
            product = Product(**item)
            valid_records.append(product.model_dump())
        except Exception:
            invalid_count += 1

    return valid_records, invalid_count
