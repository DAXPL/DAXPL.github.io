---
title: Symulator "Rouge Squadron" (Praca Inżynierska)
category: project
degree: Praca Inżynierska (Technologie komputerowe)
tags: [Unity 3D, C#, Netcode for GameObjects, VR, Symulator, Multiplayer, Badania Biometryczne, URP, Shader Graph]
status: completed
role: Developer & Researcher (wsparcie graficzne: Wiktoria Bielecka)
---

# Symulator "Rouge Squadron"

**Rouge Squadron** to zaawansowany, kooperacyjny symulator w wirtualnej rzeczywistości, stanowiący zwieńczenie mojej pracy inżynierskiej[cite: 3, 4]. Projekt ten nie tylko dostarcza w pełni funkcjonalnego środowiska wieloosobowego, w którym gracze wcielają się w załogę statku kosmicznego, ale również stanowi platformę badawczą. Rozgrywka wymaga od graczy ścisłej komunikacji, planowania zadań, zarządzania ekwipunkiem i szybkiego podejmowania decyzji w warunkach stresowych podczas naprawy systemów pokładowych czy eksploracji obcych planet.

## 1. Badania nad Immersją i Biometria w VR

Kluczowym elementem pracy było przeprowadzenie rygorystycznych badań udowadniających wyższy poziom immersji w VR w stosunku do klasycznej rozgrywki na PC[cite: 3, 4]. 
* **Metodologia:** Wykorzystałem grę *SUPERHOT* (wersje PC oraz VR) oraz aparaturę medyczną – opaskę biomedyczną Empatica E4 wristband. 
* **Analiza Danych:** Mierzyłem tętno z fotopletyzmografu, temperaturę skóry, przyspieszenie (aktywność motoryczną) oraz aktywność elektrodermalną (EDA), która koreluje z poziomem odczuwanego stresu.
* **Wnioski:** Badania wykazały drastyczny (nawet 9-krotny) wzrost współczynnika EDA podczas gry w VR w porównaniu do PC. Odnotowano również wyższe tętno oraz paradoksalny spadek temperatury skóry, będący naturalną reakcją organizmu na stres i zagrożenie (obkurczanie naczyń krwionośnych). 
Te wyniki bezpośrednio ukształtowały *Rouge Squadron* – postawiłem na wysoką interaktywność otoczenia (dźwignie, pokrętła, wspinaczka), angażującą motorykę gracza zamiast taniego bodźcowania przeciwnikami.

## 2. Architektura Sieciowa (Netcode for GameObjects)

Tworzenie dynamicznej symulacji VR narzuca rygorystyczne wymagania dotyczące opóźnień (minimalizacja motion sickness). 
* **Topologia Klient-Serwer:** Rozgrywka opiera się na sieci LAN w architekturze klient-serwer, jednak z celowym odejściem od zasady "nie ufaj klientowi". 
* **Rozproszona Odpowiedzialność:** Gracz wchodzący w interakcję z obiektem staje się jego właścicielem i odpowiada za jego logikę, co niweluje zjawisko "rubber bandingu" (przeskakiwania obiektów) przy interpolacji. Zapewnia to natychmiastową responsywność wymaganą w VR.
* **Synchronizacja:** System bazuje na klasach `NetworkTransform` do śledzenia ruchów (tickrate 60 Hz), mechanizmach `NetworkVariable` z wywołaniami `OnValueChanged()` oraz architekturze RPC (`ServerRpc`, `ClientRpc`) używanych m.in. do replikacji efektów graficznych i stanu maszyn.

## 3. Grafika i Optymalizacja VR (URP & Shader Graph)

Aby utrzymać pożądany klatkaż na poziomie 120 FPS na urządzeniach docelowych (w tym systemach klasy Meta Quest i PCVR), wdrożyłem szereg zaawansowanych technik optymalizacyjnych silnika Unity:
* **Generowanie Jednoprzejściowe (Single-Pass Rendering):** Rysowanie geometrii dla obu oczu jednocześnie na jednym potoku graficznym znacząco zredukowało liczbę odwołań procesora do karty graficznej (draw calls / batches), co podniosło wydajność z 60 do 120 FPS na wybranych mapach.
* **Optymalizacja Geometrii i Batching:** Wykorzystałem workflow *High-Poly do Low-Poly*, przenosząc detale siatki do map normalnych (Normal Maps) w ramach materiałów opartych o fizykę (PBR). Zastosowałem również statyczny batching i frustum culling, projektując układ pomieszczeń statku kosmicznego w sposób, który naturalnie blokuje widoczność dalekich obiektów.
* **Autorskie Shadery:** Za pomocą narzędzia Shader Graph zaprojektowałem m.in. symulację fal morskich (fale Gerstnera) na planecie Lirwen, operującą bezpośrednio na manipulacji pozycją wierzchołków siatki w przestrzeni trójwymiarowej w czasie rzeczywistym.
* **Oświetlenie:** Zastosowałem w pełni statyczne, wypalane oświetlenie globalne (GI) wraz z okluzją otoczenia (AO) oraz komponentami Light Probes dla obiektów dynamicznych, co zagwarantowało realistyczną oprawę przy ułamku kosztów wydajnościowych.

## Zespół i Wdrożenie
Projekt powstał przy współpracy z graficzką Wiktorią Bielecką. Model językowy ChatGPT został tu dodatkowo wykorzystany jako asystent kreatywny przy projektowaniu zarysów uniwersum i tzw. world-buildingu. Gotowy symulator został pomyślnie skompilowany przy użyciu backendu IL2CPP i upubliczniony w serwisie itch.io.

# Źródła
* https://daxpl.itch.io/rouge-squadron