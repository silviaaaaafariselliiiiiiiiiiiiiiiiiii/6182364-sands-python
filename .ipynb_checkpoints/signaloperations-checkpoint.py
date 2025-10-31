import numpy as np

#scale the signal by a certain factor
def amplify(signal, factor): 
    return signal * factor
    
#shift the signal by a certain time
def time_shift(signal, shift_seconds, sample_rate): 
    shift_amount = int(shift_seconds * sample_rate)
    return np.roll(signal, shift_amount)

#addition among signals
def add_signals(signal1, signal2):
    return signal1 + signal2

#multiplication among signals
def multiply_signals(signal1, signal2):
    return signal1 * signal2

#convolve two signals
def convolve_signals(signal1, signal2):
    return np.convolve(signal1, signal2, mode='same')