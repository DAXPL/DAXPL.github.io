---
title: "Fizjologia immersji w VR"
date: 2026-10-01
summary: "Fizjologia immersji w VR"
tags: ["VR", "Unity", "Biometria", "Hardware"]
categories: ["Projekty", "Gamedev & XR", "Badania R&D"]
---

Pełne wrażenie zanurzenia w świecie cyfrowym nie zaczyna się na ekranie monitora ani w soczewkach gogli, lecz w głowie gracza i potem przechodzi na koniuszki palców, w momencie gdy dłonie pokrywają się mikroskopijną warstwą potu. To fascynujący moment, w którym iluzja przestaje być jedynie zbiorem wyrenderowanych wielokątów, a staje się dla ludzkiego układu nerwowego rzeczywistością. Przez lata twórcy symulacji zakładali, że kluczem do tego stanu jest wyłącznie fotorealistyczna grafika, coraz gęstsze siatki geometrii czy zaawansowane cieniowanie. Kiedy jednak zdjęty zostanie marketingowy szum i obietnice technologicznych rewolucji, okazuje się, że najgłębsze poczucie obecności pojawia się wtedy, gdy technologia staje się przezroczysta, cicho ustępując miejsca emocjom.

Problem w tym, że w klasycznym podejściu do projektowania gier reakcje te pozostają dla komputera całkowicie niewidoczne. Tradycyjna ewaluacja doświadczenia gracza przypomina próbę oceny filmu wyłącznie na podstawie ankiet wypełnionych przez widzów kwadrans po opuszczeniu sali kinowej. Pytania kwestionariuszowe mierzą zniekształcone wspomnienie emocji, zacierając ulotne sekundy strachu, zawahania czy ekscytacji. Z kolei komercyjne opaski sportowe i smartwatche, choć powszechnie dostępne, w badaniach laboratoryjnych okazują się niemal bezużyteczne przez zamknięte interfejsy oraz konieczność przesyłania intymnych danych biomedycznych na zewnętrzne serwery chmurowe. Aby zbadać, czym naprawdę jest immersja i stan przepływu, musiałem zbudować własny most łączący biologię człowieka z pętlą renderowania silnika gry.

## Rouge Squadron

Ta fascynacja wirtualnymi światami kiełkowała we mnie jeszcze w czasach technikum, więc gdy nadszedł czas wyboru tematu pracy inżynierskiej, naturalnym krokiem było przekucie tej pasji w działający projekt. Razem z graficzką Wiktorią Bielecką stworzyliśmy **Rouge Squadron** – kooperacyjny symulator załogi statku kosmicznego.

Celowaliśmy w niszę użytkowników VR szukających wyzwań w trudnych i wymagających symulacjach wojskowych. Zamiast iść w stronę podręcznikowego realizmu, postawiliśmy na **wiarygodność świata przedstawionego**. Gracze stają przed szeregiem zadań – od dynamicznych starć po rozwiązywanie skomplikowanych łamigłówek środowiskowych – aby utrzymać statek w dobrej kondycji i osiągnąć cele misji, co wymaga efektywnej komunikacji i koordynacji działań. Aby przetrwać w surowym środowisku kosmicznym, załoga musi zarządzać ograniczonymi zasobami, podejmując strategiczne decyzje pod presją czasu.

Gracze mają pełną swobodę wyboru, jaką rolę chcą pełnić w załodze oraz jakie zadania chcą wykonywać. Mogą współpracować i dzielić się obowiązkami, starając się osiągnąć wspólne cele, lub też działać indywidualnie, realizując własne ambicje. Mechanika gry nie wymaga sztywnego określenia roli, a kwestię tę pozostawiamy drużynie w ramach jej zdolności komunikacyjnych. Ważnym aspektem rozgrywki jest także możliwość dostosowywania ekwipunku i narzędzi w zależności od potrzeb i preferencji graczy. Każdy uczestnik misji ma pełną dowolność doboru sprzętu, który pozwoli mu efektywniej pełnić powierzone funkcje.

Zaprojektowaliśmy dwa diametralnie odmienne środowiska planetarne. Pierwszym było słoneczne **Aridis**, inspirowane architekturą osad Bliskiego Wschodu, gdzie opuszczona baza górnicza Vas Rakhar i bunt maszyn wydobywczych „HARVEX” stawiały graczy w stanie permanentnego zagrożenia i konieczności obrony. Drugim biegunem stała się wiecznie zamglona, deszczowa planeta **Lirwen**, wzorowana na surowych wybrzeżach Irlandii. Pokryta prastarymi ruinami, mchem oraz spokojną fauną, kładła nacisk na mistycyzm, powolną eksplorację i zmysłowe wyciszenie.  Zamiast typowego dla gier wciskania wirtualnych przycisków w interfejsie użytkownika postawiliśmy na pełne zaangażowanie motoryczne. Gracze mogą wspinać się po drabinkach z wykorzystaniem siły własnych ramion, manualnie dopasowywać narzędzia, przekręcać oporne zawory i siłować się z fizycznymi dźwigniami.

