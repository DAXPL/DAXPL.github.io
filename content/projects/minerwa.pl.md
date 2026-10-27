---
title: "SNS Minerwa - Wirtualna Strzelnica"
date: 2022-09-15
summary: "System wirtualnego treningu strzeleckiego oparty na wizji maszynowej, replikach z mikrokontrolerami ESP32 i silniku Unity 3D."
tags: ["Unity", "C#", "Wizja maszynowa", "Hardware", "ESP32", "IoT", "Edukacja"]
categories: ["Projekty", "Gamedev & XR"]
---

**Od września 2024 roku nowa podstawa programowa nakłada na polskie szkoły obowiązek realizacji zajęć strzeleckich w ramach przedmiotu Edukacja dla Bezpieczeństwa (EDB).** Dla wielu placówek edukacyjnych stało się to nagłym i poważnym wyzwaniem logistycznym. Wprowadzenie praktycznej nauki strzelectwa najczęściej rozbija się o brak dostępu do strzelnic, ogromne koszty budowy własnej infrastruktury oraz oczywiste kwestie bezpieczeństwa uczniów.

Projekt Minerwa powstał jako bezpośrednia odpowiedź na ten problem. Zamiast zmuszać szkoły do budowy kosztownych, tradycyjnych kulochwytów, zaprojektowaliśmy wirtualny system pozwalający przenieść rzetelny trening do zwykłej sali lekcyjnej. Całość do działania wymaga jedynie komputera z silnikiem Unity, szkolnego rzutnika oraz wydrukowanych w 3D obudowach montowanych na replikach, wyposażonych w autorskie moduły z mikrokontrolerami.

{{< figure 
    src="/img-compressed/Minerwa/jsSrbE.webp" 
    alt="Opis dla czytników" 
>}}
## Moja rola w projekcie 

Jako **lider zespołu** zarządzałem pracą interdyscyplinarnej grupy (programiści, graficy, projektanci modeli 3D), dbając o ogólną stabilność rozwijanego systemu.

W warstwie technicznej pełniłem rolę głównego integratora. Moim największym wyzwaniem było spięcie trzech różnych środowisk: skryptów wizji maszynowej napisanych w języku Python, fizycznych mikrokontrolerów komunikujących się bezprzewodowo i głównego silnika graficznego, tak aby całość działała płynnie na słabszym sprzęcie komputerowym.

---

# Architektura systemu

## Niezależna sieć i przepływ danych
Szkoły dysponują bardzo zróżnicowaną infrastrukturą sieciową, dlatego zdecydowaliśmy się na uniezależnienie od lokalnych routerów. Komputer pełniący rolę serwera działa jednocześnie jako punkt dostępowy (Access Point). Mikrokontrolery ESP32 łączą się z nim bezpośrednio, wykorzystując protokół WebSocket. Oparcie komunikacji o protokół TCP zapewnia wysoką rzetelność dostarczania pakietów danych.

Przepływ informacji wygląda następująco: moduł z ESP32 wykonuje zdjęcie i przesyła je do Unity, następnie silnik przekazuje klatkę do zewnętrznego skryptu w Pythonie. Skrypt ten analizuje obraz i zwraca wyliczony wektor strzału z powrotem do gry.

## Silnik i optymalizacja na słabszy sprzęt (Unity 3D)
Sercem aplikacji jest silnik Unity działający w oparciu o Universal Render Pipeline (URP). Ponieważ system miał docelowo działać na standardowych, nierzadko starszych szkolnych maszynach, wdrożyliśmy system presetów graficznych wykorzystujący technologię AMD FidelityFX™ Super Resolution (FSR). Skalowanie obrazu z niższej rozdzielczości pozwala utrzymać odpowiednią płynność i responsywność nawet na zintegrowanych układach graficznych.

## Wizja maszynowa zamiast laserów
Zamiast stosować wskaźniki laserowe, system opiera się na analizie znaczników (markerów) wyświetlanych na ekranie. Zastosowanie wizji maszynowej pozwala zrezygnować z wyznaczania statycznego punktu strzeleckiego, dając użytkownikowi znacznie większą swobodę ruchu.


## Elastyczność sprzętowa
Zależało nam na tym, aby system był wysoce uniwersalny. Mikrokontroler ESP32 odpowiada wyłącznie za wykonywanie zdjęć i komunikację. Kwestie takie jak waga czy generowanie odrzutu wynikają z samej repliki, na której zamontowany jest moduł. 

Taka separacja funkcji sprawdza się w praktyce: w szkołach przyszpitalnych preferowane są lekkie, ciche i pozbawione odrzutu konstrukcje, podczas gdy inne placówki mogą z powodzeniem zamontować moduł na cięższych replikach napędzanych kapsułami CO2, które dostarczają silnych wrażeń dotykowych.

---

## Zderzenie z rzeczywistością

System był testowany w warunkach docelowych, m.in. w technikum ZSE2 w Poznaniu oraz na wydarzeniach organizowanych przez UAM. Bezpośredni kontakt użytkowników ze sprzętem dostarczył nam dwóch bardzo ważnych lekcji:

* **Test wytrzymałości materiałów:** Pierwotne, lżejsze obudowy drukowane w 3D po prostu nie przetrwały starcia z ogromną energią uczniów. Szybko musieliśmy przeprojektować systemy montażowe, stosując mocniejsze materiały i grubsze ścianki. Pozostaliśmy jednak przy druku 3D, co sprawia, że ewentualne naprawy są bardzo tanie i bezproblemowe.
* **Zarządzanie zasilaniem:** Początkowo zakładaliśmy wykorzystanie wbudowanych akumulatorów LiPo. Praktyka pokazała jednak, że nauczyciele rzadko mają czas, by pamiętać o ich systematycznym ładowaniu. Rozwiązaniem okazał się powrót do standardowych baterii 9V (lub akumulatorków w tym formacie). Możliwość szybkiej wymiany ogniwa przez nauczyciela na kilka minut przed dzwonkiem okazuje się w środowisku szkolnym rozwiązaniem znacznie bardziej adekwatnym.

---

## Główny zespół projektowy
* **Miłosz Klim** – Lider zespołu, integracja systemów (Unity & ESP)
* **Nikodem Panknin** – Programista modułu wizji maszynowej
* **Daria Mróz** – Projektantka interfejsów i grafiki 2D
* **Kamil Sell** – Twórca środowiska 3D
* **Krystian Olesiejko** – Projektant elementów drukowanych w 3D

---

## Odnośniki i źródła
* [Projekt Minerwa na Itch.io](https://propaganda-studios.itch.io/minerwa)

## Galeria
{{< gallery >}}
  <img alt="Zrzut ekranu z symulacji" src="/img-compressed/Minerwa/ahbLyZ.webp" class="grid-w50 md:grid-w33" />
  <img alt="Replika pistoletu" src="/img-compressed/Minerwa/IAdSJN.webp" class="grid-w50 md:grid-w33" />
  <img alt="Użytkowanie aplikacji" src="/img-compressed/Minerwa/IeXtBb.webp" class="grid-w50 md:grid-w33" />
  <img alt="Użytkowanie aplikacji" src="/img-compressed/Minerwa/jsSrbE.webp" class="grid-w50 md:grid-w33" />
  <img alt="Użytkowanie aplikacji" src="/img-compressed/Minerwa/lmX41G.webp" class="grid-w50 md:grid-w33" />
  <img alt="Użytkowanie aplikacji" src="/img-compressed/Minerwa/to1Faq.webp" class="grid-w50 md:grid-w33" />
  <img alt="Użytkowanie aplikacji" src="/img-compressed/Minerwa/WaPOWz.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}