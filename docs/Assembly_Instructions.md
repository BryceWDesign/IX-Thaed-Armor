# IX-Thaed-Armor – Assembly Instructions  
**Build Version:** v1.0 (Maritime-Grade)  
**Unit Size:** 1 ft x 1 ft panel  
**Objective:** Assemble a functional, vibration-damping, field-tuned armor tile using verified real-world components listed in the project BOM.

---

## 🧰 Tools & Equipment Required

| Tool | Purpose |
|------|---------|
| Graphene transfer station or hot plate | For detaching monolayer graphene from copper or transfer film |
| Cleanroom tweezers (plastic or ceramic tip) | Graphene handling |
| Sputter coater or thermal evaporator | Gold + seed layer deposition |
| Silicone casting mold (1 ft x 1 ft, 0.2” depth) | Damping matrix mold |
| Vacuum desiccator or degassing chamber | Bubble removal during silicone cure |
| Piezo amplifier / signal generator | PVDF mesh tuning |
| Multimeter / continuity tester | Layer conductivity verification |
| Adhesive roller or vacuum laminator | Bonding thin layers cleanly |
| Nitrile gloves, IPA wipes | Cleanroom protocol for anti-contamination |

---

## 🧱 Layer Stack Construction (Top → Bottom)

### **Step 1: Prepare Base Substrate**
1. Select **carbon-titanium composite** (or h-BN sheet for orbital use)
2. Clean with isopropyl alcohol, dry using filtered air
3. Lightly sand bonding side (600 grit), wipe again

---

### **Step 2: Cast Damping Matrix Core (0.2”)**
1. Mix **silicone-ceramic viscoelastic compound** per manufacturer ratio (e.g., Elastosil RT 625)
2. Pour into flat 1 ft² casting mold (depth: 0.2")
3. Use **vacuum chamber** to degas bubbles (15–30 minutes)
4. Place **PVDF piezoelectric mesh** centered within silicone while still uncured
5. Ensure mesh edges are accessible for electrode connection
6. Let cure 24 hrs at room temp or 2 hrs @ 60°C
7. Remove from mold and trim to exact square

---

### **Step 3: Attach Core to Substrate**
1. Apply thin layer of marine-grade epoxy (Loctite EA 9460)
2. Press cured damping matrix onto prepared baseplate
3. Apply uniform weight or vacuum lamination for even bonding
4. Cure per epoxy specs (~24 hrs ambient)

---

### **Step 4: Transfer Graphene Layer**
1. Use pre-transferred graphene-on-PET or wet transfer monolayer graphene
2. Carefully align and lay onto top of damping matrix
3. If using PMMA-protected graphene:
   - Bake at 90–100°C to improve adhesion
   - Use acetone vapor to remove PMMA layer
   - Rinse with IPA and dry in clean air stream
4. Do **not** stretch or crease

---

### **Step 5: Gold + Seed Layer Deposition**
1. Apply **5–10nm Ti or Cr seed layer** using sputter coater or evaporator
2. Follow with **~50nm gold vapor deposition**
3. Mask off areas where conductive edge contacts are needed
4. Allow cooling before handling

---

### **Step 6: Connect PVDF Electrodes**
1. Solder low-profile micro-wires to PVDF mesh pads (outer edges)
2. Route to amplifier or signal generator terminals
3. Test continuity; resistance should match expected piezo curve (~100–300 Ω range)

---

### **Step 7: Final Lamination & Environmental Sealing**
1. Optionally add rear CNT or copper foil shield (for EMI protection)
2. Laminate full panel edge-to-edge using heat/pressure or structural adhesive
3. Apply marine-grade or orbital-safe sealant to all seams
4. Final wipe-down with clean IPA under filtered hood

---

## ⚡ Tuning Instructions

1. Connect PVDF mesh to **AD9833 or similar waveform generator**
2. Set signal to sinusoidal pulse at:
   - 3 Hz for baseline harmonic
   - 6 Hz and 9 Hz as secondary harmonics
3. Measure resonant response with laser vibrometer or oscilloscope (if available)
4. Lock in frequency sweep mode for active field-cancellation operation

---

## ✅ Quality Control Checklist

| Test | Target Outcome |
|------|----------------|
| Graphene conductivity | ≥ 1×10⁸ S/m |
| Gold surface uniformity | ≤ 5% variation (via profilometer) |
| PVDF output @ 9 Hz | ≥ 40 pC/N |
| Adhesion (pull test) | > 5 MPa |
| Flexural test | No delamination under 10° bend |
| Thermal cycling | No cracking after -40°C to 80°C, 20x cycles |

---

## ⚠️ Notes

- This system is **non-weaponized**, **non-kinetic**, and designed for **peaceful protection only**
- When used in ship hull cladding, install panels using isolation rails or bonded mounts with expansion joints every 3 ft²
- In orbital conditions, bakeout to ≤1% outgassing mass loss is required

---

## 🧠 Summary

You now have a **real-world, buildable, vibration-damping, graphene-gold composite armor panel**, tunable via Tesla’s 3-6-9 harmonic logic, designed to save ships and sea life — and built entirely from open-source science and materials.

