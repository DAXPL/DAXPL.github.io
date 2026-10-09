---
title: "SNS Minerwa - Virtual Shooting Range"
date: 2022-09-15
summary: "An innovative virtual shooting training system based on computer vision, ESP32 rifle replica modifications, and Unity 3D."
tags: ["Unity", "C#", "Computer Vision", "Hardware", "ESP32", "IoT", "Education"]
categories: ["Projects", "Gamedev & XR"]
---

**SNS Minerwa** is an innovative virtual sports shooting system designed specifically for middle and high schools (as a tool supporting defense and safety education classes). The system redefines shooting training by eliminating the need for expensive infrastructure — all it requires is a computer, a projector, and a modified rifle replica.

<iframe src="https://itch.io/embed/1708380" loading="lazy" width="100%" height="167" frameborder="0"></iframe>

## My Role in the Project

As the **Project Leader**, I managed an interdisciplinary team (programmers, 2D/3D artists, housing designers), ensuring the delivery of a complete, rock-solid product.

On the technical side, I acted as the **Lead Unity Developer & Weapon System Integrator (Unity & ESP Developer)**:
* Designed the software architecture in Unity 3D.
* Developed and implemented core mechanics and business logic in C#.
* Modified and integrated rifle replicas using ESP microcontrollers for instant, reliable hardware-to-app communication.
* Bridged the machine vision tracking module with the main game engine.

---

## Architecture & Technologies

### 1. Engine & Optimization (Unity 3D & URP)
The core of the application is built on **Unity** using the Universal Render Pipeline (URP). The primary challenge was achieving smooth frame rates and high-fidelity graphics on standard, often outdated school hardware.

To overcome hardware bottlenecks, I implemented a graphics preset system utilizing **AMD FidelityFX™ Super Resolution (FSR)**. By rendering at lower internal resolutions and smartly upscaling, the application comfortably runs at 4K resolution even on integrated graphics such as Intel UHD 620.

### 2. Innovative Tracking System (Computer Vision)
Unlike competing solutions, Minerwa discards laser pointers and IR beacons, which can pose safety concerns in school environments. Instead, it relies on **marker-based machine vision**. A miniature camera mounted on the barrel transmits video to an algorithm tracking specific screen markers, accurately determining the shot vector. This completely eliminates the need for a fixed shooting station and allows full freedom of movement.

---

## Features & User Experience (UX)

With educators in mind, the interface was designed with a heavy focus on simplicity:
* **Rapid Setup:** Configuring a complete shooting session takes only a few seconds.
* **Official PZSS Presets:** Built-in training scenarios follow official Polish Sport Shooting Association guidelines.
* **Real-Time Analytics:** Instructors have live access to shooting statistics and target groupings, facilitating fair student evaluation.

---

## Deployments & Public Showcase

The system was verified in field conditions from day one. It was initiated at **ZSE2 Technical High School in Poznań**, which actively field-tested it for classroom deployment.

We successfully demonstrated the system at various public events:
* **Freshman Day at the Faculty of Physics, AMU**
* **Night of GITES (ZSE2)**
* **AMU Sports Day**

---

## Core Team
* **Miłosz Klim** – Team Leader, Unity & ESP Developer
* **Nikodem Panknin** – Computer Vision Developer
* **Daria Mróz** – UI/UX & 2D Designer
* **Kamil Sell** – Environment & 3D Artist
* **Krystian Olesiejko** – Housing Designer

---

## Links & Sources
* [Minerwa Project on Itch.io](https://propaganda-studios.itch.io/minerwa)
* [Propaganda Studios on Itch.io](https://propaganda-studios.itch.io)