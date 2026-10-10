---
title: "Heritage Digitization: FOSS, Drones, and 3D Printing in Archaeology"
date: 2026-10-10
summary: "A cross-sectional heritage digitization project – from reconstructing the skulls of early medieval settlers to full-island drone photogrammetry in Biskupin using open-source tools and remote compute clusters."
tags: ["3D Printing", "FDM", "Photogrammetry", "FOSS", "Biskupin", "Museums", "OpenDroneMap"]
categories: ["Projects", "Hardware & Prototyping"]
aliases:
  - /czaszki.html
  - /projects/czaszki-3d/
---

Over two hours. That was how long the cooling fan screamed inside a fairly decent laptop at our field station in Biskupin, struggling to process a mere fraction of the drone photogrammetric imagery, while our exhausted team only dreamed of getting some sleep after a full day at our exhibition stand.
That was the exact moment I completely abandoned local field processing. Instead, I installed WebODM on my home workstation, linked everything through a secure VPN tunnel, and started offloading heavy compute jobs to a rig dozens of kilometers away.

In museology and archaeology, there is growing talk of AI-integrated solutions, which all too often lock data into expensive, proprietary cloud ecosystems. In my projects, I actively advocate for an alternative: an approach rooted in hardware and software sovereignty. Let’s take a look at how the evolution of these open-source tools played out in practice.

---

## Technological Evolution: From Wooden Frames to Remote Clusters

The process of digitally preserving history also serves as a vivid timeline of how drastically the barrier to entry for rapid prototyping has dropped over the years.

### 2018: Where It All Began (Skulls and GITES)

As part of an R&D scientific initiative with the Archaeological Museum in Poznań (in collaboration with the GITES student research club), we worked on reconstructing the facial appearance of the early medieval inhabitants of the settlement in Poznań's Śródka district. Instead of prohibitively expensive powder-based ColorJet Printing (CJP), we pioneered a production workflow based on FDM 3D printing.

**This decision drastically cut production costs** while preserving the dimensional accuracy required by forensic anthropologists. Powder printing certainly delivers finer surface detail, but with innovative projects it is dangerously easy to fall into the trap of overengineering, especially when standard, proven paths don't yet exist. That makes it all the more crucial to maintain a clearly defined objective and know when to say "good enough".

Back in 2018, work started on weathered, experimental machines that demanded patience and humility at every step. Those were times when 3D printers still commonly used wooden frame parts, and iconic kits like the Ender 3 or Anet A8 were only beginning to hit the market. We printed the skulls on an Accura printer. Before any print could even begin, we had to remember to **manually level the heated bed using a sheet of paper**. Then, due to the lack of a heated print surface, the print bed had to be **meticulously covered with blue painter's tape and glue stick**.

The printing process itself, even with relatively thick layers (around 0.24 mm), took ages. Half of a skull took around two full days to print. Today, a complete and vastly more detailed model can be fabricated in under 17 hours.

We presented the finished anatomical models during an official scientific symposium held in the City of Poznań Session Hall.

{{< figure src="/img-compressed/Gites/Czaszki/accura.webp" alt="Accura 3D printer" caption="Accura 3D printer at work. Source: https://www.facebook.com/photo.php?fbid=1976835735873739&set=pb.100063602499186.-2207520000&type=3&locale=pl_PL" >}}

### 3D Printing

This temporal leap highlights the evolution of the entire philosophy of working with hardware. In the past, the printer itself was often a distinct project demanding more attention (and cooling fan modifications) than the actual object being manufactured.

The current landscape looks entirely different. Enclosed chambers, rigid CoreXY kinematics, and automated bed leveling make modern machines virtually hands-off. Slicing software has become intuitive enough that jobs can be launched directly from a smartphone.

**As a result, the center of gravity has shifted from fighting the machine to the actual research process.** Instead of stressing over first-layer adhesion, we can focus our energy on accurately replicating archaeological artifacts, while the machine simply does its job in the background.

{{< figure src="/img-compressed/Biskupin/20260907_180048.webp" alt="Ender 3 3D printer" caption="Ender 3 at work. It has undergone so many modifications that our team regularly debates whether it can even still be called an Ender." >}}

### 2026: The Biskupin Festival (Full Digitization & Guerrilla Compute Cluster)

