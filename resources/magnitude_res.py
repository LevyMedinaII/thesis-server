import json
import falcon
import pandas as pd
from .magnitude_ai import average_error, mest

class MagnitudeResource(object):
   def on_get(self, req, res):
       res.body = json.dumps({"average_error": average_error, "approximate": mest})