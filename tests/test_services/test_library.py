import pytest
from src.services import LibraryManager
from src.models import TVShow, ShowStatus
from datetime import date


class TestLibraryManager:
    @pytest.fixture
    def manager(self):
        return LibraryManager()

    @pytest.fixture
    def show_factory(self):
        def _create_show(id, title):
            return TVShow(
                id=id,
                title=title,
                release_date=date(2020, 1, 1),
                end_date=None,
                rating=8.0,
                genres=[],
                status=ShowStatus.RUNNING
            )
        return _create_show

    def test_add_show(self, manager, show_factory):
        # Arrange
        show = show_factory(1, "Show 1")

        # Act
        manager.add_show(show)

        # Assert
        assert manager.contains(1)
        assert len(manager.get_all()) == 1
        assert manager.get_all()[0] == show

    def test_remove_show(self, manager, show_factory):
        # Arrange
        show = show_factory(1, "Show 1")
        manager.add_show(show)

        # Act
        manager.remove_show(1)

        # Assert
        assert not manager.contains(1)
        assert len(manager.get_all()) == 0

    def test_add_duplicate_show_does_not_duplicate(self, manager, show_factory):
        # Arrange
        show = show_factory(1, "Show 1")

        # Act
        manager.add_show(show)
        manager.add_show(show)

        # Assert
        assert len(manager.get_all()) == 1

    def test_remove_nonexistent_show_does_nothing(self, manager):
        # Act
        manager.remove_show(999)

        # Assert
        assert len(manager.get_all()) == 0
