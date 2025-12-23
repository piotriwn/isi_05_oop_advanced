import pytest
from unittest.mock import Mock
from src.services import TVService
from src.repositories import TVMazeRepository
from src.models import Episode
from datetime import date


class TestTVService:
    @pytest.fixture
    def service(self):
        mock_repo = Mock(spec=TVMazeRepository)
        return TVService(mock_repo)

    @pytest.mark.parametrize("runtimes, expected_total", [
        ([60, 45, 30], 135),
        ([60, None, 30], 90),
        ([], 0),
        ([None, None], 0),
    ])
    def test_calculate_wasted_time(self, service, runtimes, expected_total):
        # Arrange
        episodes = [
            Episode(
                id=i,
                title=f"Ep {i}",
                release_date=date(2020, 1, 1),
                rating=5.0,
                season=1,
                number=i,
                runtime=r
            )
            for i, r in enumerate(runtimes)
        ]

        # Act
        total_time = service.calculate_wasted_time(episodes)

        # Assert
        assert total_time == expected_total
