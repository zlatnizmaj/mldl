#!/usr/bin/python
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DIST_FILE_NAME = os.path.splitext(__file__)[0] + '.csv'
N_SIGMA = 0.15

# input vector x
X = np.random.rand(100)
X.sort()
# output vector Y=2pi * X
Y = np.sin(2 * np.pi * X)
# make noise by normal distribution: mu = y
Y += N_SIGMA * np.random.randn(Y.shape[0])

# build DataFrame
df = pd.DataFrame(data=Y, index=X, columns=['y'])
# write down to CSV file
df.to_csv(DIST_FILE_NAME, header=False)
print('... sin(2*pi) data ...')

# plot
df.plot(legend=False, marker='o', color='g', mec='b', mfc='w')
plt.xlabel('x'); plt.ylabel('y'); plt.show()
