# Temat

Menedżer Seriali - Aplikacja konsolowa (CLI) służąca do wyszukiwania informacji o serialach telewizyjnych oraz zarządzania osobistą biblioteką. System korzysta z publicznego API TVMaze.

## Wymagania funkcjonalne
- Wyszukiwanie i Przeglądanie:
  - Wyszukiwanie seriali po frazie (tytuł).
  - Wyświetlanie listy wyników z podstawowymi informacjami (tytuł, rok premiery).
  - Pobieranie szczegółów wybranego serialu: data premiery, ocena, liczba odcinków.
- Agregacja Danych (Odcinki):
  - Pobieranie pełnej listy odcinków dla danego serialu.
  - Wyświetlanie listy ostatnich 5 odcinków.
- Zarządzanie Biblioteką:
  - Dodawanie seriali do biblioteki (przechowywane w pamięci podczas działania programu).
  - Usuwanie seriali z biblioteki.
  - Przeglądanie zapisanych seriali.
- Analiza i Statystyki:
  - Obliczanie całkowitego czasu potrzebnego na obejrzenie wszystkich odcinków (w minutach/godzinach).

## Wymagania Niefunkcjonalne i Techniczne
- Interfejs Użytkownika (CLI):
  - Interaktywny interfejs tekstowy (TUI) z wykorzystaniem biblioteki `questionary`.
  - Estetyczne wyświetlanie danych (tabele, panele) przy użyciu biblioteki `rich`.
- Asynchroniczność I/O:
  - Wszystkie zapytania do zewnętrznego API muszą być nieblokujące (`aiohttp`).
  - Pobieranie danych o serialu i jego odcinkach odbywa się współbieżnie (`asyncio.gather`).
- Walidacja Danych:
  - System nie może ufać danym z API.
  - Każda odpowiedź musi być zwalidowana pod kątem typów (użycie `pydantic`).
- Architektura i Czystość kodu:
  - Podział na warstwy (Klient API, Logika Biznesowa, UI).
  - Zastosowanie wzorców projektowych (Fasada dla UI).
  - Kod zgodny z zasadami SOLID.
- Obsługa Błędów:
  - Aplikacja musi elegancko obsługiwać brak połączenia z internetem oraz błędy HTTP.
