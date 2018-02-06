import json
import falcon

#Setup
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

print("Starting AI...")
### AI ###
from scipy.stats import norm
import numpy as np
import pandas as pd

from sklearn.preprocessing import normalize
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

dataset_paths = [
    "c:/Users/Levy/Documents/python_projs/shake-server/NGA_D005_Test.csv",
    "c:/Users/Levy/Documents/python_projs/shake-server/NGA_D010.csv",
    "c:/Users/Levy/Documents/python_projs/shake-server/NGA_D005.csv"
]

print("Creating dataframes...")
dataframes = []
for path in dataset_paths:
    dataframes.append(pd.read_csv(path))

print("Generating Tensors...")
# Generate Tensors
train_data = dataframes[1][list(dataframes[1].columns.values)[7:]]
category_data = dataframes[1][list(dataframes[1].columns.values)[2:4]]

test_data = dataframes[0][list(dataframes[0].columns.values)[7:]]
category_test_data = dataframes[0][list(dataframes[0].columns.values)[2:4]]

print("Normalizing Tensor Data...")
# Normalize Data
(tensor_train_data) = scale.fit_transform(train_data.values)
(tensor_category_data) = category_data.values

(tensor_test_data) = scale.fit_transform(test_data.values)
(tensor_category_test_data) = category_test_data.values

print("Creating Neural Network Model...")
#Creating Neural Network Model
model = Sequential()
model.add(Dense(111, activation='relu', input_shape=(111,)))
model.add(Dense(2, activation='softmax'))

print(model.summary())

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

print("Training model...")
history = model.fit(tensor_train_data, category_data,
                        batch_size=20,
                        epochs=10,
                        verbose=2,
                        validation_data=(tensor_train_data, category_data))

print("Done!")
print("Testing model...")
score = model.evaluate(tensor_test_data, tensor_category_test_data, verbose=0)
print("Done!")
print('Test loss:', score[0])
print('Test accuracy:', score[1])

class EarthquakePredictionResource(object):
    def on_post(self, req, res):
        if req.stream:
            #Do something
        else:
            res.status = falcon.HTTP_400
        