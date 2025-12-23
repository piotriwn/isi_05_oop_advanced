from enum import StrEnum


class ShowStatus(StrEnum):
    RUNNING = "Running"
    ENDED = "Ended"
    TO_BE_DETERMINED = "To Be Determined"
    IN_DEVELOPMENT = "In Development"
    UNKNOWN = "Unknown"
