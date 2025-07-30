# IX-Thaed-Armor — Fallback and Repair Protocol  
**Version:** 1.0  
**Scope:** Maritime, Orbital, and Environmental Systems  
**Author:** Bryce Wooster

This document outlines real-world procedures to:
- Detect failure or degradation in IX-Thaed-Armor panels
- Apply non-destructive testing
- Perform compliant patching and resonance re-tuning
- Ensure continued functionality of harmonic damping and protection system

---

## ⚠️ When Repair is Required

Initiate panel repair if **any** of the following is observed:

- Visible delamination between layers (graphene, damping, substrate)
- Saltwater ingress or corrosion breach of gold/graphene surface
- Cracking from thermal cycling (orbital/cryogenic systems)
- Loss of harmonic tuning (confirmed via FFT or waveform probe)
- Physical puncture or impact exceeding 2mm depth
- PVDF mesh lead degradation or detachment

---

## 🧪 Non-Destructive Testing (NDT) Tools

| Tool | Use Case |
|------|----------|
| Laser Vibrometer | Check PVDF resonance and vibrational phase cancellation |
| Ultrasound Scanner | Identify internal delamination or bubble expansion |
| FLIR Thermal Camera | Spot thermal anomalies during drive cycle |
| Multimeter / LCR Meter | Confirm lead integrity, capacitance shift, or grounding |

---

## 🛠️ Approved Repair Materials

| Material | Use |
|----------|------|
| Graphene Repair Film (pre-transferred) | Patch damaged monolayer (Graphenea / ACS) |
| Gold Touch-Up Pen (≥99.9% purity) | Re-establish broken EM surface continuity |
| Piezo Mesh Patch Kit | Replace localized PVDF zones (TDK-compatible) |
| Loctite EA 9460 / 3M 2216 | Edge rebonding or internal crack sealing |
| Silicone-Ceramic Damping Resin (Elastosil) | Core injection into micro-fractured layer |
| Sealant: Dow Corning 730 or equivalent | Final perimeter water/thermal barrier |

---

## 🧰 Repair Procedure Summary

### 🔧 Minor Surface Damage (Gold or Graphene Only)
1. Clean damaged zone with IPA or mild plasma brush
2. Apply pre-cut graphene patch over hole or crack
3. Vapor-deposit or pen-touch gold line to reconnect surface EM continuity
4. Re-test with probe: continuity and amplitude restoration required

---

### 🔧 PVDF Lead Repair
1. Identify broken or corroded terminal
2. Cut 2mm of mesh edge and resolder fresh microlead
3. Pot new joint with epoxy and re-seal under thermal insulator patch
4. Verify harmonic output at 3/6/9 Hz with signal generator

---

### 🔧 Damping Matrix Refill (Microfracture / Bubble Intrusion)
1. Drill 1mm access port at edge of delaminated zone
2. Inject Elastosil RT 625 using fine syringe under vacuum assist
3. Seal hole with epoxy cap and gold-patch if surface layer disturbed
4. Allow 24h cure at ambient or 2h at 60°C

---

## 🔁 Retuning Post-Repair

1. Inject signal at 3 Hz → Measure FFT dip amplitude  
2. Repeat for 6 Hz and 9 Hz  
3. If resonance cancellation <90% of baseline, **adjust waveform amplitude** or **replace mesh**  
4. Log new values into panel’s calibration file

---

## ✅ Pass Criteria After Repair

| Property | Min Spec |
|----------|----------|
| Conductivity Restored | >90% of pre-damage value |
| PVDF Impedance | Within ±10% of baseline |
| Vibration Phase Shift | ≤ ±15° from original |
| FFT Peak Damping | ≥ 10dB drop at each harmonic |
| Thermal Expansion | No edge lift after 2x thermal cycle |

---

## 📎 Certification Post Repair

- Repair Date: ___  
- Technician ID: ___  
- Retuning Verified: [✓]  
- Logged in: `/logs/PanelSerial#___-Repair.log`  

---

## 🧠 Summary

This protocol ensures:
- IX-Thaed-Armor remains field-ready under stress  
- Full harmonic function is recoverable  
- Graphene and gold can be patched without total panel replacement  
- All materials used are non-toxic, commercially available, and fully legal to deploy

**Protective systems are only useful if they can heal. This one can.**
