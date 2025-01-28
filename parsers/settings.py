from pydantic_settings import BaseSettings
from pydantic import BaseModel


class ApiV1Settings(BaseModel):
    prefix: str = "/api/v1"
    mvideo_prefix: str = "/mvideo"


class ApiSettings(BaseModel):
    v1: ApiV1Settings = ApiV1Settings()


class Settings(BaseSettings):
    api: ApiSettings = ApiSettings()
    user_agent: str = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15"


settings = Settings()
