---
title: "The Evolution of Immersion: From 'Rouge Squadron' Simulator to Multisensory VR Biofeedback"
date: 2026-10-01
summary: "A multi-year research project (Bachelor's and Master's theses) bridging Unity 3D VR simulators, custom ESP32 IoT hardware (including an olfactory display), and medical biometric analysis using Python and Pandas."
tags: ["Unity 3D", "C#", "VR", "Biometrics", "Netcode for GameObjects", "ESP32", "IoT", "Data Science", "Python", "Pandas", "GenAI", "Shader Graph", "URP"]
categories: ["Projects", "Gamedev & XR", "R&D Research"]
aliases:
  - /projects/rouge-squadron/
  - /projects/green-hour/
---

This project represents an interdisciplinary, two-stage research journey aiming to mathematically and physiologically quantify the phenomenon of immersion in virtual reality. The research was carried out as part of my Bachelor's engineering thesis (Computer Technologies) and Master's thesis (Internet of Things Applications, supervised by Prof. Dr. Hab. Sławomir Mamica) at the Faculty of Physics and Astronomy, Adam Mickiewicz University in Poznań.

---

## 1. The Origins: "Rouge Squadron" and Medical Stress Measurements

The initial phase set out to prove the heightened immersion of VR compared to conventional flat-screen PC gaming. Using *SUPERHOT* across both PC and VR versions alongside certified medical-grade telemetry — the **Empatica E4** wristband — we recorded physiological reactions. Photoplethysmography (heart rate), accelerometry, and skin temperature data revealed, among other patterns, a paradoxical drop in skin temperature (a natural vasoconstriction reflex triggered by perceived danger). Most notably, we observed a **marked surge in electrodermal activity (EDA/GSR)** in VR, directly correlating with cognitive stress and sympathetic nervous system activation.

These empirical findings laid the foundation for the first testbed environment — **Rouge Squadron**. A complex cooperative multiplayer simulator where crewmates repair a malfunctioning starship under high-stress conditions. Rather than relying on superficial gimmicks, the experience prioritized deep physical tactile interaction (climbing, mechanical levers, pressure valves) engaging whole-body motor coordination. The project was published on Itch.io in collaboration with 3D artist Wiktoria Bielecka.

### Network Architecture and 120 FPS Optimization
To eliminate motion sickness in multi-user VR spaces, I implemented:
* **Netcode for GameObjects (LAN):** Moved away from the dogmatic *"never trust the client"* architecture. When a player physically manipulates an object, client authority over its physics solver takes over locally, entirely eliminating rubber-banding artifacts. Backed by `NetworkTransform` (stable 60 Hz tickrate), `NetworkVariable` with `OnValueChanged()` callbacks, and an optimized RPC topology.
* **URP Graphics Pipeline:** Strict *High-Poly to Low-Poly* baking workflows (Normal Maps), static batching, and aggressive frustum culling secured a rock-solid 120 FPS on VR headsets. Employed *Single-Pass Instanced Rendering* to cut draw calls in half, baked global illumination augmented with Light Probes, and custom Shader Graph shaders simulating Gerstner ocean waves on planet Lirwen. The build was compiled against the high-performance IL2CPP backend.

---

## 2. Evolution: Multisensory Biofeedback and the "Virtual Director"

Advancing into Master's research, the scope expanded considerably: creating a comprehensive research sandbox across both VR (Meta Quest) and PC platforms to rigorously evaluate correlations between objective somatic responses and the subjective transition into a flow state.

I engineered a custom **IoT hardware ecosystem based on ESP32 microcontrollers** from the ground up:
* **Biometric Telemetry Logger:** Built a dedicated wearable unit logging real-time tester metrics: Electrodermal Activity (EDA/GSR), Heart Rate (HR), blood oxygen saturation (SPO2), and skin surface temperature.
* **Olfactory Display (Scent Delivery Module):** A bespoke physical apparatus communicating wirelessly with Unity 3D to deliver micro-bursts of specific aromatic compounds. Synchronizing olfactory feedback with scene transitions profoundly intensified spatial presence.

Dynamic modulation of audiovisual and environmental stimuli was orchestrated in real time by a C# **"Virtual Director"** state machine, which accurately timestamped synchronized experimental markers.

### Data Science Pipeline and Generative AI
To uphold academic scientific rigor, telemetry datasets collected during laboratory trials were cleaned and evaluated through an end-to-end **Python** statistical pipeline leveraging **Pandas**.

To accelerate the production of 3D research environment assets, I incorporated a GenAI workflow powered by the **Hunyuan3D-2 (image-to-3D)** generative model hosted locally via Stability Matrix, polished with automated retopology and UV unwrapping inside **Blender**.

---

## Summary
In-depth analysis of the sanitized biometric datasets conclusively demonstrated VR's physiological superiority. Virtual reality triggers objectively more pronounced somatic responses than flat displays, fostering faster entry into the *flow* state and sustaining it significantly longer. This multi-year initiative demonstrates how software engineering (Gamedev, XR), embedded hardware (IoT), and medical telemetry analysis (Data Science) converge to create genuinely intelligent, user-aware interactive systems.
