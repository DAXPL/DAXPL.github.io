---
title: "WST / XR BINIU - Autonomiczne Drony i Sim2Real AI"
date: 2025-06-01
summary: "Open-source'owy framework łączący silnik Unity 6, uczenie przez wzmacnianie (ML-Agents) oraz kontrolery ESP32 z modemem LTE/VPN do sterowania autonomicznymi pojazdami."
tags: ["Unity 6", "AI", "ML-Agents", "Reinforcement Learning", "ESP32", "C++", "C#", "Python", "Sim2Real", "Drony", "IoT", "Druk 3D", "Open-Source"]
categories: ["Projekty", "AI & Robotyka"]
aliases: ["/autonomiczneDrony-pl.html"]
---

> *"Naszym największym sukcesem było nauczenie piasku myślenia."*

**WST (Weird Steering Things)** to zaawansowany, open-source'owy framework do budowy i sterowania bezzałogowymi pojazdami, będący radykalną ewolucją akademickiego projektu **XR BINIU** (*miXed Reality Blended Intelligence for Navigable Interactive UV's*). 

Projekt powstał jako alternatywa dla drogich, zamkniętych rynkowych „czarnych skrzynek”. Udowadnia, że przy użyciu tanich mikrokontrolerów, potężnej mocy obliczeniowej współczesnych komputerów i zaawansowanych symulacji fizycznych, można z powodzeniem trenować sztuczną inteligencję do pilotowania maszyn w świecie rzeczywistym metodą **Sim2Real**.

---

## O Projekcie i Zasadzie Sim2Real

Trenowanie dronów w środowisku wirtualnym przed ich fizycznym wdrożeniem to podejście zyskujące na znaczeniu dzięki nowym narzędziom symulacyjnym i postępowi w uczeniu maszynowym. Dla biznesu i nauki najważniejszym argumentem przemawiającym za prototypowaniem „na sucho” jest minimalizacja kosztów: symulacje pozwalają na bezpieczne testowanie algorytmów sterowania bez ryzyka uszkodzenia cennego sprzętu, wynajmowania akwenów czy stwarzania zagrożenia dla otoczenia.

W projekcie wykorzystano **Unity ML-Agents Toolkit** – zestaw narzędzi umożliwiający trenowanie agentów w trójwymiarowych środowiskach z użyciem technik uczenia przez wzmacnianie (**Reinforcement Learning, RL**).

---

## Moja Rola i Odpowiedzialność

Jako **Project Leader** koordynowałem prace interdyscyplinarnego zespołu, wyznaczając kierunki rozwoju projektu. 

W warstwie inżynieryjnej, jako **System Architect oraz Unity & C++/ESP32 Developer**, odpowiadałem za:
* **Architekturę Sim2Real (Breadboard Interface):** Zaprojektowanie modularnej architektury („wirtualnego mózgu”), która całkowicie separuje logikę decyzyjną AI od niskopoziomowego sterowania fizycznym sprzętem.
* **Uczenie przez Wzmacnianie (RL):** Implementację i nadzór nad procesem trenowania agentów AI w środowisku wirtualnym przy użyciu Unity ML-Agents.
* **Oprogramowanie sprzętowe:** Opracowanie wysoce zoptymalizowanego kodu w C/C++ na mikrokontrolery ESP32, pełniące funkcję kontrolerów napędu i sterowania.

---

## Architektura Systemu i Technologie

Fundamentalną zasadą projektu jest **decentralizacja**: oddzielenie „Mózgu” (komputera pokładowego obsługującego AI) od „Mięśni” (kontrolera sprzętowego obsługującego sygnały PWM i sensory).

### 1. Środowisko Symulacyjne (Flight Computer)
Zbudowane w oparciu o silnik **Unity 6 (HDRP)**. Wykorzystujemy zaawansowaną fizykę do symulacji środowiska wodnego i atmosferycznego (wiatr, opory, gęstość wody, fale). Dzięki technikom Reinforcement Learning, algorytmy samodzielnie uczą się nawigacji metodą prób i błędów w wirtualnym świecie.

### 2. Sprzęt i Łączność Globalna (Flight Controller)
Niskopoziomowa logika realizowana jest na mikrokontrolerach **ESP32** (wspieranych również przez Arduino). 
W pierwotnej wersji prototypu komunikacja opierała się na lokalnym Wi-Fi i protokole WebSocket. Choć rozwiązanie to działało w testach kampusowych, miało ograniczenie do zasięgu pojedynczej sieci.

