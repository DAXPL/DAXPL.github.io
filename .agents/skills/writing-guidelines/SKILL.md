---
name: writing-guidelines
description: A set of rules
---

# Code Review Skill

When reviewing article, follow these steps:

## Review checklist


1. Mocne wejście (Zasada pierwszego zdania): Czy mój tekst zaczyna się od konkretu, intrygującego problemu lub obserwacji? (Wyrzucam wstępy w stylu: "Większość ludzi uważa, że...". Zaczynam od razu od uderzenia w sedno).

2. Kontekst przed kodem: Czy zanim pokażę skrypt w C#, logikę z Unity albo schemat pinów ESP32, wyjaśniłem czytelnikowi, jaki problem w ogóle próbowałem rozwiązać? Czy odpowiedziałem na pytanie "dlaczego to jest ciekawe?"

3. Filtr absolutów (Brak definitywów): Czy wyrzuciłem z tekstu słowa "zawsze", "nigdy", "najlepszy"? (Zamieniam je na: "sugeruje", "w tym przypadku sprawdza się lepiej", "często", "preferowane").

4. Czystość języka (Stop Ponglish): Czy wyłapałem branżowe potworki językowe? (Sprawdzam, czy nie napisałem "usecase" zamiast "zastosowanie", albo "wyoverloadować" zamiast "przeciążyć/przeładować").

5. Test skanera (Oddech w tekście): Czy mój tekst nie przypomina ściany znaków? (Rozbijam długie myśli na krótsze akapity. Używam pogrubień dla kluczowych wniosków, żeby wzrok czytelnika miał się na czym zatrzymać).

6. Ludzka twarz technologii (Pokora i błędy): Czy opisałem tylko suchy sukces, czy też drogę do niego? (Najlepiej czyta się o momentach, w których sprzęt lub kod stawiały opór – to buduje nić porozumienia z czytelnikiem).

7. Wizualne kotwice: Czy dorzuciłem chociaż jeden obrazek, schemat albo krótkiego gifa? (Nawet surowy, minimalistyczny design bloga potrzebuje czasem grafiki, która zilustruje zawiły problem architektoniczny i da oczom odpocząć).

8. Brzytwa Ockhama dla dygresji (Jeden wpis = jeden problem). Kiedy opisujesz budowę lokalnego asystenta AI w C#, łatwo odpłynąć w detale działania bazy wektorowej, a po chwili tłumaczyć zawiłości modeli LLM. Zamiast tego trzymaj się jednego, głównego wątku (np. samej integracji Whisper.net). Jeśli czujesz, że dygresja niebezpiecznie puchnie, utnij ją i zrób z niej materiał na zupełnie nowy artykuł.

9. Test „I co z tego?”. Każdy akapit z głębokimi technikalami musi obronić się przed tym pytaniem. Jeśli rozpisujesz się o optymalizacji alokacji pamięci lub zarządzaniu pinami w ESP32, na koniec akapitu pokaż realny skutek. Zdanie w stylu „dzięki temu rozwiązaniu udało się wygospodarować dodatkowe zasoby na obsługę czujników” działa znacznie lepiej niż sucha definicja z dokumentacji.

10. Kod to tylko rekwizyt, nie główny aktor. Nigdy nie wrzucaj ściany dwustu linijek skryptu z Unity z komentarzem w stylu „to rozwiązuje nasz problem”. Pokazuj tylko ten fragment, w którym faktycznie dzieje się magia – konkretną pętlę, kluczową metodę czy nieoczywiste wywołanie – a całość rozwiązania podlinkuj do GitHuba. Kod ma ilustrować Twój proces myślowy, a nie go zastępować.

11. Nie używaj list ani znaków "-". Niech tekst będzie ciągły i płynny

12. Przed przystąpieniem do poprawek, zadaj przynajmniej 3 pytania które rozszerzą Twoją wiedze na temat projektu. Niech uzupełniają one niejasności i posłużą do rozbudowania tekstu.