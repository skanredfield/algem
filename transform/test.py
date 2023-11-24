import numpy as np
import matplotlib.pyplot as plt
import time
from fourier import *

# https://stackoverflow.com/questions/15707056/get-time-of-execution-of-a-block-of-code-in-python-2-7
def time_usage(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        retval = func(*args, **kwargs)
        end_ts = time.time()
        print("Elapsed time: %f" % (end_ts - beg_ts))
        return retval
    return wrapper

N = 1024

freq1 = 13                                        # wave frequency
freq2 = 4                                        # wave frequency
amp = 1.0                                       # wave amplitude
duration = 1.0                                  # wave duration

delta_t = duration / N                          # spacing of time values

tvals = np.linspace(0, (N-1) * delta_t, N)      # sampling values
f_t1 = np.cos(2 * np.pi * freq1 * tvals)          # function to transform
f_t2 = np.cos(2 * np.pi * freq2 * tvals)          # function to transform
f_t = f_t1 + f_t2



delta_f = 1 / (N * delta_t)                     # spacing of frequency values
freqvals = np.linspace(0, (N-1) * delta_f, N)   # output frequency values
freqvals -= (N/2) * delta_f                     # shift half to center on 0 and include the negative values
    



fig, ax = plt.subplots(3, 1)

def plot_time_function():
    ax[0].set_title("f(t)")
    ax[0].set_xlabel("Time (seconds)")
    ax[0].set_ylabel("Amplitude")
    ax[0].plot(tvals, f_t, '.')

@time_usage
def plot_dft():
    ax[1].set_title("dft(f)")
    ax[1].set_xlabel("Frequency")
    ax[1].set_ylabel("Re(dft(f))")
    print("DFT:")
    ax[1].plot(freqvals, fourier_shift(dft_matrix(f_t)), '.')

@time_usage
def plot_fft():
    ax[2].set_title("fft(f)")
    ax[2].set_xlabel("Frequency")
    ax[2].set_ylabel("Re(fft(f))")
    print("FFT:")
    # fft(f_t)
    ax[2].plot(freqvals, fourier_shift(fft(f_t)), '.')

plot_time_function()
plot_dft()
plot_fft()

fig.tight_layout()
plt.show()