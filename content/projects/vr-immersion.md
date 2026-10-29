---
title: "The Physiology of VR Immersion"
date: 2026-10-01
summary: "Bridging human biology with game engine rendering loops: measuring presence, EDA, heart rate, and flow states in VR using medical biometrics and custom IoT telemetry."
tags: ["VR", "Unity", "Biometrics", "Hardware"]
categories: ["Projects", "Gamedev & XR", "R&D Research"]
---

The true sensation of immersion in a digital world does not begin on a monitor screen or within headset lenses. It starts in the player's mind and trickles down to their fingertips the moment their palms become coated in a microscopic layer of sweat. This is the fascinating threshold where an illusion ceases to be merely a collection of rendered polygons and becomes reality to the human nervous system. For years, simulation creators assumed that the key to this state lay exclusively in photorealistic graphics, increasingly dense geometric meshes, or advanced shading techniques. Yet when the marketing noise and promises of technological revolutions are stripped away, it turns out that the deepest sense of presence emerges when technology becomes transparent, quietly yielding the stage to raw emotion.

The problem is that in conventional game design, these reactions remain completely invisible to the computer. Traditional player experience evaluation resembles attempting to judge a movie solely through questionnaires filled out by audience members fifteen minutes after leaving the cinema. Retrospective survey questions measure a distorted memory of emotion, blurring fleeting seconds of dread, hesitation, or exhilaration. Meanwhile, commercial fitness trackers and smartwatches—while widely available—prove virtually useless in laboratory research due to locked-down APIs and the requirement of offloading intimate biomedical data to third-party cloud servers. To investigate what immersion and flow truly represent, I had to build my own bridge connecting human biology directly into the game engine's rendering loop.

## Rouge Squadron

This fascination with virtual worlds had already begun taking root during my technical high school years, so when the time came to choose an engineering thesis topic, translating that passion into a working project felt like the natural progression. Together with 3D artist Wiktoria Bielecka, we created **Rouge Squadron**—a cooperative spaceship crew simulator.

We targeted a niche of VR users seeking challenges in demanding, rigorous military simulations. Rather than chasing textbook realism, we prioritized the **verisimilitude of the fictional world**. Players face an array of tasks—from dynamic combat encounters to intricate environmental puzzles—to keep the ship operational and achieve mission objectives, requiring tight communication and coordination. To survive in a hostile cosmic environment, the crew must manage scarce resources, making strategic decisions under intense time pressure.

Crew members are granted complete autonomy over their roles and duties. They can collaborate and divide responsibilities to achieve shared goals, or act independently to pursue personal ambitions. The game mechanics do not mandate rigid role definitions; we intentionally left that to the team's interpersonal communication skills. Another vital gameplay pillar is equipment and tool customization based on player needs and preferences. Every mission participant has complete freedom in selecting gear that allows them to perform their assigned functions most effectively.

We engineered two diametrically opposed planetary environments. The first was sun-drenched **Aridis**, inspired by Middle Eastern settlement architecture, where the abandoned Vas Rakhar mining outpost and rogue "HARVEX" extraction machinery placed players in a constant state of threat and defensive maneuvering. The opposite pole was the perpetually shrouded, rainy planet **Lirwen**, modeled on the rugged coasts of Ireland. Carpeted in ancient ruins, moss, and placid fauna, it emphasized mysticism, deliberate exploration, and sensory stillness. Instead of the typical virtual UI button-pressing common in VR games, we insisted on full motor involvement. Players climb ladders using their own arm strength, manually fit mechanical components, turn stubborn valves, and physically wrestle with levers.

{{< gallery >}}
  <img alt="Aridis planet environment screenshot 1" src="/img-compressed/RougeSquadron/Aridis1.webp" class="grid-w50 md:grid-w33" />
  <img alt="Aridis planet environment screenshot 2" src="/img-compressed/RougeSquadron/Aridis2.webp" class="grid-w50 md:grid-w33" />
  <img alt="Aridis planet environment screenshot 3" src="/img-compressed/RougeSquadron/Aridis3.webp" class="grid-w50 md:grid-w33" />
  <img alt="Aridis planet environment screenshot 4" src="/img-compressed/RougeSquadron/Aridis4.webp" class="grid-w50 md:grid-w33" />
{{< /gallery >}}

