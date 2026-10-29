---
title: "WST / XR BINIU – Jak nauczyliśmy piasek myśleć, utopiliśmy łódkę i zbudowaliśmy własny ekosystem Sim2Real"
date: 2025-06-01
summary: "Od akademickiej symulacji w Unity 6 i wyrwanej głowicy drukarki przemysłowej po globalne sterowanie przez tunel VPN i własne protokoły UDP. Historia dwóch lat błędów, dymiącej elektroniki i budowy otwartej platformy dla pojazdów autonomicznych."
tags: ["AI", "Sim2Real", "Robotyka", "Unity"]
categories: ["Projekty", "AI & Robotyka"]
---

Komercyjne systemy sterowania autonomicznymi pojazdami to często czarne skrzynki, które narzucają sztywne ramy tego, co wolno, a czego nie da się zrobić. Zamiast kupować gotowy kontroler lotu z zamkniętym kodem źródłowym, postanowiliśmy wziąć mikrokontroler za kilkanaście złotych, silnik gier i sprawdzić, co się stanie, gdy przestaniemy być przesadnie rozsądni. Tak narodził się projekt autonomicznego drona wodnego **XR BINIU** (*miXed Reality Blended Intelligence for Navigable Interactive UV's*), który z czasem ewoluował w **WST (Weird Steering Things)**, czyli platformę do budowania i trenowania nietypowych maszyn bezzałogowych, bez ograniczeń co do środowiska. Przez dwa lata przeszliśmy drogę od fikołków w wirtualnym środowisku, przez wyrwane głowice drukarek 3D i dymiące przewody, aż po własne protokoły transmisji obrazu i globalną komunikację przez sieć komórkową. Nie wszystkie pomysły okazały się należeć do grona tych "dobrych", a większość zeszła kilka poziomów poniżej "fatalnych". Nie mniej jednak nawet kierunki które okazały się być ślepymi zaułkami, były również okazją do dobrej zabawy i nauki. Wiedza "dlaczego nie działa" potrafi być bardziej przydatna niż "dlaczego działa".
---

## Mózg w chmurze, mięśnie na wodzie

 Największym problemem który uderzył nas już od samego początku projektu był ten sam problem który nawiedza wiele projektów studenckich czyli **koszty**. Wiedzieliśmy że chcemy wypuścić autonomiczną łódkę na jezioro, ale wizja ewentualnego utopienia raspberry pi czy nawet nvidia jetson nam się nie spodobała. Początkowo rozważaliśmy podejście znane z systemów dronowych, czyli użycie sygnału radiowego do wymiany danych między stacją bazową a łódką. Przepustowość takiego rozwiązania jest stosunkowo niska, ale wystarczająca. Dodatkowo jest to już dobrze zbadane i wspierane, a wybór róznego rodzaju nadajników i odbiorników jest ogromny! Niestety nawet zasięg liczony w kilometrach był niewystarczający. Do sterowania dronem chcieliśmy użyć stacji roboczych które już posiadamy. Wiedząc że ukochany RTX 4070 SUPER jest w Suchym Lesie, nasz główny pilot w Krakowie, łódka na jeziorze na morasku a użyte przez nas ESP32 wspiera WI-FI i VPN, matematyka była prosta - stawiamy Prywatną Sieć Wirtualną!

 Dalej pozostawał jednak problem topienia się naczej "sztucznej głupoty", dlatego zdecydowaliśmy się użyć silnika **Unity 3D** do zaprojektowania symulacji. Podczas budowy autonomicznych robotów metodą **Sim2Real** (przenoszenia sztucznej inteligencji ze świata wirtualnego do rzeczywistego) jest przepaść dzieląca czyste środowisko silnika trójwymiarowego od fizycznych kabli, szumów pomiarowych i bezwładności sprzętu. Gdybyśmy pisali logikę sieci neuronowej bezpośrednio pod konkretne wyprowadzenia mikrokontrolera, każda zmiana czujnika zmuszałyby nas do przebudowy całego modelu. Potrzebowaliśmy architektury, która całkowicie oślepi sztuczną inteligencję na to, w jakim świecie aktualnie się znajduje, dając jej pewien stopień abstrakcji. Tak jak kierowcy nie muszą znać każdego szczegółu pracy samochodu, tak i AI nie musi wiedzieć jaki czujnik na jakim pinie co podaje. Musi być tylko świadome tych odczytów.

Rozwiązaniem okazała się bezwzględna decentralizacja i oddzielenie „Mózgu”, czyli komputera pokładowego uruchamiającego model decyzyjny, od „Mięśni”, czyli niskopoziomowego kontrolera generującego sygnały PWM i zbierającego surowe odczyty z czujników. W warstwie oprogramowania zaprojektowaliśmy wzorzec wirtualnej płytki stykowej – klasę `Breadboard` współpracującą z abstrakcyjnymi interfejsami silników (`IPWMMotor`) oraz czujników (`ISensor`). Podczas treningu w silniku **Unity 6** (z wykorzystaniem pakietu **ML-Agents** i uczenia przez wzmacnianie) model nadpisuje metody odpowiedzialne za zbieranie obserwacji i wydawanie akcji, komunikując się wyłącznie z ową wirtualną płytką.

Gdy nadchodzi moment wyjścia z laboratorium nad jezioro, w tym samym środowisku podmieniamy jedynie zestaw wtyczek podpiętych pod `Breadboard` na sterownik komunikujący się z fizycznym mikrokontrolerem **ESP32**. Podręcznikowa sztuka inżynierii oprogramowania sugeruje w takich miejscach wielopoziomowe wstrzykiwanie zależności i sterylny porządek w repozytorium, ale w ogniu walki, gdy kompilator w PlatformIO zaczynał płakać przy bardziej zawiłych strukturach, niektóre rzeczy spięliśmy na pojedynczym wskaźniku, żeby po prostu pchnąć prace do przodu. Czy ten kompromis ugryzł nas później podczas rozbudowy systemu? Owszem, i to wielokrotnie. **Jednak dzięki sztywnej separacji warstwy decyzyjnej od sprzętowej wytrenowany w komputerze agent AI przejmuje stery prawdziwej łódki bez zmiany choćby jednej linijki kodu sieci neuronowej.**

---

## Fale Gerstnera, merdanie dziobem i różowy mostek w VR

Zanim jednak cokolwiek wypłynęło, nasza wirtualna flota musiała przeżyć tysiące godzin przyspieszonego treningu. Wybraliśmy potok renderowania **HDRP (High Definition Render Pipeline)** w Unity 6 ze względu na natywną obsługę zaawansowanej fizyki wody. Pozwoliło nam to zasymulować złożone interferencje fal, zmienny prąd rzeki, wyporność i opory ośrodka. Zaprojektowaliśmy nienaturalnie krętą rzekę o rosnącym poziomie trudności, zwieńczoną bramką końcową z teksturą kota, za którą algorytm otrzymywał najwyższą nagrodę.

Właśnie na tym wirtualnym torze sztuczna inteligencja pokazała nam rzeczy, których wcale nie zaprogramowaliśmy. Ponieważ wyposażyliśmy model łodzi jedynie w trzy kierunkowe czujniki ultradźwiękowe, w najtrudniejszym, wąskim odcinku rzeki agenci mieli martwe pola widzenia. Ku naszemu zaskoczeniu sieć neuronowa w procesie prób i błędów samodzielnie wykształciła zachowanie przypominające „merdanie” dziobem – łódka wykonywała drobne ruchy na boki podczas płynięcia naprzód, skanując otoczenie niczym owad czułkami. 

{{< figure 
    src="/img-compressed/Errno/Drony/Obraz1.webp" 
    caption="Trasa treningowa z brankami" 
    alt="Trasa treningowa z brankami" 
>}}

{{< figure 
    src="/img-compressed/Errno/Drony/Obraz3.webp" 
    caption="Flota agentów gotowa do szybkiego utopienia jednostki, znaczy się dzielnego trenowania" 
    alt="Flota agentów gotowa do szybkiego utopienia jednostki, znaczy się dzielnego trenowania" 
>}}

Równolegle z treningiem autonomii chcieliśmy dać człowiekowi możliwość wejścia „w skórę” kapitana i przejęcia kontroli nad fizyczną jednostką za pomocą gogli rzeczywistości wirtualnej. Stworzyliśmy wirtualny mostek kapitański, który tłumaczy ruchy operatora w przestrzeni VR na polecenia wysyłane w czasie rzeczywistym do robota na wodzie. Surową, niskopoligonową bryłę pokryliśmy w programie Substance 3D Painter materiałem przybrudzonego plastiku, przełamując go jaskrawymi, różowymi akcentami wokół ekranów telemetrycznych, co nadało kabinie charakterystyczny, lekko cyberpunkowy sznyt.
{{< figure 
    src="/img-compressed/Errno/Drony/Obraz4.webp" 
    caption="Mostek kapitański w VR" 
    alt="Mostek kapitański w VR" 
>}}

---

## Wyrwana głowica i szpachla

Kiedy oprogramowanie nabierało kształtów, druga część zespołu toczyła batalię w programie Fusion 360, próbując ubrać nasze pomysły w fizyczny kadłub. Inspirując się futurystycznymi koncepcjami okrętów wojennych pokroju *FNCS 2030*, postawiliśmy sobie trzy cele:  wyporność zdolną unieść ciężkie akumulatory, wysoką zwinność na małych akwenach oraz napęd powietrzny. Rezygnacja z klasycznej śruby zanurzonej pod wodą na rzecz dwóch wentylatorów umieszczonych na bocznych ramionach wydawała nam się dobrym posunięciem, bo całkowicie eliminowała problem uszczelniania wałów napędowych poniżej linii wodnej. Tworzy to co prawda sporo innych problemów w trakcie projektowania oraz zwiększa szansę na zaplątanie się w trzcine, ale nie chcielismy też robić tego co już było znane, chcieliśmy spróbować czegoś nowego.

Pierwsza wersja kadłuba, miała szerokie, płaskie dno przypominające kontenerowiec. Wyporność była wprawdzie znakomita, ale pierwsze próby szybko sprowadziły nas na ziemię: płaskie dno powodowało, że przy próbie szybszego skrętu łódź traciła stabilność i próbowała się wywrócić. Przeprojektowaliśmy więc tylną część dna na bardziej zaostrzoną, aby jednostka stabilniej „wbijała się” w taflę wody, oraz dodaliśmy wnęki na czujniki kilka centymetrów poniżej górnej krawędzi dziobu – dokładnie tam, gdzie sugerowały to wcześniejsze symulacje w Unity.

Wtedy uderzył w nas kolejny problem: program Bambu Studio oszacował masę naszego modelu na około cztery kilogramy. W obawie, że nasze silniki nie poradzą sobie z pchaniem takiego klocka, podjęliśmy szybką decyzję o przeskalowaniu całej bryły o 20% w dół, zbijając wagę do akceptowalnych trzech kilogramów przy wymiarach 800 na 295 na 242 milimetry. 

Wydrukowanie osiemdziesięciocentymetrowego kadłuba z tworzywa PLA to zupełnie inna liga niż produkcja małych figurek na biurko. Nasze pierwsze prototypy w skali 1:5 oraz 1:2 powstawały w częściach na domowych drukarkach FDM, a następnie były spawane długopisem 3D i uszczelniane silikonem. Choć takie modele utrzymywały się na wodzie przez kilka godzin, wiedzieliśmy, że w pełnej skali każde klejenie to potencjalne miejsce pęknięcia, zalania elektroniki i zanieczyszczenia jeziora plastikiem.

Z pomocą przyszło **Wielkopolskie Centrum Zaawansowanych Technologii (WCZT)**, które udostępniło nam przemysłową drukarkę wielkoformatową *Dragon 3D* z serii Tower S o gigantycznym polu roboczym 100 na 100 na 150 centymetrów oraz potężnej dyszy o średnicy 1,8 milimetra. Tak gruba ścieżka nakładanego materiału wymusiła na nas przeprojektowanie wszystkich otworów montażowych – klasyczne półokrągłe łuki zapadały się w powietrzu, więc zastąpiliśmy je strzelistymi, gotyckimi zwieńczeniami, które stopniowo wyrastały z pionowych ścian bez konieczności stosowania jakichkolwiek podpór.

{{< figure 
    src="/img-compressed/Errno/Drony/Obraz6.webp" 
    caption="Dragon 3D i Wiktoria obok Prusy dla skali" 
    alt="Dragon 3D i Wiktoria obok Prusy dla skali"
>}}

Mimo starannego przygotowania geometrii, pierwszy pełnowymiarowy wydruk zakończył się katastrofą. Chcąc zaoszczędzić materiał, ustawiliśmy wypełnienie wewnątrz ścian na poziomie zaledwie 5%. Po kilkudziesięciu godzinach pracy maszyny warstwy zaczęły się od siebie odklejać, a luźne, grube nitki plastiku owinęły się wokół głowicy drukującej. Przy jednym ze skrajnych ruchów sztywna bryła zastygłego filamentu zadziałała jak łom i mechanicznie wyrwała blok grzewczy z mocowania. Widok pojedynczej warstwy grubszej niż filament (1,8mm w stosunku do 1,75mm) zrobił na nas wrażenie. Większości osób druk 3D kojarzy się obecnie z eleganckimi rozwiązaniami Prusy czy Bambu Lab. My co prawda pamiętamy jeszcze toporne Endery, Anety czy nawet drewniane Accury, ale skala i konstrukcja Dragon'a budzi respekt do tej technologii. Zresztą cała wycieczka po WST jaką odbyliśmy przy okazji z jednej strony dodała nam skrzydeł kiedy zobaczyliśmy jakie niesamowite rzeczy można zrobić z drukiem 3D i nowymi technologiami, a jednocześnie sprowadziła nas na ziemię, pokazując ile jeszcze musimy się nauczyć. Jest to miejsce w którym z jednej strony trzeba mieć głowę na karku, a z drugiej należy zatracić się w niesamowitości i porzucić standardowe myślenie żeby zrobić w głowie miejsce na innowacyjność

{{< figure 
    src="/img-compressed/Errno/Drony/Obraz7.webp" 
    alt="Wyrwany hotend" 
    caption="Wyrwany hotend" 
>}}

{{< figure 
    src="/img-compressed/Errno/Drony/20250602_143534.webp" 
    caption="Uszkodzony wydruk. Widok pojedynczej warstwy grubszej niż filament (1,8mm w stosunku do 1,75mm) zrobił na nas wrażenie" 
    alt="Uszkodzony wydruk. Widok pojedynczej warstwy grubszej niż filament (1,8mm w stosunku do 1,75mm) zrobił na nas wrażenie" 
>}}

Zwiększenie wypełnienia do 20% oraz wymiana głowicy rozwiązały problem delaminacji, ale los postanowił przetestować nas jeszcze raz: w trakcie kolejnego podejścia w budynku zabrakło prądu, a jeszcze później skończyła się nasza szpula filamentu. Wydruk uratowali pracownicy WCZT, poratowawszy nas potężną szpulą białego PLA. **Surowy, dwukolorowy kadłub z widocznymi śladami po ogromnej dyszy potraktowaliśmy ciężką szlifierką, szpachlą uniwersalną oraz lakierem uszczelniającym, zyskując jednolitą skorupę gotową na przyjęcie elektroniki.**

{{< figure 
    src="/img-compressed/Errno/Drony/20250602_143633.webp" 
    caption="Drukarka w akcji"
    alt="Drukarka w akcji" 
>}}
---

## Pierwsze wodowanie, czyli jak utopiliśmy nasz projekt

Jak wypadł wielki sprawdzian technologii Sim2Real w rzeczywistych warunkach? W skrócie: utopił się.

Konstrukcja spełniła wprawdzie dwa z trzech założeń – miała zapas wyporności, a napęd powietrzny dawał jej słuszny ciąg – ale zwrotność okazała się piętą achillesową. Prawdziwa woda, wiatr i bezwładność ciężkiego kadłuba sprawiły, że łódź nie chciała składać się w ostre zakręty tak chętnie, jak jej wirtualny odpowiednik, a  choroby wieku dziecięcego posłały nasz sprzęt na dno. Dopiero po osuszeniu elektroniki, uszczelnieniu newralgicznych punktów i żmudnych poprawkach, maszyna zaczęła (w miarę) słuchać poleceń i (w miarę) stabilnie pływać w sprzyjających warunkach pogodowych.

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

## WST

Ewolucja w stronę WST wymagała przecięcia pępowiny, jaką było lokalne połączenie Wi-Fi ograniczające nas do zasięgu hotspotu na brzegu. Dołożyliśmy do architektury modem **GSM/LTE** oraz bramkę **VPN** postawioną na komputerze **Raspberry Pi**. Dzięki temu nasz „Mózg” w Unity może działać na mocnym komputerze stacjonarnym w Poznaniu, podczas gdy fizyczny pojazd łączy się z nim przez sieć komórkową z dowolnego miejsca na Ziemi, w którym jest zasięg operatora.

Zależało nam na tym żeby system wspierał **wszystko**. Jednym z mini-dronów był WST-TOSIA, czyli niewielki pojazd składający się z zaledwie dwóch silników. Z technicznego punktu widzenia nie różni się on wiele od łódki. Oba drony działają na zasadzie napędu różnicowego (ang. differential drive).

{{< figure 
    src="/img-compressed/Errno/Drony/20260319_172447.webp" 
    alt="WST-TOSIA" 
>}}

{{< figure 
    src="/img-compressed/Errno/Drony/20260408_153351.webp" 
    alt="WST-TOSIA2" 
>}}

Oczywiście wpuszczenie ruchu sterującego w publiczną sieć komórkową i zaszyfrowany tunel VPN ma swoją cenę: opóźnienie sięgające od 100 do 200 milisekund. Dla gracza w *Counter-Strike 2* taki ping oznacza pewną przegraną i wyrzucenie myszki przez okno, jednak w przypadku bezwładnej łodzi wodnej – a jak teoretyzujemy, również powoli lecącego drona powietrznego – dwie dziesiąte sekundy to wciąż wystarczający czas na reakcję.

Prawdziwe schody zaczęły się przy przesyłaniu obrazu z kamery na żywo, gdzie chcieliśmy zejść z opóźnieniem poniżej 100 milisekund. Zaczęliśmy pisać własne protokoły strumieniowania wideo oparte na bezpołączeniowym protokole **UDP**. Szybko zderzyliśmy się z klasycznym dylematem sieciowym: dzielenie pojedynczej klatki obrazu na mniejsze pakiety prowadzi do koszmaru z ich ponownym składaniem, gdy choćby jeden fragment zgubi się po drodze w eterze. Z kolei upchnięcie całej skompresowanej klatki w jeden większy pakiet rozwiązuje problem fragmentacji, ale sprawia, że pakiety potrafią docierać do odbiornika w losowej kolejności, powodując cofanie się obrazu w czasie.

---

## Projekt jak dobre wino i ludzie za sterami

Naturalnym rozwinięciem filozofii WST stał się projekt **bicoptera** – maszyny latającej wyposażonej w zaledwie dwa wirniki pochylane za pomocą serwomechanizmów. To konstrukcja z natury skrajnie niestabilna aerodynamicznie, stanowiąca wymarzony poligon dla sieci neuronowych trenowanych w symulacji przed pierwszym lotem w rzeczywistym świecie. Obecnie zarówno dopieszczenie pełnej autonomii łodzi, jak i ulotnienie bicoptera musiały jednak chwilę poczekać na półce. Życie akademickie ma swoją dynamikę, a pisanie oraz obrony prac magisterskich skutecznie odciągnęły nas od lutownic. Nie traktujemy tego jednak w kategoriach porażki. **Ambitne projekty są jak dobre wino – potrzebują czasu, żeby poleżakować, dojrzeć i poczekać na moment, w którym wrócimy do nich z zupełnie nowym bagażem doświadczeń.**

{{< gallery >}}
<img alt="Bicpoter" src="/img-compressed/Errno/Drony/image.webp" class="grid-w50 md:grid-w33" />
  <img alt="Bicpoter" src="/img-compressed/Errno/Drony/20260415_094547.webp" class="grid-w50 md:grid-w33" />
  <img alt="Też bicopter, ale z dużo głupszym pomysłem" src="/img-compressed/Errno/Drony/20260416_130653.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

Nic z tej szalonej przygody na Wydziale Fizyki i Astronomii UAM nie wydarzyłoby się w pojedynkę. Całe zamieszanie w ramach Studenckiego Koła Naukowego **Errno** wspierał merytorycznie i logistycznie nasz opiekun, **dr Wojciech Czart**. Za to, że pięciodolarowe kontrolery ostatecznie przeżyły spotkania z wybuchającymi kondensatorami, odpowiadał **inż. Adam Mischke**, natomiast strażniczką jakości kodu w Unity, która powstrzymywała nasze repozytorium przed stoczeniem się w całkowity chaos, była **Oliwia „Cosinus” Pawłowska**. Kształt kadłuba i walkę z wielkoformatowym drukiem 3D wziął na swoje barki **inż. Krystian Olesiejko**, konstrukcję latającego bicoptera zaprojektował **Emil Kopytek**, a tunele VPN i niskopoziomową komunikację sieciową w C++ utrzymywał przy życiu **Mateusz Nawrot**. Z kolei **inż. Wiktoria Bielecka** zadbała o warstwę wizualną oraz interfejsy użytkownika, będąc jedyną osobą stojącą między nami a projektem wyglądającym jak terminal Linuksa z 1995 roku. Mi przypadła rola lidera projektu, architekta systemu oraz programisty łączącego światy Unity i C++ – czyli głównie tego, który pyta „dlaczego nie?”, kiedy z płytki zaczyna lecieć dym.