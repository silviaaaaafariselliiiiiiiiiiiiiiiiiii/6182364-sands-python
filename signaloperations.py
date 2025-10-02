import numpy as np
import matplotlib.pyplot as plt

def custom_triangular_wave(t, frequency=1, amplitude=1, phase=0, symmetry=0.5):
    """
    Generate a customizable triangular wave
    t: time array
    frequency: frequency in Hz
    amplitude: peak amplitude
    phase: phase shift in radians
    symmetry: duty cycle (0 to 1)
    """
    # Angular frequency
    omega = 2 * np.pi * frequency
    
    # Phase shifted time
    t_shifted = omega * t + phase
    
    # Normalize to [0, 1]
    normalized = (t_shifted % (2 * np.pi)) / (2 * np.pi)
    
    # Create asymmetric triangular wave
    wave = np.where(normalized < symmetry, 
                   (amplitude / symmetry) * normalized,
                   amplitude * (1 - (normalized - symmetry) / (1 - symmetry)))
    
    return 2 * wave - amplitude  # Center around 0

# Generate time array
t = np.linspace(0, 5, 1000)

# Generate different triangular waves
tri1 = custom_triangular_wave(t, frequency=1, amplitude=2, symmetry=0.5)
tri2 = custom_triangular_wave(t, frequency=2, amplitude=1.5, symmetry=0.3)
tri3 = custom_triangular_wave(t, frequency=0.5, amplitude=1, symmetry=0.7)

# Plot multiple signals
plt.figure(figsize=(8, 8))

plt.subplot(3, 1, 1)
plt.plot(t, tri1, 'b-', linewidth=2)
plt.title('Symmetric Triangular Wave')
plt.ylabel('Amplitude')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()