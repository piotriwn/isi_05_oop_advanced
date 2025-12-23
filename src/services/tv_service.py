import asyncio
from ..repositories.base import TVRepository
from ..models import TVShow, Episode
from .filters import EpisodeFilter


class TVService:
    def __init__(self, repository: TVRepository):
        self.repository = repository

    async def search_shows(self, query: str) -> list[TVShow]:
        return await self.repository.search_shows(query)

    async def get_full_show_info(self, show_id: int) -> tuple[TVShow | None, list[Episode]]:
        task_show_details = self.repository.get_show_details(show_id)
        task_episodes = self.repository.get_episodes(show_id)

        results = await asyncio.gather(task_show_details, task_episodes)

        show_details: TVShow | None = results[0]
        episodes: list[Episode] = results[1]

        return (show_details, episodes)

    def calculate_wasted_time(self, episodes: list[Episode]) -> int:
        return sum(ep.runtime for ep in episodes if ep.runtime is not None)

    def group_episodes_by_season(self, episodes: list[Episode]) -> dict[int, list[Episode]]:
        grouped = {}
        for ep in episodes:
            if ep.season not in grouped:
                grouped[ep.season] = []
            grouped[ep.season].append(ep)
        return grouped

    def filter_episodes(self, episodes: list[Episode], filter_strategy: EpisodeFilter) -> list[Episode]:
        return filter_strategy.filter(episodes)
