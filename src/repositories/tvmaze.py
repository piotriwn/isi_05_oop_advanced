import aiohttp
from urllib.parse import urljoin
from typing import Any, Callable
from pydantic import BaseModel
from .base import TVRepository
from ..models import TVShow, Episode, TVShowDTO, EpisodeDTO, TVShowMapper, EpisodeMapper
from ..utils.exceptions import APIConnectionError, ResourceNotFoundError, AppError, DeserializationError, MappingError


class TVMazeRepository(TVRepository):
    BASE_URL = "https://api.tvmaze.com"

    session: aiohttp.ClientSession

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def _fetch(self, endpoint_suffix: str, params: dict | None = None) -> Any:
        url = urljoin(TVMazeRepository.BASE_URL, endpoint_suffix)

        try:
            async with self.session.get(url, params=params) as response:
                if response.status == 404:
                    raise ResourceNotFoundError

                if response.status >= 500:
                    raise APIConnectionError(
                        f"TVMaze server error: {response.status}")

                response.raise_for_status()
                return await response.json()

        except aiohttp.ClientError as e:
            raise APIConnectionError(f"Connection failed: {str(e)}")
        except Exception as e:
            raise AppError(f"Unexpected error: {str(e)}")

    def _map_data(self, data_list: list[dict], dto_cls: type[BaseModel], mapper_func: Callable[[Any], Any]) -> list[Any]:
        try:
            dtos = [dto_cls(**item) for item in data_list]
        except Exception as e:
            raise DeserializationError(
                f"Validation error for: {dto_cls.__name__}: {str(e)}")

        try:
            return [mapper_func(dto) for dto in dtos]
        except Exception as e:
            raise MappingError(f"Mapping error: {str(e)}")

    async def search_shows(self, query: str) -> list[TVShow]:
        data = await self._fetch("search/shows", params={"q": query})

        if not data:
            return []

        try:
            raw_shows = [item['show'] for item in data]
        except (KeyError, TypeError):
            raise DeserializationError(
                "Unexpected API response structure for search")

        return self._map_data(
            raw_shows,
            TVShowDTO,
            TVShowMapper.map_to_domain)

    async def get_show_details(self, show_id: int) -> TVShow | None:
        data = await self._fetch(f"shows/{show_id}")

        if not data:
            return None

        show_domain = self._map_data(
            [data],
            TVShowDTO,
            TVShowMapper.map_to_domain)[0]

        return show_domain

    async def get_episodes(self, show_id: int) -> list[Episode]:
        data = await self._fetch(f"shows/{show_id}/episodes")

        if not data:
            return []

        episodes_domains = self._map_data(
            data,
            EpisodeDTO,
            EpisodeMapper.map_to_domain)

        return episodes_domains
