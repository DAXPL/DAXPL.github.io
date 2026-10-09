---
title: "Biofeedback & Multisensory Immersion in VR (Master's Thesis)"
date: 2026-06-15
summary: "An R&D environment investigating physiological correlations between human biometrics and subjective VR/PC flow states, featuring ESP32 telemetry, a custom Olfactory Display, and Python data science."
tags: ["Unity 3D", "C#", "Python", "ESP32", "IoT", "Biofeedback", "VR", "Biometric Sensors", "R&D", "Data Science", "Pandas", "GenAI"]
categories: ["Projects", "Gamedev & XR", "R&D Research"]
---

# Investigating the relationship between physiological body metrics and subjective immersion across digital reality environments

This project represents a comprehensive, interdisciplinary scientific research testbed developed for my Master's thesis in **Internet of Things Applications** at the Faculty of Physics and Astronomy, Adam Mickiewicz University, supervised by Prof. Sławomir Mamica.

The primary research objective was to mathematically correlate objective physiological responses with subjective perceptions of immersion and ***flow*** (deep cognitive engagement) across Virtual Reality (VR) and traditional PC desktop configurations.

---

## 1. Hardware Architecture & Custom IoT Ecosystem

I engineered a specialized hardware ecosystem built around **ESP32** microcontrollers, interfacing the participant's biological state in a closed feedback loop with the Unity 3D engine:

* **Biometric Telemetry System:** Real-time data acquisition recording participant physiological metrics, including electrodermal activity (**EDA/GSR**), heart rate (**HR**), blood oxygen saturation (**SPO2**), and skin surface temperature.
* **Custom Olfactory Display Module:** Designed and assembled an embedded physical olfactory emission device delivering synchronized scent bursts directly triggered by virtual environmental cues, substantially elevating presence within virtual spaces.

---

## 2. Software Architecture & "Virtual Director" Engine

The experimental application was implemented in **Unity 3D (C#)**, targeting both standalone VR head-mounted displays (Meta Quest) and conventional desktop setups.

The engine orchestrated audiovisual and sensory stimulation based on deterministic experimental protocols while injecting millisecond-accurate event markers directly into physiological telemetry streams.

---

## 3. R&D Pipeline & Data Science

The research bridged modern software engineering practices with rigorous scientific methodology:

* **Statistical Modeling & Analysis:** Telemetry datasets collected across participant trials were preprocessed and analyzed using **Python** and **Pandas**, mathematically validating correlations between sensory stimuli and physiological arousal markers.
* **Modern Generative 3D Asset Pipeline:** To rapidly generate diverse, bespoke test environments in Unity, I built an asset workflow utilizing the **Hunyuan3D-2** generative image-to-3D model managed through Stability Matrix, with automated retopology and UV baking scripts in **Blender**.

---

## Key Achievements & Insights

* **Physiological Dominance of VR:** Biometric data conclusively showed that VR environments evoke significantly stronger physiological reactions compared to PC monitors, facilitating faster transition into and extended maintenance of psychological *flow*.
* **Embedded R&D Engineering:** Successful end-to-end realization of a wireless multi-sensor IoT device communicating bidirectionally with a 3D simulation engine.
* **Interdisciplinary Synthesis:** Seamlessly bridging immersive XR gaming technologies, medical biomedical signal analysis, and embedded IoT systems.

