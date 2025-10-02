import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    
    num_samples = int(duration * sample_rate)
    
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    sine_wave = np.sin(2 * np.pi * frequency * t)
    
    return sine_wave
