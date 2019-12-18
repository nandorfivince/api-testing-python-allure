import json


class ResourceReader:

    def read_by_name(self, resourceName):
        config = json.loads(open(resourceName).read())
        return config
