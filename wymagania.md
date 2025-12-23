Punktowanie:

- Wykorzystanie dataclasses do przechowywania punktów danych (10pkt)
- Wykorzystanie async/multithreading do przetwarzania danych (10pkt)
- Diagram klas zgodny z SOLID / Wykorzystanie wzorców projektowych (10pkt)
- Kilka testów jednostkowym dla krytycznych fragmentów projektu (10pkt)
- Prawidłowe typowanie zmiennych w projekcie (10pkt)

Dodatkowe punkty (do limitu 50pkt za całość):
- dobre wykorzystanie Enum (5pkt)
- wykorzystanie pydantic dataclasses do walidacji danych (5pkt)


Styl:

1. Kod powinien być zwięzły. Im mniej linii kodu, tym lepiej
2. Unikać rozpisywania elementów kolekcji. Gdzie się da używać list comprehension, list upack, dict unpack
3. Dane przechowywać w odpowiednim formacie: Daty w datetime.date/datetime.datetime a nie w str
4. Czas powinien być przechowywany w UTC, a wyświetlany w czasie lokalnym
5. Unikać powtarzania kodu - konieczność powtórzenia albo parafrazy kodu najczęściej oznacza potrzebę wydzielenia tego kodu do wspólnej klasy
