import json
import os

import mypackage


class ResourceReader:

    def read_by_name(self, resourceName):
        file = os.path.join(mypackage.__path__[0], 'resources', resourceName)
        json_input = file.read()
        requests_json = json.loads(json_input)
        print(requests_json)
        return requests_json
