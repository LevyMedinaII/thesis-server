import numpy as np
import pandas as pd

B0 = 4.3977
B1 = -5.3746
B2 = 9.6426
average_error = 0

mestimates = []
errors = []
ave_error = 0

for index, xrow in X.iterrows():
    mest = (B1 * xrow['PGA (g)']) + (B2 * xrow['PGD (cm)']) + B0
    mestimates.append(mest)
    
for index in range(0, len(y)):
    current_error =  abs(((mestimates[index] - y[index])/y[index])*100)
    errors.append(current_error)
    
from numpy import array
average_error = array(errors).mean()

print(average_error)