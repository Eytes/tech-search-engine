from typing import Self

from pydantic import BaseModel, Field, model_validator


class City(BaseModel):
    name: str = Field(alias="cityName")
    id: str = Field(alias="cityId")
    region: str | None = None

    @model_validator(mode="after")
    def set_region(self) -> Self:
        self.region = self.id.split("_")[-1]
        return self
