import matplotlib.pyplot as plt
import numpy as np
from signals import *
from signaloperations import *

# properties of the signal
duration = 2.0      
sample_rate = 100  
frequency = 5 
step_time = 1.0  

sine_signal = sine_wave(frequency, duration, sample_rate)

# Array of time values 
t = np.linspace(0, duration, len(sine_signal))

# Plot 1: Original Sine Wave
plt.subplot(2, 2, 1)
plt.plot(t, sine_signal)
plt.title('Original Sine Wave')
plt.grid(True)

# Apply operations to sine signal only
amplified_sine = amplify(sine_signal, factor=2.0)
shifted_sine = time_shift(sine_signal, shift_seconds=0.5, sample_rate=sample_rate)

# Plot 2: Amplified Sine Wave
plt.subplot(2, 2, 2)
plt.plot(t, amplified_sine)
plt.title('Amplified Sine Wave')
plt.grid(True)

# Plot 3: Time-Shifted Sine Wave
plt.subplot(2, 2, 3)
plt.plot(t, shifted_sine)
plt.title('Time-Shifted Sine Wave')
plt.grid(True)

plt.tight_layout()
plt.show()