To prove how far hardware capabilities have come, in 2026 we teamed up with "Fantastyczny UAM" at the Archaeological Museum in Biskupin. Our station was far from a static exhibition. Using a Creality Otter handheld scanner, we performed real-time 3D scans of newly unearthed micro-artifacts, such as small clay jugs and historical tools.

We then took things a step further: setting out to construct a **complete photogrammetric map of the entire island** using drones.

Initially, we benchmarked DJI Cloud against a locally deployed OpenDroneMap (ODM) pipeline. With a dataset of ~150 photos, DJI yielded marginally cleaner results, but it hit the hard wall of our free tier limit. ODM, on the other hand, accepted massive photo batches without restrictions, easily overcoming any quality delta through pure dataset volume. However, the laptops on site couldn't handle the compute load. Rather than giving up, **we assembled a guerrilla compute cluster**. We used a home server running Home Assistant and Wake-on-LAN to remotely power on a high-performance workstation stationed safely back in Suchy Las. We tunneled in through a secure VPN and used the WebODM interface to offload the entire processing heavy lifting to our remote machine.

As students running non-profit initiatives, we've often operated on shoestring budgets. Such improvised servers and ad-hoc compute clusters have repeatedly allowed us to bypass hardware bottlenecks.

{{< figure src="/img-compressed/Biskupin/dzbanek.webp" alt="Jug 3D scan in slicer" caption="Scanned clay jug inside the Cura slicer." >}}

## Why FOSS (Free and Open-Source Software)?

Over years of working with commercial hardware, I've encountered countless scenarios where unexpected vendor updates stripped away critical functionality, or restrictive software licenses tied our hands regarding downstream usage of our own research.

Over time, the maturity and performance of open-source software reached a point where FOSS is no longer just an ideological stance, but a rock-solid, production-ready toolchain.

In scientific research, maintaining full ownership and control over the pipeline is vital. Leveraging tools like OpenDroneMap and self-hosted WebODM instances guarantees absolute data independence. We know exactly how our data is handled at every stage of the pipeline, avoiding the need to funnel sensitive datasets into third-party corporate black boxes.

---

## Project Gallery

{{< gallery >}}
  <img alt="FDM 3D printed skull replica" src="/img-compressed/Gites/Czaszki/czacha2.webp" class="grid-w50 md:grid-w33" />
  <img alt="Anatomical details of the skull" src="/img-compressed/Gites/Czaszki/czacha3.webp" class="grid-w50 md:grid-w33" />
  <img alt="Symposium presentation at Poznań City Hall" src="/img-compressed/Gites/Czaszki/prezentacja.webp" class="grid-w50 md:grid-w33" />
  <img alt="Biskupin site photogrammetry" src="/img-compressed/Biskupin/20260913_161659.webp" class="grid-w50 md:grid-w33" />
  <img alt="Field scanning station" src="/img-compressed/Biskupin/20260912_114401.webp" class="grid-w50 md:grid-w33" />
  <img alt="Drone data acquisition" src="/img-compressed/Biskupin/20260912_114406.webp" class="grid-w50 md:grid-w33" />
  <img alt="Workstation setup" src="/img-compressed/Biskupin/20260912_103706.webp" class="grid-w50 md:grid-w33" />
  <img alt="Field operation in Biskupin" src="/img-compressed/Biskupin/20260912_133326.webp" class="grid-w50 md:grid-w33" />
  <img alt="Exhibition stand visitors" src="/img-compressed/Biskupin/FB_IMG_1789632112095.webp" class="grid-w50 md:grid-w33" />
  <img alt="On-site demonstration" src="/img-compressed/Biskupin/20260912_101603.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

---

## Sources & Links
* [Genius Loci Archaeological Reserve News](https://rezerwat.muzarp.poznan.pl/pl/aktualnosci/49)
* [GITES Research Club Facebook Report](https://www.facebook.com/zse2gites/posts/pfbid0T9AtZgTAMncz14Fjx8NEi2smfvrtko7Nech2FTHBARnfvNkssZ7AYTQ3BQNA7dWHl?locale=pl_PL)
* [Biskupin Festival Summary - Fantastyczny UAM](https://www.facebook.com/permalink.php?story_fbid=pfbid0BajhipXeAfVtUBW23CTJg8rN5ReKYkxrDxpmQp3wZ25o9iyhLNcH3F8FKc4KCnB1l&id=61576909868074)
* [WebODM - Drone Mapping Software](https://webodm.org/)

