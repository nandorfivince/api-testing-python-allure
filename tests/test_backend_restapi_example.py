import pytest

import utils.Config
import utils.RequestSpecificationHelper
import utils.TestDataProvider

testDataTable = [
    ("TC_001", "POST", utils.Config.Config.DEFAULT_REST_API_BASE_URL,
     utils.TestDataProvider.TestDataProvider.PLACEHOLDER_REQ_JSON_FILE, 201, None),
    ("TC_002", "PUT", utils.Config.Config.USERS_REST_API_BASE_URL + "/2",
     utils.TestDataProvider.TestDataProvider.PLACEHOLDER_REQ_JSON_FILE, 200, None),
    ("TC_003", "GET", utils.Config.Config.USERS_REST_API_BASE_URL + "?page=2", None, 200,
     utils.TestDataProvider.TestDataProvider.PLACEHOLDER_RESP_JSON_FILE),
    ("TC_004", "DELETE", utils.Config.Config.USERS_REST_API_BASE_URL + "/2", None, 200, None),
]


@pytest.mark.parametrize(testDataTable)
def test_restapi_example(testCaseID, requestMethod, endpointPath, requestBodyResourceName,
                         responseStatusCode, responseBodyJsonResourceName):
    utils.RequestSpecificationHelper.RequestSpecificationHelper \
        .build_http_request(testCaseID, requestMethod, endpointPath, requestBodyResourceName,
                            responseStatusCode, responseBodyJsonResourceName)
