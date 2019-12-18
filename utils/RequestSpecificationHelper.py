import json
import time

import utils.RequestSpecificationFactory
import utils.ResourceReader


class RequestSpecificationHelper:

    def build_http_request(self, testCaseID, requestMethod, endpointPath, requestBodyResourceName,
                           responseStatusCode, responseBodyJsonResourceName):

        if testCaseID and requestMethod and endpointPath and responseStatusCode is not None:

            print("Executing test: {" + testCaseID + "}")

            if requestBodyResourceName and responseBodyJsonResourceName is not None:
                reqBodyResourceName = utils.ResourceReader.ResourceReader.read_by_name(requestBodyResourceName)
                expectedJsonBody = utils.ResourceReader.ResourceReader.read_by_name(responseBodyJsonResourceName)
                time.sleep(1)
                response = utils.RequestSpecificationFactory.RequestSpecificationFactory. \
                    request_specification_factory(requestMethod, endpointPath, reqBodyResourceName)
                print(response)
                assert response.status_code == responseStatusCode
                actualJsonBody = json.loads(response.text)
                assert expectedJsonBody == actualJsonBody

            elif requestBodyResourceName and responseBodyJsonResourceName is None:
                reqBodyResourceName = requestBodyResourceName
                time.sleep(1)
                response = utils.RequestSpecificationFactory.RequestSpecificationFactory. \
                    request_specification_factory(requestMethod, endpointPath, reqBodyResourceName)
                print(response)
                assert response.status_code == responseStatusCode

            elif requestBodyResourceName is not None and responseBodyJsonResourceName is None:
                reqBodyResourceName = utils.ResourceReader.ResourceReader.read_by_name(requestBodyResourceName)
                time.sleep(1)
                response = utils.RequestSpecificationFactory.RequestSpecificationFactory. \
                    request_specification_factory(requestMethod, endpointPath, reqBodyResourceName)
                print(response)
                assert response.status_code == responseStatusCode

            elif requestBodyResourceName is None and responseBodyJsonResourceName is not None:
                reqBodyResourceName = requestBodyResourceName
                expectedJsonBody = utils.ResourceReader.ResourceReader.read_by_name(responseBodyJsonResourceName)
                time.sleep(1)
                response = utils.RequestSpecificationFactory.RequestSpecificationFactory. \
                    request_specification_factory(requestMethod, endpointPath, reqBodyResourceName)
                print(response)
                assert response.status_code == responseStatusCode
                actualJsonBody = json.loads(response.text)
                assert expectedJsonBody == actualJsonBody
