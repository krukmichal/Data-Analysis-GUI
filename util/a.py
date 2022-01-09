import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

Fs = 2000
tstep = 1 / Fs
f0 = 1

N = int(Fs / f0)


t = np.linspace(0, (N-1)*tstep, N)
fstep = Fs / N
f = np.linspace(0, (N-1)*fstep, N)

y = 1 * np.sin(2 * np.pi * f0 * t)

X = np.fft.fft(y)
X_mag = np.abs(X) / N
print(X_mag)
print(f)

plt.plot(f,X_mag)
plt.show()

