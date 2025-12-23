import questionary
from ..models import TVShow
from .menu import MainMenuAction, LibraryAction


class InputHandler:
    BACK_OPTION: str = "[ Back ]"
    BACK_VALUE: str = "BACK"

    async def main_menu(self) -> MainMenuAction:
        choice = await questionary.select(
            "Select an action",
            choices=[a.value for a in MainMenuAction]
        ).ask_async()
        return MainMenuAction(choice)

    async def get_text(self, prompt: str) -> str | None:
        text = await questionary.text(prompt).ask_async()
        return text.strip() if text and text.strip() else None

    async def confirm(self, message: str) -> bool:
        return await questionary.confirm(message).ask_async()

    async def wait_for_key(self) -> None:
        await questionary.press_any_key_to_continue().ask_async()

    async def select_show_from_search(self, shows: list[TVShow]) -> TVShow | None:
        if not shows:
            return None

        shows_dict = {str(s.id): s for s in shows}

        choices = []
        for show in shows:
            year = show.release_date.year if show.release_date else "????"
            choices.append(questionary.Choice(
                title=f"{show.title} ({year})",
                value=str(show.id)
            ))

        choices.append(questionary.Choice(
            title=InputHandler.BACK_OPTION, value=InputHandler.BACK_VALUE))

        selected_id = await questionary.select(
            "Choose Series:",
            choices=choices
        ).ask_async()

        if selected_id == InputHandler.BACK_VALUE:
            return None

        return shows_dict[selected_id]

    async def select_show_from_library(self, shows: list[TVShow]) -> TVShow | None:
        if not shows:
            return None

        shows_map = {str(s.id): s for s in shows}

        choices = []
        for show in shows:
            choices.append(questionary.Choice(
                title=show.title,
                value=str(show.id)
            ))

        choices.append(questionary.Choice(
            title=InputHandler.BACK_OPTION,
            value=InputHandler.BACK_VALUE
        ))

        selected_id = await questionary.select(
            "Your Library:",
            choices=choices
        ).ask_async()

        if selected_id == InputHandler.BACK_VALUE:
            return None

        return shows_map[selected_id]

    async def library_context_menu(self, show: TVShow) -> LibraryAction:
        choice = await questionary.select(
            f"Options for '{show.title}':",
            choices=[a.value for a in LibraryAction]
        ).ask_async()
        return LibraryAction(choice)
