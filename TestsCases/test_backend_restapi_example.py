import pytest

import Utils.Config
import Utils.RequestSpecificationHelper
import Utils.TestDataProvider

testDataTable = [
    ("TC_001", "POST", Utils.Config.Config.DEFAULT_REST_API_BASE_URL,
     Utils.TestDataProvider.TestDataProvider.PLACEHOLDER_REQ_JSON_FILE, 201, None),
    ("TC_002", "PUT", Utils.Config.Config.USERS_REST_API_BASE_URL + "/2",
     Utils.TestDataProvider.TestDataProvider.PLACEHOLDER_REQ_JSON_FILE, 200, None),
    ("TC_003", "GET", Utils.Config.Config.USERS_REST_API_BASE_URL + "?page=2", None, 200,
     Utils.TestDataProvider.TestDataProvider.PLACEHOLDER_RESP_JSON_FILE),
    ("TC_004", "DELETE", Utils.Config.Config.USERS_REST_API_BASE_URL + "/2", None, 200, None),
]


@pytest.mark.parametrize(testDataTable)
def test_restapi_example(testCaseID, requestMethod, endpointPath, requestBodyResourceName,
                         responseStatusCode, responseBodyJsonResourceName):
    Utils.RequestSpecificationHelper.RequestSpecificationHelper \
        .build_http_request(testCaseID, requestMethod, endpointPath, requestBodyResourceName,
                            responseStatusCode, responseBodyJsonResourceName)
