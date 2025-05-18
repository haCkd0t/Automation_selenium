import requests
class api:
    def __init__(self,driver):
        self.driver = driver

    def api_covid(self):
        res = requests.get("https://api.restful-api.dev/objects")
        return res.json()