import numpy as np
from signals import *
from signaloperations import *

def test_signal_generation():
    """Test all signal generation functions using assert"""
    
    duration = 2.0
    sample_rate = 100
    frequency = 2
    
    # Test sine wave
    sine = sine_wave(frequency, duration, sample_rate)
    assert len(sine) == 200, "Sine wave wrong length"
    assert sine.min() >= -1.0, "Sine wave min value too low"
    assert sine.max() <= 1.0, "Sine wave max value too high"
    print("Sine wave test passed")
    
    # Test sawtooth wave
    sawtooth = sawtooth_wave(frequency, duration, sample_rate)
    assert len(sawtooth) == 200, "Sawtooth wave wrong length"
    assert sawtooth.min() >= -1.0, "Sawtooth min value too low"
    assert sawtooth.max() <= 1.0, "Sawtooth max value too high"
    print("Sawtooth wave test passed")
    
    # Test triangular wave
    triangle = triangular_wave(frequency, duration, sample_rate)
    assert len(triangle) == 200, "Triangular wave wrong length"
    assert triangle.min() >= -1.0, "Triangle min value too low"
    assert triangle.max() <= 1.0, "Triangle max value too high"
    print("Triangular wave test passed")
    
    # Test square wave
    square = square_wave(frequency, duration, sample_rate)
    assert len(square) == 200, "Square wave wrong length"
    assert square.min() == -1, "Square wave min value wrong"
    assert square.max() == 1, "Square wave max value wrong"
    print("Square wave test passed")
    
    # Test unit step
    step = unit_step(duration, sample_rate, step_time=1.0)
    assert len(step) == 200, "Unit step wrong length"
    assert step.min() == 0, "Unit step min value wrong"
    assert step.max() == 1, "Unit step max value wrong"
    print("Unit step test passed")

def test_signal_operations():
    """Test all signal operation functions using assert"""
    
    duration = 2.0
    sample_rate = 100
    frequency = 2
    
    # Create test signals
    test_signal = sine_wave(frequency, duration, sample_rate)
    signal1 = sine_wave(1, duration, sample_rate)
    signal2 = sine_wave(5, duration, sample_rate)
    
    # Test amplify
    amplified = amplify(test_signal, factor=2.0)
    assert len(amplified) == len(test_signal), "Amplify changed signal length"
    assert amplified.max() > test_signal.max(), "Amplify didn't increase amplitude"
    print("Amplify test passed")
    
    # Test time shift
    shifted = time_shift(test_signal, shift_seconds=0.5, sample_rate=sample_rate)
    assert len(shifted) == len(test_signal), "Time shift changed signal length"
    print("Time shift test passed")
    
    # Test add signals
    added = add_signals(signal1, signal2)
    assert len(added) == len(signal1), "Add signals changed length"
    print("Add signals test passed")
    
    # Test multiply signals
    multiplied = multiply_signals(signal1, signal2)
    assert len(multiplied) == len(signal1), "Multiply signals changed length"
    print("Multiply signals test passed")
    
    # Test convolve signals
    convolved = convolve_signals(signal1, signal2)
    assert len(convolved) == len(signal1), "Convolve signals changed length"
    print("Convolve signals test passed")
