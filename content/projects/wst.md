---
title: "WST / XR BINIU – How We Taught Sand to Think, Sank a Boat, and Built Our Own Sim2Real Ecosystem"
date: 2025-06-01
summary: "From an academic Unity 6 simulation and a ripped-off industrial 3D printer hotend to global cellular VPN control and custom UDP protocols. A two-year journey of mistakes, smoking electronics, and building an open-source platform for autonomous vehicles."
tags: ["AI", "Sim2Real", "Robotics", "Unity"]
categories: ["Projects", "AI & Robotics"]
---

Commercial autonomous vehicle control systems are often proprietary black boxes that impose rigid boundaries on what you are allowed to build and what is deemed impossible. Rather than purchasing an off-the-shelf, closed-source flight controller, we decided to grab a microcontroller costing barely a few dollars, fire up a game engine, and see what happens when you stop being overly sensible. That was the genesis of the autonomous surface vessel project **XR BINIU** (*miXed Reality Blended Intelligence for Navigable Interactive UVs*), which steadily evolved into **WST (Weird Steering Things)**—an open platform for engineering and training unconventional unmanned robotics across any environment. Over two years, our journey wound from physics somersaults in virtual space, through ripped-off 3D printer hotends and smoking wiring harnesses, all the way to bespoke video streaming protocols and global telemetry over cellular networks. Not all our ideas turned out to be "good," and plenty sank several leagues below "terrible." Yet even the avenues that led into dead ends provided tremendous fun and deep learning. Knowing *why* something fails can be infinitely more valuable than knowing *why* it works.

---

## Brain in the Cloud, Muscle on the Water

The primary hurdle that struck us right at the outset was the universal nemesis of student projects: **budget**. We knew we wanted to unleash an autonomous boat onto an open lake, but the prospect of drowning an expensive Raspberry Pi or Nvidia Jetson didn't sit well with us. Initially, we weighed the classic approach from amateur drone systems—using direct radio frequency links for data exchange between a ground control station and the boat. While radio bandwidth is modest, it is generally sufficient, well-documented, and backed by a vast marketplace of transceivers. Unfortunately, even operating ranges measured in kilometers fell short of what we envisioned. We wanted to run autonomy workloads on the high-end workstations we already owned. Considering that our beloved RTX 4070 SUPER was sitting at home in Suchy Las, our lead pilot was in Kraków, the boat was floating on the lake at the Morasko university campus, and our chosen ESP32 supported onboard Wi-Fi and VPN tunnels, the math became obvious: we spin up a Virtual Private Network!

Still, there remained the constant threat of drowning our "artificial stupidity," which drove our decision to build the simulation within **Unity 3D**. In developing autonomous robotics via **Sim2Real** (transferring artificial intelligence trained in simulation into the physical world), an immense chasm separates the immaculate mathematics of a 3D engine from physical cabling, sensor noise, and mechanical inertia. If we hardcoded neural network inference directly to specific microcontroller GPIO pins, every single sensor upgrade would force us to retrain the entire model from scratch. We needed a decoupled architecture that completely blinded the AI to whichever reality it was currently navigating, granting it a clean layer of abstraction. Just as a driver doesn't need to know the inner valve timings of an engine to steer, the AI shouldn't care which physical pin delivers what voltage—it only needs to interpret the abstract telemetry readings.

Our answer was rigorous decentralization: strictly segregating the "Brain" (the workstation running the decision-making model) from the "Muscle" (the low-level microcontroller firing PWM pulses to motor drivers and aggregating raw sensor inputs). At the software architecture level, we designed a virtual breadboard pattern—a `Breadboard` abstraction interfacing with modular contracts for motors (`IPWMMotor`) and sensors (`ISensor`). During reinforcement learning training in **Unity 6** (leveraging the **ML-Agents** toolkit), the agent overrides observation and action routines, communicating solely with this virtual breadboard.

When the time comes to step out of the lab and head to the lake, we simply swap out the virtual breadboard's simulated endpoints for a network driver that talks over the air to a physical **ESP32**. Textbook software engineering literature would prescribe multi-tier dependency injection containers and immaculate repository hygiene here. In the heat of late-night triage, however, when the PlatformIO compiler began choking on nested generic structures, we bridged several subsystems using raw single pointers just to shove the project forward. Did that architectural shortcut come back to bite us during subsequent feature expansions? Absolutely, and repeatedly so. **Yet thanks to the rigid separation between the decision and hardware layers, an AI agent trained entirely inside a computer takes full operational command of the physical boat without modifying a single line of neural network weights or logic.**

