---
title: "Digitalizacja dziedzictwa: FOSS, drony i druk 3D w służbie archeologii"
date: 2026-10-10
summary: "Przekrojowy projekt digitalizacji obiektów historycznych – od rekonstrukcji czaszek pierwszych Wielkopolan po fotogrametrię całej wyspy w Biskupinie przy użyciu wolnego oprogramowania i zdalnych klastrów obliczeniowych."
tags: ["Druk 3D", "Fotogrametria", "Open-Source", "Hardware"]
categories: ["Projekty", "Hardware & Prototypowanie"]
aliases:
  - /czaszki-pl.html
  - /pl/projects/czaszki-3d/
  - /projects/czaszki-3d/
---

Ponad dwie godziny. Tyle czasu rzęził wentylator w całkiem nienajgorszym laptopie na stanowisku w Biskupinie, próbując przetworzyć zaledwie ułamek zdjęć fotogrametrycznych z drona, kiedy wraz z całym zespołem tylko marzyliśmy żeby położyć się spać po całym dniu na stoisku.
To był ten moment, w którym całkowicie porzuciłem próby lokalnego przetwarzania w terenie. Zamiast tego doinstalowałem na swojej domowej stacji roboczej WebODM, spiąłem całość tunelem VPN i zacząłem zdalnie zrzucać zlecenia na maszynę oddaloną o kilkadziesiąt kilometrów.

W muzealnictwie i archeologii coraz więcej mówi się o rozwiązaniach zintegrowanych ze sztuczną inteligencją, które często kończą się zamykaniem danych w kosztownych, chmurowych ekosystemach. Ja w swoich projektach staram się promować alternatywę: podejście oparte na suwerenności sprzętu i oprogramowania. Zobaczmy, jak ewolucja tych otwartych narzędzi wyglądała w praktyce.

---

## Ewolucja technologiczna: Od drewnianych ram po zdalne klastry

Proces cyfrowego zachowywania historii to dla mnie również obraz tego, jak drastycznie na przestrzeni lat zmienił się próg wejścia w szybkie prototypowanie.

### 2018: Tu się wszystko zaczęło (Czaszki i GITES)

W ramach projektu naukowo-badawczego z Muzeum Archeologicznym w Poznaniu (przy współpracy z kołem GITES), pracowaliśmy nad odtworzeniem wyglądu pierwszych mieszkańców grodu na poznańskiej Śródce. Zamiast niezwykle kosztownej technologii proszkowej (CJP), wdrożyliśmy proces oparty na druku FDM. 

**Decyzja ta drastycznie obniżyła koszty wytworzenia modeli**, zachowując przy tym dokładność wymaganą przez antropologów. Technologia proszkowa oferuje oczywiście wyższą jakość detali, ale przy innowacyjnych projektach bardzo łatwo o pułapkę przerostu formy nad treścią, ponieważ nie istnieją jeszcze wydeptane i sprawdzone ścieżki. Dlatego tym bardziej ważne jest, żeby mieć przed sobą jasno zdefiniowany cel i wiedzieć, kiedy po prostu powiedzieć „dość”.

Praca w 2018 roku zaczynała się od wysłużonych, wręcz eksperymentalnych konstrukcji, które uczyły cierpliwości i pokory na każdym etapie. To były czasy, kiedy w drukarkach wciąż powszechnie używano drewnianych części, a na rynku konstrukcje pokroju legendarnego Endera 3 czy Anet A8 dopiero się pojawiały. Czaszki wykonaliśmy na drukarce Accura, więc zanim w ogóle druk mógł zostać uruchomiony, musieliśmy pamiętać o ręcznym **wypoziomowaniu stołu za pomocą kartki papieru**. Następnie, z racji braku podgrzewania, obszar roboczy należało **pokryć taśmą malarską i klejem w sztyfcie**.

Również sam druk, mimo użycia dość grubych warstw (około 0,24 mm), trwał bardzo długo. Wtedy połowa czaszki drukowała się około dwa dni, podczas gdy współcześnie kompletny i znacznie bardziej szczegółowy model jesteśmy w stanie uzyskać w niecałe 17 godzin.

Gotowe modele prezentowaliśmy podczas oficjalnej sesji naukowej w Sali Sesyjnej Urzędu Miasta Poznania.

{{< figure src="/img-compressed/Gites/Czaszki/accura.webp" alt="Drukarka accura" caption="Drukarka accura. Źródło: https://www.facebook.com/photo.php?fbid=1976835735873739&set=pb.100063602499186.-2207520000&type=3&locale=pl_PL" >}}

### Druk 3D
Ten przeskok czasowy pokazuje ewolucję całej filozofii pracy ze sprzętem. Dawniej drukarka często była odrębnym projektem, wymagającym więcej uwagi (i modyfikacji układów chłodzenia) niż sam wytwarzany obiekt. 

Obecny krajobraz wygląda zupełnie inaczej. Zamknięte komory, stabilna kinematyka CoreXY oraz systemy automatycznego mapowania przestrzeni roboczej sprawiają, że nowoczesne maszyny są wysoce bezobsługowe. Oprogramowanie przygotowujące pliki do druku stało się na tyle intuicyjne, że zadania możemy uruchamiać prosto ze smartfona. 

**Dzięki temu środek ciężkości przeniósł się z walki z maszyną na właściwy proces badawczy.** Zamiast stresować się przyczepnością pierwszej warstwy, możemy skupić energię na precyzyjnym odwzorowaniu historycznych znalezisk, podczas gdy maszyna po prostu wykonuje swoją pracę w tle.