{{< gallery >}}
  <img alt="" src="/img-compressed/RougeSquadron/Aridis1.webp" class="grid-w50 md:grid-w33" />
  <img alt="" src="/img-compressed/RougeSquadron/Aridis2.webp" class="grid-w50 md:grid-w33" />
  <img alt="" src="/img-compressed/RougeSquadron/Aridis3.webp" class="grid-w50 md:grid-w33" />
  <img alt="" src="/img-compressed/RougeSquadron/Aridis4.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

### Materiały z rozgrywki
{{< youtube "https://www.youtube.com/watch?v=nMWQzpWiL40" >}}

{{< youtube "https://www.youtube.com/watch?v=W0C1-RdMRig" >}}

{{< youtube "https://www.youtube.com/watch?v=MUfFjoHZpU4" >}}

Obserwując uczestników testów, którzy kompletnie zapominali o otaczającym ich świecie, zacząłem dociekać, jak tę obecność zmierzyć w sposób obiektywny. Wielokrotnie wcześniej słyszałem, że VR jest bardziej immersyjnym medium, ale za tymi twierdzeniami rzadko stały twarde liczby a najczęściej opierano się na wynikach subiektywnych ankiet. Do badania pilotażowego wykorzystałem polską produkcję „SUPERHOT” od SUPERHOT Team, ze względu na obecność wersji zarówno na standardowe komputery PC, jak i na gogle VR, co pozwala wyeliminować różnice sprzętowe. Liczba generowanych klatek na sekundę i ustawienia graficzne zostały dostosowane w taki sposób, by obie wersje były do siebie jak najbardziej zbliżone (stałe 120 klatek na sekundę na obu urządzeniach).

Do rejestracji danych posłużyła certyfikowana opaska **Empatica E4 wristband Rev. 2** (wyrób medyczny klasy IIa wg dyrektywy 93/42/EEC). Badanie rozpoczynało się od umieszczenia opaski na dominującej ręce badanego. Umiejscowienie to pozwalało mierzyć aktywność ręki obsługującej mysz komputerową (dzięki wbudowanemu akcelerometrowi), nie zmuszając użytkownika do zdejmowania własnego zegarka. Następnie badany był proszony o 10-minutową rozgrywkę w wersji na PC lub VR, a po krótkiej przerwie – o zagranie w drugą wersję gry przez kolejne 10 minut. Przez cały czas opaska mierzyła tętno za pomocą fotopletyzmografii (PPG), temperaturę skóry, przyspieszenie dłoni oraz parametr EDA (ang. *ElectroDermal Activity*) określający przewodnictwo elektryczne skóry. Zmienne te pozwalają na bezpośrednią kwantyfikację pobudzenia układu współczulnego.

Wybrana gra została zaprojektowana w taki sposób, aby wywoływać u gracza poczucie zagrożenia i wzmagać je poprzez stymulację dźwiękami, surową paletą barw, a w przypadku VR – także haptyką płynącą z wibracji kontrolerów. Czas płynie w niej tylko wtedy, gdy gracz się porusza, co wymusza nieustanne kalkulowanie każdego gestu.

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz8.webp" 
    caption="Wykresy prezentujące zmiany odczytywanych parametrów w czasie u jednego z badanych. Czerwone pionowe linie wyznaczają konkretne momenty – początek i koniec rozgrywki"
    alt="Wykresy prezentujące zmiany odczytywanych parametrów w czasie u jednego z badanych. Czerwone pionowe linie wyznaczają konkretne momenty – początek i koniec rozgrywki" 
>}}

Podczas obserwacji badanych w środowisku VR uwidoczniła się fascynująca transformacja behawioralna. Użytkownicy, którzy początkowo wykonywali krótkie, asekuracyjne ruchy samymi dłońmi, po kilku minutach zaczynali dynamicznie przemieszczać się całym ciałem, wykonywać głębokie uniki i wypady. Gdy oswoili się z wirtualną przestrzenią, iluzja stawała się na tyle kompletna, że badani nagminnie tracili świadomość fizycznych granic laboratorium, w ferworze walki przekraczając wirtualne siatki bezpieczeństwa. Po zdjęciu gogli wielu z nich było wyraźnie zdyszanych, co znalazło odzwierciedlenie w gwałtownych skokach tętna i przyspieszenia kątowego dłoni.

Poniższe wykresy przedstawiają aktywność elektrodermalną u badanych w trakcie rozgrywki na komputerze stacjonarnym oraz w rzeczywistości wirtualnej. W niemal każdym przypadku wartość EDA (wyrażana w mikrosiemensach i bezpośrednio odzwierciedlająca pobudzenie emocjonalne) wzrastała skokowo w VR w stosunku do sesji na PC. Jedynie u jednej badanej zaobserwowano odwrócenie tej tendencji. Z wywiadu wynikało jednak, że badana miała doświadczenie z zestawami VR, przez co sterowanie w wersji desktopowej uznała za toporne i wysoce frustrujące, co zaowocowało skokiem stresu przed monitorem. Niemniej nawet w jej przypadku odczyty pozostałych parametrów potwierdziły głębsze zaabsorbowanie w świecie wirtualnym.

