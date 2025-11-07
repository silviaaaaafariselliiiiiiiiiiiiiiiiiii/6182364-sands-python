import numpy as np
from signals import *
from signaloperations import *


def test_sine_wave():
    """
    Test the create_sine_signal function with various test cases.
    
    Tests include:
    - Signal length verification
    - Initial value check
    - Amplitude validation
    - Error handling for invalid duration
    - Zero amplitude case
    """
    t,sine = sine_wave(1, 10, 1000)
    assert len(t) == 10000
    assert sine[0] == 0

    t,sine = sine_wave(1, 10, 1000)
    assert np.isclose(max(sine),1,atol=1e-2)

    t,sine = sine_wave(1, -1, 1000)
    assert len(t) == 0 and len(sine) == 0
def test_sawtooth_wave():
    """
    Test sawtooth_wave function with test cases:
    
    - Length verification
    - Initial value check
    - Amplitude validation
    - Invalid duration error handling 
    - Zero amplitude check
    """
    t, sawtooth = sawtooth_wave(1, 2, 1000)
    assert len(sawtooth) == 2000
    assert np.isclose(sawtooth[0], -1, atol=1e-10)

    t, sawtooth = sawtooth_wave(1, 2, 1000)
    assert np.isclose(max(sawtooth), 1, atol=1e-2)

    t, sawtooth = sawtooth_wave(1, -1, 1000)
    assert len(sawtooth) == 0 and len(t) == 0
def test_triangular_wave():
    """
    Test triangular_wave function with test cases:
    
    - Length verification
    - Initial value check
    - Amplitude validation
    - Invalid duration error handling 
    - Zero amplitude check
    """
    t, triangle = triangular_wave(1, 2, 1000)
    assert len(triangle) == 2000
    assert np.isclose(triangle[0], -1, atol=1e-10)

    t, triangle = triangular_wave(1, 2, 1000)
    assert np.isclose(max(triangle), 1, atol=1e-3)

    t, triangle = triangular_wave(1, -1, 1000)
    assert len(t) == 0

def test_square_wave():
    """
    Test square_wave function with test cases:
    
    - Length verification
    - Initial value check
    - Amplitude validation
    - Invalid duration error handling 
    - Zero amplitude check
    """
    t, square = square_wave(1, 2, 1000)
    assert len(t) == 2000
    assert square[0] == 0  

    t, square = square_wave(1, 2, 100)
    assert np.isclose(max(square), 1, atol=1e-3)

    t, square = square_wave(1, -1, 100)
    assert len(t) == 0

def test_unit_step():
    """
    Test unit_step function with test cases:
    
    - Length verification
    - Initial value check
    - Amplitude validation
    - Invalid duration error handling 
    - Zero amplitude check
    """
    t, step = unit_step(2, 1000, step_time=1.0)
    assert len(step) == 2000
    assert step[0] == 0
    assert step[1000] == 1  # At step_time (1 second * 100 samples/sec)

    t, step = unit_step(2, 100, step_time=1.0, amplitude=3)
    assert np.isclose(max(step), 3, atol=1e-3)

    t, step = unit_step(-1, 100, step_time=1.0)
    assert len(t) == 0

    t, step = unit_step(2, 100, step_time=1.0, amplitude=0)
    assert np.allclose(step, 0)

def test_amplify():
    """
    Test amplify function with test cases:
    
    - Signal length preservation
    - Amplitude scaling check
    - Zero factor case
    - Negative factor case
    """
    t, signal = sine_wave(1, 2, 100)
    
    scaled_signal = amplify(signal, 2)
    assert np.array_equal(scaled_signal, signal * 2)

    scaled_signal = amplify(signal, -1)
    assert np.array_equal(scaled_signal, signal * -1)

    scaled_signal = amplify(signal, 0)
    assert np.allclose(scaled_signal, 0)

def test_time_shift():
    """
    Test time_shift function with test cases:
    
    - Signal length preservation
    - Positive shift check
    - Negative shift check
    - Zero shift case
    """
    t, signal = sine_wave(1, 2, 100)
    
    shifted = time_shift(signal, shift_seconds=0.5, sample_rate=100)
    assert len(shifted) == len(signal)
    
    shifted = time_shift(signal, shift_seconds=-0.5, sample_rate=100)
    assert len(shifted) == len(signal)
    
    shifted = time_shift(signal, shift_seconds=0.0, sample_rate=100)
    assert np.array_equal(shifted, signal)

def test_add_signals():
    """
    Test add_signals function with test cases:
    
    - Element-wise addition check
    - Different length handling
    - Zero signal addition
    """
    t1, signal1 = sine_wave(1, 2, 100)
    t2, signal2 = sine_wave(2, 2, 100)
    
    added = add_signals(signal1, signal2)
    assert len(added) == min(len(signal1), len(signal2))
    assert np.array_equal(added, signal1 + signal2)
    
    short_signal = signal1[:50]
    added = add_signals(signal1, short_signal)
    assert len(added) == len(short_signal)
    
    zero_signal = np.zeros(10)
    added = add_signals(signal1, zero_signal)
    assert np.array_equal(added, signal1[:10])

def test_multiply_signals():
    """
    Test multiply_signals function with test cases:
    
    - Element-wise multiplication check
    - Different length handling
    - Zero signal multiplication
    """
    t1, signal1 = sine_wave(1, 2, 100)
    t2, signal2 = sine_wave(2, 2, 100)
    
    multiplied = multiply_signals(signal1, signal2)
    assert len(multiplied) == len(signal1)
    assert np.array_equal(multiplied, signal1 * signal2)
    
    short_signal = signal1[:50]
    multiplied = multiply_signals(signal1, short_signal)
    assert len(multiplied) == len(short_signal)
    
    zero_signal = np.zeros(10)
    multiplied = multiply_signals(signal1, zero_signal)
    assert np.allclose(multiplied, 0)
