---
title: "SNS Minerwa - Virtual Shooting Range"
date: 2022-09-15
summary: "A virtual marksmanship training system based on computer vision, ESP32-modified replicas, and Unity 3D."
tags: ["Unity", "Hardware", "ESP32", "Computer Vision"]
categories: ["Projects", "Gamedev & XR"]
---

**Starting in September 2024, the updated national curriculum mandates marksmanship training for Polish schools under the Defense and Safety Education (EDB) syllabus.** For many educational institutions, this suddenly presented a massive logistical headache. Introducing hands-on marksmanship training routinely clashes with the lack of access to shooting ranges, astronomical construction costs for dedicated infrastructure, and evident student safety concerns.

Project Minerwa was conceived as a direct response to this challenge. Instead of forcing schools to construct costly bullet traps, we designed a virtual system that brings reliable training straight into an ordinary classroom. All it requires to run is a computer running Unity, a school projector, and 3D-printed modular enclosures mounted on rifle replicas housing custom microcontroller modules.

{{< figure 
    src="/img-compressed/Minerwa/jsSrbE.webp" 
    alt="Minerwa virtual shooting system in action" 
>}}
## My Role in the Project

As **team leader**, I coordinated the work of an interdisciplinary team (programmers, 2D artists, 3D modelers), ensuring the overall stability of the deployed system.

In the technical domain, I served as the lead systems integrator. My primary challenge was bridging three disparate environments: computer vision scripts written in Python, physical microcontrollers communicating wirelessly, and the primary graphics engine — keeping the entire pipeline running smoothly even on modest school hardware.

---

# System Architecture

## Independent Network & Data Flow
Schools feature wildly inconsistent network infrastructure, which prompted us to eliminate any dependency on local school routers. The host computer serving as the game machine doubles as a standalone Wi-Fi Access Point. The ESP32 microcontrollers connect to it directly over WebSockets. Basing communication on the TCP protocol guarantees rock-solid reliability for data packet delivery.

The data flow operates as follows: the ESP32 module captures a frame and sends it to Unity, which then hands the frame off to an external Python script. The script processes the computer vision pipeline and returns the computed shot vector back into the game.

## Engine & Low-Spec Optimization (Unity 3D)
The beating heart of the application is the Unity engine built on the Universal Render Pipeline (URP). Because the system needed to run smoothly on standard, often aging school computers, we implemented a graphics preset pipeline leveraging AMD FidelityFX™ Super Resolution (FSR). Upscaling from a lower internal resolution allows the simulation to sustain high framerates and snappy responsiveness even on integrated graphics.

## Machine Vision Instead of Lasers
Rather than relying on laser pointers, the system is driven by computer vision tracking markers projected onto the screen. This optical approach eliminates the need to anchor users to a static shooting bench, granting trainees complete freedom of movement.

## Hardware Flexibility
We aimed to make the system exceptionally versatile. The ESP32 microcontroller is strictly responsible for image acquisition and telemetry communication. Tactile factors like weight distribution and recoil dynamics are dictated entirely by the underlying replica on which the module is mounted.

This functional decoupling pays off in practice: in hospital schools, light, quiet, recoil-free replicas are favored, whereas other institutions can readily attach the module to heavier CO2 blowback replicas that deliver realistic tactile feedback.

---

## The Reality Check

The system underwent rigorous field testing in target environments, including the ZSE2 technical high school in Poznań and public STEM events hosted by Adam Mickiewicz University. Hands-on student interactions yielded two crucial lessons:

* **Material Durability Stress Test:** The initial, lightweight 3D-printed enclosures simply did not survive the overwhelming enthusiasm and physical force of energized students. We swiftly redesigned the mounting brackets with reinforced walls and tougher filament. Sticking with 3D printing meant that field repairs and maintenance remained dirt cheap and hassle-free.
* **Power Management:** We initially planned on integrated LiPo rechargeable battery packs. In practice, however, teachers rarely found the time or routine to keep them systematically charged. The winning solution was reverting to standard 9V batteries (or rechargeable 9V cells). A teacher being able to swap in a fresh battery two minutes before the class bell proved to be vastly more sensible for school life.

---

## Core Project Team
* **Miłosz Klim** – Team Leader, Systems Integration (Unity & ESP)
* **Nikodem Panknin** – Computer Vision Developer
* **Daria Mróz** – UI & 2D Designer
* **Kamil Sell** – 3D Environment Artist
* **Krystian Olesiejko** – 3D Enclosure & Housing Designer

---

## Sources & Links
* [Minerwa Project on Itch.io](https://propaganda-studios.itch.io/minerwa)

## Gallery
{{< gallery >}}
  <img alt="Simulation screenshot" src="/img-compressed/Minerwa/ahbLyZ.webp" class="grid-w50 md:grid-w33" />
  <img alt="Pistol replica" src="/img-compressed/Minerwa/IAdSJN.webp" class="grid-w50 md:grid-w33" />
  <img alt="Testing the application" src="/img-compressed/Minerwa/IeXtBb.webp" class="grid-w50 md:grid-w33" />
  <img alt="Classroom training session" src="/img-compressed/Minerwa/jsSrbE.webp" class="grid-w50 md:grid-w33" />
  <img alt="Target practice drill" src="/img-compressed/Minerwa/lmX41G.webp" class="grid-w50 md:grid-w33" />
  <img alt="Student training session" src="/img-compressed/Minerwa/to1Faq.webp" class="grid-w50 md:grid-w33" />
  <img alt="System demonstration" src="/img-compressed/Minerwa/WaPOWz.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