### Gameplay Footage
{{< youtube "https://www.youtube.com/watch?v=nMWQzpWiL40" >}}

{{< youtube "https://www.youtube.com/watch?v=W0C1-RdMRig" >}}

{{< youtube "https://www.youtube.com/watch?v=MUfFjoHZpU4" >}}

Watching playtest participants completely forget their physical surroundings drove me to investigate how this presence could be measured objectively. I had repeatedly heard claims that VR is inherently more immersive, but those assertions were seldom supported by hard quantitative metrics—relying almost exclusively on subjective questionnaires. For the pilot study, I utilized the Polish production *SUPERHOT* by SUPERHOT Team, specifically because it offers dedicated releases for both standard desktop PCs and VR headsets, eliminating cross-game software discrepancies. Render framerates and graphical configurations were locked to ensure parity (a constant 120 FPS on both platforms).

Data acquisition was handled using a certified **Empatica E4 wristband Rev. 2** (Class IIa medical device under Directive 93/42/EEC). The test protocol began by securing the wristband onto the participant's dominant hand. This placement enabled tracking the hand operating the computer mouse (via the integrated accelerometer) without requiring the subject to remove their personal watch. The participant was then instructed to play a 10-minute session on either PC or VR, followed by a short rest interval, and then play the alternate version for an additional 10 minutes. Throughout the sessions, the band continuously recorded heart rate via photoplethysmography (PPG), skin temperature, hand acceleration, and Electrodermal Activity (EDA), which measures skin electrical conductance. These metrics allow direct quantification of sympathetic nervous system arousal.

The selected title was designed to induce a sense of impending danger, amplified through audio cues, a minimalist color palette, and—in the case of VR—haptic feedback delivered via controller vibration motors. Time advances only when the player moves, forcing continuous mental calculation behind every physical gesture.

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz8.webp" 
    caption="Graphs depicting biometric parameter fluctuations over time for an individual participant. Vertical red lines mark specific milestones: the start and conclusion of gameplay."
    alt="Graphs depicting biometric parameter fluctuations over time for an individual participant. Vertical red lines mark specific milestones: the start and conclusion of gameplay." 
>}}

Observing participants inside the VR environment revealed a striking behavioral transformation. Users who initially made small, cautious wrist movements began—within minutes—moving their entire bodies dynamically, executing deep crouches, dodges, and lunges. Once acclimatized to virtual space, the illusion became so pervasive that subjects routinely lost awareness of the laboratory's physical boundaries, crossing virtual guardian boundaries in the heat of battle. Upon removing the headset, many were visibly breathless, an exertion reflected in sharp spikes in heart rate and angular hand acceleration.

The following graphs illustrate electrodermal activity across participants during desktop PC and virtual reality sessions. In nearly every instance, EDA values (expressed in microSiemens and directly reflecting emotional arousal) surged in VR relative to the desktop session. Only a single participant demonstrated an inverted trend. Post-test debriefing revealed that this subject had substantial prior VR experience, finding desktop mouse-and-keyboard controls clunky and intensely frustrating, which produced a stress spike in front of the flat monitor. Even in her case, however, the remaining telemetry channels confirmed deeper sensory absorption within the virtual world.

Among participants transitioning from VR to desktop gameplay, an elevated baseline of somatic arousal persisted for a noticeable period on the PC. Interviews indicated that following the dynamic, whole-body engagement of the headset, returning to a flat monitor produced an acute sense of anticlimax and disengagement.

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz9.webp" 
    caption="Graph showing the EDA coefficient (electrodermal activity) across subjects during desktop PC gameplay."
    alt="Graph showing the EDA coefficient (electrodermal activity) across subjects during desktop PC gameplay." 
>}}

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz10.webp" 
    caption="Graph showing the EDA coefficient (electrodermal activity) across subjects during virtual reality gameplay."
    alt="Graph showing the EDA coefficient (electrodermal activity) across subjects during virtual reality gameplay." 
