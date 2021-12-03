from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_api.views import Jobs


class JobsEndpointsTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = Jobs.as_view()

    def test_getJobsEndpoint_noElementsExistingYet_returnsEmptyList(self):
        request = self.factory.get('jobs/')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_postJobsEndpoint_noAuthorized_returns401Error(self):
        input_data = {
            "name": "test_name",
            "data": [1, 2, 3]
        }

        request = self.factory.post('jobs/', input_data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_postJobsEndpoint_authorized_returnsCorrectData(self):
        input_data = {
            "name": "test_name",
            "data": [1, 2, 3]
        }

        request = self.factory.post('jobs/', input_data,  HTTP_AUTHORIZATION='allow')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = response.data
        self.assertTrue("name" in response_data)
        self.assertTrue("status" in response_data)
        self.assertTrue("data" in response_data)
        self.assertTrue("result" in response_data)
        self.assertTrue("id" in response_data)

    def test_getJobsEndpoint_returnsDataWhenExists(self):
        input_data = {
            "name": "test_name",
            "data": [1, 2, 3]
        }

        request = self.factory.post('jobs/', input_data, HTTP_AUTHORIZATION='allow')
        self.view(request)
        request = self.factory.get('jobs/')
        response = self.view(request)
        response_data = response.data[0]
        self.assertTrue("name" in response_data)
        self.assertTrue("status" in response_data)
        self.assertTrue("data" in response_data)
        self.assertTrue("result" in response_data)
        self.assertTrue("id" in response_data)

    def test_getJobsEndpoint_filterByStatus(self):
        input_data = {
            "name": "test_name",
            "data": [1, 2, 3]
        }

        request = self.factory.post('jobs/', input_data, HTTP_AUTHORIZATION='allow')
        self.view(request)
        request = self.factory.get('jobs/pending')
        response = self.view(request)
        response_data = response.data[0]
        self.assertTrue("name" in response_data)
        self.assertTrue("status" in response_data)
        self.assertTrue("data" in response_data)
        self.assertTrue("result" in response_data)
        self.assertTrue("id" in response_data)
