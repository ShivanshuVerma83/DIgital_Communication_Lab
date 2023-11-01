# make a sinusoidal pulse in dc

import numpy as np

import matplotlib.pyplot as plot



time = np.arange(0, 10, 0.1);



amplitude = np.sin(time)


plot.plot(time, amplitude)



plot.title('Sine wave')



plot.xlabel('Time')

# Give y axis label for the sine wave plot

plot.ylabel('Amplitude = sin(time)')

plot.grid(True, which='both')