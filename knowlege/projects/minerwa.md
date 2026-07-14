---
title: System Nauki Strzelectwa "Minerwa"
category: project
tags: [Unity 3D, C#, XR, Machine Vision, Edukacja, Hardware Integration, ESP32, IoT]
status: completed
role: Team Leader, Unity & ESP Developer, Hardware Integrator
---

# System Nauki Strzelectwa "Minerwa"

**Minerwa** to innowacyjny, wirtualny system nauki strzelectwa sportowego, zaprojektowany specjalnie z myślą o szkołach średnich i podstawowych (jako element wspierający zajęcia Edukacji dla Bezpieczeństwa - EDB). System redefiniuje podejście do treningu strzeleckiego, eliminując potrzebę budowy drogiej infrastruktury – do działania wymaga jedynie komputera, rzutnika oraz zmodyfikowanej repliki karabinu.

## Moja rola w projekcie

Jako **Project Leader** zarządzałem interdyscyplinarnym zespołem (programiści, graficy, projektanci 3d), dbając o dowiezienie kompletnego, działającego produktu. 

W warstwie technicznej pełniłem rolę **głównego specjalisty ds. implementacji w Unity oraz integratora systemów uzbrojenia (Unity & ESP Developer)**. Moje główne zadania obejmowały:
* Zaprojektowanie architektury aplikacji w środowisku Unity.
* Rozwój i implementację logiki biznesowej oraz mechaniki w języku C#.
* Modyfikację i integrację sprzętową replik karabinów przy wykorzystaniu mikrokontrolerów (ESP), co pozwalało na bezbłędną komunikację sprzętu z aplikacją.
* Połączenie modułu wizji maszynowej z głównym silnikiem gry.

## Architektura i Technologie

### 1. Silnik i Optymalizacja (Unity 3D & URP)
Sercem aplikacji jest silnik **Unity (wersja 2021)** działający w oparciu o Universal Render Pipeline (URP). Głównym wyzwaniem technologicznym było dostarczenie płynnych animacji i wysokiej jakości grafiki na standardowym, często przestarzałym szkolnym sprzęcie komputerowym. 
Aby zniwelować ograniczenia sprzętowe, zaimplementowałem system presetów graficznych wykorzystujący technologię **AMD FidelityFX™ Super Resolution (FSR)**. Dzięki generowaniu obrazu w niższej rozdzielczości i inteligentnemu skalowaniu, system jest w stanie działać w rozdzielczości 4K nawet na zintegrowanych układach graficznych pokroju Intel UHD 620.

### 2. Innowacyjny system śledzenia (Computer Vision)
W przeciwieństwie do konkurencyjnych rozwiązań, Minerwa odrzuca niebezpieczne w środowisku szkolnym wskaźniki laserowe czy latarnie IR. System opiera się na **wizji maszynowej (marker-based machine vision)**. Na lufie karabinu zintegrowano niewielką kamerę, z której obraz trafia do algorytmu wyszukującego specyficzne markery wyświetlane na ekranie/ścianie. Na ich podstawie system precyzyjnie określa wektor strzału. Metoda ta całkowicie eliminuje konieczność wyznaczania statycznego punktu strzeleckiego.

## Funkcjonalności i UX (User Experience)

Mając na uwadze, że użytkownikami docelowymi są nauczyciele, interfejs został zaprojektowany z naciskiem na maksymalną prostotę i intuicyjność:
* **Szybka konfiguracja:** Ustawienie pełnego treningu strzeleckiego zajmuje zaledwie kilka sekund.
* **Presety PZSS:** System posiada wbudowane scenariusze i konkurencje strzeleckie przygotowane ściśle według oficjalnych zaleceń Polskiego Związku Strzelectwa Sportowego (PZSS).
* **Analityka:** Prowadzący zajęcia ma w czasie rzeczywistym podgląd do statystyk i wyników każdego strzelającego, co ułatwia ewaluację postępów.

## Wdrożenia i Rozpoznawalność

Projekt od samego początku był ściśle weryfikowany w warunkach bojowych. Został zainicjowany w **technikum ZSE2 w Poznaniu**, które aktywnie testowało system w kontekście docelowego wprowadzenia go na zajęcia EDB. 

Z powodzeniem prezentowaliśmy system na publicznych wydarzeniach, zbierając świetny feedback od użytkowników, m.in. podczas:
* **Dnia Studenta I roku na Wydziale Fizyki UAM**
* **Nocnego GITES ZSE2**
* **Dniu sportu UAM**

## Zespół Projektowy (Core Team)
* **Miłosz Klim** – Team Leader, Unity & ESP Developer
* **Nikodem Panknin** – Computer Vision Developer
* **Daria Mróz** – UI/UX & 2D Designer
* **Kamil Sell** – Environment & 3D Artist
* **Krystian Olesiejko** – Housing Designer

## Źródła i linki
* https://propaganda-studios.itch.io/minerwa