>}}

The manufacturer's bundled software struggled with accurate heart rate calculation under rapid physical movement, yet raw photoplethysmography data clearly illuminated the overarching trend. In all recorded cases, the VR environment prompted a marked increase in heart rate.

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz11.webp" 
    caption="Graph showing heart rate across subjects during desktop PC gameplay."
    alt="Graph showing heart rate across subjects during desktop PC gameplay." 
>}}

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz12.webp" 
    caption="Graph showing heart rate across subjects during virtual reality gameplay."
    alt="Graph showing heart rate across subjects during virtual reality gameplay." 
>}}

Comparing datasets between platforms revealed that in VR—despite substantially higher physical exertion and whole-body mobility—skin temperature consistently declined. This phenomenon stems from **peripheral vasoconstriction**. In response to perceived threat, the autonomic nervous system constricts blood vessels in the skin and extremities, shunting blood toward skeletal muscles and internal organs (preparing the organism for fight-or-flight while mitigating potential hemorrhage from injury). The player's brain was treating virtual projectiles as an authentic physical hazard.

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz19.webp" 
    caption="Graph showing skin surface temperature across subjects during desktop PC gameplay."
    alt="Graph showing skin surface temperature across subjects during desktop PC gameplay." 
>}}

{{< figure 
    src="/img-compressed/RougeSquadron/Obraz20.webp" 
    caption="Graph showing skin surface temperature across subjects during virtual reality gameplay."
    alt="Graph showing skin surface temperature across subjects during virtual reality gameplay." 
>}}

Post-session questionnaires corroborated these empirical observations: 90% of subjects reported a substantially higher degree of absorption in VR than on PC. Crucially, this effect proved entirely invariant with respect to age, prior gaming tenure, or previous exposure to VR hardware.

Yet while the medical wristband delivered rigorous data, its closed proprietary ecosystem prohibited real-time streaming directly into the game engine runtime. Data could only be exported as CSV dumps after concluding a session. It became evident that if virtual worlds were ever to dynamically adapt to player emotional states, I needed to architect a bespoke, open IoT telemetry platform operating entirely free from third-party cloud infrastructure.

## The Green Hour

The resolution to this requirement came in the form of **The Green Hour**, developed as part of my Master's thesis in Internet of Things Applications under the academic supervision of Prof. Sławomir Mamica at Adam Mickiewicz University. The project aimed to build a comprehensive research testbed: an atmospheric investigative simulation in Unity paired with wireless sensor telemetry engineered on *privacy by design* principles, processing all biometrics strictly within a local network boundary.

Opting for wireless data transmission was guided by psychological ergonomics: dangling wires and the physical drag of cabling act as severe emersive vectors, constantly reminding the participant of the laboratory setting and shattering the illusion of presence. At the core of the telemetry module sat an ultra-compact ESP32-C3 Super Mini microcontroller (RISC-V architecture, 160 MHz clock speed) equipped with onboard Wi-Fi and Bluetooth connectivity.

To measure skin conductance, I integrated a Grove Galvanic Skin Response (GSR) sensor with electrodes positioned on the participant's fingers (inverted ADC dynamics record resistance drops as sweat glands fill). Peripheral skin temperature was logged using a DS18B20 digital sensor housed in a waterproof stainless steel probe over a 1-Wire bus, allowing swift medical sanitization between successive participants.

{{< figure 
    src="/img-compressed/GreenHour/Obraz4_1_1.webp" 
    caption="Circuit schematic of the measurement system. During testing, the unit was powered via USB-C at a constant 5V supply."
    alt="Circuit schematic of the measurement system. During testing, the unit was powered via USB-C at a constant 5V supply." 
>}}

{{< figure 
    src="/img-compressed/GreenHour/Obraz4_1_2.webp" 
    caption="CAD model of the custom enclosure designed in Autodesk Fusion 360."
    alt="CAD model of the custom enclosure designed in Autodesk Fusion 360." 
>}}

