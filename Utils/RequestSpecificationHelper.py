import json
import time

import Utils.RequestSpecificationFactory
import Utils.ResourceReader


class RequestSpecificationHelper:

    def build_http_request(self, testCaseID, requestMethod, endpointPath, requestBodyResourceName,
                           responseStatusCode, responseBodyJsonResourceName):

        if testCaseID and requestMethod and endpointPath and responseStatusCode is not None:

            print("Executing test: {" + testCaseID + "}")

            if requestBodyResourceName and responseBodyJsonResourceName is not None:
                reqBodyResourceName = Utils.ResourceReader.ResourceReader.read_by_name(requestBodyResourceName)
                expectedJsonBody = Utils.ResourceReader.ResourceReader.read_by_name(responseBodyJsonResourceName)
                time.sleep(1)
                response = Utils.RequestSpecificationFactory.RequestSpecificationFactory. \
                    request_specification_factory(requestMethod, endpointPath, reqBodyResourceName)
                print(response)
                assert response.status_code == responseStatusCode
                actualJsonBody = json.loads(response.text)
                assert expectedJsonBody == actualJsonBody

            elif requestBodyResourceName and responseBodyJsonResourceName is None:
                reqBodyResourceName = requestBodyResourceName
                time.sleep(1)
                response = Utils.RequestSpecificationFactory.RequestSpecificationFactory. \
                    request_specification_factory(requestMethod, endpointPath, reqBodyResourceName)
                print(response)
                assert response.status_code == responseStatusCode

            elif requestBodyResourceName is not None and responseBodyJsonResourceName is None:
                reqBodyResourceName = Utils.ResourceReader.ResourceReader.read_by_name(requestBodyResourceName)
                time.sleep(1)
                response = Utils.RequestSpecificationFactory.RequestSpecificationFactory. \
                    request_specification_factory(requestMethod, endpointPath, reqBodyResourceName)
                print(response)
                assert response.status_code == responseStatusCode

            elif requestBodyResourceName is None and responseBodyJsonResourceName is not None:
                reqBodyResourceName = requestBodyResourceName
                expectedJsonBody = Utils.ResourceReader.ResourceReader.read_by_name(responseBodyJsonResourceName)
                time.sleep(1)
                response = Utils.RequestSpecificationFactory.RequestSpecificationFactory. \
                    request_specification_factory(requestMethod, endpointPath, reqBodyResourceName)
                print(response)
                assert response.status_code == responseStatusCode
                actualJsonBody = json.loads(response.text)
                assert expectedJsonBody == actualJsonBody
