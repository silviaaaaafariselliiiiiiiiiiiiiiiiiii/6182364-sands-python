import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    sine_wave = np.sin(2 * np.pi * frequency * t)
    
    return sine_wave

def generate_sawtooth_wave(frequency, duration, sample_rate):
    
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    phase = (t * frequency) % 1.0  # Phase from 0 to 1
    sawtooth_wave = 2 * phase - 1  # Scale from -1 to 1
    
    return sawtooth_wave

def generate_triangle_wave(frequency, duration, sample_rate):
    
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    phase = (t * frequency) % 1.0  # Phase from 0 to 1
    
    triangle_wave = np.where(phase < 0.5, 
                            4 * phase - 1,      # Rise from -1 to 1
                            -4 * phase + 3)     # Fall from 1 to -1
    
    return triangle_wave