---

## Gerstner Waves, Bow-Wagging, and a Pink VR Bridge

Before anything could ever touch real water, our virtual fleet had to endure thousands of hours of accelerated simulation. We selected the **HDRP (High Definition Render Pipeline)** in Unity 6 specifically for its native, physically based water simulation. This enabled us to replicate intricate wave interference patterns, dynamic river currents, hydrodynamic buoyancy, and viscous drag. We designed an unnaturally winding canyon river with an escalating difficulty curve, crowned with a cat-textured finish gate that awarded the agent its maximum reward payload.

It was on this virtual proving ground that the artificial intelligence revealed behaviors we never explicitly programmed. Because we had equipped the simulated hull with only three directional ultrasonic rangefinders, the agents faced severe perceptual blind spots along the narrowest, twistiest bends of the canyon. To our astonishment, through brute trial and error, the neural network independently converged on a distinctive "bow-wagging" behavior: the boat executed rhythmic, side-to-side sweeping maneuvers while advancing, actively scanning its environment like an insect probing with antennae.

{{< figure 
    src="/img-compressed/Errno/Drony/Obraz1.webp" 
    caption="Training course with navigation gates" 
    alt="Training course with navigation gates" 
>}}

{{< figure 
    src="/img-compressed/Errno/Drony/Obraz3.webp" 
    caption="A fleet of agents ready to quickly drown the vessel—I mean, bravely train" 
    alt="A fleet of agents ready to quickly drown the vessel—I mean, bravely train" 
>}}

In parallel with autonomous training, we wanted human operators to step into the captain's shoes and assume real-time control of the physical vessel using a virtual reality headset. We built a virtual captain's bridge that translates spatial VR controller maneuvers into low-latency command packets dispatched to the robot on the water. The geometric model was textured inside Substance 3D Painter as scuffed industrial plastic, accented with vibrant neon-pink borders framing the telemetry displays, giving the helm a signature cyberpunk aesthetic.

{{< figure 
    src="/img-compressed/Errno/Drony/Obraz4.webp" 
    caption="Captain's bridge in VR" 
    alt="Captain's bridge in VR" 
>}}

---

## Ripped-Off Hotend and Body Filler

While the software stack was materializing, the other half of the team was waging war inside Autodesk Fusion 360, striving to translate our aerodynamic and hydrodynamic concepts into a physical hull. Drawing inspiration from futuristic naval designs such as the *FNCS 2030*, we set three core criteria: sufficient displacement to carry heavy lithium batteries, high agility across tight inland waterways, and aerial propulsion. Swapping an underwater propeller for twin brushless aerothrusters mounted on lateral pylons seemed like an elegant move, as it entirely bypassed the headache of sealing rotating drive shafts beneath the waterline. Naturally, it introduced its own fair share of engineering quirks—not least of which was an increased risk of snagging lake reeds—but we had no interest in treading well-worn paths; we wanted to explore something genuinely novel.

Our initial hull revision sported a broad, flat bottom reminiscent of a cargo barge. While its static displacement was stellar, our first water trials delivered a harsh dose of reality: the flat hull meant that under aggressive cornering, the craft lost lateral bite and threatened to capsize outright. We redesigned the stern section with a sharper deadrise angle so the hull could slice into the water surface, and hollowed out dedicated sensor bays beneath the bow rim—placed precisely where our Unity raycast simulations indicated optimal coverage.

Then came another logistical shock: Bambu Studio estimated our sliced CAD model would weigh around four kilograms. Fearing that our drone motors would burn out trying to propel such a heavyweight brick, we hastily scaled the entire model down by 20%, shrinking the weight down to a manageable three kilograms at dimensions of 800 × 295 × 242 millimeters.

3D printing an eighty-centimeter vessel from PLA filament is in an entirely different universe than churning out desktop figurines. Our initial 1:5 and 1:2 scale prototypes were printed in multiple modular segments on consumer FDM machines, joined using 3D pens as thermal welders, and sealed with silicone caulk. Although those scale models happily floated for hours, we recognized that on a full-scale craft, every structural seam was an inevitable failure point: an invitation for delamination, water ingress, fried electronics, and plastic littering the lake.

Rescue arrived via the **Wielkopolska Centre for Advanced Technologies (WCZT)**, which granted us access to their industrial large-format *Dragon 3D* Tower S machine—boasting a massive 100 × 100 × 150 centimeter build volume and a monstrous 1.8-millimeter extrusion nozzle. Laying down bead paths that thick necessitated redesigning every structural mounting port: traditional semi-circular overhangs sagged in mid-air, so we replaced them with steep Gothic pointed arches that rose gracefully from vertical bulkheads without requiring a scrap of temporary support material.