Wdrożyliśmy skalowalną architekturę opartą o modem **GSM/LTE** oraz bramkę **VPN** skonfigurowaną na Raspberry Pi:
* Dron uwalnia się od zasięgu lokalnego Wi-Fi i łączy się z globalną siecią komórkową.
* Umożliwia to sterowanie jednostką z dowolnego miejsca na Ziemi – agent AI może działać na serwerze w odległym data center, wymieniając dane telemetryczne w czasie rzeczywistym z lekkim dronem na wodzie.

### 3. Rapid Prototyping i Druk 3D (FDM)
Całość konstrukcji fizycznej opiera się na technologii druku 3D (FDM). Technologia ta pozwoliła na błyskawiczne prototypowanie i produkcję mocowań silników, wieżyczek, nadbudówek oraz ramion napędu powietrznego.

Szczególne podziękowania kierujemy do **Wielkopolskiego Centrum Zaawansowanych Technologii (WCZT)** za udostępnienie zespołowi przemysłowej drukarki *Dragon 3D* oraz wsparcie materiałowe w postaci filamentu. Pozwoliło to na wydrukowanie pełnowymiarowego, zintegrowanego kadłuba jednostki pływającej w jednym elemencie, co było kluczowe dla integralności konstrukcji i sukcesu wodowania.

---

## Galeria Projektowa

{{< gallery >}}
  <img alt="Wodowanie drona wodnego" src="/img-compressed/Errno/Drony/20250602_143615.webp" class="grid-w50 md:grid-w33" />
  <img alt="Testy konstrukcyjne drona" src="/img-compressed/Errno/Drony/20250602_143633.webp" class="grid-w50 md:grid-w33" />
  <img alt="Prace laboratoryjne nad elektroniką" src="/img-compressed/Errno/Drony/20250609_143529.webp" class="grid-w50 md:grid-w33" />
  <img alt="Zintegrowana jednostka autonomiczna" src="/img-compressed/Errno/Drony/IMG-20250609-WA0000.webp" class="grid-w50 md:grid-w33" />
  <img alt="Detale kadłuba i napędu" src="/img-compressed/Errno/Drony/20250602_144957.webp" class="grid-w50 md:grid-w33" />
  <img alt="Etap prototypowania elektroniki" src="/img-compressed/Errno/Drony/20250511_222628.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

---

## Status i Przyszłość: Projekt Bicopter

Wodowanie pierwszego autonomicznego drona wodnego było ogromnym sukcesem i potwierdzeniem słuszności zaprojektowanej architektury Sim2Real.

Kolejnym, znacznie bardziej wymagającym celem zespołu jest wykorzystanie tego samego środowiska do **nauczenia AI pilotowania bicoptera** – konstrukcji z dwoma wirnikami wspomaganymi serwomechanizmami, która z natury jest silnie niestabilna aerodynamicznie. Model trenowany jest w precyzyjnej symulacji fizycznej Unity przed próbami w locie rzeczywistym.

---

## Zespół WST ("The Weird Team")

Projekt rozwijany jest z pasją na Wydziale Fizyki i Astronomii UAM, we współpracy z dr. Wojciechem Czartem (Studenckie Koło Naukowe Errno):

* **mgr inż. Miłosz Klim** – Project Leader, System Architect, Unity/C++ Developer
* **inż. Adam Mischke** – Electronics Specialist, architekt układów elektronicznych
* **Cosinus** – Unity 3D Programmer & Code Quality Guardian
* **Emil Kopytek** – Bicopter Architect & 3D Printing Specialist
* **inż. Krystian Olesiejko** – Naval Architect & 3D Printing Specialist
* **Mateusz Nawrot** – Network Specialist & C++ Programmer, odpowiedzialny za infrastrukturę VPN
* **Wiktoria Bielecka** – UI/UX Designer, odpowiedzialna za warstwę wizualną

---

## Źródła i Linki
* [Repozytorium WST na GitHubie](https://github.com/DAXPL/WST)
* [Oficjalny Raport Projektowy (Google Docs)](https://docs.google.com/document/d/1-k4Ll4qevaH445sVjVkQF32h3w11uCgUwEZ2eICMMHg/edit?usp=sharing)

