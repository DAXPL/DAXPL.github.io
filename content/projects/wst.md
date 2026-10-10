---
title: "WST / XR BINIU - Autonomous Drones & Sim2Real AI"
date: 2025-06-01
summary: "An open-source framework connecting Unity 6, reinforcement learning (ML-Agents), and ESP32 controllers over LTE/VPN for autonomous unmanned vehicles."
tags: ["Unity 6", "AI", "ML-Agents", "Reinforcement Learning", "ESP32", "C++", "C#", "Python", "Sim2Real", "Drones", "IoT", "3D Printing", "Open-Source"]
categories: ["Projects", "AI & Robotics"]
aliases:
  - /autonomiczneDrony.html
  - /projects/wst-drony/
---

> *"Our greatest success was teaching sand how to think."*

**WST (Weird Steering Things)** is an advanced, open-source framework for building and piloting unmanned vehicles, representing a radical evolution of the academic project **XR BINIU** (*miXed Reality Blended Intelligence for Navigable Interactive UV's*). 

The project was born as an alternative to expensive, proprietary "black boxes". It proves that by combining affordable microcontrollers, the computational horsepower of modern workstations, and high-fidelity physics simulations, we can successfully train artificial intelligence to pilot physical machines in reality via **Sim2Real** methodology.

---

## About the Project & The Sim2Real Principle

Training drones in a virtual environment prior to real-world deployment is a paradigm rapidly gaining momentum thanks to modern simulation engines and breakthroughs in machine learning. For both industry and research, virtual prototyping drastically lowers costs: simulations allow risk-free testing of control policies without endangering expensive hardware, renting testing lakes, or posing hazards to surrounding environments.

The project leverages the **Unity ML-Agents Toolkit** – a framework enabling the training of intelligent agents inside 3D environments using **Reinforcement Learning (RL)**.

---

## My Role and Responsibilities

As **Project Leader**, I coordinated our interdisciplinary team and defined the project's strategic roadmap.

On the engineering front, acting as **System Architect and Unity & C++/ESP32 Developer**, I was responsible for:
* **Sim2Real Architecture (Breadboard Interface):** Designing a modular "virtual brain" architecture that cleanly decouples high-level AI decision logic from low-level physical hardware actuators.
* **Reinforcement Learning (RL):** Implementing and supervising the AI agent training pipeline in virtual simulation using Unity ML-Agents.
* **Embedded Firmware:** Developing highly optimized C/C++ firmware for ESP32 microcontrollers serving as propulsion and steering controllers.

---

## System Architecture & Technologies

The core architectural pillar of the project is **decentralization**: separating the "Brain" (onboard compute hosting the AI agent) from the "Muscles" (hardware controllers managing PWM signals and sensors).

### 1. Simulation Environment (Flight Computer)
Built on **Unity 6 (HDRP)**. We utilize advanced physical simulation for aquatic and atmospheric dynamics (wind resistance, drag, water density, wave kinematics). Using Reinforcement Learning, the control algorithms independently learn optimal navigation policies through trial and error in the virtual world.

### 2. Hardware & Global Telemetry (Flight Controller)
Low-level logic runs on **ESP32** microcontrollers (supported by Arduino).
In the original prototype, communication relied on local Wi-Fi and WebSockets. While sufficient for early campus pond trials, it was confined to single network coverage.

We engineered a scalable architecture utilizing a **GSM/LTE** modem and a dedicated **VPN** gateway configured on a Raspberry Pi:
* The drone is liberated from local Wi-Fi limits, connecting directly to the global cellular network.
* This allows piloting the vehicle from anywhere on Earth – the AI agent can execute on a cloud server in a remote data center while exchanging low-latency telemetry in real time with the lightweight vessel on the water.

### 3. Rapid Prototyping & 3D Printing (FDM)
All physical airframe and hull structures were manufactured using FDM 3D printing. This technology enabled rapid prototyping and iteration of motor mounts, turrets, superstructures, and air-propulsion brackets.

Special thanks go to the **Wielkopolskie Center for Advanced Technologies (WCZT)** for granting our team access to an industrial *Dragon 3D* printer along with engineering filament supplies. This made it possible to print the full-scale, integrated vessel hull as a single monolithic element, which was vital for structural integrity and a successful maiden voyage.

---

## Project Gallery

{{< gallery >}}
  <img alt="Launching the autonomous water drone" src="/img-compressed/Errno/Drony/20250602_143615.webp" class="grid-w50 md:grid-w33" />
  <img alt="Structural tests of the watercraft" src="/img-compressed/Errno/Drony/20250602_143633.webp" class="grid-w50 md:grid-w33" />
  <img alt="Lab assembly of vehicle electronics" src="/img-compressed/Errno/Drony/20250609_143529.webp" class="grid-w50 md:grid-w33" />
  <img alt="Integrated autonomous unit" src="/img-compressed/Errno/Drony/IMG-20250609-WA0000.webp" class="grid-w50 md:grid-w33" />
  <img alt="Hull and air-drive details" src="/img-compressed/Errno/Drony/20250602_144957.webp" class="grid-w50 md:grid-w33" />
  <img alt="Breadboard electronics prototyping phase" src="/img-compressed/Errno/Drony/20250511_222628.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

---

## Status and Future: The Bicopter Project

The successful deployment of our first autonomous water drone proved the validity of our Sim2Real architecture.

The team's next, considerably more demanding goal is to utilize this identical pipeline to **train AI to pilot a bicopter** – a dual-rotor configuration with servo-tilted thrust vectors that is naturally and intensely aerodynamically unstable. The policy is being trained inside Unity's physics engine before moving to physical flight tests.

---

## The WST Team ("The Weird Team")

The project is developed with passion at the Faculty of Physics and Astronomy, Adam Mickiewicz University, in collaboration with Dr. Wojciech Czart (Student Science Club Errno):

* **Miłosz Klim, M.Sc. Eng.** – Project Leader, System Architect, Unity/C++ Developer
* **Adam Mischke, Eng.** – Electronics Specialist, Circuit Architect
* **Cosinus** – Unity 3D Programmer & Code Quality Guardian
* **Emil Kopytek** – Bicopter Architect & 3D Printing Specialist
* **Krystian Olesiejko, Eng.** – Naval Architect & 3D Printing Specialist
* **Mateusz Nawrot** – Network Specialist & C++ Programmer, VPN Infrastructure
* **Wiktoria Bielecka** – UI/UX Designer, Visual Layer

---

## Sources & Links
* [WST Repository on GitHub](https://github.com/DAXPL/WST)
* [Official Project Report (Google Docs)](https://docs.google.com/document/d/1-k4Ll4qevaH445sVjVkQF32h3w11uCgUwEZ2eICMMHg/edit?usp=sharing)

