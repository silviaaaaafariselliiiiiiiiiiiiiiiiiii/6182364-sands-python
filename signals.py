import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    """
    Generate a sine wave signal.
    
    Parameters:
    frequency (float): Frequency of the sine wave in Hz
    duration (float): Duration of the signal in seconds
    sample_rate (int): Sampling rate in samples per second
    
    Returns:
    numpy.ndarray: Array containing the sine wave samples
    """
    # Calculate the number of samples
    num_samples = int(duration * sample_rate)
    
    # Create time array
    t = np.linspace(0, duration, num_samples, endpoint=False)
    
    # Generate sine wave
    sine_wave = np.sin(2 * np.pi * frequency * t)
    
    return sine_wave
