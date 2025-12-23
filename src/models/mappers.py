from .dtos import TVShowDTO, EpisodeDTO
from .domain import Domain, TVShow, Episode
from .enums import ShowStatus


class TVShowMapper:
    @staticmethod
    def map_to_domain(dto: TVShowDTO) -> TVShow:
        try:
            status_enum = ShowStatus(dto.status)
        except ValueError:
            status_enum = ShowStatus.UNKNOWN

        return TVShow(
            id=dto.id,
            title=dto.name,
            release_date=dto.premiered,
            end_date=dto.ended,
            rating=dto.rating_avg,
            genres=dto.genres,
            status=status_enum
        )


class EpisodeMapper:
    @staticmethod
    def map_to_domain(dto: EpisodeDTO) -> Episode:
        return Episode(
            id=dto.id,
            title=dto.name,
            release_date=dto.airdate,
            rating=dto.rating_avg,
            season=dto.season,
            number=dto.number,
            runtime=dto.runtime
        )
