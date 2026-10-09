---
title: "SNS Minerwa - Wirtualna Strzelnica"
date: 2022-09-15
summary: "Innowacyjny system wirtualnego treningu strzeleckiego oparty na wizji maszynowej (computer vision), replikach karabinów z ESP32 i silniku Unity 3D."
tags: ["Unity", "C#", "Computer Vision", "Hardware", "ESP32", "IoT", "Edukacja"]
categories: ["Projekty", "Gamedev & XR"]
---

**Minerwa** to innowacyjny, wirtualny system nauki strzelectwa sportowego, zaprojektowany z myślą o szkołach średnich i podstawowych (jako element wspierający zajęcia Edukacji dla Bezpieczeństwa - EDB). System redefiniuje podejście do treningu strzeleckiego, eliminując potrzebę budowy drogiej infrastruktury – do działania wymaga jedynie komputera, rzutnika oraz zmodyfikowanej repliki karabinu.

<iframe src="https://itch.io/embed/1708380" loading="lazy" width="100%" height="167" frameborder="0"></iframe>

## Moja rola w projekcie

Jako **Project Leader** zarządzałem interdyscyplinarnym zespołem (programiści, graficy, projektanci 3D), dbając o dowiezienie kompletnego, stabilnego produktu. 

W warstwie technicznej pełniłem rolę **głównego specjalisty ds. implementacji w Unity oraz integratora systemów uzbrojenia (Unity & ESP Developer)**:
* Zaprojektowanie architektury aplikacji w środowisku Unity.
* Rozwój i implementacja logiki biznesowej oraz mechaniki w języku C#.
* Modyfikacja i integracja sprzętowa replik karabinów przy wykorzystaniu mikrokontrolerów ESP, co pozwoliło na bezbłędną i natychmiastową komunikację sprzętu z aplikacją.
* Połączenie modułu wizji maszynowej z głównym silnikiem gry.

---

## Architektura i Technologie

### 1. Silnik i Optymalizacja (Unity 3D & URP)
Sercem aplikacji jest silnik **Unity** działający w oparciu o Universal Render Pipeline (URP). Głównym wyzwaniem technologicznym było dostarczenie płynnych animacji i wysokiej jakości grafiki na standardowym, często przestarzałym szkolnym sprzęcie komputerowym. 

Aby zniwelować ograniczenia sprzętowe, zaimplementowałem system presetów graficznych wykorzystujący technologię **AMD FidelityFX™ Super Resolution (FSR)**. Dzięki generowaniu obrazu w niższej rozdzielczości i inteligentnemu skalowaniu, system jest w stanie działać w rozdzielczości 4K nawet na zintegrowanych układach graficznych pokroju Intel UHD 620.

### 2. Innowacyjny system śledzenia (Computer Vision)
W przeciwieństwie do konkurencyjnych rozwiązań, Minerwa odrzuca niebezpieczne w środowisku szkolnym wskaźniki laserowe czy latarnie IR. System opiera się na **wizji maszynowej (marker-based machine vision)**. Na lufie karabinu zintegrowano niewielką kamerę, z której obraz trafia do algorytmu wyszukującego specyficzne markery wyświetlane na ekranie lub ścianie. Na ich podstawie system precyzyjnie określa wektor strzału. Metoda ta całkowicie eliminuje konieczność wyznaczania statycznego punktu strzeleckiego i pozwala strzelcowi na swobodę ruchu.

---

## Funkcjonalności i UX (User Experience)

Mając na uwadze, że użytkownikami docelowymi są nauczyciele, interfejs został zaprojektowany z naciskiem na maksymalną prostotę i intuicyjność:
* **Szybka konfiguracja:** Ustawienie pełnego treningu strzeleckiego zajmuje zaledwie kilka sekund.
* **Presety PZSS:** System posiada wbudowane scenariusze i konkurencje strzeleckie przygotowane ściśle według oficjalnych zaleceń Polskiego Związku Strzelectwa Sportowego (PZSS).
* **Analityka:** Prowadzący zajęcia ma w czasie rzeczywistym podgląd do statystyk i wyników każdego strzelającego, co ułatwia rzetelną ewaluację postępów uczniów.

---

## Wdrożenia i Rozpoznawalność

Projekt od samego początku był weryfikowany w warunkach bojowych. Został zainicjowany w **technikum ZSE2 w Poznaniu**, które aktywnie testowało system w kontekście docelowego wprowadzenia go na zajęcia EDB. 

Z powodzeniem prezentowaliśmy system na publicznych wydarzeniach, zbierając świetny feedback od użytkowników, m.in. podczas:
* **Dnia Studenta I roku na Wydziale Fizyki UAM**
* **Nocnego GITES ZSE2**
* **Dnia Sportu UAM**

---

## Zespół Projektowy (Core Team)
* **Miłosz Klim** – Team Leader, Unity & ESP Developer
* **Nikodem Panknin** – Computer Vision Developer
* **Daria Mróz** – UI/UX & 2D Designer
* **Kamil Sell** – Environment & 3D Artist
* **Krystian Olesiejko** – Housing Designer

---

## Odnośniki i Źródła
* [Projekt Minerwa na Itch.io](https://propaganda-studios.itch.io/minerwa)
* [Propaganda Studios na Itch.io](https://propaganda-studios.itch.io)

