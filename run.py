import matplotlib.pyplot as plt
import numpy as np
from signals import sine_wave, unit_step

# properties of the signal
duration = 2.0      
sample_rate = 100  
frequency = 5 
step_time = 1.0  

sine_signal = sine_wave(frequency, duration, sample_rate)
step_signal = unit_step(step_time, duration, sample_rate)

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
