from dataclasses import dataclass
from datetime import date
from typing import ClassVar, Final
from abc import ABC, abstractmethod
from .enums import ShowStatus


class Domain(ABC):
    pass


@dataclass
class TVShow(Domain):
    id: int
    title: str
    release_date: date | None
    end_date: date | None
    rating: float | None
    genres: list[str]
    status: ShowStatus

    GOOD_SHOW_CUTOFF: ClassVar[Final[float]] = 8.0
    NEW_SHOW_CUTOFF: ClassVar[Final[date]] = date(2020, 1, 1)

    def is_highly_rated(self) -> bool | None:
        return self.rating >= TVShow.GOOD_SHOW_CUTOFF if self.rating else None

    def is_new_show(self) -> bool | None:
        if self.release_date is None:
            return None
        return self.release_date >= TVShow.NEW_SHOW_CUTOFF

    def get_years_active(self) -> int | None:
        if not self.release_date:
            return None
        end = self.end_date if self.end_date else date.today()
        return end.year - self.release_date.year

    def is_running(self) -> bool:
        return self.status == ShowStatus.RUNNING


@dataclass
class Episode(Domain):
    id: int
    title: str
    release_date: date | None
    rating: float | None
    season: int
    number: int
    runtime: int | None

    GOOD_EPISODE_CUTOFF: ClassVar[Final[float]] = 8.0

    def is_highly_rated(self) -> bool | None:
        return self.rating >= Episode.GOOD_EPISODE_CUTOFF if self.rating else None
