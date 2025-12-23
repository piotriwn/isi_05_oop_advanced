from enum import StrEnum


class MainMenuAction(StrEnum):
    SEARCH = "Series search"
    LIBRARY = "Library"
    EXIT = "Exit"


class LibraryAction(StrEnum):
    DETAILS = "See the details"
    REMOVE = "Remove from the library"
    BACK = "Go back"
