import pytest
from datetime import date
from src.services import YearFilter
from src.models import Episode


class TestYearFilter:
    @pytest.fixture
    def episodes(self):
        return [
            Episode(id=1, title="Ep 1", release_date=date(2019, 12, 31),
                    rating=8.0, season=1, number=1, runtime=60),
            Episode(id=2, title="Ep 2", release_date=date(2020, 1, 1),
                    rating=8.0, season=1, number=2, runtime=60),
            Episode(id=3, title="Ep 3", release_date=date(2020, 6, 15),
                    rating=8.0, season=1, number=3, runtime=60),
            Episode(id=4, title="Ep 4", release_date=date(2021, 1, 1),
                    rating=8.0, season=1, number=4, runtime=60),
            Episode(id=5, title="Ep 5", release_date=None,
                    rating=8.0, season=1, number=5, runtime=60),
        ]

    @pytest.mark.parametrize("year, expected_count, expected_ids", [
        (2020, 2, {2, 3}),
        (2019, 1, {1}),
        (2021, 1, {4}),
        (2022, 0, set()),
    ])
    def test_filter_by_year(self, episodes, year, expected_count, expected_ids):
        # Arrange
        year_filter = YearFilter(year)

        # Act
        result = year_filter.filter(episodes)

        # Assert
        assert len(result) == expected_count
        assert {ep.id for ep in result} == expected_ids
