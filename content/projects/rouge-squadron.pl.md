---
title: "Symulator VR \"Rouge Squadron\" & Badania Biometryczne"
date: 2024-11-20
summary: "Zaawansowany kooperacyjny symulator statku kosmicznego w VR (LAN Multiplayer / Netcode) połączony z medycznymi badaniami nad reakcjami biometrycznymi (EDA/stres) graczy."
tags: ["Unity 3D", "C#", "Netcode for GameObjects", "VR", "Symulator", "Multiplayer", "Biometria", "URP", "Shader Graph", "Badania R&D"]
categories: ["Projekty", "Gamedev & XR"]
---

**Rouge Squadron** to zaawansowany, kooperacyjny symulator w wirtualnej rzeczywistości, stanowiący zwieńczenie mojej pracy inżynierskiej na kierunku Technologie Komputerowe (Wydział Fizyki i Astronomii UAM). 

Projekt nie tylko dostarcza w pełni funkcjonalnego środowiska wieloosobowego, w którym gracze wcielają się w załogę statku kosmicznego, ale również stanowi unikalną platformę badawczą weryfikującą fizjologiczne reakcje ludzkiego organizmu na immersję w VR.

Rozgrywka wymaga od graczy ścisłej komunikacji, planowania zadań, zarządzania ekwipunkiem i szybkiego podejmowania decyzji w warunkach stresowych podczas naprawy systemów pokładowych czy eksploracji obcych planet.

---

## 1. Badania nad Immersją i Biometria w VR

Kluczowym elementem pracy było przeprowadzenie rygorystycznych badań udowadniających wyższy poziom immersji w VR w stosunku do klasycznej rozgrywki na ekranie PC.

* **Metodologia:** W badaniu wykorzystano grę *SUPERHOT* (w wersji PC oraz VR) oraz certyfikowaną aparaturę medyczną – opaskę biometryczną **Empatica E4 wristband**.
* **Rejestrowane Parametry:** Pomiary obejmowały tętno (fotopletyzmograf), temperaturę skóry, aktywność motoryczną (akcelerometr 3-osiowy) oraz aktywność elektrodermalną (**EDA / GSR**), która bezpośrednio koreluje z pobudzeniem układu współczulnego i poziomem odczuwanego stresu.
* **Wnioski:** Badania wykazały drastyczny – **nawet 9-krotny** – wzrost współczynnika EDA podczas gry w VR w porównaniu do PC. Odnotowano również podwyższone tętno oraz paradoksalny spadek temperatury skóry (naturalna reakcja organizmu obkurczająca naczynia krwionośne w stanie zagrożenia).

Wyniki te bezpośrednio ukształtowały projekt *Rouge Squadron*: zamiast powierzchownego straszenia przeciwnikami, postawiłem na głęboką, fizyczną interaktywność otoczenia (dźwignie, zawory, wspinaczka, fizyka obiektów), angażującą motorykę całego ciała.

---

## 2. Architektura Sieciowa (Netcode for GameObjects)

Tworzenie dynamicznej symulacji VR w trybie multiplayer narzuca bezkompromisowe wymagania dotyczące minimalizacji opóźnień (kluczowe dla eliminacji choroby lokomocyjnej – *motion sickness*):

* **Topologia Klient-Serwer LAN:** Architektura opiera się na sieci lokalnej, jednak ze świadomym odejściem od klasycznej zasady *"nigdy nie ufaj klientowi"*.
* **Rozproszona Odpowiedzialność:** Gracz wchodzący w fizyczny kontakt z przedmiotem natychmiast staje się jego właścicielem sieciowym i przejmuje obliczenia fizyki. Niweluje to zjawisko *rubber bandingu* (przeskakiwania obiektów przy interpolacji) i daje natychmiastową, organiczną responsywność wymaganą w VR.
* **Synchronizacja Danych:** Wykorzystanie komponentów `NetworkTransform` ze stabilnym tickrate 60 Hz, `NetworkVariable` z mechanizmem `OnValueChanged()` oraz architekturę RPC (`ServerRpc`, `ClientRpc`) do replikacji maszyn, pożarów i awarii pokładowych.

---

## 3. Grafika i Optymalizacja VR (URP & Shader Graph)

Aby utrzymać stabilny klatkaż na poziomie **120 FPS** na goglach VR, wdrożyłem szereg technik optymalizacyjnych silnika Unity:

* **Generowanie Jednoprzejściowe (Single-Pass Rendering):** Rysowanie geometrii dla obu oczu jednocześnie w jednym przejściu potoku graficznego zredukowało liczbę wywołań rysowania (draw calls/batches), podnosząc płynność z 60 do 120 FPS.
* **Optymalizacja Geometrii:** Rygorystyczny pipeline *High-Poly do Low-Poly* z przeniesieniem detali do map normalnych (Normal Maps) w materiałach PBR. Zastosowano statyczny batching oraz frustum culling, projektując układ grodzi statku tak, aby naturalnie zasłaniały odległe przestrzenie.
* **Autorskie Shadery:** Za pomocą Shader Graph stworzyłem autorską symulację fal oceanicznych (fale Gerstnera) na obcej planecie Lirwen, modyfikując pozycję wierzchołków siatki w czasie rzeczywistym.
* **Wypalane Oświetlenie:** Statyczne, w pełni wypalone oświetlenie globalne (GI) z okluzją otoczenia (AO) oraz siatką próbników światła (Light Probes) dla obiektów dynamicznych zapewniło fotorealistyczny klimat przy zerowym koszcie dynamicznego oświetlenia.

---

## Zespół i Wdrożenie

Projekt powstał przy współpracy z graficzką **Wiktorią Bielecką**. Symulator został pomyślnie skompilowany przy użyciu backendu **IL2CPP** i opublikowany publicznie na platformie Itch.io.

---

## Odnośniki i Źródła
* [Zagraj w Rouge Squadron na Itch.io](https://daxpl.itch.io/rouge-squadron)

