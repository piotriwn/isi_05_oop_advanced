# TV Show Manager CLI

A command-line application for searching, tracking, and analyzing TV series using the public [TVMaze API](https://www.tvmaze.com/api). Built as a beginner's excercie in SOLID principles and Design Patterns. It features an interactive terminal UI, asynchronous data fetching, and local library management.


# Features

- TUI: Terminal interface using `questionary` and `rich`.
- Asynchronous I/O: Non-blocking API requests using `aiohttp` and `asyncio`.
- Data Validation: Data parsing with `pydantic` and `dataclasses`.
- Local state (in RAM): Add/Remove shows.
- Analytics: Calculate total "wasted" time on TV shows.
- (**TO COMPLETE**) Filtering: Filter episodes by year, season, or upcoming dates.
- Unit tests: a handful of unit tests for practice.


# Installation & Configuration

This project uses Poetry for dependency management.


## Prerequisites

Ensure you have Python and Poetry installed:


## Install dependencies

Navigate to the project root and run:
```bash
poetry install
```


## Test

You can run unit tests by:

```bash
pytest -v
```


##  Run

```bash
poetry run python app.py
```