import json
import falcon
import os

#Setup
os.environ['KERAS_BACKEND'] = 'theano'

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from keras.models import model_from_json

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
    "NGA_D005_Test.csv",
    "NGA_D010.csv"
]

print("Creating dataframes...")
dataframes = []
for path in dataset_paths:
    dataframes.append(pd.read_csv(path))

print("Generating Tensors...")
# Generate Tensors
train_data = dataframes[1][list(dataframes[1].columns.values)[7:]]
category_data = dataframes[1][list(dataframes[1].columns.values)[3:4]]

test_data = dataframes[0][list(dataframes[0].columns.values)[7:]]
category_test_data = dataframes[0][list(dataframes[0].columns.values)[3:4]]

print("Normalizing Tensor Data...")
# Normalize Data
(tensor_train_data) = scale.fit_transform(train_data.values)
(tensor_category_data) = category_data.values

(tensor_test_data) = scale.fit_transform(test_data.values)
(tensor_category_test_data) = category_test_data.values

# Open model file
json_file = open('model.json', 'r')

#### CREATING A MODEL ####
# print("Creating Neural Network Model...")
# model = Sequential()

# print("Added Layer with 20 neurons")
# model.add(Dense(20, activation='relu', input_shape=(20,)))

# print("Added Layer with 1 neurons for activation")
# model.add(Dense(1, activation='softmax'))

# print(model.summary())

# model.compile(loss='binary_crossentropy',
#             optimizer=RMSprop(),
#             metrics=['accuracy'])

# # Training Neural Network Model
# print("Training model...")
# history = model.fit(tensor_train_data, category_data,
#                         batch_size=20,
#                         epochs=10,
#                         verbose=1,
#                         validation_data=(tensor_train_data, category_data))

# print("Done!")  

# print("Saving model...")
# # Saving model
# model_json = model.to_json()
# with open("model.json", "w") as json_file:
#     json_file.write(model_json)
# # serialize weights to HDF5
# model.save_weights("model.h5")
# print("Saved model to disk")
#########################

#### LOADING A MODEL ####
print('Loading model from file...')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model.h5")

print("Loaded model from disk")

model.compile(loss='binary_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])
##############################


# Sample Model Test
print("Testing model...")
score = model.evaluate(tensor_test_data, tensor_category_test_data, verbose=1)
print("Done!")
print('Test loss:', score[0])
print('Test accuracy:', score[1])

class EarthquakePredictionResource(object):
    def on_post(self, req, res):
        if req.stream:
            data = json.load(req.stream)
            data = data['earthquake_data']

            data_np = np.array([data])
            prediction = model.predict(data_np)

            print(prediction[0][0])
            # TODO: Integrate Mobile Stream Sending
            
            res.body = json.dumps({
                "prediction": int(prediction[0][0])
            })
        else:
            res.status = falcon.HTTP_400