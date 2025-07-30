# IX-Thaed-Armor — Full Bill of Materials (BOM)  
**Version:** 1.0  
**Author:** Bryce Wooster  
**Purpose:** Provide a complete list of real, buyable components required to build a 1ft x 1ft operational unit of IX-Thaed-Armor for maritime and orbital safety applications.

---

## ⚙️ MATERIAL STACK OVERVIEW

| Layer | Material | Specs | Qty per 1ft² | Vendor Example |
|-------|----------|-------|---------------|----------------|
| **1** | Monolayer Graphene Sheet | CVD-grown, copper-backed or transferred | 1 sheet (12"x12") | Graphenea, ACS Materials |
| **2** | Gold Plating (Vapor or Sputter Coated) | ≥99.99% pure Au, ~50nm thick | 1 gold vapor deposition session | Sigma-Aldrich, Kurt J. Lesker |
| **3** | Titanium (Ti) or Chromium (Cr) Seed Layer | 5–10nm adhesion layer for gold | 1 layer | AdNano, Evochem |
| **4** | PVDF Piezoelectric Mesh | ~50μm thick, stretchable, patternable | 1 mesh sheet (12"x12") | Measurement Specialties, TDK |
| **5** | Damping Matrix (Core Layer) | Silicone-ceramic blend, viscoelastic | 0.2" (5mm) thickness, 1 layer | Elastosil RT 625, Momentive RTV |
| **6** | Substrate: Carbon-Titanium Composite or h-BN Panel | Marine or orbital baseplate | 1 ft² panel | Toray Advanced Composites, Goodfellow, Momentive |
| **7** | Copper or CNT Termination Layer (optional) | Edge wrapping or rear shield | Optional | Nanocomposix, Cheap Tubes Inc. |

---

## 🛠️ INTEGRATED COMPONENTS

| Component | Description | Vendor / Model |
|----------|-------------|----------------|
| **Piezo Amplifier Driver (Tuning Circuit)** | Drives PVDF at 3, 6, 9 Hz harmonics | Analog Devices AD9833 or Siglent SDG1032X |
| **Tesla Harmonic Waveform Generator (Low-Freq Synth)** | Used for tuning resonance matching | Arduino Nano + AD9850 module + amplifier |
| **Graphene Transfer Kit (if copper foil base)** | Used to move graphene to target substrate | Graphenea transfer kit or wet-transfer manual |
| **Thermal Isolation Tape (for orbital)** | Prevents delamination at temp extremes | Kapton tape or aerogel gasket strips |
| **Marine-Grade Epoxy or Adhesive Layer** | Binds damping matrix to substrate | 3M 2216 B/A Gray, Loctite EA 9460 |

---

## 🧪 MATERIAL PROPERTIES SUMMARY (Per Layer)

| Layer | Tensile Strength | Electrical Conductivity | Thermal Conductivity |
|-------|------------------|--------------------------|----------------------|
| Graphene | ~130 GPa | ~1×10⁸ S/m | ~5,000 W/m·K |
| Gold Layer | ~120 MPa (thin film) | ~4.1×10⁷ S/m | ~318 W/m·K |
| PVDF Mesh | N/A (flexible) | Piezo response ~20–40 pC/N | N/A |
| Silicone-Ceramic Damping | ~6–12 MPa | Insulator | ~0.2–0.4 W/m·K |
| Substrate (Carbon-Ti) | ~500–900 MPa | Optional conductor | 5–12 W/m·K |

---

## 🧾 SUGGESTED VENDORS

- **Graphenea:** [https://graphenea.com](https://graphenea.com) (Graphene sheets, transfer kits)  
- **ACS Materials:** [https://www.acsmaterials.com](https://www.acsmaterials.com) (CNT, MXene, h-BN)  
- **TDK, Digikey:** (PVDF mesh, piezo components)  
- **Momentive, Elastosil, 3M:** (Damping matrix, adhesives)  
- **Kurt J. Lesker / Sigma-Aldrich:** (Gold deposition materials)  
- **Toray / Goodfellow:** (Carbon-titanium substrates)

---

## 🧠 TUNING NOTES

- PVDF piezo mesh must be driven at **Tesla harmonic nodes**:
  - ƒ₁ = 3 Hz  
  - ƒ₂ = 6 Hz  
  - ƒ₃ = 9 Hz  
  - ƒₙ = 3n Hz, where n = 1–10 for marine, 1–30 for orbital

- Gold must be sputtered over a titanium or chromium adhesion seed layer (5–10 nm)  
- Graphene should be protected with transfer polymer during lamination (PVA, PMMA)  
- All adhesives must be tested for outgassing if used in orbital configurations

---

## 📌 Final Notes

This BOM represents a **real-world, fully functional materials stack** for IX-Thaed-Armor v1.0.  
All components are available from commercial or academic suppliers.  
No ITAR, EAR, or proprietary material restrictions exist in this stack.

System designed to **save lives**, **shield sea life**, and **resist catastrophic mechanical failure**.

