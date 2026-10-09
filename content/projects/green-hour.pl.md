---
title: "Biofeedback i Immersja Multisensoryczna w VR (Praca Magisterska)"
date: 2026-06-15
summary: "Badawcze środowisko VR/PC korelujące reakcje fizjologiczne organizmu ze stanem immersji i flow, wykorzystujące mikrokontrolery ESP32, autorski moduł zapachowy (Olfactory Display) i analizę w Pythonie."
tags: ["Unity 3D", "C#", "Python", "ESP32", "IoT", "Biofeedback", "VR", "Sensory Biometryczne", "R&D", "Data Science", "Pandas", "GenAI"]
categories: ["Projekty", "Gamedev & XR", "Badania R&D"]
---

# Badanie zależności pomiędzy wybranymi parametrami fizycznymi organizmu a poczuciem immersji użytkownika w środowiskach rzeczywistości cyfrowych

Projekt stanowi kompletne, interdyscyplinarne środowisko badawczo-testowe zrealizowane w ramach mojej pracy magisterskiej na kierunku **Aplikacje Internetu Rzeczy** (Wydział Fizyki i Astronomii UAM) pod kierunkiem prof. UAM dr. hab. Sławomira Mamicy.

Głównym celem naukowym było zbadanie i matematyczne skorelowanie obiektywnych reakcji fizjologicznych ludzkiego ciała z subiektywnym odczuwaniem stanów immersji oraz ***flow*** (stanu głębokiego zaangażowania poznawczego) w środowiskach VR oraz na tradycyjnych ekranach PC.

---

## 1. Architektura Sprzętowa i Autorskie Urządzenia IoT

W ramach projektu zaprojektowałem i zbudowałem dedykowany ekosystem sprzętowy oparty na mikrokontrolerach **ESP32**, integrujący stan fizyczny użytkownika w pętli sprzężenia zwrotnego z silnikiem Unity 3D:

* **System Rejestracji Biometrycznej:** Układ zbierający w czasie rzeczywistym parametry fizjologiczne testerów. Aparatura monitorowała m.in. aktywność elektrodermalną (**EDA/GSR**), tętno (**HR**), saturację krwi (**SPO2**) oraz temperaturę powłok skórnych.
* **Autorski Moduł Zapachowy (Olfactory Display):** Zaprojektowałem od zera i zintegrowałem fizyczne urządzenie odpowiedzialne za stymulację węchową użytkownika poprzez precyzyjnie kontrolowaną emisję kompozycji zapachowych. Urządzenie komunikowało się bezprzewodowo z silnikiem Unity, uwalniając zapachy synchronicznie ze scenami w świecie wirtualnym, co drastycznie pogłębiało poczucie obecności (*spatial presence*).

---

## 2. Warstwa Programistyczna i System "Virtual Director"

Aplikacja testowa została zaimplementowana w środowisku **Unity 3D przy użyciu języka C#** w wersjach dostosowanych zarówno do gogli VR (Meta Quest), jak i klasycznych monitorów PC. 

Silnik dynamicznie zarządzał bodźcami audiowizualnymi i sensorycznymi w oparciu o scenariusz badawczy, precyzyjnie synchronizując markery zdarzeń w logach pomiarowych.

---

## 3. Pipeline R&D i Analiza Danych (Data Science)

Projekt wymagał połączenia inżynierii oprogramowania z rygorem metodologii naukowej:

* **Analiza Statystyczna:** Logi telemetryczne i biometryczne zebrane podczas testów laboratoryjnych były czyszczone i przetwarzane w języku **Python** przy użyciu biblioteki **Pandas**, co pozwoliło na matematyczną weryfikację korelacji między bodźcami zmysłowymi a fizjologicznymi wykładnikami emocji.
* **Nowoczesny Potok Generowania Assetów 3D (GenAI):** W celu szybkiego tworzenia zróżnicowanych lokacji testowych w Unity, wdrożyłem proces wykorzystujący model generatywny **Hunyuan3D-2** (image-to-3D) zarządzany poprzez środowisko Stability Matrix, z późniejszą automatyzacją retopologii i mapowania UV w programie **Blender**.

---

## Kluczowe Osiągnięcia i Wnioski

* **Fizjologiczna Przewaga VR:** Analiza pomiarów biometrycznych potwierdziła, że środowisko VR indukuje drastycznie silniejsze, obiektywne reakcje fizjologiczne niż klasyczna rozgrywka monitorowa, ułatwiając szybsze wejście w stan *flow* i jego dłuższą stabilizację.
* **Inżynieria R&D:** Pomyślne zaprojektowanie i uruchomienie wielomodułowego systemu IoT działającego w czasie rzeczywistym z silnikiem graficznym.
* **Interdyscyplinarność:** Połączenie technologii immersyjnych (XR), medycznej rejestracji sygnałów biometrycznych oraz systemów embedded.

