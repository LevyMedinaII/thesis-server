import json
import falcon
import pandas as pd
import requests
import numpy as np
import ast

from db import Sample, Earthquakes
from .classifier_ai import model

import csv

class DataResource(object):
    pingCountTOtal = 0
    def on_get(self, req, res):
        data = self.session.query(Earthquakes).all()
        
        res_data = [
            {
                'name': entry.name,
                'lat': entry.lat,
                'long': entry.long,
                'pga': entry.pga,
                'pgv': entry.pgv,
                'pgd': entry.pgd,
                'magnitude': entry.magnitude
            } for entry in data
        ]

        res.body = json.dumps({
            "earthquake_data": res_data
        })

    def on_post(self, req, res):
        B0 = 4.3977
        B1 = -5.3746
        B2 = 9.6426

        if req.stream:
            data = json.load(req.stream.read().decode('utf8').replace("'", '"'))

            waveform_data = ast.literal_eval(data['Displacement'][0])
            pga = data['PGA']
            pgv = data['PGV']
            pgd = max(waveform_data)
            
            data_np = np.array([waveform_data])
            prediction = model.predict(data_np)
            prediction =int(prediction[0][0])

            print('{}*{} + {}*{} + {}'.format(B1, pga, B2, pgd, B0))
            mest = abs((B1*float(pga)) + (B2*float(pgd)) + B0)

            if len(waveform_data) > 0:
                with open('Not_Earthquakes.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(waveform_data)

            # if prediction != 1:
            #     with open('Not_Earthquakes.csv', 'a') as csvfile:
            #         writer = csv.writer(csvfile, delimiter=',')
            #         writer.writerow(waveform_data)
            # else:
            #     pingCountTotal += 1
            #     print('Ping Count:', pingCountTotal)
            #     print('Prediction:', prediction)
            #     print('Magnitude Est:', mest)
            
            res.body = json.dumps({
                "prediction": prediction,
                "magnitude": int(mest)
            })
        else:
            res.status = falcon.HTTP_400
        