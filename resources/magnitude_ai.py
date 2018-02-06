%matplotlib inline
import numpy as np
import pandas as pd
#import statsmodels.api as sm
#from sklearn.preprocessing import StandardScaler

df = pd.read_excel('C:/Levy Courses and Lectures/Non-Levy Files/NGA_West2_Flatfile_RotD50_d200_public_version.xlsx')

scale = StandardScaler()

X = df[['PGA (g)', 'PGD (cm)']]
y = df['Earthquake Magnitude']

X[['PGA (g)', 'PGD (cm)']] = scale.fit_transform(X[['PGA (g)', 'PGD (cm)']].as_matrix())
X = sm.add_constant(X)
                    
print (X)
est = sm.OLS(y, X).fit()

#est.summary()

#Code above this line are the added ones.

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