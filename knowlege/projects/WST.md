---
title: WST / XR BINIU (Weird Steering Things)
category: project
tags: [Unity 6, C++, C#, Python, ESP32, ML-Agents, VPN, Drony, AI, Hardware, Open-Source, Sim2Real]
status: active
role: Project Leader, System Architect, Unity & ESP32 Developer
---

# WST / XR BINIU: Mixed Reality Blended Intelligence for Navigable Interactive UV's

**WST (Weird Steering Things)** to zaawansowany, open-source'owy framework do budowy i sterowania bezzałogowymi pojazdami, będący radykalną ewolucją akademickiego projektu **XR BINIU**. Powstał jako alternatywa dla drogich, zamkniętych rynkowych "czarnych skrzynek". Projekt udowadnia, że przy użyciu tanich mikrokontrolerów, potężnej mocy obliczeniowej współczesnych komputerów i zaawansowanych symulacji, można z powodzeniem trenować sztuczną inteligencję do pilotowania maszyn w świecie rzeczywistym.

## Moja Rola i Odpowiedzialność

Jako **Project Leader** koordynowałem prace interdyscyplinarnego zespołu, nadając kierunek rozwojowi projektu. W warstwie technicznej (jako **System Architect oraz Unity & C++/ESP32 Developer**) odpowiadałem za:
* **Architekturę Sim2Real (Breadboard Interface):** Zaprojektowałem modularną architekturę ("wirtualny mózg"), która całkowicie separuje logikę AI od niskopoziomowego sterowania sprzętem.
* **Uczenie przez Wzmacnianie (RL):** Zaimplementowałem i nadzorowałem proces trenowania agentów AI w środowisku wirtualnym przy użyciu biblioteki Unity ML-Agents.
* **Oprogramowanie sprzętowe:** Tworzyłem mocno zoptymalizowany kod w C/C++ na mikrokontrolery ESP32, pełniące funkcję kontrolerów lotu i napędu.

## Architektura Systemu i Technologie

Fundamentalną zasadą projektu jest **decentralizacja**. Oddzieliliśmy "Mózg" (komputer pokładowy obsługujący AI) od "Mięśni" (kontroler sprzętowy obsługujący sygnały PWM i sensory). 

### 1. Środowisko Symulacyjne (Flight Computer)
Zbudowane w oparciu o silnik **Unity 6 (HDRP)**. Wykorzystujemy zaawansowaną fizykę do symulacji środowiska (wiatr, gęstość wody, fale). Dzięki pakietowi **Unity ML-Agents Toolkit** i technikom Reinforcement Learning, algorytmy samodzielnie uczą się nawigacji metodą prób i błędów w wirtualnym środowisku. Pozwala to na drastyczne obniżenie kosztów prototypowania i ryzyka uszkodzenia sprzętu ("testowanie na sucho").

### 2. Sprzęt i Komunikacja (Flight Controller)
Niskopoziomowa logika realizowana jest na mikrokontrolerach **ESP32** (wspieranych również przez Arduino). Kluczowym wyzwaniem była stabilność połączenia. Zastąpiliśmy standardowe, lokalne połączenia Wi-Fi/WebSocket i UART innowacyjną architekturą rozproszoną:
* Wdrożenie modemu GSM/LTE z bramką **VPN** postawioną na Raspberry Pi.
* Umożliwia to sterowanie jednostką z dowolnego miejsca na Ziemi – AI może działać na potężnym serwerze w innym kraju, komunikując się w czasie rzeczywistym z lekkim dronem na wodzie.

### 3. Rapid Prototyping i Druk 3D
Całość platformy fizycznej opiera się na technologii FDM (Fused Deposition Modeling). Dzięki współpracy z *Wielkopolskim Centrum Zaawansowanych Technologii (WCZT)* i dostępowi do przemysłowych drukarek (Dragon 3D), stworzyliśmy pełnowymiarowe, zintegrowane kadłuby jednostek pływających, zoptymalizowane pod kątem wyporności i wagi.

## Obecny Status i Przyszłość Projektu

Wodowanie pierwszego autonomicznego drona wodnego potwierdziło słuszność zaprojektowanej architektury Sim2Real. Obecnym, znacznie bardziej wymagającym celem zespołu jest wykorzystanie tego samego środowiska do **nauczenia AI pilotowania bicoptera** – konstrukcji z dwoma wirnikami i serwomechanizmami, która jest z natury silnie niestabilna aerodynamicznie.

---

## Zespół WST ("The Weird Team")

Projekt rozwijany jest z pasją na Wydziale Fizyki i Astronomii UAM, we współpracy z dr. Wojciechem Czartem (Koło Naukowe Errno).

* **mgr inż. Miłosz Klim** – Project Leader, System Architect, Unity/C++ Developer.
* **inż. Adam Mischke** – Electronics Specialist. Architekt układów elektronicznych.
* **Cosinus** – Unity 3D Programmer & Code Quality Guardian.
* **Emil Kopytek** – Bicopter Architect & 3D Printing Specialist.
* **inż. Krystian Olesiejko** – Naval Architect & 3D Printing Specialist.
* **Mateusz Nawrot** – Network Specialist & C++ Programmer. Odpowiedzialny za infrastrukturę VPN.
* **Wiktoria Bielecka** – UI/UX Designer. Odpowiedzialna za warstwę wizualną.

## Źródła
* https://daxpl.github.io/autonomiczneDrony.html
* https://github.com/DAXPL/WST 