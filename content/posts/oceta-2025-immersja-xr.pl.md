---
title: "Doświadczanie immersji w rzeczywistościach wirtualnych i techniki jej pogłębiania (OCETA 2025)"
date: 2025-06-12
summary: "Wykład na konferencji OCETA poświęcony zjawisku embodied presence w XR, metodom pomiaru immersji za pomocą sensorów biometrycznych oraz technikom potęgowania obecności."
tags: ["Konferencja", "VR", "XR", "Biometria", "Embodied Presence", "Prelekcja", "R&D"]
categories: ["Wpisy & Relacje", "Prelekcje & Wystąpienia"]
---

Podczas czerwcowej konferencji **OCETA 2025** wygłosiłem autorski wykład poświęcony zagadnieniu ***embodied presence*** w rzeczywistościach wirtualnych i rozszerzonych (XR) – czyli mechanizmom, dzięki którym ludzkie ciało i zmysły organicznie „wchodzą” w wirtualny świat.

---

## Główne Zagadnienia Wystąpienia

### 1. Metodologia pomiaru immersji przy użyciu aparatury biometrycznej
W tradycyjnym gamedevie immersję ocenia się głównie za pomocą subiektywnych ankiet post-factum. W mojej prelekcji przedstawiłem metody obiektywnego pomiaru zaangażowania użytkownika w czasie rzeczywistym przy użyciu aparatury biomedycznej (m.in. opaski Empatica E4 oraz autorskich układów pomiarowych na ESP32):
* Rejestracja aktywności elektrodermalnej (**EDA / GSR**) jako bezpośredniego wskaźnika pobudzenia układu współczulnego.
* Zmiany parametrów tętna (**HR**) oraz mikro-wahania temperatury skóry.

### 2. Wyniki badań empirycznych
Przedstawiłem wnioski z eksperymentów porównujących identyczne środowiska w wersji klasycznej (monitor PC) oraz w goglach VR (Meta Quest). Wyniki dowiodły drastycznego (nawet wielokrotnego) wzrostu amplitudy EDA w środowisku immersyjnym, co stanowi dowód na głębokie zaangażowanie struktur motorycznych i emocjonalnych gracza.

### 3. Techniki i narzędzia pogłębiające obecność w XR
W drugiej części wystąpienia omówiłem praktyczne techniki dla programistów i projektantów XR:
* **Fizyka i interakcje tactile:** Zastępowanie prostych kliknięć gałką kontrolera bogatą fizyką manipulacji obiektami (dźwignie, pokrętła, konieczność użycia obu rąk).
* **Multisensoryczność:** Projektowanie bodźców wykraczających poza wzrok i słuch – w tym wstępne wnioski z integracji modułów zapachowych (Olfactory Displays) kontrolowanych z poziomu silnika Unity.
* **Architektura sieciowa o zerowym motion sickness:** Wskazówki implementacyjne dla wieloosobowych gier VR (Netcode), gdzie rozproszona własność obiektów niweluje opóźnienia i nudności.

