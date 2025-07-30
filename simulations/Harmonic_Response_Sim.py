"""
IX-Thaed-Armor Harmonic Response Simulation
Simulates PVDF piezoelectric layer's resonant output under Tesla 3-6-9 harmonic drive.
Author: Bryce Wooster
Date: 2025
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
sample_rate = 1000  # Hz
duration = 5  # seconds
time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Frequencies tuned to Tesla's 3-6-9 harmonic logic
harmonics = [3, 6, 9, 18, 27]  # Hz

# Simulate PVDF voltage response (idealized sine wave outputs)
def simulate_pvdf_response(freqs, amplitude=1.0):
    response = np.zeros_like(time)
    for f in freqs:
        response += amplitude * np.sin(2 * np.pi * f * time)
    return response

# Generate the response signal
pvdf_output = simulate_pvdf_response(harmonics, amplitude=1.0)

# Visualization
plt.figure(figsize=(10, 5))
plt.plot(time, pvdf_output, label='PVDF Harmonic Output', color='mediumblue')
plt.title("IX-Thaed-Armor: Simulated PVDF Output Under Tesla 3-6-9 Harmonics")
plt.xlabel("Time (s)")
plt.ylabel("Voltage Output (a.u.)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("simulations/IX-Thaed-Armor_Harmonic_Response.png", dpi=300)
plt.show()
