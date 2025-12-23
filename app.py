import asyncio
import aiohttp
from src.repositories import TVMazeRepository
from src.services import TVService, LibraryManager
from src.ui import ConsoleInterface, MainMenuAction, LibraryAction


async def main():
    ui = ConsoleInterface()
    library = LibraryManager()

    async with aiohttp.ClientSession() as session:
        repo = TVMazeRepository(session)
        service = TVService(repo)

        while True:
            action = await ui.show_main_menu()

            if action == MainMenuAction.EXIT:
                ui.show_success("Goodbye!")
                break

            elif action == MainMenuAction.SEARCH:
                query = await ui.get_search_query()
                if not query:
                    continue

                with ui.show_loader("Searching for TV shows..."):
                    results = await service.search_shows(query)

                selected_show = await ui.select_show_from_search(results)

                if not selected_show:
                    continue

                with ui.show_loader("Fetching details and episodes..."):
                    full_show, episodes = await service.get_full_show_info(selected_show.id)

                if full_show:
                    wasted_time = service.calculate_wasted_time(episodes)

                    ui.display_show_details(full_show, episodes, wasted_time)

                    if not library.contains(full_show.id):
                        if await ui.confirm("Add to library?"):
                            library.add_show(full_show)
                            ui.show_success(
                                f"Added '{full_show.title}' to library!")
                    else:
                        ui.show_info("This show is already in your library.")

                await ui.wait_for_key()

            elif action == MainMenuAction.LIBRARY:
                while True:
                    saved_shows = library.get_all()
                    selected_library_show = await ui.select_show_from_library(saved_shows)

                    if not selected_library_show:
                        break

                    sub_action = await ui.show_library_context_menu(selected_library_show)

                    if sub_action == LibraryAction.BACK:
                        continue

                    elif sub_action == LibraryAction.DETAILS:
                        with ui.show_loader("Refreshing data..."):
                            full_show, episodes = await service.get_full_show_info(selected_library_show.id)

                        if full_show:
                            wasted_time = service.calculate_wasted_time(
                                episodes)
                            ui.display_show_details(
                                full_show, episodes, wasted_time)
                            await ui.wait_for_key()

                    elif sub_action == LibraryAction.REMOVE:
                        if await ui.confirm(f"Are you sure you want to remove '{selected_library_show.title}'?"):
                            library.remove_show(selected_library_show.id)
                            ui.show_success("Removed from library.")


if __name__ == "__main__":
    asyncio.run(main())
