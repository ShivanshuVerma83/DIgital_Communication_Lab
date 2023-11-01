import numpy.random as nr
import numpy as np

# Generate a single Gaussian random variable with mean 0 and standard deviation 1
print(nr.normal())

# Generate a single Gaussian random variable with mean 1 and standard deviation 1
b = nr.normal(1, 1, 1)
print(b)

# Generate a 2x2 array of Gaussian random variables with mean 3 and standard deviation 5^0.5
c = []
for i in range(2):
    k = []
    for j in range(2):
        k.append(nr.normal(3, 5**0.5, 1))
    c.append(k)
print(c)

# Generate white Gaussian noise
# Generate a uniform random variable between 2 and 5, repeated 5 times
d = nr.uniform(2, 5, 5)
print(d)

# Generate random integers between 0 and 4, repeated 5 times
e = nr.randint(4, size=5)

# Generate a random sequence of 1s and 0s of length 7
f = nr.randint(0, 2, size=7)
print(f)

# Generate BPSK symbols with amplitude A=5
A = 5
g = nr.randint(0, 2, size=10)
h = [1*A if i == 0 else i*(-A) for i in g]
print(h)

# Alternative way to generate BPSK symbols using array operations
bpsk_symbols = 2 * g - 1
i = A * bpsk_symbols
print(i)

# Generate Additive White Gaussian Noise (AWGN)
snr_db = 10  # Signal-to-Noise Ratio in dB
snr = 10 ** (snr_db / 10.0)  # Convert SNR from dB to linear scale
noise_power = A**2 / (2 * snr)  # Calculate noise power based on SNR
awgn = np.random.normal(0, np.sqrt(noise_power), len(i))
received_symbols = i + awgn
print(received_symbols)




