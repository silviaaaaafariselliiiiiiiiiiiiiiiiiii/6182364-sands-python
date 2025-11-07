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
    length = min(len(signal1),len(signal2))
    return signal1[:length] + signal2[:length]

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
    length = min(len(signal1),len(signal2))
    return signal1[:length] * signal2[:length]
