from ..settings import settings


def default_headers():
    return {
        "Accept": "application/json",
        "Sec-Fetch-Site": "same-origin",
        "Accept-Language": "ru",
        "Sec-Fetch-Mode": "cors",
        "User-Agent": settings.user_agent,
        "Sec-Fetch-Dest": "empty",
    }
