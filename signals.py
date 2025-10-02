import numpy as np

def sine_wave(frequency, duration, sample_rate):
    
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    sine_wave = np.sin(2 * np.pi * frequency * t)
    
    return sine_wave

def sawtooth_wave(frequency, duration, sample_rate):
    
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    phase = (t * frequency) % 1.0  # Phase from 0 to 1
    sawtooth_wave = 2 * phase - 1  # Scale from -1 to 1
    
    return sawtooth_wave

def triangular_wave(frequency, duration, sample_rate):
    
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    phase = (t * frequency) % 1.0  # Phase from 0 to 1
    
    triangle_wave = np.where(phase < 0.5, 
                            4 * phase - 1,      # Rise from -1 to 1
                            -4 * phase + 3)     # Fall from 1 to -1
    
    return triangle_wave

def square_wave(frequency, duration, sample_rate, duty_cycle=0.5):
    
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    phase = (t * frequency) % 1.0
    square_wave = np.where(phase < duty_cycle, 1, -1)
    
    return square_wave

def unit_step(duration, sample_rate, step_time=0.5, amplitude=1.0):

    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    unit_step = np.where(t >= step_time, amplitude, 0)
    
    return unit_step



    