{{< figure 
    src="/img-compressed/Errno/Drony/Obraz6.webp" 
    caption="Dragon 3D and Wiktoria next to a Prusa for scale" 
    alt="Dragon 3D and Wiktoria next to a Prusa for scale" 
>}}

Despite our meticulous geometry prep, our first full-scale print run ended in catastrophe. Seeking to conserve raw filament, we set the internal wall infill to a meager 5%. After dozens of hours of continuous deposition, the massive layers began delaminating, and thick loops of stray plastic tangled around the hotend assembly. During an extreme travel move, the rigid block of cooling plastic acted like a pry bar, mechanically tearing the heater block straight off its gantry mount. Staring at an individual layer bead thicker than standard raw filament (1.8 mm bead vs. 1.75 mm filament) was humbling. Most people today associate 3D printing with pristine, plug-and-play machines from Prusa or Bambu Lab. While our team cut our teeth on clunky Enders, Anets, and even wooden Accura rigs, the sheer scale and raw power of the Dragon commanded immense respect. Our tour of the facility both invigorated our ambitions and grounded our expectations, showing us how much we still had to master. It is an environment where you must keep your feet firmly on the ground while allowing yourself to be captivated by possibilities, discarding conventional thinking to leave room for true innovation.

{{< figure 
    src="/img-compressed/Errno/Drony/Obraz7.webp" 
    alt="Ripped-off hotend" 
    caption="Ripped-off hotend" 
>}}

{{< figure 
    src="/img-compressed/Errno/Drony/20250602_143534.webp" 
    caption="Damaged print. The view of an individual layer thicker than standard filament (1.8 mm vs. 1.75 mm) made quite an impression on us" 
    alt="Damaged print. The view of an individual layer thicker than standard filament (1.8 mm vs. 1.75 mm) made quite an impression on us" 
>}}

Bumping the infill to 20% and replacing the mangled printhead resolved the layer separation issue, but fate wasn't done testing us: midway through the subsequent attempt, the municipal grid suffered a local blackout, and shortly thereafter our material spool ran dry. The print was ultimately saved by WCZT's technicians, who graciously donated an enormous spool of white PLA to finish the job. **We attacked the raw, two-toned hull—grooved with pronounced layer lines from the colossal nozzle—with an industrial angle grinder, automotive body filler, and marine sealing enamel, finally producing a seamless, watertight shell ready to house our avionics.**

{{< figure 
    src="/img-compressed/Errno/Drony/20250602_143633.webp" 
    caption="The printer in action" 
    alt="The printer in action" 
>}}

---

## Maiden Voyage, or How We Sank Our Project

So how did our grand Sim2Real trial fare when confronted with physical reality? In short: it sank.

The craft certainly satisfied two of its three design goals—it possessed ample buoyancy reserve, and the air thrusters generated impressive forward momentum—yet turn authority proved to be our fatal flaw. Real-world water resistance, gusty wind, and the momentum of the heavy printed hull meant the boat refused to pivot into sharp corners with anything resembling its virtual counterpart's agility. A cascade of early teething issues promptly sent our creation to the bottom of the lake. Only after fishing it out, drying the electronics, sealing critical ingress points, and implementing painstaking adjustments did the machine begin (more or less) respecting steering commands and cruising (reasonably) stably in calm weather.

{{< gallery >}}
  <img alt="Launching the water drone" src="/img-compressed/Errno/Drony/20250602_143615.webp" class="grid-w50 md:grid-w33" />
  <img alt="Structural testing of the drone" src="/img-compressed/Errno/Drony/20250602_143633.webp" class="grid-w50 md:grid-w33" />
  <img alt="Lab work on electronics" src="/img-compressed/Errno/Drony/20250609_143529.webp" class="grid-w50 md:grid-w33" />
  <img alt="Integrated autonomous unit" src="/img-compressed/Errno/Drony/IMG-20250609-WA0000.webp" class="grid-w50 md:grid-w33" />
  <img alt="Hull and propulsion assembly details" src="/img-compressed/Errno/Drony/20250602_144957.webp" class="grid-w50 md:grid-w33" />
  <img alt="Electronics prototyping stage" src="/img-compressed/Errno/Drony/20250511_222628.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

