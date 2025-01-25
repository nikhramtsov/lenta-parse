import pydantic

class Price(pydantic.BaseModel):
    price: int
    priceRegular: int

class Item(pydantic.BaseModel):
    id: int
    name: str
    prices: Price


class ApiResponse(pydantic.BaseModel):
    items: list[Item]
    total: int


class ApiRequestPayload(pydantic.BaseModel):
    categoryId: int
    sort: dict[str, str]
    offset: int
    limit: int
