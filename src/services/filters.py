from abc import ABC, abstractmethod
from datetime import date
from ..models import Episode

# TODO:
# I need to im

class EpisodeFilter(ABC):
    @abstractmethod
    def filter(self, episodes: list[Episode]) -> list[Episode]:
        ...


class YearFilter(EpisodeFilter):
    def __init__(self, year: int):
        self.year = year

    def filter(self, episodes: list[Episode]) -> list[Episode]:
        return [
            ep for ep in episodes
            if ep.release_date and ep.release_date.year == self.year
        ]


class SeasonFilter(EpisodeFilter):
    def __init__(self, season_number: int):
        self.season_number = season_number

    def filter(self, episodes: list[Episode]) -> list[Episode]:
        return [
            ep for ep in episodes
            if ep.season == self.season_number
        ]


class UpcomingFilter(EpisodeFilter):
    def filter(self, episodes: list[Episode]) -> list[Episode]:
        return [
            ep for ep in episodes
            if ep.release_date and ep.release_date > date.today()
        ]
