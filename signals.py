import numpy as np

def sine_wave(frequency, duration, sample_rate):
    """
    Generate a sine wave signal with the parameters:
    
    Parameters:
    frequency : float
        Frequency of the sine wave in Hertz (Hz)
    duration : float
        Duration of the signal in seconds
    sample_rate : int
        Sampling rate in samples per second (Hz)
    
    Returns:
    numpy.ndarray
        Array containing the sine wave samples ranging from -1 to 1
    """
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    sine_wave = np.sin(2 * np.pi * frequency * t)
    
    return sine_wave

def sawtooth_wave(frequency, duration, sample_rate):
    """
    Generate a sawtooth wave signal with the parameters:
    
    Parameters:
    frequency : float
        Frequency of the sawtooth wave in Hertz (Hz)
    duration : float
        Duration of the signal in seconds
    sample_rate : int
        Sampling rate in samples per second (Hz)
    
    Returns:
    numpy.ndarray
        Array containing the sawtooth wave samples ranging from -1 to 1
    """
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    phase = (t * frequency) % 1.0  # Phase from 0 to 1
    sawtooth_wave = 2 * phase - 1  # Scale from -1 to 1
    
    return sawtooth_wave

def triangular_wave(frequency, duration, sample_rate):
    """
    Generate a triangular wave signal with the parameters:
    
    Parameters:
    frequency : float
        Frequency of the triangular wave in Hertz (Hz)
    duration : float
        Duration of the signal in seconds
    sample_rate : int
        Sampling rate in samples per second (Hz)
    
    Returns:
    numpy.ndarray
        Array containing the triangular wave samples ranging from -1 to 1
        The wave rises linearly from -1 to 1 during the first half of the period
        and falls linearly from 1 to -1 during the second half
    """
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    phase = (t * frequency) % 1.0  # Phase from 0 to 1
    
    triangle_wave = np.where(phase < 0.5, 
                            4 * phase - 1,      # Rise from -1 to 1
                            -4 * phase + 3)     # Fall from 1 to -1
    
    return triangle_wave

def square_wave(frequency, duration, sample_rate, duty_cycle=0.5):
     """
    Generate a square wave signal with the parameters:
    
    Parameters:
    frequency : float
        Frequency of the square wave in Hertz (Hz)
    duration : float
        Duration of the signal in seconds
    sample_rate : int
        Sampling rate in samples per second (Hz)
    duty_cycle : float, optional
        Duty cycle of the square wave (0.0 to 1.0), where 0.5 represents 
        equal time high and low. Default is 0.5.
    
    Returns:
    numpy.ndarray
        Array containing the square wave samples with values of 1 (high) 
        and -1 (low) based on the duty cycle
    """
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    phase = (t * frequency) % 1.0
    square_wave = np.where(phase < duty_cycle, 1, -1)
    
    return square_wave

def unit_step(duration, sample_rate, step_time=0.5, amplitude=1.0):
"""
    Generate a unit step (Heaviside) signal with the parameters:
    
    Parameters:
    duration : float
        Duration of the signal in seconds
    sample_rate : int
        Sampling rate in samples per second (Hz)
    step_time : float, optional
        Time in seconds when the step occurs. Default is 0.5 seconds
    amplitude : float, optional
        Amplitude of the step signal after the step time. Default is 1.0
    
    Returns:
    numpy.ndarray
        Array containing the unit step signal samples. The signal has value 0
        before step_time and the specified amplitude after step_time.
    """
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    unit_step = np.where(t >= step_time, amplitude, 0)
    
    return unit_step
