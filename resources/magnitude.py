import json
import falcon
import pandas as pd
# from .magnitude_ai import average_error, mest

B0 = 4.3977
B1 = -5.3746
B2 = 9.6426

class MagnitudeResource(object):
    def on_get(self, req, res):
        if req.stream:
            requestBody = json.load(req.stream)
            
            pga = requestBody.get('pga')
            pgd = requestBody.get('pgd')

            mest = (B1*float(pga)) + (B2*float(pgd)) + B0
            res.body = json.dumps({ "magnitude_prediction": mest })
        else:
            res.status = falcon.HTTP_400