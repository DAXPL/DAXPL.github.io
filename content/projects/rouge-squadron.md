---
title: "VR Simulator \"Rouge Squadron\" & Biometric Research"
date: 2024-11-20
summary: "An advanced cooperative VR spaceship simulator (LAN Multiplayer / Netcode) paired with clinical biometric research measuring player stress (EDA) and presence in VR."
tags: ["Unity 3D", "C#", "Netcode for GameObjects", "VR", "Simulator", "Multiplayer", "Biometrics", "URP", "Shader Graph", "R&D"]
categories: ["Projects", "Gamedev & XR"]
---

**Rouge Squadron** is an advanced cooperative virtual reality simulator that served as the capstone project for my Bachelor of Engineering degree in Computer Technologies (Faculty of Physics and Astronomy, AMU).

The project not only provides a fully realized multiplayer gaming environment where players manage and repair a spaceship crew cabin, but also doubles as an empirical research platform analyzing physiological responses to VR immersion.

Gameplay demands active voice communication, resource allocation, and high-pressure decision-making during ship emergencies and foreign planetary explorations.

---

## 1. Immersion Research & Biometrics in VR

A core element of the engineering thesis was clinical experimentation demonstrating the significant leap in immersion provided by VR relative to traditional desktop displays.

* **Methodology:** We utilized *SUPERHOT* (PC and VR editions) paired with clinical-grade medical instrumentation — the **Empatica E4 biometric wristband**.
* **Metrics Captured:** Photoplethysmography heart rate (HR), skin temperature, 3-axis motion acceleration, and electrodermal activity (**EDA / GSR**), which directly reflects sympathetic nervous system activation and psychological stress.
* **Findings:** Experiments demonstrated an extreme — **up to 9-fold** — surge in EDA amplitude during VR gameplay compared to PC. Players exhibited elevated heart rates and a physiological drop in skin temperature (vasoconstriction under perceived threat).

These clinical insights directly informed the design of *Rouge Squadron*: instead of surface-level jumpscares, gameplay leans heavily into fine physical tactile interactions (switches, levers, physical climbing, tool manipulation) engaging the user's motor cortex.

---

## 2. Multiplayer Architecture (Netcode for GameObjects)

Designing a cooperative VR multiplayer title imposes tight latency budgets to avoid vestibular desynchronization and motion sickness:

* **LAN Client-Server Topology:** Built over local networks, deliberately adapting the traditional *"never trust the client"* paradigm for VR interactions.
* **Distributed Object Ownership:** When a player physically grabs a tool or console control, network ownership transfers directly to that client. This eliminates interpolation rubber-banding and provides instantaneous physical tactile feedback.
* **Data Synchronization:** Utilized `NetworkTransform` components operating at a stable 60 Hz tickrate, `NetworkVariable` structures with `OnValueChanged()` callbacks, and remote procedure calls (`ServerRpc`, `ClientRpc`) for machine states and fire propagation.

---

## 3. Graphics Pipeline & VR Optimization (URP)

To maintain a rock-solid **120 FPS** target on VR head-mounted displays, I applied comprehensive graphics pipeline optimizations:

* **Single-Pass Rendering:** Drawing geometry for both eyes simultaneously inside a single render pass dramatically cut draw calls and batch overhead, elevating frame rates from 60 to 120 FPS.
* **Geometry Workflow:** High-Poly to Low-Poly baking transfers intricate details onto Normal Maps within PBR materials. Static batching and aggressive occlusion culling ensure only immediate bulkheads are submitted to the GPU.
* **Custom Vertex Shaders:** Using Shader Graph, I engineered real-time Gerstner wave calculations directly manipulating vertex displacement for the alien ocean world of planet Lirwen.
* **Baked Lighting:** Fully baked global illumination (GI) with ambient occlusion (AO) and Light Probe grids for dynamic actors achieved rich visual fidelity with virtually zero dynamic lighting compute penalty.

---

## Team & Deployment

Developed in creative collaboration with 3D/2D artist **Wiktoria Bielecka**. The game was compiled targeting the high-performance **IL2CPP** backend and released publicly on Itch.io.

---

## Sources & Links
* [Play Rouge Squadron on Itch.io](https://daxpl.itch.io/rouge-squadron)