{{< figure 
    src="/img-compressed/GreenHour/Obraz4_1_3.webp" 
    caption="Internal electronics assembly of the measurement unit."
    alt="Internal electronics assembly of the measurement unit." 
>}}

A pivotal design decision was embedding a six-axis MPU6050 inertial measurement unit (accelerometer + gyroscope) into the enclosure. Initially, I planned to harness native telemetry from DualSense gamepads; however, Unity's input subsystem intentionally stripped raw IMU packets, and the Steam Input wrapper mapped gyroscope data to mouse cursor movement, corrupting the experimental setup. Our dedicated MPU6050 guaranteed complete platform agnosticism: we mounted the identical telemetry enclosure onto a traditional gamepad for desktop tests and onto the player's wrist during Meta Quest 3 VR sessions.

The project's most notable technical disappointment proved to be the MAX30102 optical heart rate and pulse oximetry sensor. On paper, a miniature LED illuminating subcutaneous tissue alongside a photodetector tracking pulse waves appeared ideal, yet dynamic usage in VR invalidated this premise. Rapid controller maneuvers, forearm muscular tension, and grip adjustments caused micro-displacements between sensor and skin. Outlier rejection filters discarded such a massive volume of corrupted packets that the buffer received virtually nothing usable. Rather than cosmetically smoothing meaningless data, I treated this as a valuable negative result: in dynamic VR environments, optical pulse readings are highly fragile against motion artifacts. Empirical inference must instead rely on the significantly more stable metrics of galvanic skin response (GSR), skin temperature, and acceleration kinetics.

Concurrently, I resolved a library bottleneck with the DS18B20 sensor, whose standard 12-bit temperature conversion blocked the microcontroller's main loop for over 700 ms. Implementing asynchronous non-blocking conversion reclaimed CPU cycles, enabling 50 Hz accelerometer sampling accompanied by a 21 Hz hardware low-pass filter, transmitting clean JSON telemetry frames via WebSocket (port 81) at reliable 100 ms intervals.

{{< figure 
    src="/img-compressed/GreenHour/MocowanieGamepad.webp" 
    caption="Mounting configuration of the central telemetry unit onto a controller for the PC testing environment. The unit houses an MPU6050 sensor capturing linear and angular acceleration."
    alt="Mounting configuration of the central telemetry unit onto a controller for the PC testing environment. The unit houses an MPU6050 sensor capturing linear and angular acceleration." 
>}}

{{< figure 
    src="/img-compressed/GreenHour/MocowanieReka.webp" 
    caption="Placement of biophysical sensors on the participant's hand."
    alt="Placement of biophysical sensors on the participant's hand." 
>}}

In virtual reality, framerate stability is an uncompromising usability requirement. Any momentary hitch on the main rendering thread that drops framerates below the headset's native refresh rate can instantly induce simulator sickness and shatter immersion. Simultaneously, Unity's built-in JSON deserializer is not thread-safe; attempting to parse incoming network strings directly on an asynchronous socket thread leads to immediate memory access exceptions.

To reconcile a high-frequency telemetry stream with absolute visual fluidity, I engineered a two-stage producer–consumer buffering architecture backed by dual independent FIFO queues and a synchronization lock (`wsLock`). The network thread strictly enqueues raw payload strings into the intake queue, while Unity's main thread safely deserializes them into structured memory objects within the `Update()` lifecycle.

```csharp
// WebSocket library network thread – purely enqueuing raw string
private void OnMessageReceived(object sender, MessageEventArgs e)
{
    lock (wsLock)
    {
        incomingRawJson.Enqueue(e.Data);
    }
}

// Unity main rendering thread – safe deserialization into engine memory
private void Update()
{
    lock (wsLock)
    {
        while (incomingRawJson.Count > 0)
        {
            string json = incomingRawJson.Dequeue();
            SensorData data = JsonUtility.FromJson<SensorData>(json);
            incomingReadings.Enqueue(data);
        }
    }
}
```

