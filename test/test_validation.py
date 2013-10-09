import requests
import unittest
import json

class ValidateGeoJson(unittest.TestCase):

    def setUp(self):
        pass

    def test_validate(self):
        with open('./ros_users.geojson') as fh:
            contents = fh.read()

        validate_endpoint = 'http://geojsonlint.com/validate'

        good_request = requests.post(validate_endpoint, data=contents)

        j = json.loads(good_request.content)
        self.assertTrue('status' in j)
        self.assertTrue(j['status'] == 'ok')
                



if __name__ == '__main__':
    unittest.main()
