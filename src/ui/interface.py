from rich.status import Status
from ..models import TVShow, Episode
from .menu import MainMenuAction, LibraryAction
from .display import DisplayManager
from .input import InputHandler


class ConsoleInterface:
    _display: DisplayManager
    _input: InputHandler

    def __init__(self) -> None:
        self._display = DisplayManager()
        self._input = InputHandler()

    async def show_main_menu(self) -> MainMenuAction:
        return await self._input.main_menu()

    async def get_search_query(self) -> str | None:
        return await self._input.get_text("Enter TV show title:")

    async def select_show_from_search(self, shows: list[TVShow]) -> TVShow | None:
        return await self._input.select_show_from_search(shows)

    async def select_show_from_library(self, shows: list[TVShow]) -> TVShow | None:
        if not shows:
            self._display.show_info("Your library is empty.")
            await self._input.wait_for_key()
            return None
        return await self._input.select_show_from_library(shows)

    async def show_library_context_menu(self, show: TVShow) -> LibraryAction:
        return await self._input.library_context_menu(show)

    async def confirm(self, message: str) -> bool:
        return await self._input.confirm(message)

    async def wait_for_key(self) -> None:
        await self._input.wait_for_key()

    def show_loader(self, message: str) -> Status:
        return self._display.show_loader(message)

    def show_error(self, message: str) -> None:
        self._display.show_error(message)

    def show_success(self, message: str) -> None:
        self._display.show_success(message)

    def show_info(self, message: str) -> None:
        self._display.show_info(message)

    def display_show_details(self, show: TVShow, episodes: list[Episode], wasted_time: int) -> None:
        self._display.print_details(show, episodes, wasted_time)