W przypadku użytkowników przechodzących z VR na klasyczny komputer, przez pewien czas na PC utrzymywał się podwyższony poziom pobudzenia somatycznego. Z wywiadów wynikało, że po dynamicznym i angażującym ciele doświadczeniu w goglach, powrót przed płaski monitor rodził poczucie niedosytu i nudy.

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz9.webp" 
    caption="Wykres przedstawiający współczynnik EDA (aktywność elektrodermalna) u badanych w trakcie rozgrywki na komputerze stacjonarnym"
    alt="Wykres przedstawiający współczynnik EDA (aktywność elektrodermalna) u badanych w trakcie rozgrywki na komputerze stacjonarnym" 
>}}

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz10.webp" 
    caption="Wykres przedstawiający współczynnik EDA (aktywność elektrodermalna) u badanych w trakcie rozgrywki w rzeczywistości wirtualnej"
    alt="Wykres przedstawiający współczynnik EDA (aktywność elektrodermalna) u badanych w trakcie rozgrywki w rzeczywistości wirtualnej" 
>}}

Oprogramowanie producenta opaski nie radziło sobie najlepiej z precyzyjnym wyliczaniem tętna w warunkach dynamicznych, jednak surowe wyniki fotopletyzmografu posłużyły do identyfikacji ogólnego trendu. We wszystkich przypadkach w środowisku VR obserwowano wzrost częstości akcji serca.

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz11.webp" 
    caption="Wykres przedstawiający tętno u badanych w trakcie rozgrywki na komputerze stacjonarnym"
    alt="Wykres przedstawiający tętno u badanych w trakcie rozgrywki na komputerze stacjonarnym" 
>}}

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz12.webp" 
    caption="Wykres przedstawiający tętno u badanych w trakcie rozgrywki w rzeczywistości wirtualnej"
    alt="Wykres przedstawiający tętno u badanych w trakcie rozgrywki w rzeczywistości wirtualnej" 
>}}

Porównując dane z obu platform, zauważono, że w VR – mimo znacznie większego wysiłku fizycznego i dynamicznego poruszania całym ciałem – temperatura skóry systematycznie spadała. Zjawisko to wynika z **wazokonstrykcji obwodowej**. W reakcji na postrzegane zagrożenie autonomiczny układ nerwowy obkurcza naczynia krwionośne w skórze i kończynach, przekierowując krew do mięśni szkieletowych i narządów wewnętrznych (przygotowanie organizmu do walki lub ucieczki oraz minimalizacja utraty krwi przy potencjalnym zranieniu). Mózg gracza traktował wirtualne pociski jako realne dla niego niebezpieczeństwo.

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz19.webp" 
    caption="Wykres przedstawiający temperaturę powierzchni skóry u badanych w trakcie rozgrywki na komputerze stacjonarnym"
    alt="Wykres przedstawiający temperaturę powierzchni skóry u badanych w trakcie rozgrywki na komputerze stacjonarnym" 
>}}

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz20.webp" 
    caption="Wykres przedstawiający temperaturę powierzchni skóry u badanych w trakcie rozgrywki w rzeczywistości wirtualnej"
    alt="Wykres przedstawiający temperaturę powierzchni skóry u badanych w trakcie rozgrywki w rzeczywistości wirtualnej" 
>}}

Ankiety ewaluacyjne potwierdziły te obserwacje: aż 90% badanych zadeklarowało zdecydowanie wyższy poziom zaabsorbowania w VR niż na PC. Co kluczowe, efekt ten występował całkowicie niezależnie od wieku, stażu w grach wideo czy wcześniejszego kontaktu z technologią VR.

Choć opaska medyczna dostarczała rzetelnych danych, jej zamknięty ekosystem uniemożliwiał pobieranie próbek w czasie rzeczywistym bezpośrednio do silnika gry. Eksport do plików CSV był możliwy dopiero po zakończeniu sesji. Zrozumiałem wtedy, że jeśli wirtualne światy mają dynamicznie reagować na emocje gracza, potrzebuję autorskiego, otwartego modułu telemetrycznego IoT działającego bez pośrednictwa zewnętrznych chmur.

## The Green Hour

Odpowiedzią na tę potrzebę stał się projekt **The Green Hour**, zrealizowany w ramach pracy magisterskiej na kierunku Aplikacje Internetu Rzeczy pod kierunkiem prof. UAM dr. hab. Sławomira Mamicy. Założeniem projektu było stworzenie kompletnego stanowiska badawczego: klimatycznej gry symulacyjno-śledczej w silniku Unity oraz bezprzewodowej aparatury pomiarowej, działającej w myśl zasady prywatności u podstaw (*privacy by design*) i przetwarzającej biometrię wyłącznie w obrębie lokalnej sieci.

