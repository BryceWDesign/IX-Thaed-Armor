# IX-Thaed-Armor — Power & Harmonic Drive Interface

## 🧠 Objective

Define the electrical interface, waveform generation logic, and physical wiring used to drive the embedded PVDF piezoelectric mesh at Tesla 3-6-9 harmonic frequencies. This system enables the dynamic stress-canceling response of IX-Thaed-Armor in real time under vibrational or impact loads.

---

## ⚡ Electrical Supply

| Parameter | Value |
|----------|--------|
| Supply Voltage | 3.3V or 5V (DC) |
| Peak Current (active mode) | ~25–40 mA (depends on mesh size and gain) |
| Power Source | Microcontroller rail or isolated battery pack |
| Electrical Isolation | Required for marine deployments |
| Ground Strategy | Common return between waveform driver and mesh array; no hull loop allowed |

---

## 🔄 Signal Generation Options

### 💻 Option 1: Arduino Nano + AD9833 Module
- Pros: Small, cheap, fully programmable, easy to tune
- Output: Sine wave (3–9 Hz programmable), SPI-controlled
- Compatible with: 3.3V or 5V mesh driver circuits

### ⚙️ Option 2: Teensy 4.1 + DAC + AudioShield
- Pros: Higher resolution, dual channel output
- Optional: Inject separate harmonic sets to different mesh zones

### 🛰️ Option 3: Radiation-Hardened PLL Synth
- Use Case: Orbital platforms only
- Source: Honeywell HX5000 or similar  
- Firmware: Generate 3/6/9 Hz directly to radiation-safe DAC line

---

## 📐 Circuit Diagram Description

[Microcontroller] --SPI--> [AD9833 DDS Module] --> [Op-Amp Buffer] --> [PVDF Mesh Electrodes]
|
[Voltage Divider] --> [Feedback Sense (optional)]


- PVDF mesh requires **buffered output**, not direct DAC drive
- Op-amp or transistor-based driver recommended (e.g. LM358, MCP602)
- Current draw is minimal, but capacitive coupling must be stable

---

## 🎛️ Configuration Parameters

| Setting | Value |
|---------|--------|
| Default Frequencies | 3 Hz, 6 Hz, 9 Hz |
| Waveform | Sine (pure tone) |
| Amplitude | 0.5–2.5V peak (adjustable) |
| Sweep Mode | Optional (e.g., 3→6→9 every 10 sec) |
| Phase Sync | Not required across panels unless mesh is continuous |

---

## 🧪 Deployment & Testing

1. Power up microcontroller and verify clean waveform via oscilloscope
2. Connect PVDF mesh through buffer circuit
3. Monitor response using:
   - Laser vibrometer
   - Piezo back EMF voltage
   - Acoustic resonance microphone (for test validation)
4. Tune gain per panel during pre-seal calibration
5. Lock in waveform profile and deploy

---

## 🔒 Safety Notes

- Do NOT allow direct electrical contact between PVDF lines and metallic hull
- Use dielectric standoffs or terminal epoxy where needed
- Shield all waveform lines for EMI compliance in marine or aerospace
- Disable drive circuit during maintenance or when armor is not sealed

---

## 📎 Summary

This document enables real-world electrical activation of IX-Thaed-Armor's vibration-canceling Tesla harmonic layer.

- **Microcontroller-based harmonic drive**
- **3.3–5V DC safe**
- **3/6/9 Hz programmable injection**
- **Marine and orbital compatible**
- **Fully open-source, buildable today**

