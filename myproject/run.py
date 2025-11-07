import matplotlib.pyplot as plt
import numpy as np
from signals import *
from signaloperations import *

# properties of the signal
duration = 2.0      
sample_rate = 1000  
frequency = 5.0 
step_time = 1.0  

t, signal = sine_wave(frequency, duration, sample_rate)

# Array of time values 
t = np.linspace(0, duration, len(signal))

# Plot 1: Original Sine Wave
plt.subplot(2, 2, 1)
plt.plot(t, signal)
plt.title('Original Wave')
plt.grid(True)

# Apply operations to sine signal only
amplified_wave = amplify(signal, factor=2)
shifted_wave = time_shift(signal, shift_seconds=0.5, sample_rate=sample_rate)

# Plot 2: Amplified Sine Wave
plt.subplot(2, 2, 2)
plt.plot(t, amplified_wave)
plt.title('Amplified Wave')
plt.grid(True)

# Plot 3: Time-Shifted Sine Wave
plt.subplot(2, 2, 3)
plt.plot(t, shifted_wave)
plt.title('Time-Shifted Wave')
plt.grid(True)

plt.tight_layout()
plt.show()