Subsequently, data is downsampled to 1 Hz within a dedicated aggregation loop that acts as a low-pass filter smoothing out minor contact noise. Within the same interval, the engine samples microphone input (RMS amplitude), non-invasively capturing vocal reactions ranging from subtle gasps to accelerated breathing patterns. A global motor input listener tallies button press frequency per second. Disk logging to CSV executes asynchronously via background I/O tasks, eliminating any frame stutters during active gameplay.

### The Virtual Director

Even the most sophisticated biometric stream becomes useless for statistical modeling and machine learning algorithms without knowing precisely what transpired in the virtual environment at that exact second. A transparent causal relationship must bridge dry physiological readings with player behavior. To solve this, I designed the **Virtual Director** subsystem, inspired by the role of the Game Master in tabletop role-playing games and Mihály Csíkszentmihályi's psychological theory of flow.

Flow represents a narrow channel of optimal equilibrium between a player's evolving competency and the escalating challenges presented by the game. If the challenge is trivial, the player drifts into boredom; if overwhelming, into paralyzing anxiety and frustration. The Virtual Director dynamically modulates environmental stimuli to sustain the player within this zone of maximum absorption.

The script choreographs the scenario, alternating between periods of quiet exploration and sequences of mounting tension. It governs in-game temporal progression, intensifies wind gusts, cuts lighting fixtures, or triggers contextual audio events (e.g., snapping twigs, footsteps circling an abandoned cabin, fuse box failures). Through tight integration with the telemetry aggregator, every one-second biometric record is automatically stamped with current map zone coordinates, narrative flags, and a list of active stimuli.

It is worth noting the inclusion of an olfactory stimulation prototype. Built as an independent multichannel scent diffuser controlled via network commands, it released specific aromas when players crossed defined forest zones. Echoing Morton Heilig's historic 1962 Sensorama concept, incorporating olfaction serves as an intriguing immersive modality whose quantifiable impact on skin conductance I plan to explore in subsequent research.

### Hybrid Bridge and Diegetization

A glaring methodological weakness across many studies comparing virtual reality against traditional monitors is the reliance on two fundamentally different game builds. Frequently, the desktop counterpart features altered level geometry or different locomotion mechanics, introducing severe confounding variables into the experiment. For *The Green Hour*, my objective was to engineer **a single, fully unified codebase and level**, where both modalities operated under identical Unity HDRP physics simulations.

To achieve this, I developed a custom first-person camera compatibility bridge for desktop PC controls. Instead of maintaining parallel interaction logic for mouse and keyboard, the desktop camera casts raycasts and programmatically invokes interaction methods on native XR Interaction Toolkit components. Consequently, the identical codebase governs grasping objects, inserting cassette tapes into VCR decks, or manipulating generator sliders, regardless of whether input originates from a VR hand controller or a desktop peripheral.

An equally critical challenge was user interface design. In alignment with Piotr Kubiński's typology of emersion, conventional health bars, digital counters, and static HUD elements pinned to screen margins act as emersive disruptors, constantly reminding the user of the simulation's artificiality. To counter this, I implemented comprehensive **diegetization**: the entire visual presentation was framed as the viewfinder of a turn-of-the-century analog camcorder carried by the character documenting the forest investigation.

Drawing upon the aesthetic of found footage cinema and games (*The Blair Witch Project*, *Backrooms*), deliberately introducing analog film grain, subtle chromatic aberration, and vignetting yielded a double benefit: it fostered an unsettling, gritty atmosphere while masking minute texture resolution disparities. Core parameters—battery life representing daylight depletion, an audio VU meter, and live heart rate streamed from the telemetry module—became organic elements within the fictional world. Supplemental information, such as controller bindings, lore documents, and a creature bestiary, was integrated directly into level geometry as posters, legible paper notes, and an old desktop computer running a slide presentation.

In the VR environment, diegetization naturally catalyzed **asynchronous bimanual interaction**. Headset participants instinctively used both hands independently—directing a flashlight with one hand while repairing an electrical panel held with the other, or placing objects onto nearby virtual tables—an intuitive motor workflow completely unachievable on a desktop gamepad.