Wybór transmisji bezprzewodowej był podyktowany względami psychologicznymi: plączące się przewody i fizyczny ciężar kabli stanowią potężny czynnik emersyjny, który stale przypomina użytkownikowi o obecności w laboratorium i niszczy iluzję odcięcia od świata realnego. Sercem modułu uczyniłem miniaturowy mikrokontroler ESP32-C3 Super Mini (architektura RISC-V, 160 MHz) z łącznością Wi-Fi i Bluetooth. 

Do rejestracji przewodnictwa skóry wykorzystałem sensor reakcji skórno-galwanicznej Grove z elektrodami umieszczonymi na palcach dłoni (odwrócona dynamika ADC wskazuje spadek oporu wraz z wypełnianiem się gruczołów potowych). Do pomiaru temperatury obwodowej posłużył sensor DS18B20 umieszczony w metalowej gilzie na magistrali 1-Wire, co umożliwiło szybką dezynfekcję medyczną pomiędzy kolejnymi uczestnikami badania.

{{< figure 
    src="/img-compressed/GreenHour/Obraz4_1_1.webp" 
    caption="Schemat połączeń układu pomiarowego. W trakcie badań układ był zasilany przez port USB-C stałym napięciem 5 V"
    alt="Schemat połączeń układu pomiarowego. W trakcie badań układ był zasilany przez port USB-C stałym napięciem 5 V" 
>}}

{{< figure 
    src="/img-compressed/GreenHour/Obraz4_1_2.webp" 
    caption="Zrzut ekranu projektu obudowy urządzenia pomiarowego z programu Autodesk Fusion 360"
    alt="Zrzut ekranu projektu obudowy urządzenia pomiarowego z programu Autodesk Fusion 360" 
>}}

{{< figure 
    src="/img-compressed/GreenHour/Obraz4_1_3.webp" 
    caption="Wnętrze urządzenia pomiarowego"
    alt="Wnętrze urządzenia pomiarowego" 
>}}

Istotną decyzją było wbudowanie w obudowę sześcioosiowego modułu inercyjnego MPU6050 (akcelerometr + żyroskop). Początkowo planowałem wykorzystać wbudowaną telemetrię kontrolerów DualSense, jednak system wejścia w silniku Unity celowo odcinał surowe pakiety IMU, a interfejs Steam Input mapuje żyroskop na ruch kursora myszy, co zaburzało eksperyment. Własny moduł MPU6050 zapewnił pełną agnostyczność. Mogliśmy zamontować tę samą aparaturę na tradycyjnym gamepadzie w teście PC oraz na nadgarstku gracza w goglach Meta Quest 3.

Największym zawodem projektu okazał się optyczny czujnik tętna i saturacji MAX30102. W teorii miniaturowa dioda naświetlająca tkanki i fotodetektor zliczający fale tętna wydawały się odpowiednie, ale w praktyce straciłem na ten sensor zbyt wiele czasu. Dynamiczne operowanie kontrolerem ruchowym w przestrzeni, napinanie mięśni przedramienia i zaciskanie chwytu powodowały przesunięcia sensora względem skóry. Algorytmy odrzucania próbek eliminowały tak ogromną liczbę zaszumionych pakietów, że do bufora nie trafiało niemal nic. Zamiast sztucznie wygładzać bezwartościowe dane, potraktowałem to jako cenny wynik negatywny. W dynamicznym VR puls jest wysoce podatny na artefakty ruchowe, dlatego główny ciężar wnioskowania należy oprzeć na znacznie stabilniejszym przewodnictwie skóry (GSR), temperaturze oraz kinetyce przyspieszeń.

Równolegle pokonałem ograniczenie biblioteki DS18B20, która przy pełnej rozdzielczości 12-bitowej blokowała pętlę mikrokontrolera na ponad 700 ms. Zastosowanie asynchronicznej konwersji uwolniło zasoby na próbkowanie akcelerometru z częstotliwością 50 Hz i filtr dolnoprzepustowy (21 Hz), przesyłając stabilne ramki JSON przez protokół WebSocket (port 81) w 100-milisekundowych interwałach.

{{< figure 
    src="/img-compressed/GreenHour/MocowanieGamepad.webp" 
    caption="Sposób montażu jednostki centralnej układu pomiarowego do kontrolera na potrzeby badania w środowisku PC. Jednostka centralna wyposażona jest w układ MPU6050 zbierający informacje o przyspieszeniu liniowym i kątowym."
    alt="Sposób montażu jednostki centralnej układu pomiarowego do kontrolera na potrzeby badania w środowisku PC. Jednostka centralna wyposażona jest w układ MPU6050 zbierający informacje o przyspieszeniu liniowym i kątowym." 
>}}

