from __future__ import print_function

import json
from botocore.vendored import requests

def lambda_handler(event, context):
    print('Received event: ' + json.dumps(event))
    print(requests.get('http://7.23.50.3:5646'))