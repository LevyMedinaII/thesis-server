import json
import falcon
import pandas as pd

from db import Sample

class DataResource(object):
    def on_get(self, req, res):
        df = pd.read_csv('NGA_D005.csv')
        json_data = df.to_json(orient='records')
        res.body = json.dumps(json_data)
        
    def on_post(self, req, res):
        # x-www-form-urlencoded
        # requestBody = req.params
        # earthquakeData = req.get_param_as_list('earthquake_data')

        # raw/json
        # requestBody  = json.load(req.stream)
        # earthquakeData = requestBody.get('earthquake_data')
        df = pd.read_csv('NGA_D005.csv')
        json_data = df.to_json(orient='records')

        # TODO: Analyze data with AI

        responseData = {
            'earthquake_data': json_data
        }

        res.body = json.dumps(responseData)
        res.status = falcon.HTTP_200