{{< figure 
    src="/img-compressed/GreenHour/Interface.webp" 
    caption="During gameplay, the player encounters an information board. It clarifies core mechanics and displays approximations of two fundamental metrics the player must balance."
    alt="During gameplay, the player encounters an information board. It clarifies core mechanics and displays approximations of two fundamental metrics the player must balance." 
>}}

### Findings

Technical evaluation of the pipeline was conducted via a within-subject laboratory study involving ten volunteers. Each participant completed two ~30-minute experimental sessions: one facing an ultrawide monitor with a gamepad in hand, and another wearing a Meta Quest 3 VR headset streaming wirelessly in PCVR mode. Presentation order was randomized, separated by a 30-minute washout rest interval to allow somatic baselines to restabilize and mitigate cognitive fatigue.

Statistical analysis using the non-parametric Wilcoxon signed-rank test for paired samples revealed dramatic motor behavioral divergences. In the VR environment, mean action density escalated more than eightfold compared to the desktop monitor, reaching nearly 2.5 motor inputs per second at full statistical significance ($p = 0.0039$) and maximum effect size. Simultaneously, I logged a nearly fivefold increase in mean angular velocity of hand movements via the embedded IMU. These hard empirical metrics demonstrate that virtual reality demands a fundamentally distinct kinesthetic profile: the user ceases to be a passive observer clicking thumb buttons and transforms into an active agent navigating spatial boundaries with their entire body.

The **orienting reflex to spatialized audio** proved remarkably instructive. Despite the VR headset utilizing integrated open-ear speakers (which provide objectively lower acoustic isolation from ambient room noise than the ISK HD9999 circumaural studio headphones used for PC tests), VR participants snapped their head and torso toward the faintest virtual rustle instantly. In post-test interviews, several subjects asserted with complete conviction that the VR build featured "substantially richer sound design," even though identical audio assets and attenuation curves were deployed across both setups.

Physiological telemetry proved equally illuminating. Under VR conditions, datasets displayed a consistent downward trajectory in skin temperature paired with an ongoing decrease in skin electrical resistance (higher conductance), confirming elevated sympathetic nervous system activation.

Most striking from an immersion psychology standpoint is that this effect was achieved in a title where **I intentionally implemented neither a physical monster model nor any direct mortality threat**. Due to scope constraints, the codebase contained not a single line of hostile AI. Yet VR participants stared into the tree line with palpable tension, convinced that a cryptid was stalking their every move. The dread and somatic defense response were induced purely through the psychological power of suggestion, cultivated by 3D positional audio, dynamic lighting, and environmental storytelling.

The sensitivity of this setup in capturing acute emotional spikes was vividly demonstrated during one participant's session. While rummaging through a cabin interior, she accidentally knocked a glass bottle off a table. The sound of shattering glass triggered an instantaneous startle reflex, culminating in an audible gasp. Overlaying the telemetry traces afterward revealed a sharp, narrow spike in microphone audio amplitude perfectly synchronized with a steep cliff in galvanic skin resistance (GSR), capturing the exact millisecond her nervous system triggered a sweat response in the palms.

*Table 8.2.1. Wilcoxon Signed-Rank Test Results across Analyzed Dimensions*

| Dimension | Statistic (*W*) | Statistical Significance (*p*) | PC Mean | VR Mean |
| :--- | :---: | :---: | :---: | :---: |
| Spatial Awareness | 1.00 | 0.0039 | 2.72 | 4.22 |
| Engagement | 7.50 | 0.0430 | 2.84 | 3.87 |
| Flow State | 11.50 | 0.1133 | 3.40 | 3.73 |
| Environmental Awareness | 7.50 | 0.0410 | 3.32 | 3.68 |
| Simulator Sickness | 0.50 | 0.0039 | 1.30 | 2.50 |
| Time Perception | 27.0000 | 1.0000 | 6.44% | 8.48% |

Time perception variance proved intensely individualized; the Wilcoxon test (Table 8.2.1) yielded a *p*-value of 1.0 for the time perception dimension, indicating that recorded discrepancies between platforms were statistically insignificant across the cohort.

