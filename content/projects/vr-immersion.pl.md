---
title: "Ewolucja Immersji: Od Symulatora 'Rouge Squadron' po Multisensoryczny Biofeedback w VR"
date: 2026-10-01
summary: "Wieloletni projekt badawczy (inżynierski i magisterski) łączący symulatory VR w Unity 3D, autorski sprzęt IoT na ESP32 (w tym moduł zapachowy) oraz medyczną analizę biometryczną przy użyciu Pythona i Pandas."
tags: ["Unity 3D", "C#", "VR", "Biometria", "Netcode for GameObjects", "ESP32", "IoT", "Data Science", "Python", "Pandas", "GenAI", "Shader Graph", "URP"]
categories: ["Projekty", "Gamedev & XR", "Badania R&D"]
aliases:
  - /projects/rouge-squadron/
  - /projects/green-hour/
---

Projekt ten stanowi interdyscyplinarną, dwuetapową podróż badawczą, w której postanowiłem matematycznie i fizjologicznie zmierzyć zjawisko immersji w rzeczywistości wirtualnej. Badania te były realizowane w ramach mojej pracy inżynierskiej (kierunek: Technologie Komputerowe) oraz magisterskiej (kierunek: Aplikacje Internetu Rzeczy, pod kierunkiem prof. dr. hab. Sławomira Mamicy) na Wydziale Fizyki i Astronomii UAM.

---

## 1. Początki: "Rouge Squadron" i Medyczne Pomiary Stresu

Pierwszym krokiem było udowodnienie wyższego poziomu immersji w VR w stosunku do klasycznej rozgrywki PC. Wykorzystałem grę *SUPERHOT* (w obu wersjach) oraz certyfikowaną aparaturę medyczną – opaskę **Empatica E4**. Pomiary fotopletyzmografem (tętno), akcelerometrem i termometrem wykazały m.in. paradoksalny spadek temperatury skóry (naturalna reakcja obkurczania naczyń krwionośnych w stanie zagrożenia). Przede wszystkim jednak odnotowałem nawet **zauważalny wzrost aktywności elektrodermalnej (EDA/GSR)** w VR, co bezpośrednio koreluje ze stresem i pobudzeniem układu współczulnego.

Wyniki te ukształtowały pierwszy system testowy – **Rouge Squadron**. To zaawansowany, kooperacyjny symulator, w którym gracze naprawiają statek kosmiczny w warunkach stresowych. Zamiast tanich sztuczek, postawiłem na głęboką fizyczną interaktywność (wspinaczka, dźwignie, zawory) angażującą motorykę całego ciała. Projekt został opublikowany na platformie Itch.io we współpracy z graficzką Wiktorią Bielecką.

### Architektura Sieciowa i Optymalizacja 120 FPS
Aby zapobiec chorobie lokomocyjnej w wieloosobowym VR, zastosowałem:
* **Netcode for GameObjects (LAN):** Zrezygnowałem z zasady *"nigdy nie ufaj klientowi"*. Gracz dotykający przedmiotu przejmuje nad nim obliczenia fizyki, co całkowicie niweluje zjawisko *rubber bandingu*. Zastosowałem `NetworkTransform` (stabilny tickrate 60 Hz), `NetworkVariable` z `OnValueChanged()` oraz architekturę RPC.
* **Potok Graficzny URP:** Rygorystyczny proces *High-Poly do Low-Poly* (Normal Maps), statyczny batching i frustum culling pozwoliły uzyskać 120 FPS na goglach VR. Wdrożyłem *Single-Pass Rendering* redukujący draw calls, wypalane oświetlenie globalne z Light Probes, a także autorskie shadery w Shader Graph symulujące fale oceaniczne (fale Gerstnera) na planecie Lirwen. Całość skompilowałem na backendzie IL2CPP.

---

## 2. Ewolucja: Multisensoryczny Biofeedback i "Virtual Director"

Na etapie studiów magisterskich cel stał się jeszcze bardziej ambitny: stworzyć kompleksowe środowisko (VR/Meta Quest oraz PC) do badania korelacji między obiektywnymi reakcjami ludzkiego ciała a subiektywnym wejściem w stan głębokiego zaangażowania (*flow*).

Zaprojektowałem od podstaw własny ekosystem sprzętowy **IoT oparty na mikrokontrolerach ESP32**:
* **Rejestrator Biometryczny:** Zbudowany układ zbierał w czasie rzeczywistym logi parametrów testerów, w tym: aktywność elektrodermalną (EDA/GSR), tętno (HR), saturację krwi (SPO2) oraz temperaturę powłok skórnych.
* **Olfactory Display (Moduł Zapachowy):** Autorskie urządzenie fizyczne, które komunikowało się bezprzewodowo z silnikiem Unity 3D i precyzyjnie emitowało kompozycje zapachowe. Synchronizacja złożeń zapachowych z wirtualnymi scenami drastycznie pogłębiła odczuwanie obecności (*spatial presence*). 

Za dynamiczne sterowanie bodźcami audiowizualnymi i sensorycznymi odpowiadał napisany w C# system **"Virtual Director"**, który precyzyjnie logował markery zdarzeń.

### Pipeline Data Science i Generative AI
Ponieważ projekt wymagał rygoru naukowego, logi telemetryczne z testów laboratoryjnych poddałem dogłębnej analizie statystycznej w środowisku **Python**, wykorzystując bibliotekę **Pandas**. 

Z kolei dla przyspieszenia produkcji assetów 3D środowisk testowych wdrożyłem workflow oparty o modele GenAI. Wykorzystałem generatywny model **Hunyuan3D-2 (image-to-3D)** sprzęgnięty przez środowisko Stability Matrix, a cały proces wykańczałem poprzez zautomatyzowaną retopologię i mapowanie UV w **Blenderze**.

---

## Podsumowanie
Analiza zgromadzonych i wyczyszczonych danych bezsprzecznie potwierdziła fizjologiczną przewagę VR. Rzeczywistość wirtualna indukuje obiektywnie silniejsze reakcje organizmu niż klasyczne monitory, co przekłada się na szybsze wejście w stan *flow* i jego dłuższą stabilizację. Całe to badawcze przedsięwzięcie jest świetnym przykładem, jak skutecznie można łączyć inżynierię oprogramowania (Gamedev, XR), systemy wbudowane (Hardware) i analizę medycznych danych telemetrycznych (Data Science).