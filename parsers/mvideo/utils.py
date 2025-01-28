from typing import Any, Annotated

import requests
from fastapi import Body, Depends

from .config import default_headers
from .schemas import City


def fetch(
    url: str,
    headers: dict[str, Any] = default_headers(),
    cookies: dict[str, Any] | None = None,
    params: dict[str, Any] | None = None,
) -> dict:
    return requests.get(url=url, headers=headers, cookies=cookies, params=params).json()


def search_location(
    city: Annotated[str, Body()],
    headers: Annotated[dict[str, Any], Depends(default_headers)],
) -> City | None:
    """
    Поиск id города по его названию. Если найдено полное соответствие, то возвращается словарь, иначе None.
    Сравнение названий в верхнем регистре.
    """
    response = fetch(
        "https://www.mvideo.ru/bff/region/searchLocation",
        params={"query": city},
        headers=headers,
    )
    for city_info in response.get("body").get("results"):
        city_info: dict
        if city_info.get("cityName").upper() == city.upper():
            return City(**city_info)
