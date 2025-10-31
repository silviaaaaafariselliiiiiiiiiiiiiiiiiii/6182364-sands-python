import numpy as np

#scale the signal by a certain factor
def amplify(signal, factor): 
    """
    Scales the amplitude of a signal by a given factor.
    
    Parameters:
        signal: Input signal array
        factor: Scaling factor 

    Returns:
        Scaled signal array
    """
    return signal * factor
    
#shift the signal by a certain time
def time_shift(signal, shift_seconds, sample_rate): 
    """
    Shifts a signal in time by a specified duration.
    
    Parameters:
        signal: Input signal array
        shift_seconds: Time shift in seconds 
        sample_rate: Sampling rate in Hz
    
    Returns:
        Time-shifted signal array
    """
    shift_amount = int(shift_seconds * sample_rate)
    return np.roll(signal, shift_amount)

#addition among signals
def add_signals(signal1, signal2):
    """
    Performs addition of two signals.
    
    Parameters:
        signal1: First input signal array
        signal2: Second input signal array
    
    Returns:
        Sum of the two signals
    """
    return signal1 + signal2

#multiplication among signals
def multiply_signals(signal1, signal2):
    """
    Performs multiplication of two signals.
    
    Parameters:
        signal1: First input signal array
        signal2: Second input signal array
    
    Returns:
        Product of the two signals
    """
    return signal1 * signal2

#convolve two signals
def convolve_signals(signal1, signal2):
    """
    Computes the convolution of two signals.
    
    Parameters:
        signal1: First input signal array
        signal2: Second input signal array
    
    Returns:
        Convolved signal with same length as input signals
    """
    return np.convolve(signal1, signal2, mode='same')