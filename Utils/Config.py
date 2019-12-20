import os


class Config:
    global BASE_URL_ENV_VAR_NAME
    global REQRES_API_BASE_URL

    DEFAULT_REST_API_BASE_URL = "https://reqres.in/api/"
    USERS_REST_API_BASE_URL = DEFAULT_REST_API_BASE_URL + "/users"

    BASE_URL_ENV_VAR_NAME = "TEST_API_BASE_URL"

    def initialize_api_base_url(self):
        base_url_env_var = os.getenv(BASE_URL_ENV_VAR_NAME)
        if base_url_env_var is None:
            DEFAULT_REST_API_BASE_URL = "https://reqres.in/api/"
            base_url = DEFAULT_REST_API_BASE_URL
            print("Api BASE URL is: " + base_url)
        else:
            base_url = base_url_env_var
            print("Api BASE URL is: " + base_url)
        return base_url

    REQRES_API_BASE_URL = initialize_api_base_url()

    def is_secured_environment(self):
        if REQRES_API_BASE_URL.__contains__("https"):
            return True
