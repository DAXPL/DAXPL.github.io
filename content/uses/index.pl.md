---
title: "Ekwipunek (/uses)"
description: "Spis aparatury pomiarowej, maszyn warsztatowych, sprzętu XR, stacji roboczych i oprogramowania w Input Garage."
cascade:
  showDate: false
  showAuthor: false
---

<div class="telemetry-badge-container">
  <span class="status-pill">STATUS: SPIS INWENTARZA</span>
  <span class="status-pill status-pill-meta">REWIZJA: 2026.4 // TOLERANCJA: NOMINALNA</span>
</div>

> [!NOTE]
> Strona w formacie [**/uses**](https://uses.tech) – szczegółowy spis sprzętu, maszyn, aparatury pomiarowej i narzędzi programistycznych, które tworzą mój warsztat.

---

### 🖨️ Fabrykacja & Rapid Prototyping
* **Drukarka Ender 3 (a właściwie 3 i 3/4):** Oryginalny Ender 3 z 2018 roku, zmodyfikowany tak bardzo, że często toczymy ze znajomymi dyskusje, czy dalej to się kwalifikuje jako Ender 3. Kupiony na chwilę, wciąż nie do zajechania.
  * **Płyta główna:** MKS Robin Nano V3.1
  * **Oś Z:** Podwójna oś Z
  * **Stół:** Szklany stół
  * **Chłodzenie:** [Satsana Dual 5015 Fan Duct](https://www.thingiverse.com/thing:5750189) z wentylatorem 4020
  * **Ekstruder:** [Direct Drive](https://www.thingiverse.com/thing:5396802)
  * **Host druku:** DELL WYSE 3040 z OctoPrintem na systemie DietPi i najtańszą kamerką Logitech, jaką kupiłem w okolicach 2018 roku
* **Suszarka do filamentu:** CREALITY Space Pi
* **Stacja lutownicza:** Yihua 878D 700W (kolba + Hot-Air)

---

### 🥽 Hardware XR & Sensoryka
* **Gogle VR:** Meta Quest 3, 128 GB
* **Mikrokontrolery:**
  * **Różne różniaste ESP32**
  * **Raspberry Pi 3B+:** Ostatnie opłacalne Raspberry Pi. Po tym, jak nie mogłem kupić czwórki w akceptowalnej cenie, nauczyłem się kochać cienkie klienty (thin clients). Przy okazji jestem eko i ratuję sprzęt przed wylądowaniem na wysypisku.
  * **Raspberry Pi Pico**

---

### 💻 Stacja robocza & Środowisko
* **Stacja robocza:** Zbudowana pod kątem kompilacji projektów w Unity, treningu modeli ML oraz renderowania w VR:
  * **CPU:** AMD Ryzen 7 7800X3D
  * **GPU:** RTX 4070 SUPER
  * **RAM:** GOODRAM IRDM 64GB [2x32GB 6400MHz DDR5 CL32 DIMM] ustawiony na 6000 MT/s
  * **Płyta główna:** Gigabyte X670 GAMING X AX V2
  * **Chłodzenie CPU:** Noctua NH-D15 chromax.black — ponieważ mam dość awaryjnych pomp w układach AiO
  * **Zasilacz:** be quiet! Pure Power 12 M 1000W
  * **Obudowa:** SilentiumPC Aquarius AQ-X70W Pure Black — najlepsza obudowa na świecie, nikt mnie nie przekona, że jest inaczej
  * **OS:** Windows 11 Edu potraktowany skryptem [winutil](https://github.com/christitustech/winutil)
  * **Klawiatura:** Dark Project ALU Midnight — w momencie, w którym zdałem sobie sprawę, że nigdy nie będę tak dobry w Blenderze jak Emil z zawiązanymi rękami i zasłoniętymi oczami, porzuciłem numpada na rzecz fajnego klikania, WYMIENNEGO KABLA oraz oprogramowania w przeglądarce
  * **Myszka:** Logitech G305
* **Serwery & Homelab:**
  * **DELL WYSE 5070:** Mały serwer hostujący HAOS (Home Assistant OS), n8n i te usługi, których akurat potrzebuję
  * **Linux (Debian / DietPi / Arch):** Na serwerach domowych, homelabie, do kompilacji firmware i konteneryzacji

---

### ⚙️ Software & Toolchain
* **Silniki i Grafika 3D:**
  * **Unity 3D**
  * **Blender**
  * **Fusion 360**
  * **Visual Studio & VS Code**
  * **Git**
  * **Google Antigravity**
* **Strona & Web:**
  * **Hugo (Blowfish):** Statyczny generator stron, Markdown, brak skryptów śledzących, hosting na GitHub Pages.
