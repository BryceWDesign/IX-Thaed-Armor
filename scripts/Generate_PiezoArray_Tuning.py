"""
IX-Thaed-Armor: Tesla 3-6-9 Harmonic Drive Signal Generator
Generates sine waveforms for 3 Hz, 6 Hz, 9 Hz, and their harmonics.
Intended for DAC or microcontroller output to PVDF mesh.
Author: Bryce Wooster
Date: 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

# Settings
duration = 10  # seconds
sample_rate = 44100  # Hz for microcontroller-compatible DAC

# Harmonic frequencies (Tesla set)
frequencies = [3, 6, 9, 18, 27]  # Hz
amplitudes = [0.5, 0.3, 0.3, 0.2, 0.1]  # Tuned gain weights

# Generate waveform
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
signal = np.zeros_like(t)

for f, a in zip(frequencies, amplitudes):
    signal += a * np.sin(2 * np.pi * f * t)

# Normalize
signal /= np.max(np.abs(signal))

# Optional export to .wav for signal playback or DAC testing
wav.write("scripts/PVDF_369_HarmonicSignal.wav", sample_rate, (signal * 32767).astype(np.int16))

# Plot preview
plt.figure(figsize=(10, 4))
plt.plot(t[0:2000], signal[0:2000])  # Zoomed in to show waveform cycles
plt.title("Tesla 3-6-9 Harmonic Output for PVDF Drive")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("scripts/PVDF_369_HarmonicSignal_Preview.png", dpi=300)
plt.show()
