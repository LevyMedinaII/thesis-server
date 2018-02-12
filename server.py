import json
import falcon
from falcon_cors import CORS
import requests

from resources import DataResource
from db import SQLAlchemySessionManager, Session, Sample, Earthquakes

# class TestResource(object):
#     def on_post(self, req, res):
#         # Test route
#         ### External API Call ###
#         ## Call
#         # root = 'https://reqres.in'
#         # route = '/api/users?page=2'
#         # test_data = requests.get(root + route)
        
#         ## API Response Parsing
#         # test_data = test_data.json()
#         # res.body = json.dumps(test_data)
        
#         ### Database add to table ###
#         # sample_test = Sample(name='sample', fullname='Sample Name', password='samplepass')
#         # self.session.add(sample_test)
#         # self.session.commit()

#         # raw/json
        
#         if req.stream:
#             requestBody  = json.load(req.stream)
#             username = requestBody.get('username')
#             password = requestBody.get('password')

#             if username == 'hello' and password == 'world':
#                 res.body = json.dumps({
#                     'id_number': 100000,
#                     'last_name': 'Jacob Yap',
#                     'first_name': 'Mabry Baeron Jackyle',
#                     'course': 'BS CoE/ MS CS',
#                     'year': 5
#                 })
#         else:
#             res.status = falcon.HTTP_400

# Allow CORS
cors = CORS(allow_origins_list=['http://localhost:3000'])

# falcon.API instances are callable WSGI apps
app = falcon.API(middleware=[
    SQLAlchemySessionManager(Session),
    cors.middleware,
])

from resources import model

# set x-www-form-urlencoded to be available with req.params
app.req_options.auto_parse_form_urlencoded = True

# Resources are represented by long-lived class instances
test = TestResource()
data = DataResource()

# things will handle all requests to the '/things' URL path
app.add_route('/test', test)
app.add_route('/data', data)