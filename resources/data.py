import json
import falcon
import pandas as pd
import requests

from db import Sample, Earthquakes

class DataResource(object):
    def on_get(self, req, res):
        data = self.session.query(Earthquakes).all()
        
        res_data = []
        for entry in data:
            res_data.append({
                'name': entry.name,
                'lat': entry.lat,
                'long': entry.long,
                'pga': entry.pga,
                'pgv': entry.pgv,
                'pgd': entry.pgd,
                'magnitude': entry.magnitude
            })

        res.body = json.dumps({
            "earthquake_data": res_data
        })

    def on_post(self, req, res):
        B0 = 4.3977
        B1 = -5.3746
        B2 = 9.6426

        mest = (B1*float(pga)) + (B2*float(pgd)) + B0
        
        if req.stream:
            requestBody = json.load(req.stream)

            route = '/'
            test_data = requests.get(route)
        else:
            res.status = falcon.HTTP_400
        