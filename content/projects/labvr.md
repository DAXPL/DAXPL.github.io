---
title: "LAB-VR - Educational Virtual Reality Platform"
date: 2023-09-01
summary: "An open-source educational VR platform (physics, astronomy, geology, computer hardware) funded by the Kowadło 2.0 grant, optimized for Meta Quest 2 and deployed in schools nationwide."
tags: ["VR", "Unity", "Open-Source", "Education"]
categories: ["Projects", "Gamedev & XR", "Education"]
---

Squeezing an entire virtual classroom into around 70 batches (draw calls) sounds borderline reckless. Yet that was the strict performance ceiling we imposed upon ourselves right from the start. We wanted absolute certainty that our application would run without a hitch on Meta Quest 2 and 3 headsets, which is why we adopted the uncompromising optimization guidelines from the first-generation Quest as our baseline. When dynamic physics comes into play — like interactively slicing through 3D models of soda cans or computer monitors — that draw call budget melts away before your eyes.

This demanded hours of scene debugging in Unity, combining geometric meshes, and drastically optimizing materials. Even the level architecture had to be deliberately planned — ensuring the engine never had to render too many objects simultaneously, while never making the player feel trapped in a claustrophobic box.

This was the behind-the-scenes reality of creating **LAB-VR** – an innovative, interactive classroom simulation crafted for primary and secondary schools. We transport traditional curriculum lessons into virtual reality, transforming abstract theory into tangible hands-on experience. The project was funded through the prestigious **Kowadło 2.0** initiative and released completely free of charge (open-source) as a universal teaching toolkit for schools.

---

## My Role in the Project: From Optimization to Mentoring

As **Project Leader and Lead Unity Developer**, I oversaw the complete software lifecycle:

* **VR System Architecture:** Designing and implementing core physical interaction mechanics within virtual reality using Unity 3D.
* **Standalone VR Optimization:** The relentless fight for draw calls mentioned earlier. These efforts secured a rock-solid 72 FPS on mobile Snapdragon XR2 chipsets, without needing any cable tethering to a PC.
* **Team Leadership & Mentoring:** Directing the development work of the Errno Student Science Club and coordinating technical internships for vocational IT students.

That final point came with quite the reality check. For young programming apprentices, the greatest hurdle was rarely code architecture itself — it was acclimating to commercial gamedev standards and internalizing the concept of **DoD (Definition of Done)**. School trains students to believe a task is finished the moment they write the code. In a development team, you have to defend your implementation, document it, and physically drag the card across the Trello board. There were times when a student built a brilliant mechanic but couldn't explain how it actually functioned under the hood (and keep in mind, this was before the AI revolution, so we couldn't blame it on "vibe coding"). It was a tough but indispensable lesson in taking true ownership of the software you deliver.

---

## Educational Areas

The simulation is divided into dedicated classrooms, each hosting interactive experiments that are difficult or dangerous to conduct in standard school conditions:

* **Physics:** A safe lab for conducting mechanics, optics, and magnetic experiments with real-time physical phenomena visualization.
* **Astronomy:** A scalable cosmic voyage enabling direct interaction with 3D celestial bodies and observing orbital mechanics from both first- and third-person perspectives.
* **Geology:** Virtual field expeditions dissecting Earth's geological cross-sections, inspecting mineral specimens, and studying tectonic processes.
* **Computer Hardware Engineering (UTK):** An engineering sandbox where computer components come to life. Students can disassemble hardware into components and explore hardware architecture from the inside out. Contrary to expectations, implementing precise grabbing and manipulation of small electronic components in this room went remarkably smoothly.

---

## The Reality Check: Nationwide Workshops in Poland

All the sweat poured into draw calls and physics mechanics served a single goal: combating technological exclusion. The true acid test for the application came during our nationwide travels and youth workshops. The moment students put on the headsets and we saw their pure joy exploring the virtual classrooms, it proved that immersive education simply works.

Below are detailed field reports and devlogs from our deployments:

* **Sep 8, 2023:** ZSE2 Technical High School in Poznań – initial field validation and technical student workshops. [Read report from Poznań](https://propaganda-studios.itch.io/lab-vr/devlog/667924/warsztaty-vr-w-zse2-w-poznaniu)
* **Dec 8, 2023:** Tischner Technical High School in Rabka-Zdrój – pilot rollout and developer presentations. [Read report from Rabka-Zdrój](https://propaganda-studios.itch.io/lab-vr/devlog/650457/warsztaty-vr-w-rabce-zdroju)
* **Feb 22, 2024:** Complex of Schools No. 1 in Stargard – classroom deployment and student mentoring. [Read report from Stargard](https://propaganda-studios.itch.io/lab-vr/devlog/686407/warsztaty-vr-w-zespole-szk-w-stargardzie)
* **Apr 12, 2024:** Primary School in Gołańcz – STEM popularization workshops for younger students. [Read report from Gołańcz](https://propaganda-studios.itch.io/lab-vr/devlog/715663/warsztaty-vr-w-goaczy)

---

## Sources & Links
* [LAB-VR on Itch.io](https://propaganda-studios.itch.io/lab-vr)
* [Source Code on GitHub](https://github.com/Studenckie-Kolo-Naukowe-ERRNO/LabVR)

