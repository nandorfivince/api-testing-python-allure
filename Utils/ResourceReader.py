import json


class ResourceReader:

    def read_by_name(self, resource_path_name):
        specific_json_resource = json.loads(open(resource_path_name).read())
        return specific_json_resource