{{< figure 
    src="/img-compressed/GreenHour/MocowanieReka.webp" 
    caption="Sposób umocowania sensorów biofizycznych na dłoni osoby badanej"
    alt="Sposób umocowania sensorów biofizycznych na dłoni osoby badanej" 
>}}

W aplikacjach VR stabilność klatkażu to istotna kwestia komfortu użytkownika. Każde chwilowe przycięcie głównego wątku renderowania, powodujące spadek płynności poniżej progu odświeżania gogli, potrafi w ułamku sekundy wywołać u odbiorcy nudności (chorobę symulatorową) i zniszczyć poczucie zanurzenia. Tymczasem natywny deserializator tekstu silnika nie jest bezpieczny wątkowo i próba parsowania danych bezpośrednio na wątku sieciowym prowadzi do natychmiastowych błędów pamięci.

Aby pogodzić intensywny napływ danych telemetrycznych z absolutnym priorytetem płynności grafiki, zaprojektowałem dwustopniową architekturę buforowania producent–konsument opartą na dwóch niezależnych kolejkach FIFO i semaforze blokującym `wsLock`. Wątek sieciowy jedynie odkłada surowy string do pierwszej kolejki, a główny wątek Unity w metodzie `Update()` dokonuje bezpiecznej deserializacji do struktur pamięciowych.

```csharp
// Wątek sieciowy biblioteki WebSocket – wyłącznie odkładanie surowego tekstu
private void OnMessageReceived(object sender, MessageEventArgs e)
{
    lock (wsLock)
    {
        incomingRawJson.Enqueue(e.Data);
    }
}

// Główny wątek renderowania Unity – bezpieczna deserializacja do pamięci silnika
private void Update()
{
    lock (wsLock)
    {
        while (incomingRawJson.Count > 0)
        {
            string json = incomingRawJson.Dequeue();
            SensorData data = JsonUtility.FromJson<SensorData>(json);
            incomingReadings.Enqueue(data);
        }
    }
}
```

W kolejnym kroku dane poddawane są redukcji częstotliwości do poziomu 1 Hz w dedykowanej pętli agregującej, działającej jak filtr wygładzający drobne artefakty kontaktowe. W tym samym interwale silnik analizuje sygnał z mikrofonu (wartość RMS), rejestrując bezinwazyjnie reakcje wokalne: od westchnień po przyspieszony oddech. Globalny nasłuch zdarzeń motorycznych zlicza gęstość wciśnięć przycisków na sekundę. Zapis do pliku CSV odbywa się asynchronicznie w osobnym zadaniu dyskowym, eliminując jakiekolwiek przycięcia klatkażu podczas zabawy.

### Wirtualny Reżyser

Najbardziej zaawansowany zapis biometryczny staje się bezużyteczny dla analizy statystycznej i algorytmów uczenia maszynowego, jeśli nie wiemy dokładnie, co w danej sekundzie działo się w świecie wirtualnym. Pomiędzy suchym odczytem fizjologicznym a zachowaniem gracza musi istnieć czytelny kontekst przyczynowo-skutkowy. Aby rozwiązać ten problem, stworzyłem moduł **Wirtualnego Reżysera**, inspirowany rolą Mistrza Gry w tradycyjnych papierowych grach fabularnych oraz psychologiczną teorią przepływu (*flow*) Mihálya Csíkszentmihályiego.

Stan przepływu to wąski kanał optymalnego balansu między rosnącymi umiejętnościami gracza a stawianym przed nim wyzwaniem. Gdy wyzwanie jest zbyt małe, gracz wpada w nudę. Fdy zbyt gwałtowne – w paraliżujący lęk i frustrację. Zadaniem Wirtualnego Reżysera powinno być dynamiczne modulowanie natężenia bodźców w taki sposób, aby utrzymać gracza w strefie maksymalnego zaabsorbowania. 

Skrypt zarządza scenariuszem, przełączając go pomiędzy fazami wyciszenia a sekwencjami narastającego stresu. Kontroluje upływ wirtualnego czasu, wzmaga porywy wiatru, wygasza światła czy aktywuje sekwencje dźwiękowe (np. trzask gałęzi, odgłosy kroków wokół opuszczonej chatki, awaria bezpieczników). Dzięki ścisłej integracji z agregatorem danych każdy jednosekundowy rekord biometrii jest automatycznie wzbogacany o stempel strefy mapy, stan fabularny oraz listę wyzwolonych bodźców.

Warto w tym miejscu wspomnieć o przygotowanym prototypie stymulacji węchowej. Jest to niezależny moduł oparty na wielokanałowym dyfuzorze zapachów, sterowany komendami sieciowymi w momencie przekraczania przez gracza określonych stref lasu. Nawiązując do historycznej koncepcji Sensoramy Mortona Heiligera z 1962 roku, zaangażowanie zmysłu węchu może stanowić ciekawe narzędzie immersyjne, którego wpływ na przewodnictwo skóry zamierzam rozwijać w kolejnych projektach.

