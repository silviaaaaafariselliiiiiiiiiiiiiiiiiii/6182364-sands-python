import numpy as np

def amplify(signal, factor):
    return signal * factor

def time_shift(signal, shift_seconds, sample_rate):
    shift_amount = int(shift_seconds * sample_rate)
    return np.roll(signal, shift_amount)

def add_signals(signal1, signal2):
    return signal1 + signal2

def multiply_signals(signal1, signal2):
    return signal1 * signal2

def reverse_signal(signal):
    return signal[::-1]