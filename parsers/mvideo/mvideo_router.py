import math
from typing import Any, Annotated

from fastapi import APIRouter, Depends, Body

from .schemas import City
from .utils import search_location, fetch
from .filters import Filter
from .config import default_headers
from ..settings import settings


router = APIRouter(prefix=settings.api_v1_prefix + "/mvideo", tags=["MVideo"])


@router.post("/search")
def search(
    query: str = Annotated[str, Body()],
    city: City = Annotated[City, Depends(search_location)],
    headers: dict[str, Any] = default_headers(),
    offset: int = 0,
    limit: int = 50,
    filter: Filter = Filter.AVAILABLE_ONLY.value,
):
    cookies = {
        "MVID_CITY_ID": city.id,
        "MVID_REGION_ID": city.region,
        "MVID_REGION_SHOP": "S958",
        "MVID_TIMEZONE_OFFSET": "2",
    }
    params = {
        "offset": offset,
        "filterParams": filter,
        "limit": limit,
        "query": query,
    }

    response_body = fetch(
        "https://www.mvideo.ru/bff/products/v2/search",
        params=params,
        cookies=cookies,
        headers=headers,
    ).get("body")

    product_ids = response_body.get("products")
    pages_amount = math.ceil(response_body.get("total") / limit)
    for i in range(1, pages_amount - 1):
        params.update({"offset": limit * i + 1})
        product_ids.extend(
            fetch(
                "https://www.mvideo.ru/bff/products/v2/search",
                params=params,
                cookies=cookies,
                headers=headers,
            )
            .get("body")
            .get("products")
        )
    return product_ids
