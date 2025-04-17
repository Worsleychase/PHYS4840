"""
Compare Fourier Transform Implementations
PHYS 4840 - Minimal benchmarking
"""

import numpy as np
import time
import matplotlib.pyplot as plt
import fourier_transform as ft

def compare_speeds():
    sizes = [2, 4, 6, 8, 16, 32, 64, 128, 256, 512, 1024]
    times_dft = []
    times_radix2 = []
    times_bluestein = []
    times_zeropad = []
    times_numpy = []

    for N in sizes:
        x = np.random.rand(N)

        if N & (N - 1) != 0:
            next_pow2 = 1 << (N - 1).bit_length() 
            x_padded = np.pad(x, (0, next_pow2 - N), mode='constant')
        else:
            x_padded = x

        start = time.time()
        ft.dft(x)
        times_dft.append(time.time() - start)

        start = time.time()
        ft.fft_ct(x_padded)
        times_radix2.append(time.time() - start)

        start = time.time()
        ft.fft_bluestein(x)
        times_bluestein.append(time.time() - start)

        start = time.time()
        ft.fft_zeropad(x)
        times_zeropad.append(time.time() - start)

        start = time.time()
        np.fft.fft(x)
        times_numpy.append(time.time() - start)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_dft, label='DFT', marker='o')
    plt.plot(sizes, times_radix2, label='FFT Radix-2', marker='o')
    plt.plot(sizes, times_bluestein, label='Bluestein FFT', marker='o')
    plt.plot(sizes, times_zeropad, label='Zero-padded FFT', marker='o')
    plt.plot(sizes, times_numpy, label='NumPy FFT', marker='o')
    plt.xlabel('Signal Size (N)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Fourier Transform Implementations Timing')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    compare_speeds()