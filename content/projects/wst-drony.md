---
title: "WST / XR BINIU - Autonomous AI Drones & Sim2Real"
date: 2025-06-01
summary: "An open-source framework connecting Unity 6 physics simulations, reinforcement learning (ML-Agents), and ESP32 controllers over LTE/VPN for autonomous unmanned vehicles."
tags: ["Unity 6", "AI", "ML-Agents", "Reinforcement Learning", "ESP32", "C++", "C#", "Python", "Sim2Real", "Drones", "IoT", "3D Printing", "Open-Source"]
categories: ["Projects", "AI & Robotics"]
aliases: ["/autonomiczneDrony.html"]
---

> *"Our greatest success was teaching sand to think."*

**WST (Weird Steering Things)** is an advanced open-source framework for building and piloting unmanned vehicles, representing a major evolution of the academic project **XR BINIU** (*miXed Reality Blended Intelligence for Navigable Interactive UV's*).

Born as an alternative to expensive, proprietary "black boxes", the project proves that by leveraging affordable microcontrollers, modern computational horsepower, and accurate physics simulations, we can train AI agents in virtual worlds to pilot physical machines in reality through **Sim2Real** techniques.

---

## About the Project & The Sim2Real Principle

Training drones in virtual worlds prior to real-world deployment is a paradigm rapidly gaining traction thanks to advanced simulation engines and breakthroughs in machine learning. For both industry and research, virtual prototyping drastically lowers costs: control algorithms can be rigorously evaluated without risks of hardware destruction, expensive field testing rentals, or environmental hazards.

The project utilizes the **Unity ML-Agents Toolkit**, training autonomous agents directly in 3D environments using **Reinforcement Learning (RL)**.

---

## My Role & Contribution

As the **Project Leader**, I coordinated the interdisciplinary development team and set the technical roadmap.

On the engineering side, acting as **System Architect and Unity & C++/ESP32 Developer**, my responsibilities included:
* **Sim2Real Architecture (Breadboard Interface):** Designing a modular "virtual brain" separating high-level AI policy decision logic from low-level motor and actuator hardware control.
* **Reinforcement Learning (RL):** Implementing and overseeing agent training pipelines within Unity ML-Agents.
* **Embedded Firmware:** Writing optimized C/C++ firmware for ESP32 microcontrollers serving as vehicle propulsion and flight controllers.

---

## System Architecture & Technologies

The foundational architectural principle is **decentralization**: cleanly separating the "Brain" (onboard compute handling AI inference) from the "Muscles" (hardware controllers managing PWM signals and sensors).

### 1. Simulation Environment (Flight Computer)
Built on **Unity 6 (HDRP)**, using advanced physics to model hydrodynamics and aerodynamics (waves, drag, water density, wind forces). Reinforcement Learning agents learn optimal navigation policies through trial and error in simulation.

### 2. Hardware & Global Telemetry (Flight Controller)
Low-level control runs on **ESP32** microcontrollers (supported by Arduino). 
While initial campus prototypes utilized local Wi-Fi and WebSockets, range and connection instability posed severe operational constraints.

We re-architected the communications pipeline using **GSM/LTE** modems combined with a dedicated **VPN** gateway running on Raspberry Pi:
* The watercraft is untethered from local Wi-Fi, tapping directly into global cellular networks.
* The vehicle can be monitored and controlled from anywhere worldwide — the AI agent can execute on a cloud server in another country while exchanging real-time telemetry with a lightweight vessel on the water.

### 3. Rapid Prototyping & FDM 3D Printing
All structural airframe and hull components are fabricated using FDM 3D printing, enabling rapid iterations for engine mounts, turrets, superstructures, and air-propulsion brackets.

Special thanks go to the **Wielkopolskie Center for Advanced Technologies (WCZT)** for granting our team access to an industrial *Dragon 3D* printer along with engineering filament supplies. This enabled printing the full-scale hull in a single monolithic piece, ensuring structural buoyancy and integrity.

---

## Project Gallery

{{< gallery >}}
  <img alt="Launching the autonomous boat" src="/img-compressed/Errno/Drony/20250602_143615.webp" class="grid-w50 md:grid-w33" />
  <img alt="Structural hull and watercraft testing" src="/img-compressed/Errno/Drony/20250602_143633.webp" class="grid-w50 md:grid-w33" />
  <img alt="Electronics assembly in the lab" src="/img-compressed/Errno/Drony/20250609_143529.webp" class="grid-w50 md:grid-w33" />
  <img alt="Integrated autonomous vehicle" src="/img-compressed/Errno/Drony/IMG-20250609-WA0000.webp" class="grid-w50 md:grid-w33" />
  <img alt="Air-propulsion and mechanical details" src="/img-compressed/Errno/Drony/20250602_144957.webp" class="grid-w50 md:grid-w33" />
  <img alt="Early breadboard electronics prototyping" src="/img-compressed/Errno/Drony/20250511_222628.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

---

## Current Status & Next Steps: Bicopter Challenge

The maiden voyage and deployment of our autonomous water drone proved the validity of our Sim2Real architecture.

Our current challenge raises the bar significantly: **teaching AI to pilot an aerodynamic bicopter** — a dual-rotor configuration with tilt servomechanisms that is inherently aerodynamically unstable. The policy is trained inside Unity's physics environment before being flashed to physical flight controllers.

---

## The WST Team ("The Weird Team")

Developed at the Faculty of Physics and Astronomy, Adam Mickiewicz University, in collaboration with Dr. Wojciech Czart (Student Science Club Errno):

* **Miłosz Klim, M.Sc. Eng.** – Project Leader, System Architect, Unity/C++ Developer
* **Adam Mischke, Eng.** – Electronics Specialist, Circuit Architect
* **Cosinus** – Unity 3D Programmer & Code Quality Guardian
* **Emil Kopytek** – Bicopter Architect & 3D Printing Specialist
* **Krystian Olesiejko, Eng.** – Naval Architect & 3D Printing Specialist
* **Mateusz Nawrot** – Network Specialist & C++ Programmer, VPN Infrastructure
* **Wiktoria Bielecka** – UI/UX Designer, Visual Assets

---

## Sources & Links
* [WST Repository on GitHub](https://github.com/DAXPL/WST)
* [Full Technical Report (Google Docs)](https://docs.google.com/document/d/1-k4Ll4qevaH445sVjVkQF32h3w11uCgUwEZ2eICMMHg/edit?usp=sharing)
