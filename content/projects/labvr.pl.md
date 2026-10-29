---
title: "LAB-VR - Edukacyjna Platforma Wirtualnej Rzeczywistości"
date: 2023-09-01
summary: "Otwarta platforma edukacyjna VR (fizyka, astronomia, geologia, UTK) zrealizowana w ramach grantu Kowadło 2.0, zoptymalizowana pod gogle Meta Quest 2 i wdrożona w szkołach w całym kraju."
tags: ["VR", "Unity", "Open-Source", "Edukacja"]
categories: ["Projekty", "Gamedev & XR", "Edukacja"]
---

Ściśnięcie całej wirtualnej klasy w około 70 batchach (wywołaniach rysowania) wydaje się karkołomne. Taki rygorystyczny limit narzuciliśmy sobie jednak na samym starcie. Chcieliśmy mieć pewność, że nasza aplikacja będzie działać bez zająknięcia na goglach Meta Quest 2 i 3, dlatego za punkt odniesienia przyjęliśmy surowe wytyczne optymalizacyjne z Questa pierwszej generacji. Kiedy w grę wchodzi fizyka, polegająca między innymi na dynamicznym przecinaniu modeli puszek czy monitorów, ten budżet wydajnościowy topi się w oczach. 

Wymagało to od nas godzin debugowania sceny w Unity, łączenia siatek geometrycznych (meshy) i drastycznej optymalizacji materiałów. Nawet architekturę poziomów trzeba było zaprojektować z premedytacją – tak, aby silnik nie musiał renderować zbyt wielu obiektów naraz, a jednocześnie by gracz nie czuł się zamknięty w klaustrofobicznym pudełku. 

Takie były kulisy powstawania **LAB-VR** – innowacyjnej, interaktywnej symulacji przestrzeni klasowych stworzonej dla szkół podstawowych i ponadpodstawowych. Przenosimy w niej tradycyjne lekcje w świat wirtualnej rzeczywistości, zamieniając abstrakcyjną teorię w namacalne doświadczenie. Projekt sfinansowano w ramach inicjatywy **Kowadło 2.0** i udostępniono całkowicie bezpłatnie (open-source) jako narzędzie dla placówek oświatowych.

---

## Moja Rola w Projekcie: Od optymalizacji po mentoring

Jako **Project Leader oraz Lead Unity Developer** odpowiadałem za pełen cykl życia oprogramowania:

* **Architektura Systemu VR:** Projektowanie i implementacja głównych mechanik interakcji fizycznych w środowisku wirtualnym w silniku Unity 3D.
* **Optymalizacja pod Standalone VR:** Wspomniana wcześniej walka o draw calls. Rezultatem tych zabiegów było osiągnięcie stabilnych 72 FPS na procesorach mobilnych Snapdragon XR2, bez konieczności podłączania kabla do PC.
* **Zarządzanie Zespołem i Mentoring:** Kierowanie pracami deweloperskimi Studenckiego Koła Naukowego Errno oraz koordynowanie praktyk dla uczniów techników. 

Ten ostatni punkt wiązał się z potężnym zderzeniem z rzeczywistością. Dla młodych adeptów programowania największym wyzwaniem wcale nie była architektura kodu, a wejście w standardy komercyjnego gamedevu i pojęcie **DOD (Definition of Done)**. Szkoła przyzwyczaja, że zadanie wystarczy po prostu „zrobić”. W zespole trzeba je jeszcze obronić, udokumentować i fizycznie przesunąć karteczkę na Trello. Zdarzało się, że ktoś wdrażał świetną mechanikę, ale nie potrafił opowiedzieć, jak ona w zasadzie działa pod spodem (a pamiętajmy, że to były czasy przed rewolucją AI, więc nie zrzucimy tego na „vibe coding”). To była dla nich twarda, ale bardzo potrzebna lekcja odpowiedzialności za dostarczane oprogramowanie.

---

## Obszary Edukacyjne

Symulacja dzieli się na dedykowane sale lekcyjne, z których każda oferuje interaktywne eksperymenty, trudne do zrealizowania w klasycznych warunkach szkolnych:

* **Fizyka:** Przestrzeń do przeprowadzania w pełni bezpiecznych doświadczeń mechanicznych, optycznych i magnetycznych z wizualizacją zjawisk fizycznych w czasie rzeczywistym.
* **Astronomia:** Skalowalna podróż kosmiczna umożliwiająca interakcję z trójwymiarowymi modelami ciał niebieskich i obserwację zjawisk orbitalnych z perspektywy pierwszej i trzeciej osoby.
* **Geologia:** Wirtualne ekspedycje badawcze pozwalające na analizę przekrojów geologicznych Ziemi, badanie minerałów i zjawisk tektonicznych.
* **U.T.K. (Urządzenia Techniki Komputerowej):** Przestrzeń inżynieryjna, w której podzespoły ożywają. Uczniowie mogą rozkładać komputer na części i analizować architekturę sprzętową od środka. Wbrew pozorom, skomplikowane chwytanie i manipulowanie małymi obiektami w tej sali udało się zaimplementować wyjątkowo gładko.

---

## Zderzenie z rzeczywistością, czyli warsztaty w Polsce

Cały pot wylany przy optymalizacji i mechanikach miał jeden cel: walkę z wykluczeniem technologicznym. Prawdziwym testem aplikacji były nasze ogólnopolskie wyjazdy i warsztaty dla młodzieży. Moment, w którym uczniowie zakładali gogle i widzieliśmy ich czystą radość z eksploracji wirtualnych klas, udowadniał, że immersyjna edukacja po prostu działa.

Poniżej znajdziesz szczegółowe raporty i devlogi z naszych wdrożeń:

* **8.09.2023:** Zespół Szkół Elektrycznych Nr 2 w Poznaniu – pierwsze oficjalne testy z młodzieżą techniczną. [Przeczytaj raport z Poznania](https://propaganda-studios.itch.io/lab-vr/devlog/667924/warsztaty-vr-w-zse2-w-poznaniu)
* **8.12.2023:** Technikum Informatyczne w Rabce-Zdroju – wdrożenie pilotażowe i prelekcje deweloperskie. [Przeczytaj raport z Rabki-Zdroju](https://propaganda-studios.itch.io/lab-vr/devlog/650457/warsztaty-vr-w-rabce-zdroju)
* **22.02.2024:** Zespół Szkół nr 1 w Stargardzie – wdrożenie pilotażowe i warsztaty z uczniami. [Przeczytaj raport ze Stargardu](https://propaganda-studios.itch.io/lab-vr/devlog/686407/warsztaty-vr-w-zespole-szk-w-stargardzie)
* **12.04.2024:** Szkoła Podstawowa w Gołańczy – warsztaty popularyzatorskie. [Przeczytaj raport z Gołańczy](https://propaganda-studios.itch.io/lab-vr/devlog/715663/warsztaty-vr-w-goaczy)

---

## Źródła i Odnośniki
* [LAB-VR na platformie Itch.io](https://propaganda-studios.itch.io/lab-vr)
* [Kod źródłowy na GitHubie](https://github.com/Studenckie-Kolo-Naukowe-ERRNO/LabVR)