It was right there, standing on the water's edge and watching our dripping prototype, that an important revelation struck us. Developing software tied strictly to a single boat just to earn course credit is fundamentally limiting. If our virtual breadboard abstraction could command this custom hull, it could drive practically anything we threw at it—and (as we naively believed back then) doing so would be a breeze. **At that moment, our student project XR BINIU shed its narrow academic shell and transformed into WST (Weird Steering Things)—an open ecosystem conceived not for monetization or investors, but for the pure thrill of tinkering with the strange.**

---

## WST

Evolving toward WST meant severing the umbilical cord of short-range local Wi-Fi, which confined us to a shore-side hotspot. We upgraded the architecture with a **GSM/LTE** cellular modem and a dedicated **VPN** gateway hosted on a **Raspberry Pi**. As a result, our Unity-based "Brain" can run on a powerful workstation in Poznań while the physical unmanned craft links into it over the cellular web from anywhere on the planet with network coverage.

We were determined to ensure the architecture could accommodate **any kinematic topology**. One such testbed was WST-TOSIA: a miniature ground vehicle sporting only two driven wheels. From an algorithmic perspective, it is virtually identical to our boat: both platforms rely on differential drive steering.

{{< figure 
    src="/img-compressed/Errno/Drony/20260319_172447.webp" 
    alt="WST-TOSIA" 
>}}

{{< figure 
    src="/img-compressed/Errno/Drony/20260408_153351.webp" 
    alt="WST-TOSIA2" 
>}}

Naturally, routing critical control traffic across public cellular towers and an encrypted VPN tunnel extracts a latency tax: round-trip times hover between 100 and 200 milliseconds. For an esports player in *Counter-Strike 2*, that kind of ping means immediate defeat and a broken mouse, but for a high-inertia watercraft—and, as we theorize, a slow-moving aerial platform—two-tenths of a second provides more than enough margin for stable correction.

The true trial began with live video streaming, where our goal was to drive latency below the 100 ms threshold. We set about crafting our own lightweight video transmission protocols on top of connectionless **UDP**. We quickly slammed into the classic network transport conundrum: splitting a single compressed video frame across multiple small packets invites reassembly nightmares whenever a fragment drops in transit. Conversely, shoving an entire compressed I-frame into a single oversized packet sidesteps fragmentation, but introduces jitter where packets arrive out of order, making the video stream visibly "rewind" in time.

---

## Like Fine Wine, and the Team Behind the Helm

The natural culmination of the WST design philosophy was our **bicopter** initiative—an aerial vehicle stabilized by only two main rotors tilted via servo linkages. Inherently unstable aerodynamically, it provides the ultimate sandbox for training neural network control policies in simulation prior to any physical flight attempt. At present, polishing the boat's full autonomy suite and taking the bicopter airborne have had to pause briefly on the shelf. Academic life follows its own calendar, and writing and defending Master's theses effectively pulled our team away from our soldering stations. We do not view this as a setback. **Ambitious engineering projects are like fine wine: they require time to rest, mature, and await the day we return to them armed with fresh experience and sharper skills.**

{{< gallery >}}
  <img alt="Bicopter" src="/img-compressed/Errno/Drony/image.webp" class="grid-w50 md:grid-w33" />
  <img alt="Bicopter" src="/img-compressed/Errno/Drony/20260415_094547.webp" class="grid-w50 md:grid-w33" />
  <img alt="Also a bicopter, but with a considerably sillier premise" src="/img-compressed/Errno/Drony/20260416_130653.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

None of this wild adventure at the Faculty of Physics and Astronomy at AMU could have succeeded in isolation. The entire endeavor within the **Errno** Student Science Club was backed academically and logistically by our faculty advisor, **dr Wojciech Czart**. Ensuring that our five-dollar microcontrollers survived violent encounters with exploding capacitors fell to **inż. Adam Mischke**, while our vigilant guardian of Unity code quality—who kept our git repository from devolving into total anarchy—was **Oliwia „Cosinus” Pawłowska**. Hull geometry and the grueling struggle with large-format 3D printing were spearheaded by **inż. Krystian Olesiejko**, the mechanical airframe of the bicopter was engineered by **Emil Kopytek**, and our VPN tunnels and low-level C++ network plumbing were kept alive by **Mateusz Nawrot**. Meanwhile, **inż. Wiktoria Bielecka** crafted the visual identity, 3D assets, and user interfaces—standing as the sole guardian preventing our project from looking like a 1995 Linux terminal. My own role was serving as project lead, systems architect, and the software engineer bridging the worlds of Unity and C++—which mostly meant being the person asking "why not?" whenever smoke started curling off a circuit board.

