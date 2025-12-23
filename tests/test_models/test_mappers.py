import pytest
from datetime import date
from src.models import TVShowDTO, EpisodeDTO, TVShowMapper, EpisodeMapper, ShowStatus


class TestTVShowMapper:
    def test_map_valid_show_from_json(self, raw_show_data):
        # Arrange
        dto = TVShowDTO(**raw_show_data)

        # Act
        domain = TVShowMapper.map_to_domain(dto)

        # Assert
        assert domain.id == 23
        assert domain.title == "Once Upon a Time in Wonderland"
        assert domain.release_date == date(2013, 10, 10)
        assert domain.end_date == date(2014, 4, 3)
        assert domain.rating == 6.8
        assert domain.status == ShowStatus.ENDED
        assert "Fantasy" in domain.genres


class TestEpisodeMapper:
    def test_map_valid_episodes_from_json(self, raw_episodes_data):
        # Arrange
        dtos = [EpisodeDTO(**ep) for ep in raw_episodes_data]

        # Act
        domain_episodes = [EpisodeMapper.map_to_domain(dto) for dto in dtos]

        # Assert
        assert len(domain_episodes) == 2
        ep1 = domain_episodes[0]
        assert ep1.id == 1301
        assert ep1.title == "Down the Rabbit Hole"
        assert ep1.season == 1
        assert ep1.number == 1
        assert ep1.release_date == date(2013, 10, 10)
        assert ep1.runtime == 60
        assert ep1.rating == 6.9
