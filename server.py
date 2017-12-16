import json
import falcon
import requests

from resources import DataResource
from db import SQLAlchemySessionManager, Session, Sample

class TestResource(object):
    def on_get(self, req, res):
        # Test route
        ### External API Call ###
        # root = 'https://reqres.in'
        # route = '/api/users?page=2'
        # test_data = requests.get(root + route)
        # res.status = falcon.HTTP_200  # This is the default status
        # test_data = test_data.json()
        # res.body = json.dumps(test_data)
        
        ### Database add to table ###
        # sample_test = Sample(name='sample', fullname='Sample Name', password='samplepass')
        # self.session.add(sample_test)
        # self.session.commit()

        res.body = json.dumps({ 'status': 'finished' })


# falcon.API instances are callable WSGI apps
app = falcon.API(middleware=[
    SQLAlchemySessionManager(Session),
])

# set x-www-form-urlencoded to be available with req.params
app.req_options.auto_parse_form_urlencoded = True

# Resources are represented by long-lived class instances
test = TestResource()
data = DataResource()

# things will handle all requests to the '/things' URL path
app.add_route('/test', test)
app.add_route('/data', data)