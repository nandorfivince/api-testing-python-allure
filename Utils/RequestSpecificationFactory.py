import json

import requests
from requests.auth import HTTPBasicAuth

import Utils.Config


class RequestSpecificationFactory:

    def request_specification_factory(self, methodType, url, data):
        json_content_type = {'content-type': 'application/json'}

        if Utils.Config.Config.is_secured_environment() is True:
            if methodType is "GET" and data is not None:
                return requests.get(url, data=json.dumps(data), headers=json_content_type,
                                    auth=HTTPBasicAuth("usrname", "pwd"))
            elif methodType is "GET" and data is None:
                return requests.get(url, headers=json_content_type, auth=HTTPBasicAuth("usrname", "pwd"))

            elif methodType is "POST" and data is not None:
                return requests.post(url, data=json.dumps(data), headers=json_content_type,
                                     auth=HTTPBasicAuth("usrname", "pwd"))
            elif methodType is "POST" and data is None:
                return requests.post(url, headers=json_content_type, auth=HTTPBasicAuth("usrname", "pwd"))

            elif methodType is "PUT" and data is not None:
                return requests.put(url, data=json.dumps(data), headers=json_content_type,
                                    auth=HTTPBasicAuth("usrname", "pwd"))
            elif methodType is "PUT" and data is None:
                return requests.put(url, headers=json_content_type, auth=HTTPBasicAuth("usrname", "pwd"))

            elif methodType is "DELETE" and data is not None:
                return requests.delete(url, data=json.dumps(data), headers=json_content_type,
                                       auth=HTTPBasicAuth("usrname", "pwd"))
            elif methodType is "DELETE" and data is None:
                return requests.delete(url, headers=json_content_type, auth=HTTPBasicAuth("usrname", "pwd"))
        else:
            if methodType is "GET" and data is not None:
                return requests.get(url, data=json.dumps(data), headers=json_content_type)
            elif methodType is "GET" and data is None:
                return requests.get(url, headers=json_content_type)

            elif methodType is "POST" and data is not None:
                return requests.post(url, data=json.dumps(data), headers=json_content_type)
            elif methodType is "POST" and data is None:
                return requests.post(url, headers=json_content_type)

            elif methodType is "PUT" and data is not None:
                return requests.put(url, data=json.dumps(data), headers=json_content_type)
            elif methodType is "PUT" and data is None:
                return requests.put(url, headers=json_content_type)

            elif methodType is "DELETE" and data is not None:
                return requests.delete(url, data=json.dumps(data), headers=json_content_type)
            elif methodType is "DELETE" and data is None:
                return requests.delete(url, headers=json_content_type)
