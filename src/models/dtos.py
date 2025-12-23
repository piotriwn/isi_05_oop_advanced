from datetime import date
from pydantic import BaseModel, Field, AliasPath


class TVShowDTO(BaseModel):
    id: int
    name: str
    premiered: date | None = None
    ended: date | None = None
    rating_avg: float | None = Field(
        default=None, validation_alias=AliasPath('rating', 'average')
    )
    status: str
    genres: list[str] = Field(default_factory=list)


class EpisodeDTO(BaseModel):
    id: int
    name: str
    season: int
    number: int
    airdate: date | None = None
    runtime: int | None = None
    rating_avg: float | None = Field(
        default=None, validation_alias=AliasPath('rating', 'average'))