### Most hybrydowy i diegetyzacja

Poważnym błędem metodologicznym w wielu publikacjach porównujących wirtualną rzeczywistość z tradycyjnymi monitorami jest tworzenie dwóch osobnych gier. Często wersja komputerowa różni się geometrią poziomów lub mechaniką poruszania się, co wprowadza do eksperymentu potężne zmienne zakłócające. W projekcie *The Green Hour* postawiłem sobie za cel stworzenie **jednej, w pełni współdzielonej bazy kodu i sceny**, na której oba tryby działają w oparciu o identyczne zasady fizyki silnika Unity z potokiem HDRP.

Aby to osiągnąć, zaprojektowałem autorski most kompatybilności dla kamery pierwszoosobowej na komputerze osobistym. Zamiast pisać osobną logikę interakcji dla myszy i klawiatury, skrypt kamery rzuca promienie detekcyjne (raycasting) i programowo wywołuje metody bezpośredniej interakcji na natywnych komponentach zestawu narzędzi VR (XR Interaction Toolkit). W efekcie ta sama gałąź kodu odpowiada za chwytanie przedmiotów, wkładanie wirtualnych kaset do magnetowidu czy operowanie suwakami generatora, bez względu na kontroler.

Równie istotnym wyzwaniem było rozwiązanie problemu interfejsu użytkownika. Zgodnie z typologią emersji Piotra Kubińskiego, klasyczne paski zdrowia, cyfrowe liczniki czy ikony zawieszone na krawędziach ekranu działają wybijająco, nieustannie przypominając odbiorcy o sztuczności symulacji. Aby temu zapobiec, zastosowałem pełną **diegetyzację**: cała warstwa wizualna została wystylizowana na ekran analogowej kamery wideo z przełomu wieków, trzymanej przez sterowaną postać dokumentującą leśne śledztwo. 

Nawiązując do estetyki filmów i gier *found footage* (*The Blair Witch Project*, *Backrooms*), celowe wprowadzenie ziarna filmowego, lekkiej aberracji chromatycznej i winiety dało podwójną korzyść: nadało grze surowy, niepokojący klimat, a jednocześnie zamaskowało drobne różnice w rozdzielczości tekstur. Parametry kamery – stan baterii wyznaczający upływ dnia, wskaźnik poziomu dźwięku oraz tętno przesyłane na żywo z aparatury pomiarowej – stały się integralnymi elementami świata przedstawionego. Dodatkowe informacje, takie jak instrukcja sterowania, notatki fabularne czy bestiariusz, zostały wprowadzone wprost do poziomów jako plakaty, czytelne kartki papieru i stary komputer z prezentacją slajdów.

W środowisku VR diegetyzacja przełożyła się na zjawisko **asynchronicznej dwuręczności**. Uczestnicy badania w goglach natychmiast wykorzystywali obie dłonie niezależnie – oświetlając latarką w jednej ręce naprawianą instalację elektryczną trzymaną w drugiej, lub intuicyjnie odkładając przedmioty na pobliskie wirtualne półki i stoły, co przy sterowaniu gamepadem na PC było zupełnie nieosiągalne.

{{< figure 
    src="/img-compressed/GreenHour/Interface.webp" 
    caption="W trakcie rozgrywki gracz natrafia na tablicę informacyjną. Tłumaczy ona najważniejsze zasady gry oraz wyświetla w przybliżeniu dwie wartości, którymi gracz musi zarządzać."
    alt="W trakcie rozgrywki gracz natrafia na tablicę informacyjną. Tłumaczy ona najważniejsze zasady gry oraz wyświetla w przybliżeniu dwie wartości, którymi gracz musi zarządzać." 
>}}

### Wnioski

Ewaluację techniczną potoku przeprowadziłem w ramach wewnątrzgrupowego badania laboratoryjnego z udziałem dziesięciu ochotników. Każdy uczestnik przechodził przez dwie około półgodzinne sesje badawcze – jedną przed panoramicznym monitorem z kontrolerem w dłoniach oraz drugą w goglach wirtualnej rzeczywistości Meta Quest 3 działających bezprzewodowo w trybie PCVR. Kolejność środowisk była dobierana losowo, a pomiędzy rozgrywkami obowiązywała trzydziestominutowa przerwa regeneracyjna w celu ustabilizowania parametrów somatycznych i zniwelowania zmęczenia poznawczego.

Analiza statystyczna z wykorzystaniem nieparametrycznego testu znakowanych rang Wilcoxona dla par wiązanych wykazała spektakularne różnice w zachowaniu motorycznym badanych. W środowisku VR średnia gęstość akcji wzrosła ponad ośmiokrotnie w porównaniu z klasycznym ekranem, osiągając wartość niemal dwóch i pół akcji na sekundę przy pełnej istotności statystycznej ($p = 0.0039$) i maksymalnej wielkości efektu. Równolegle zanotowałem blisko pięciokrotny wzrost średniej prędkości kątowej ruchów dłoni rejestrowanej przez wbudowany moduł inercyjny. Te twarde dane liczbowe dowodzą, że wirtualna rzeczywistość wymusza zupełnie inny wzorzec zaangażowania kinestetycznego: gracz przestaje być statycznym obserwatorem wciskającym przyciski pod kciukiem, a staje się aktywnym aktorem eksplorującym przestrzeń całym ciałem.

