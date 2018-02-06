import json
import falcon
import pandas as pd

from db import Sample, Earthquakes

class DataResource(object):
    def on_get(self, req, res, earthquake_id):
        data = Earthquakes.query.get(earthquake_id)
        res.body = json.dumps({
            "earthquake_data": data
        })