{{< figure src="/img-compressed/Biskupin/20260907_180048.webp" alt="Drukarka Ender 3" caption="Drukarka ender 3 przy pracy. Przeszła już tyle modyfikacji, że w zespole dyskutujemy czy wciąż można ją w ogóle nazywać enderem." >}}

### 2026: Piknik w Biskupinie (Pełna cyfryzacja i partyzancki klaster)

Jak bardzo zmieniły się możliwości sprzętowe, udowodniliśmy w 2026 roku, współpracując z Fantastycznym UAMem w Biskupinie. Nasze stoisko przestało być statyczną wystawą. Wykorzystując ręczny skaner Creality Otter, na bieżąco cyfryzowaliśmy drobne znaleziska, takie jak dzbanuszki czy narzędzia.

Poszliśmy jednak o krok dalej – postawiliśmy sobie za cel stworzenie **mapy fotogrametrycznej całej wyspy** za pomocą dronów.

Początkowo porównaliśmy efekty działania chmury DJI z lokalnie wdrożonym systemem OpenDroneMap (ODM). Przy pakiecie około 150 zdjęć DJI wygenerowało nieco lepszą jakość, jednak był to twardy limit naszej darmowej licencji. ODM pozwalał na wgrywanie potężnych paczek danych, z nawiązką nadrabiając jakość ilością materiału wejściowego.Laptopy na miejscu nie dawały sobie z tym jednak rady. Zamiast rezygnować, **zbudowaliśmy improwizowany klaster obliczeniowy**. Użyliśmy domowego serwera z Home Assistant oraz protokołu Wake-on-LAN do zdalnego wybudzenia stacji roboczej pozostawionej bezpiecznie w Suchym Lesie. Połączyliśmy się z nią przez bezpieczny tunel VPN i za pomocą interfejsu WebODM zrzuciliśmy cały ciężar obliczeniowy na lokalny komputer.

Jako studenci realizujący projekty non-profit, wielokrotnie dysponowaliśmy minimalnym budżetem. Takie improwizowane serwery a nawet klastry obliczeniowe wielokrotnie pozwoliły nam z sukcesem obejść sprzętowe wąskie gardła.

{{< figure src="/img-compressed/Biskupin/dzbanek.webp" alt="Skan dzbanka w slicerze" caption="Zeskanowany dzbanuszek w programie Cura." >}}

## Dlaczego FOSS (Wolne i Otwarte Oprogramowanie)?

Przez lata pracy ze sprzętem komercyjnym wielokrotnie doświadczałem sytuacji, w których niespodziewana aktualizacja producenta blokowała przydatną funkcjonalność, a restrykcyjne licencje wiązały ręce przy dalszym wykorzystaniu własnej pracy.

Z czasem jakość otwartego oprogramowania wzrosła na tyle, że przestało być ono wyłącznie moralnym wyborem, a stało się w pełni stabilnym narzędziem. 

W badaniach naukowych kluczowa jest pełna kontrola nad procesem. Wykorzystanie rozwiązań takich jak OpenDroneMap czy lokalne instancje WebODM gwarantuje nam pełną niezależność. Wiemy dokładnie, co dzieje się z naszymi danymi na każdym etapie przetwarzania, co pozwala uniknąć wysyłania wrażliwych zbiorów do zewnętrznych, korporacyjnych „czarnych skrzynek”.

---

## Galeria Projektowa

{{< gallery >}}
  <img alt="Wydrukowana czaszka FDM" src="/img-compressed/Gites/Czaszki/czacha2.webp" class="grid-w50 md:grid-w33" />
  <img alt="Detale anatomiczne czaszki" src="/img-compressed/Gites/Czaszki/czacha3.webp" class="grid-w50 md:grid-w33" />
  <img alt="Prezentacja w Sali Sesyjnej Urzędu Miasta" src="/img-compressed/Gites/Czaszki/prezentacja.webp" class="grid-w50 md:grid-w33" />
  <img alt="" src="/img-compressed/Biskupin/20260913_161659.webp" class="grid-w50 md:grid-w33" />
  <img alt="" src="/img-compressed/Biskupin/20260912_114401.webp" class="grid-w50 md:grid-w33" />
  <img alt="" src="/img-compressed/Biskupin/20260912_114406.webp" class="grid-w50 md:grid-w33" />
  <img alt="" src="/img-compressed/Biskupin/20260912_103706.webp" class="grid-w50 md:grid-w33" />
  <img alt="" src="/img-compressed/Biskupin/20260912_133326.webp" class="grid-w50 md:grid-w33" />
  <img alt="" src="/img-compressed/Biskupin/FB_IMG_1789632112095.webp" class="grid-w50 md:grid-w33" />
  <img alt="" src="/img-compressed/Biskupin/20260912_101603.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

---

## Źródła i Linki
* [Aktualności Rezerwatu Archeologicznego Genius Loci](https://rezerwat.muzarp.poznan.pl/pl/aktualnosci/49)
* [Relacja Koła GITES na Facebooku](https://www.facebook.com/zse2gites/posts/pfbid0T9AtZgTAMncz14Fjx8NEi2smfvrtko7Nech2FTHBARnfvNkssZ7AYTQ3BQNA7dWHl?locale=pl_PL)
* [Podsumowanie Pikniku w Biskupinie - Fantastyczny UAM](https://www.facebook.com/permalink.php?story_fbid=pfbid0BajhipXeAfVtUBW23CTJg8rN5ReKYkxrDxpmQp3wZ25o9iyhLNcH3F8FKc4KCnB1l&id=61576909868074)
* [Oprogramowanie użyte do mapowania wyspy](https://webodm.org/)