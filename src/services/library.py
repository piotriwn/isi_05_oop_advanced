from ..models import TVShow


class LibraryManager:
    _library: dict[int, TVShow]

    def __init__(self):
        self._library = {}

    def add_show(self, show: TVShow) -> None:
        if show.id not in self._library:
            self._library[show.id] = show

    def remove_show(self, show_id: int) -> None:
        if show_id in self._library:
            del self._library[show_id]

    def get_all(self) -> list[TVShow]:
        return list(self._library.values())

    def contains(self, show_id: int) -> bool:
        return show_id in self._library
