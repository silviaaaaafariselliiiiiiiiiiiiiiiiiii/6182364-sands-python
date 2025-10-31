import matplotlib.pyplot as plt
import numpy as np
from signals import sine_wave, unit_step

# properties of the signal
duration = 2.0      
sample_rate = 100   

# Plot sine wave
t = np.linspace(0, duration, len(sine_signal))
plt.figure(figsize=(10, 4))
plt.plot(t, sine_signal)
plt.title(f'Sine Wave: {frequency} Hz, {duration} seconds')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# Plot unit step
plt.figure(figsize=(10, 4))
plt.plot(t, step_signal)
plt.title(f'Unit Step: step at {step_time} seconds')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

plt.tight_layout()
plt.show()