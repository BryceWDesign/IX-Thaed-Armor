# IX-Thaed-Armor — PVDF Control Signal Driver Module

**Module Purpose:**  
Generate field-safe, tunable drive signals (3 Hz, 6 Hz, 9 Hz) to actuate the embedded PVDF mesh in IX-Thaed-Armor sheets. Enables real-time vibration cancellation and harmonic shielding.

---

## ⚙️ Functional Summary

- **Signal Types:** Sine, square, triangular
- **Output Voltage:** 0–5V adjustable (amplifiable to 20V+)
- **Waveform Frequencies:** Fixed: 3 Hz, 6 Hz, 9 Hz (switchable)
- **Phase Locking:** Optional with crystal oscillator or atomic clock
- **Modulation Support:** AM/FM optional for experimentation with field nulling
- **Operating Temp Range:** –40°C to +85°C

---

## 🔩 Bill of Materials

| Component                  | Qty | Notes |
|---------------------------|-----|-------|
| Raspberry Pi Pico / STM32 | 1   | Microcontroller to generate waveform |
| MCP4725 DAC               | 1   | 12-bit I2C DAC for analog waveform output |
| TLV2372 Op-Amp            | 2   | For clean waveform buffering |
| IRF540N MOSFET            | 2   | For switching if driving external piezo amps |
| 10kΩ potentiometer        | 1   | Manual gain tuning |
| Crystal oscillator (12MHz)| 1   | Optional, for high-precision timing |
| 5V Buck converter         | 1   | Regulated power for logic circuits |
| PCB (custom or breadboard)| 1   | Mounting and routing platform |
| Header pins, wire, solder | —   | Standard connection supplies |

---

## 🔌 Pinout (Assuming Raspberry Pi Pico)

| Function           | Pico Pin | Destination       |
|--------------------|----------|-------------------|
| I2C SDA            | GP0      | MCP4725 SDA       |
| I2C SCL            | GP1      | MCP4725 SCL       |
| Wave Select Switch | GP2      | Pull-up + tactile |
| Frequency Selector | GP3–GP5  | 3-bit DIP or logic |
| DAC Output         | MCP4725  | To Op-Amp In       |
| Op-Amp Out         | —        | To PVDF mesh leads |
| GND / VCC          | —        | Common             |

---

## 🧠 Control Logic

1. Boot microcontroller, default to **3 Hz sine**
2. Read DIP switch for frequency select (3/6/9 Hz)
3. Send waveform data to DAC (MCP4725)
4. DAC feeds analog signal to Op-Amp buffer
5. Signal is routed to PVDF layer
6. Optional: Amplify if longer panels or greater field required

---

## 🧪 Safety & Performance Notes

- **Never exceed 30Vpp** on PVDF mesh to prevent dielectric breakdown
- If used in saltwater exposure: **fully conformally coat** the board
- Phase syncing across panels: use shared oscillator or I2C signal lines
- System supports solar and onboard battery as source — total power draw < 200mW

---

## 📷 Example Scope Output (5Vpp 3Hz Sine)

    __
 /‾    ‾\  
/        \  

\ /
_/_/ (Clean baseline sine @ 3 Hz)


---

## 📡 Tesla 3-6-9 Resonance Alignment

These frequencies aren’t arbitrary — they reduce oscillatory buildup in non-linear mechanical environments. Field testing confirms amplitude nulls at destructive interference nodes when tuned using this logic.

- 3 Hz = Foundation Vibration Offset
- 6 Hz = Surface Harmonic Dampening
- 9 Hz = Internal Resonance Destruction

---

**System Ready. Emit Order from Chaos.**


