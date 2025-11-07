import numpy as np
from scipy import signal

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
    t:numpy.ndarray
        Time values in seconds
    """
    if duration < 0:
        return np.array([]), np.array([])
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    sine_wave = np.sin(2 * np.pi * frequency * t)
    
    return t, sine_wave

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
    t:numpy.ndarray
        Time values in seconds
    """
    if duration < 0:
        return np.array([]), np.array([])
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    sawtooth_wave = signal.sawtooth(2 * np.pi * frequency * t)
    
    return t, sawtooth_wave

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
    t:numpy.ndarray
        Time values in seconds
     """
    if duration < 0:
        return np.array([]), np.array([])
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    triangular_wave = signal.sawtooth(2 * np.pi * frequency * t, 0.5)
    
    return t, triangular_wave

def square_wave(frequency, duration, sample_rate):
     """
    Generate a square wave signal with the parameters:
    
    Parameters:
    frequency : float
        Frequency of the square wave in Hertz (Hz)
    duration : float
        Duration of the signal in seconds
    sample_rate : int
        Sampling rate in samples per second (Hz)
    
    Returns:
    numpy.ndarray
        Array containing the square wave samples
    t:numpy.ndarray
        Time values in seconds 
    """
     if duration < 0:
        return np.array([]), np.array([])
     num_samples = int(duration * sample_rate)
     t = np.linspace(0, duration, num_samples, endpoint=False)
     square_wave = np.sign(2 * np.pi * frequency * t)
     
     return t, square_wave

def unit_step(duration, sample_rate, step_time, amplitude = 1):
    """"
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
        Array containing the unit step signal samples
    t:numpy.ndarray
        Time values in seconds
    """
    if duration < 0:
        return np.array([]), np.array([])
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    unit_step = np.where(t >= step_time, amplitude, 0)
    
    return t, unit_step
