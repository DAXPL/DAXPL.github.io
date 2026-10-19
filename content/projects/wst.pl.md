---
title: "WST / XR BINIU – Jak nauczyliśmy piasek myśleć, utopiliśmy łódkę i zbudowaliśmy własny ekosystem Sim2Real"
date: 2025-06-01
summary: "Od akademickiej symulacji w Unity 6 i wyrwanej głowicy drukarki przemysłowej po globalne sterowanie przez tunel VPN i własne protokoły UDP. Historia dwóch lat błędów, dymiącej elektroniki i budowy otwartej platformy dla pojazdów autonomicznych."
tags: ["Unity 6", "AI", "ML-Agents", "Reinforcement Learning", "ESP32", "C++", "C#", "Python", "Sim2Real", "Drony", "IoT", "Druk 3D", "Open-Source"]
categories: ["Projekty", "AI & Robotyka"]
---

> *"Naszym największym sukcesem było nauczenie piasku myślenia."*

Komercyjne systemy sterowania autonomicznymi pojazdami to często czarne skrzynki, które narzucają sztywne ramy tego, co wolno, a czego nie da się zrobić. Zamiast kupować gotowy kontroler lotu z zamkniętym kodem źródłowym, postanowiliśmy wziąć mikrokontroler za kilkanaście złotych, silnik gier i sprawdzić, co się stanie, gdy przestaniemy być przesadnie rozsądni. Tak narodził się projekt autonomicznego drona wodnego **XR BINIU** (*miXed Reality Blended Intelligence for Navigable Interactive UV's*), który z czasem przeszedł radykalną ewolucję w **WST (Weird Steering Things)**, czyli otwartą platformę do budowania i trenowania nietypowych maszyn bezzałogowych, bez ograniczeń co do środowiska. Przez dwa lata przeszliśmy drogę od pięknych fikołków w wirtualnym środowisku, przez wyrwane głowice drukarek 3D i dymiące przewody, aż po własne protokoły transmisji obrazu i globalną komunikację przez sieć komórkową. Nie wszystkie pomysły okazały się należeć do grona "dobrych" pomysłów, a większość zeszła kilka poziomów poniżej "zły pomysł". Nie mniej jednak nawet kierunki które okazały się być ślepymi zaułkami, były również okazją do dobrej zabawy i nauki. Wiedza "dlaczego nie działa" potrafi być bardziej przydatna niż "dlaczego działa".
---

## Mózg w chmurze, mięśnie na wodzie

 Największym problemem który uderzył nas już od samego początku projektu był ten sam problem który nawiedza wiele projektów - **koszty**. Wiedzieliśmy że chcemy wypuścić autonomiczną łódkę na jezioro, ale wizja ewentualnego utopienia raspberry pi czy nawet nvidia jetson nam się nie spodobała. Początkowo rozważaliśmy podejście znane z systemów dronowych, czyli użycie sygnału radiowego do wymiany danych między stacją bazową a łódką. Przepustowość takiego rozwiązania jest stosunkowo niska, ale wystarczająca. Dodatkowo jest to już dobrze zbadane i wspierane, a wybór róznego rodzaju nadajników i odbiorników jest ogromny! Niestety nawet zasięg liczony w kilometrach był niewystarczający. Do sterowania dronem chcieliśmy użyć stacji roboczych które już posiadamy. Wiedząc że ukochany RTX 4070 SUPER jest w Suchym Lesie, łódka na jeziorze na morasku a użyte przez nas ESP32 wspiera WI-FI i VPN, matematyka była prosta - stawiamy Prywatną Sieć Wirtualną!

 Dalej pozostawał jednak problem topienia się naczej "sztucznej głupoty", dlatego zdecydowaliśmy się użyć silnika **Unity 3D** do zaprojektowania symulacji. Podczas budowy autonomicznych robotów metodą **Sim2Real** (przenoszenia sztucznej inteligencji ze świata wirtualnego do rzeczywistego) jest przepaść dzieląca czyste środowisko silnika trójwymiarowego od fizycznych kabli, szumów pomiarowych i bezwładności sprzętu. Gdybyśmy pisali logikę sieci neuronowej bezpośrednio pod konkretne wyprowadzenia mikrokontrolera, każda zmiana czujnika zmuszałyby nas do przebudowy całego modelu. Potrzebowaliśmy architektury, która całkowicie oślepi sztuczną inteligencję na to, w jakim świecie aktualnie się znajduje, dając jej pewien stopień abstrakcji. Tak jak kierowcy nie muszą znać każdego szczegółu pracy samochodu, tak i AI nie musi wiedzieć jaki czujnik na jakim pinie co podaje. Musi być tylko świadome tych odczytów.

Rozwiązaniem okazała się bezwzględna decentralizacja i oddzielenie „Mózgu”, czyli komputera pokładowego uruchamiającego model decyzyjny, od „Mięśni”, czyli niskopoziomowego kontrolera generującego sygnały PWM i zbierającego surowe odczyty z czujników. W warstwie oprogramowania zaprojektowaliśmy wzorzec wirtualnej płytki stykowej – klasę `Breadboard` współpracującą z abstrakcyjnymi interfejsami silników (`IPWMMotor`) oraz czujników (`ISensor`). Podczas treningu w silniku **Unity 6** (z wykorzystaniem pakietu **ML-Agents** i uczenia przez wzmacnianie) model nadpisuje metody odpowiedzialne za zbieranie obserwacji i wydawanie akcji, komunikując się wyłącznie z ową wirtualną płytką.

Gdy nadchodzi moment wyjścia z laboratorium nad jezioro, w tym samym środowisku podmieniamy jedynie zestaw wtyczek podpiętych pod `Breadboard` na sterownik komunikujący się z fizycznym mikrokontrolerem **ESP32**. Podręcznikowa sztuka inżynierii oprogramowania sugeruje w takich miejscach wielopoziomowe wstrzykiwanie zależności i sterylny porządek w repozytorium, ale w ogniu walki, gdy kompilator w PlatformIO zaczynał płakać przy bardziej zawiłych strukturach, niektóre rzeczy spięliśmy na pojedynczym wskaźniku, żeby po prostu pchnąć prace do przodu. Czy ten kompromis ugryzł nas później podczas rozbudowy systemu? Owszem, i to wielokrotnie. **Jednak dzięki sztywnej separacji warstwy decyzyjnej od sprzętowej wytrenowany w komputerze agent AI przejmuje stery prawdziwej łódki bez zmiany choćby jednej linijki kodu sieci neuronowej.**

---

## Fale Gerstnera, merdanie dziobem i różowy mostek w VR

Zanim jednak cokolwiek wypłynęło na prawdziwy akwen, nasza wirtualna flota musiała przeżyć tysiące godzin przyspieszonego treningu. Wybraliśmy potok renderowania **HDRP (High Definition Render Pipeline)** w Unity 6 ze względu na natywną obsługę zaawansowanej fizyki wody opartej na falach Gerstnera (trochoidalnych). Pozwoliło nam to zasymulować nie tylko ładne odbicia światła, ale przede wszystkim złożone interferencje fal, zmienny prąd rzeki, wyporność i opory ośrodka. Zaprojektowaliśmy nienaturalnie krętą rzekę o rosnącym poziomie trudności, zwieńczoną bramką końcową z teksturą kota, za którą algorytm otrzymywał najwyższą nagrodę.

Właśnie na tym wirtualnym torze sztuczna inteligencja pokazała nam rzeczy, których wcale nie zaprogramowaliśmy. Ponieważ wyposażyliśmy model łodzi jedynie w trzy kierunkowe czujniki ultradźwiękowe, w najtrudniejszym, wąskim odcinku rzeki agenci mieli martwe pola widzenia. Ku naszemu zaskoczeniu sieć neuronowa w procesie prób i błędów samodzielnie wykształciła zachowanie przypominające „merdanie” dziobem – łódka wykonywała drobne, rytmiczne ruchy na boki podczas płynięcia naprzód, skanując otoczenie niczym owad czułkami. Z drugiej strony obserwowaliśmy też przypadki, w których pojedyncze instancje wpadały w lokalne minimum funkcji nagrody, całkowicie ignorowały logikę toru i z uporem maniaka zaczynały płynąć pod prąd, gdzie nie czekały na nie żadne punkty. **Wychwycenie tych anomalii na ekranie monitora pozwoliło nam skorygować rozmieszczenie czujników i system kar, zanim jeszcze wydaliśmy pierwszą złotówkę na fizyczny laminat i śruby.**

<!-- Miejsce na zrzut ekranu z toru treningowego w Unity z widocznymi bramkami i flotą agentów (Rys. 2.2 / 2.4 z raportu) -->

Równolegle z treningiem autonomii chcieliśmy dać człowiekowi możliwość wejścia „w skórę” kapitana i przejęcia kontroli nad fizyczną jednostką za pomocą gogli rzeczywistości wirtualnej. Stworzyliśmy wirtualny mostek kapitański, który tłumaczy ruchy operatora w przestrzeni VR na polecenia wysyłane w czasie rzeczywistym do robota na wodzie. Ponieważ mobilne gogle VR dysponują mocno ograniczoną mocą obliczeniową, model centralnego panelu sterowania wymodelowany w Blenderze został odchudzony do zaledwie 126 wierzchołków. Surową, niskopoligonową bryłę pokryliśmy w programie Substance 3D Painter materiałem przybrudzonego plastiku, przełamując go jaskrawymi, różowymi akcentami wokół ekranów telemetrycznych, co nadało kabinie charakterystyczny, lekko cyberpunkowy sznyt. **Tak radykalna optymalizacja siatki geometrycznej zagwarantowała płynność obrazu w goglach, chroniąc operatora przed chorobą lokomocyjną podczas zdalnego manewrowania łodzią.**

<!-- Miejsce na wizualizację mostka VR z różowymi akcentami (Rys. 2.5 / 2.8 z raportu) -->

---

## Płaskie dno, skurczone otwory i pacyfistyczna wieżyczka

Kiedy oprogramowanie nabierało kształtów, druga część zespołu toczyła batalię w programie Fusion 360, próbując ubrać nasze pomysły w fizyczny kadłub. Inspirując się futurystycznymi koncepcjami okrętów wojennych pokroju *FNCS 2030*, postawiliśmy sobie trzy cele: ogromną wyporność zdolną unieść ciężkie akumulatory, wysoką zwinność na małych akwenach oraz napęd powietrzny. Rezygnacja z klasycznej śruby zanurzonej pod wodą na rzecz dwóch wentylatorów umieszczonych na bocznych ramionach wydawała się genialnym posunięciem, bo całkowicie eliminowała problem uszczelniania wałów napędowych poniżej linii wodnej.

Pierwsza wersja kadłuba, wymodelowana za pomocą gładkich powierzchni T-spline, miała szerokie, płaskie dno przypominające kontenerowiec. Wyporność była wprawdzie znakomita, ale pierwsze próby szybko sprowadziły nas na ziemię: płaskie dno powodowało, że przy próbie szybszego skrętu łódź traciła stabilność i próbowała się wywrócić. Przeprojektowaliśmy więc tylną część dna na bardziej zaostrzoną, aby jednostka stabilniej „wbijała się” w taflę wody, oraz dodaliśmy wnęki na czujniki kilka centymetrów poniżej górnej krawędzi dziobu – dokładnie tam, gdzie sugerowały to wcześniejsze symulacje w Unity.

Wtedy uderzył w nas kolejny problem inżynierski: program Bambu Studio oszacował masę naszego modelu na około cztery kilogramy. W obawie, że nasze silniki nie poradzą sobie z pchaniem takiego klocka, podjęliśmy szybką decyzję o przeskalowaniu całej bryły o 20% w dół, zbijając wagę do akceptowalnych trzech kilogramów przy wymiarach 800 na 295 na 242 milimetry. Niestety, w ferworze walki zapomnieliśmy, że globalne skalowanie zmniejszy też wycięte wcześniej gniazda montażowe. **Ten pozornie drobny skrót myślowy kosztował nas godziny ręcznego poprawiania otworów pod czujniki ultradźwiękowe i kamerę ESP32-CAM, ucząc nas, że analizę masy robi się przed wycinaniem detali pod elektronikę.**

Ciekawą ewolucję przeszła też osadzona na dziobie wieżyczka bojowa, obracana serwomechanizmem w zakresie 160 stopni. Pierwotnie planowaliśmy zamontować w niej układ pneumatyczny strzelający metalowymi kulkami, jednak zdrowy rozsądek i względy bezpieczeństwa na kampusie wzięły górę. Zamiast zbroić sztuczną inteligencję w wiatrówkę, podłączyliśmy wieżyczkę elastycznym wężem do pompy zanurzonej bezpośrednio w akwenie. **W ten sposób powstała bezpieczna armatka wodna o niewyczerpanym magazynku, która doskonale sprawdzała się w testach celowania bez ryzyka wybicia komuś oka.**

<!-- Miejsce na rysunek techniczny ostatecznej wersji kadłuba z wieżyczką (Rys. 4.5 z raportu) -->

---

## Wyrwana głowica i szpachla, czyli dramat druku 3D

Wydrukowanie osiemdziesięciocentymetrowego kadłuba z tworzywa PLA to zupełnie inna liga niż produkcja małych figurek na biurko. Nasze pierwsze prototypy w skali 1:5 oraz 1:2 powstawały w częściach na domowych drukarkach FDM, a następnie były spawane długopisem 3D i uszczelniane silikonem. Choć takie modele utrzymywały się na wodzie przez kilka godzin, wiedzieliśmy, że w pełnej skali każde klejenie to potencjalne miejsce pęknięcia, zalania elektroniki i zanieczyszczenia jeziora plastikiem.

Z pomocą przyszło **Wielkopolskie Centrum Zaawansowanych Technologii (WCZT)**, które udostępniło nam przemysłową drukarkę wielkoformatową *Dragon 3D* z serii Tower S o gigantycznym polu roboczym 100 na 100 na 150 centymetrów oraz potężnej dyszy o średnicy 1,8 milimetra. Tak gruba ścieżka nakładanego materiału wymusiła na nas przeprojektowanie wszystkich otworów montażowych – klasyczne półokrągłe łuki zapadały się w powietrzu, więc zastąpiliśmy je strzelistymi, gotyckimi zwieńczeniami, które stopniowo wyrastały z pionowych ścian bez konieczności stosowania jakichkolwiek podpór.

Mimo starannego przygotowania geometrii, pierwszy pełnowymiarowy wydruk zakończył się katastrofą. Chcąc zaoszczędzić materiał, ustawiliśmy wypełnienie wewnątrz ścian na poziomie zaledwie 5%. Po kilkudziesięciu godzinach pracy maszyny warstwy zaczęły się od siebie odklejać, a luźne, grube nitki plastiku owinęły się wokół głowicy drukującej. Przy jednym ze skrajnych ruchów sztywna bryła zastygłego filamentu zadziałała jak łom i mechanicznie wyrwała blok grzewczy z mocowania.

<!-- Miejsce na zdjęcie wyrwanego bloku grzewczego / uszkodzonego wydruku (Rys. 5.4 / 5.5 z raportu lub broken.webp) -->

Zwiększenie wypełnienia do 20% oraz wymiana głowicy rozwiązały problem delaminacji, ale los postanowił przetestować nas jeszcze raz: w trakcie kolejnego podejścia w budynku zabrakło prądu, a chwilę później skończyła się nasza szpula filamentu. Wydruk uratowali pracownicy WCZT, poratowawszy nas dwuipółkilogramową szpulą białego PLA z zapasów instytutu. **Surowy, dwukolorowy kadłub z widocznymi śladami po ogromnej dyszy potraktowaliśmy ciężką szlifierką, szpachlą uniwersalną oraz lakierem uszczelniającym, zyskując pancerną, jednolitą skorupę gotową na przyjęcie elektroniki.**

---

## Mit pięciu woltów i drżący akcelerometr

Gdyby wierzyć oficjalnej dokumentacji technicznej, budowa warstwy elektronicznej polega na podpięciu pięciu woltów do płytki ESP32, połączeniu kilku przewodów z mostkiem H (L298N) i wgraniu gotowej biblioteki. W rzeczywistości układ zasilania okazał się naszym największym koszmarem i źródłem siwych włosów. Kiedy dwa silniki prądu stałego (6–12V) gwałtownie ruszały, a moduł Wi-Fi jednocześnie próbował wypchnąć pakiet danych, spadki napięcia i szpilki prądowe potrafiły zresetować mikrokontroler w ułamku sekundy lub wywołać zapach palonego krzemu.

Musieliśmy szybko przejść przyspieszony kurs pokory wobec praw elektrotechniki. Nauczyliśmy się odpowiednio dobierać i lutować kondensatory filtrujące, odseparowaliśmy zasilanie napędów od logiki sterującej i zaczęliśmy agresywnie optymalizować moc nadawczą samego modułu radiowego w ESP32. Na tym jednak schody się nie kończyły. Czujnik ciśnienia BMP280 oraz akcelerometr ADXL345 odmówiły współpracy na jednej magistrali I2C, co zmusiło nas do ręcznego konfigurowania alternatywnych portów na osobnych pinach SDA i SCL. Co więcej, wibracje generowane przez boczne śmigła napędu powietrznego wprowadzały tak potężny szum na akcelerometrze, że odczyty przypominały zapis trzęsienia ziemi, a ciągła serializacja danych z wielu czujników do obiektów `JsonDocument` błyskawicznie zapychała skromną pamięć RAM mikrokontrolera.

Zamiast walczyć ze sprzętem na siłę, rozłożyliśmy obliczenia i komunikację w czasie. Wprowadziliśmy buforowanie odczytów i ograniczyliśmy częstotliwość wysyłania pełnych raportów telemetrycznych przez WebSocket. **Choć celowe spowolnienie cyklu komunikacyjnego może brzmieć jak krok wstecz, w praktyce uwolniło pamięć mikrokontrolera i dało nam stabilność, bez której łódka stawała się bezwładnym kawałkiem plastiku na środku stawu.**

---

## Pierwsze wodowanie, czyli jak utopiliśmy nasz projekt

Nadszedł dzień prawdy, wokół którego narosło całe wydarzenie promocyjne – z plakatami generowanymi w ComfyUI (gdzie stoczyliśmy osobną, przezabawną walkę z modelami dyfuzyjnymi, które za nic nie potrafiły poprawnie przeliterować nazwy projektu na grafikach). Stanęliśmy nad brzegiem z gotową, trzykilogramową jednostką, uruchomiliśmy połączenie i położyliśmy nasz statek na wodzie.

Jak wypadł wielki sprawdzian technologii Sim2Real w rzeczywistych warunkach? W skrócie: utopił się.

Konstrukcja spełniła wprawdzie dwa z trzech założeń – miała zapas wyporności, a napęd powietrzny dawał jej słuszny ciąg – ale zwrotność okazała się piętą achillesową. Prawdziwa woda, wiatr i bezwładność ciężkiego kadłuba sprawiły, że łódź nie chciała składać się w ostre zakręty tak chętnie, jak jej wirtualny odpowiednik, a drobne nieszczelności i choroby wieku dziecięcego niemal posłały nasz sprzęt na dno. Dopiero po osuszeniu elektroniki, uszczelnieniu newralgicznych punktów i żmudnym dostrojeniu siły oraz czasu trwania impulsów sterujących na silnikach, maszyna zaczęła słuchać poleceń i stabilnie pływać w sprzyjających warunkach pogodowych.

{{< gallery >}}
  <img alt="Wodowanie drona wodnego" src="/img-compressed/Errno/Drony/20250602_143615.webp" class="grid-w50 md:grid-w33" />
  <img alt="Testy konstrukcyjne drona" src="/img-compressed/Errno/Drony/20250602_143633.webp" class="grid-w50 md:grid-w33" />
  <img alt="Prace laboratoryjne nad elektroniką" src="/img-compressed/Errno/Drony/20250609_143529.webp" class="grid-w50 md:grid-w33" />
  <img alt="Zintegrowana jednostka autonomiczna" src="/img-compressed/Errno/Drony/IMG-20250609-WA0000.webp" class="grid-w50 md:grid-w33" />
  <img alt="Detale kadłuba i napędu" src="/img-compressed/Errno/Drony/20250602_144957.webp" class="grid-w50 md:grid-w33" />
  <img alt="Etap prototypowania elektroniki" src="/img-compressed/Errno/Drony/20250511_222628.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

To właśnie tam, stojąc nad wodą i patrząc na pływający prototyp, zrozumieliśmy coś ważnego. Pisanie oprogramowania pod jedną konkretną łódkę na zaliczenie przedmiotu jest na dłuższą metę nudne. Skoro nasza wirtualna płytka stykowa potrafiła przejąć kontrolę nad tym kadłubem, to równie dobrze możemy podpiąć pod nią cokolwiek innego – i (jak nam się wtedy naiwnie wydawało) zrobimy to niezwykle łatwo. **W tym momencie studencki projekt XR BINIU zrzucił akademicką skórę i przekształcił się w WST (Weird Steering Things) – otwarte środowisko tworzone nie dla zysku czy inwestorów, lecz z czystej radości eksperymentowania z tym, co dziwne.**

---

## Globalny tunel VPN, lag z Counter-Strike'a i wojna o klatki UDP

Ewolucja w stronę WST wymagała przecięcia pępowiny, jaką było lokalne połączenie Wi-Fi ograniczające nas do zasięgu hotspotu na brzegu. Dołożyliśmy do architektury modem **GSM/LTE** oraz bramkę **VPN** postawioną na komputerze **Raspberry Pi**. Dzięki temu nasz „Mózg” w Unity może działać na mocnym komputerze stacjonarnym w Poznaniu, podczas gdy fizyczny pojazd łączy się z nim przez sieć komórkową z dowolnego miejsca na Ziemi, w którym jest zasięg operatora.

Oczywiście wpuszczenie ruchu sterującego w publiczną sieć komórkową i zaszyfrowany tunel VPN ma swoją cenę: opóźnienie sięgające od 100 do 200 milisekund. Dla gracza w *Counter-Strike 2* taki ping oznacza pewną przegraną i wyrzucenie myszki przez okno, jednak w przypadku bezwładnej łodzi wodnej – a jak teoretyzujemy, również powoli lecącego drona powietrznego – dwie dziesiąte sekundy to wciąż wystarczający czas na reakcję.

Prawdziwe schody zaczęły się przy przesyłaniu obrazu z kamery na żywo, gdzie chcieliśmy zejść z opóźnieniem poniżej 100 milisekund. Zaczęliśmy pisać własne protokoły strumieniowania wideo oparte na bezpołączeniowym protokole **UDP**. Szybko zderzyliśmy się z klasycznym dylematem sieciowym: dzielenie pojedynczej klatki obrazu na mniejsze pakiety prowadzi do koszmaru z ich ponownym składaniem, gdy choćby jeden fragment zgubi się po drodze w eterze. Z kolei upchnięcie całej skompresowanej klatki w jeden większy pakiet rozwiązuje problem fragmentacji, ale sprawia, że pakiety potrafią docierać do odbiornika w losowej kolejności, powodując cofanie się obrazu w czasie. **Opracowanie własnego mechanizmu numerowania i odrzucania spóźnionych klatek po stronie odbiorczej pozwoliło nam okiełznać chaos protokołu UDP i uzyskać płynny podgląd bez zamrażania pasma sterującego.**

---

## Projekt jak dobre wino i ludzie za sterami

Naturalnym rozwinięciem filozofii WST stał się projekt **bicoptera** – maszyny latającej wyposażonej w zaledwie dwa wirniki pochylane za pomocą serwomechanizmów. To konstrukcja z natury skrajnie niestabilna aerodynamicznie, stanowiąca wymarzony poligon dla sieci neuronowych trenowanych w symulacji przed pierwszym lotem w rzeczywistym świecie. Obecnie zarówno dopieszczenie pełnej autonomii łodzi, jak i ulotnienie bicoptera musiały jednak chwilę poczekać na półce. Życie akademickie ma swoją dynamikę, a pisanie oraz obrony prac magisterskich skutecznie odciągnęły nas od lutownic i żywicy. Nie traktujemy tego jednak w kategoriach porażki. **Ambitne projekty inżynierskie są jak dobre wino – potrzebują czasu, żeby poleżakować w głowach twórców, dojrzeć i poczekać na moment, w którym wrócimy do nich z zupełnie nowym bagażem doświadczeń.**

<!-- Miejsce na zdjęcie zespołu (team.webp) -->

Nic z tej szalonej, dwuletniej przygody na Wydziale Fizyki i Astronomii UAM nie wydarzyłoby się w pojedynkę. Całe zamieszanie w ramach Studenckiego Koła Naukowego **Errno** wspierał merytorycznie i logistycznie nasz opiekun, **dr Wojciech Czart**. Za to, że pięciodolarowe kontrolery ostatecznie przeżyły spotkania z wybuchającymi kondensatorami, odpowiadał architekt elektroniki **inż. Adam Mischke**, natomiast strażniczką jakości kodu w Unity, która powstrzymywała nasze repozytorium przed stoczeniem się w całkowity chaos, była **Oliwia „Cosinus” Pawłowska**. Kształt kadłuba i walkę z wielkoformatowym drukiem 3D wziął na swoje barki **inż. Krystian Olesiejko**, konstrukcję latającego bicoptera zaprojektował **Emil Kopytek**, a tunele VPN i niskopoziomową komunikację sieciową w C++ utrzymywał przy życiu **Mateusz Nawrot**. Z kolei **inż. Wiktoria Bielecka** zadbała o warstwę wizualną oraz interfejsy użytkownika, będąc jedyną osobą stojącą między nami a projektem wyglądającym jak terminal Linuksa z 1995 roku. Mi przypadła rola lidera projektu, architekta systemu oraz programisty łączącego światy Unity i C++ – czyli głównie tego, który pyta „dlaczego nie?”, kiedy z płytki zaczyna lecieć dym.

Jeśli chcecie zajrzeć pod maskę naszych rozwiązań, prześledzić ewolucję kodu lub zbudować własny dziwny pojazd, aktualne repozytorium platformy znajdziecie na [GitHubie projektu WST](https://github.com/DAXPL/WST), natomiast pierwotną wersję badawczą zachowaliśmy w [archiwum XR-BINIU](https://github.com/DAXPL/XR-BINIU) wraz z pełną [dokumentacją techniczną w Google Docs](https://docs.google.com/document/d/1-k4Ll4qevaH445sVjVkQF32h3w11uCgUwEZ2eICMMHg/edit?usp=sharing).