Niezwykle pouczający okazał się **odruch orientacyjny na dźwięk przestrzenny**. Mimo że zestaw VR wykorzystywał zintegrowane głośniki otwarte (oferujące obiektywnie niższą izolację od hałasów otoczenia niż wokółuszne słuchawki ISK HD9999 użyte na PC), gracze w goglach błyskawicznie reagowali gwałtownym obrotem głowy i całego tułowia w stronę każdego najcichszego szelestu. Wielu z nich po teście twierdziło z przekonaniem, że wersja VR miała „znacznie bogatsze udźwiękowienie”, choć w obu scenariuszach wyzwalano dokładnie te same pliki audio.

Równie fascynujące okazały się odczyty fizjologiczne. W warunkach wirtualnej rzeczywistości zaobserwowałem trend spadkowy temperatury skóry oraz systematyczne obniżanie się oporu elektrycznego skóry, co sugeruje aktywację współczulnego układu nerwowego.

Co najbardziej uderzające z punktu widzenia psychologii immersji, efekt ten osiągnąłem w grze, w której **celowo nie zaimplementowałem żadnego fizycznego modelu potwora ani bezpośredniego zagrożenia życia**. Z powodów technicznych w kodzie nie było ani jednej linijki sztucznej inteligencji oponenta. Mimo to gracze w VR wpatrywali się w ciemność z napięciem, przekonani, że w gęstwinie czai się kryptyda obserwująca każdy ich krok. Poczucie grozy i somatyczna reakcja obronna wynikały wyłącznie z psychologicznej siły sugestii, budowanej przez udźwiękowienie 3D, grę cieni i narrację środowiskową.

O tym, jak niebywale czuły okazał się ten układ w rejestracji gwałtownych emocji, przekonałem się podczas sesji jednej z uczestniczek. W trakcie przeszukiwania chatki przypadkowo strąciła ze stołu szklaną butelkę. Dźwięk rozbijającego się szkła wywołał u niej odruchowy lęk, zwieńczony głośnym okrzykiem. Kiedy po zakończeniu badania nałożyłem na siebie wykresy telemetryczne, wysoka, wąska szpilka amplitudy dźwięku z mikrofonu zsynchronizowała się ze stromym załamaniem oporu elektrycznego skóry (GSR), dokumentując moment, w którym impuls nerwowy w ułamku sekundy pobudził gruczoły potowe dłoni.

*Tabela 8.2.1. Zestawienie wyników testu Wilcoxona dla analizowanych wymiarów*

| Wymiar | Statystyka (*W*) | Istotność statystyczna (*p*) | Średnia PC | Średnia VR |
| :--- | :---: | :---: | :---: | :---: |
| Świadomość przestrzenna | 1.00 | 0.0039 | 2.72 | 4.22 |
| Zaangażowanie | 7.50 | 0.0430 | 2.84 | 3.87 |
| Poczucie przepływu | 11.50 | 0.1133 | 3.40 | 3.73 |
| Świadomość środowiskowa | 7.50 | 0.0410 | 3.32 | 3.68 |
| Poczucie choroby symulatorowej | 0.50 | 0.0039 | 1.30 | 2.50 |
| Percepcja czasu | 27.0000 | 1.0000 | 6.44% | 8.48% |

Różnice w postrzeganiu czasu są bardzo indywidualne i test Wilcoxona (Tabela 8.2.1) daje wartość *p* na poziomie równym 1,0 dla wymiaru percepcji czasu, co oznacza, że wyznaczone różnice są nieistotne statystycznie.

*Tabela 8.2.2. Zestawienie deklarowanego przez badanych czasu rozgrywki z rzeczywistym, z uwzględnieniem platform*

| Badany | Platforma | Raportowany czas badania | Rzeczywisty czas badania | Błąd percepcji |
| :---: | :---: | :---: | :---: | :---: |
| 1 | PC | 15 min | 31.04 min | -52% |
| 1 | VR | 20 min | 32.84 min | -39% |
| 2 | PC | 30 min | 30.43 min | -1% |
| 2 | VR | 20 min | 19.19 min | 4% |
| 3 | PC | 30 min | 30.61 min | -2% |
| 3 | VR | 30 min | 16.98 min | 77% |
| 4 | PC | 30 min | 24.06 min | 25% |
| 4 | VR | 20 min | 22.21 min | -10% |
| 5 | PC | 20 min | 25.90 min | -23% |
| 5 | VR | 15 min | 21.82 min | -31% |
| 6 | PC | 20 min | 20.68 min | -3% |
| 6 | VR | 22 min | 25.73 min | -14% |
| 7 | PC | 30 min | 25.98 min | 15% |
| 7 | VR | 50 min | 24.17 min | 107% |
| 8 | PC | 30 min | 20.37 min | 47% |
| 8 | VR | 25 min | 21.35 min | 17% |
| 9 | PC | 25 min | 26.09 min | -4% |
| 9 | VR | 25 min | 22.06 min | 13% |
| 10 | PC | 30 min | 18.48 min | 62% |
| 10 | VR | 15 min | 24.44 min | -39% |

