---
title: Biofeedback i Immersja Multisensoryczna (Praca Magisterska)
category: project
type: academic_thesis
degree: Praca Magisterska (Aplikacje Internetu Rzeczy)
tags: [Unity 3D, C#, Python, ESP32, IoT, Biofeedback, Multi-sensory VR, Sensory Biometryczne, R&D, Data Science, Pandas]
status: completed
role: Solo Developer, Hardware Engineer & Researcher
---

# Badanie zależności pomiędzy wybranymi parametrami fizycznymi organizmu a poczuciem immersji użytkownika w środowiskach rzeczywistości cyfrowych

Projekt stanowi pełne środowisko badawczo-testowe zrealizowane w ramach pracy magisterskiej na kierunku Aplikacje Internetu Rzeczy (Wydział Fizyki UAM) pod kierunkiem prof. UAM dr hab. Sławomira Mamicy. Głównym celem pracy było zbadanie i skorelowanie obiektywnych reakcji fizjologicznych ludzkiego organizmu z subiektywnym odczuwaniem stanów immersji oraz *flow* (stanu głębokiego zaangażowania) w środowiskach VR i PC.

## 1. Architektura Sprzętowa i Autorskie Urządzenia IoT

W ramach projektu zaprojektowałem i zbudowałem dedykowany ekosystem sprzętowy oparty na mikrokontrolerach **ESP32**, który integrował sferę fizyczną użytkownika z cyfrowym środowiskiem silnika Unity 3D:

* **System Rejestracji Biometrycznej:** Stworzyłem układ zbierający w czasie rzeczywistym parametry fizjologiczne testerów. Aparatura monitorowała m.in. aktywność elektrodermalną (EDA/GSR), tętno (HR), saturację (SPO2) oraz temperaturę skóry.
* **Autorski Moduł Zapachowy (Olfactory Display):** Zaprojektowałem od zera i zintegrowałem fizyczne urządzenie odpowiedzialne za multisensoryczną stymulację użytkownika poprzez kontrolowaną emisję zapachów. Urządzenie komunikowało się bezpośrednio z grą, uwalniając odpowiednie kompozycje zapachowe synchronicznie z wydarzeniami na ekranie, co drastycznie zwiększało poczucie obecności (presence) w świecie wirtualnym. Nie zostało ono jeszcze opublikowane.

## 2. Warstwa Programistyczna i System "Virtual Director"

Aplikacja testowa została zaimplementowana w środowisku **Unity 3D przy użyciu języka C#** w wersjach dostosowanych zarówno do gogli VR, jak i klasycznych ekranów PC.

## 3. Pipeline R&D i Analiza Danych (Data Science)

Projekt wymagał interdyscyplinarnego podejścia do wytwarzania oprogramowania oraz metodologii naukowej:

* **Analiza Statystyczna:** Zebrane logi biometryczne z testów użytkowników były przetwarzane i analizowane przy użyciu języka **Python** oraz biblioteki **Pandas**, co pozwoliło na matematyczne udowodnienie korelacji między bodźcami multisensorycznymi a fizjologicznymi wykładnikami emocji.
* **Nowoczesny Pipeline 3D Asset Generation:** W celu szybkiego i efektywnego generowania unikalnych zasobów graficznych do środowisk testowych w Unity, wdrożyłem potok produkcyjny wykorzystujący generatywną sztuczną inteligencję (GenAI) – model **Hunyuan3D-2** (image-to-3D) zarządzany poprzez środowisko Stability Matrix, z późniejszą automatyzacją procesów retopologii i mapowania w programie **Blender**.

## Kluczowe Osiągnięcia i Wnioski

* **Znacząca przewaga VR w budowaniu zaangażowania:** Analiza wyników pomiarów biometrycznych sugeruje, że środowisko wirtualnej rzeczywistości (VR) potrafi angażować użytkownika w sposób drastycznie bardziej intensywny niż klasyczna rozgrywka na monitorze PC. Bodźce płynące z gogli VR wywoływały u testerów silniejsze, obiektywne reakcje fizjologiczne, przekładając się na szybsze osiąganie i dłuższą stabilizację stanu *flow*.
* **Inżynieria R&D:** Skuteczne wdrożenie autorskiego, bezprzewodowego urządzenia IoT działającego w pętli sprzężenia zwrotnego z silnikiem Unity.
* **Synergia medycyny i gamingu:** Stworzenie kompletnego, skalowalnego narzędzia badawczego łączącego technologie immersyjne (XR) z bioanalizą medyczną w czasie rzeczywistym.