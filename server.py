import json
import falcon
import requests

from resources import DataResource, AccelerometerResource
from db import SQLAlchemySessionManager, Session, Sample

class TestResource(object):
    def on_post(self, req, res):
        # Test route
        ### External API Call ###
        ## Call
        # root = 'https://reqres.in'
        # route = '/api/users?page=2'
        # test_data = requests.get(root + route)
        
        ## API Response Parsing
        # test_data = test_data.json()
        # res.body = json.dumps(test_data)
        
        ### Database add to table ###
        # sample_test = Sample(name='sample', fullname='Sample Name', password='samplepass')
        # self.session.add(sample_test)
        # self.session.commit()

        # raw/json
        if req.stream:
            requestBody  = json.load(req.stream)
            latitude = requestBody.get('latitude')
            longitude = requestBody.get('longitude')

            res.body = json.dumps({
                'latitude': latitude,
                'longitude': longitude
            })  
        else:
            res.status = falcon.HTTP_400


# falcon.API instances are callable WSGI apps
app = falcon.API(middleware=[
    SQLAlchemySessionManager(Session),
])

# set x-www-form-urlencoded to be available with req.params
app.req_options.auto_parse_form_urlencoded = True

# Resources are represented by long-lived class instances
test = TestResource()
data = DataResource()
accelerometer = AccelerometerResource()

# things will handle all requests to the '/things' URL path
app.add_route('/test', test)
app.add_route('/data', data)
app.add_route('/accelerometer', accelerometer)