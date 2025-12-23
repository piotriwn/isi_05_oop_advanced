from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.status import Status
from ..models import TVShow, Episode


class DisplayManager:
    console: Console

    def __init__(self) -> None:
        self.console = Console()

    def show_loader(self, message: str) -> Status:
        return self.console.status(f"[bold green]{message}[/bold green]")

    def show_error(self, message: str) -> None:
        self.console.print(f"[bold red]Error:[/bold red] {message}")

    def show_success(self, message: str) -> None:
        self.console.print(f"[bold green]Success:[/bold green] {message}")

    def show_info(self, message: str) -> None:
        self.console.print(f"[blue]{message}[/blue]")

    def print_details(self, show: TVShow, episodes: list[Episode], wasted_time: int) -> None:
        content = Text()
        content.append(f"ID: {show.id}\n", style="dim")

        if show.release_date:
            content.append(f"Premiered: {show.release_date}\n", style="cyan")

        if show.rating:
            content.append(f"Rating: {show.rating}/10\n", style="yellow")

        content.append(
            f"\nEpisodes count: {len(episodes)}\n", style="bold white")

        hours, minutes = divmod(wasted_time, 60)
        time_str = f"{hours}h {minutes}m" if hours > 0 else f"{minutes}m"
        content.append(
            f"Time to watch: {time_str} ({wasted_time} min)\n", style="bold magenta")

        self.console.print(
            Panel(content, title=f"[bold]{show.title}[/bold]", expand=False))

        if episodes:
            self._print_episodes_table(episodes)

    def _print_episodes_table(self, episodes: list[Episode]) -> None:
        table = Table(title="Episodes (Last 5)",
                      show_header=True, header_style="bold magenta")
        table.add_column("Season", justify="center")
        table.add_column("No.", justify="center")
        table.add_column("Title")
        table.add_column("Air Date", justify="right")
        table.add_column("Rating", justify="right")

        sorted_episodes = sorted(episodes, key=lambda e: (e.season, e.number))

        for ep in sorted_episodes[-5:]:
            table.add_row(
                str(ep.season),
                str(ep.number),
                ep.title,
                str(ep.release_date) if ep.release_date else "-",
                str(ep.rating) if ep.rating else "-"
            )

        self.console.print(table)
        if len(episodes) > 5:
            remaining = len(episodes) - 5
            self.console.print(
                f"[dim]...and {remaining} more episodes[/dim]", justify="center")
