from abc import ABC, abstractmethod
from ..models import TVShow, Episode


class TVRepository(ABC):
    @abstractmethod
    async def search_shows(self, query: str) -> list[TVShow]:
        pass

    @abstractmethod
    async def get_show_details(self, show_id: int) -> TVShow | None:
        pass

    @abstractmethod
    async def get_episodes(self, show_id: int) -> list[Episode]:
        pass
