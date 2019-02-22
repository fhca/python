__author__ = 'fhca'

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.01)
y = np.log(x)

plt.figure()
plt.plot(x, y, color=(.5, .2, .1))
plt.show()
