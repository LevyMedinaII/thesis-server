import json
import falcon
import pandas as pd

from db import Sample

class AccelerometerResource(object):
    def on_post(self, req, res):
        if req.stream:
            requestBody  = json.load(req.stream)
            res.body = json.dumps(requestBody)  
        else:
            res.status = falcon.HTTP_400