*Table 8.2.2. Comparison of Self-Reported vs. Actual Gameplay Duration across Platforms*

| Participant | Platform | Self-Reported Duration | Actual Duration | Perception Error |
| :---: | :---: | :---: | :---: | :---: |
| 1 | PC | 15 min | 31.04 min | -52% |
| 1 | VR | 20 min | 32.84 min | -39% |
| 2 | PC | 30 min | 30.43 min | -1% |
| 2 | VR | 20 min | 19.19 min | 4% |
| 3 | PC | 30 min | 30.61 min | -2% |
| 3 | VR | 30 min | 16.98 min | 77% |
| 4 | PC | 30 min | 24.06 min | 25% |
| 4 | VR | 20 min | 22.21 min | -10% |
| 5 | PC | 20 min | 25.90 min | -23% |
| 5 | VR | 15 min | 21.82 min | -31% |
| 6 | PC | 20 min | 20.68 min | -3% |
| 6 | VR | 22 min | 25.73 min | -14% |
| 7 | PC | 30 min | 25.98 min | 15% |
| 7 | VR | 50 min | 24.17 min | 107% |
| 8 | PC | 30 min | 20.37 min | 47% |
| 8 | VR | 25 min | 21.35 min | 17% |
| 9 | PC | 25 min | 26.09 min | -4% |
| 9 | VR | 25 min | 22.06 min | 13% |
| 10 | PC | 30 min | 18.48 min | 62% |
| 10 | VR | 15 min | 24.44 min | -39% |

Data interpretation assisted by a large language model suggests that within the studied sample, the virtual reality environment exhibited higher efficacy in stimulating specific dimensions of user experience than traditional desktop gameplay. The observed trajectories strongly indicate the feasibility of real-time acquisition and analysis of physiological telemetry to evaluate presence and flow states. Given the modest sample size, extrapolating broad population-level conclusions remains premature. Nevertheless, this study serves a critical exploratory purpose, establishing a rigorous methodological foundation for future deep-dive experiments.

## Summary

These pilot experiments offer valuable insights into perceptual divergence across hardware platforms and the mechanics governing immersion and flow. In light of cohort constraints and time boundaries, the findings remain fundamentally exploratory, aimed at mapping overarching trends and formulating preliminary research hypotheses.

The empirical evidence—derived from synchronized laboratory testing and structured psychometric surveying—indicates that **immersion and flow are distinct psychological phenomena triggered by contrasting design paradigms**:
1. **Flow state** is most effectively cultivated by mechanically demanding environments centered on escalating challenge curves, competitive PvP dynamics, or iterative task optimization (farming/grinding loops). The user enters a focused mechanical trance requiring fine motor precision, which does not necessarily require the sensation of "being physically inside the virtual world."
2. **Immersion and Presence**, conversely, dominate in titles prioritizing open exploration, environmental narrative, and rich sensory world-building. High environmental immersion lowers the friction for entering flow by stimulating **autotelic motivation**—engaging in an activity for the pure satisfaction derived from the act itself, which proves far more resilient than extrinsic reward loops.

Sensory mismatch (visual input indicating continuous velocity while the vestibular system reports physical stillness) remains the root cause of simulator sickness. This is compounded by a two-pronged fatigue: mechanical (headset facial pressure, visual accommodation) and cognitive exhaustion stemming from intense stereoscopic stimulation. This accounts for why 70% of surveyed VR users report average individual session lengths below one hour.

Future research will focus on integrating non-invasive pupillometry (gaze tracking available in headsets featuring foveated rendering) and optimizing the telemetry pipeline with localized edge AI models. Deploying specialized inference agents will unlock the full vision of the **Virtual Director**—an adaptive gaming environment that modulates pacing, lighting, and challenge curves in real time, directly responsive to the autonomic nervous system of the human at the controls.

Ultimately, the goal of integrating biometric telemetry into interactive media is not to diminish the human being into a predictable matrix of data plots. Genuine immersion begins when the digital world respects the user's intelligence, evolving into a responsive sandbox—a space that does not merely surround the player, but quietly and perceptively attunes to their biological presence.

