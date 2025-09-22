from signals import generate_sine_wave

# Generate sine wave with specified parameters
frequency = 5  # Hz
duration = 2   # seconds
sample_rate = 100  # samples per second

sine_wave = generate_sine_wave(frequency, duration, sample_rate)

# Print the first 10 samples
print("First 10 samples of the sine wave:")
for i in range(10):
    print(f"Sample {i}: {sine_wave[i]:.6f}")
    