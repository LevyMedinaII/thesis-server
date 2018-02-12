import json
import falcon
import pandas as pd

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
    # def on_post(self, req, res):
        