Interpretacja danych badawczych przeprowadzona przy wsparciu dużego modelu językowego sugeruje, że w obrębie badanej próby środowisko rzeczywistości wirtualnej wykazuje wyższą skuteczność w stymulowaniu wybranych wymiarów doświadczenia użytkownika niż standardowa rozgrywka desktopowa. Zaobserwowane tendencje stanowią wyraźną przesłankę ku temu, iż możliwa jest skuteczna, prowadzona w czasie rzeczywistym akwizycja i analiza wskaźników fizjologicznych użytkownika pod kątem identyfikacji jego poczucia immersji i przepływu. Ze względu na relatywnie niewielką liczebność próby wyciąganie kategorycznych wniosków populacyjnych byłoby na obecnym etapie nieuzasadnione. Niemniej jednak niniejsze studium ma istotny charakter eksploracyjny i dostarcza fundamentu metodologicznego do zaprojektowania pogłębionych eksperymentów w tym obszarze.

## Podsumowanie

Przeprowadzone badania pilotażowe dostarczają istotnych przesłanek dotyczących różnic w percepcji środowisk wirtualnych w zależności od platformy sprzętowej oraz mechanizmów generowania immersji i stanu przepływu. Ze względu na ograniczoną liczebność próby oraz ramy czasowe uzyskane wyniki mają charakter eksploracyjny. Ich głównym celem jest identyfikacja ogólnych trendów i sformułowanie wstępnych hipotez badawczych.

Zgromadzony materiał – poparty zarówno eksperymentem laboratoryjnym, jak i badaniem ankietowym sugeruje, że **zjawiska immersji oraz stanu przepływu (flow) nie są tożsame i wyzwalają je odmienne uwarunkowania projektowe**:
1. **Stan przepływu (*flow*)** najsilniej generują środowiska o wysokiej dynamice mechanicznej, oparte na rosnącym poziomie trudności, rywalizacji PvP czy powtarzalnym optymalizowaniu czynności (*farming/grinding*). Gracz wchodzi wówczas w swoisty mechaniczny trans wymagający precyzji, który nie musi jednak wiązać się z poczuciem „bycia wewnątrz wirtualnego świata”.
2. **Poczucie immersji i obecności (*presence*)** dominują z kolei w produkcjach zorientowanych na eksplorację, narrację środowiskową i zmysłowe doświadczanie świata przedstawionego. Wysoka immersja środowiskowa ułatwia graczowi wejście w stan przepływu poprzez stymulację **motywacji autotelicznej**, czyli podejmowania wyzwań dla czystej satysfakcji z samej czynności, co okazuje się znacznie trwalsze niż zewnętrzne systemy nagród.

Dysonans sensoryczny (wzrok rejestruje dynamiczny ruch, podczas gdy błędnik informuje o braku przyspieszeń fizycznych) prowadzi do symptomów choroby symulatorowej. Dochodzi do tego zmęczenie dwutorowo: czysto fizyczne (nacisk gogli na twarz, akomodacja wzroku) oraz wyczerpanie poznawcze wynikające z potężnej stymulacji stereoskopowej. Tłumaczy to, dlaczego w ankietach aż 70% graczy deklaruje czas pojedynczej sesji VR poniżej jednej godzin.

Dalsze prace powinny skupić się na włączeniu nieinwazyjnej pupilometrii (śledzenia ruchów źrenic, dostępnego w goglach z *foveated rendering*) oraz optymalizacji potoku analitycznego o lokalne modele AI. Wdrożenie wyspecjalizowanych agentów pozwoli w przyszłości na pełną realizację koncepcji **Wirtualnego Reżysera** – adaptacyjnego środowiska gry, które w czasie rzeczywistym moduluje tempo, oświetlenie i poziom wyzwania w bezpośredniej odpowiedzi na odczyty z autonomicznego układu nerwowego gracza.

Ostatecznym celem wdrażania zaawansowanych systemów biometrycznych nie jest zredukowanie człowieka do przewidywalnego zestawu wykresów. Prawdziwa immersja zaczyna się wtedy, gdy cyfrowy świat szanuje inteligencję odbiorcy, stając się responsywnym placem zabaw – przestrzenią, która nie tylko otacza gracza, ale bezgłośnie i czule reaguje na jego biologiczną obecność.
