from django.test import TestCase
from rest_api.models import Job


class JobModelTestCase(TestCase):
    def setUp(self):
        Job.objects.create(name="test_name", data=[1, 2, 3])

    def test_job_model_default_values_are_correct(self):
        test_object = Job.objects.filter(name="test_name").first()
        self.assertEqual(test_object.name, "test_name")
        self.assertEqual(test_object.data, [1, 2, 3])
        self.assertEqual(test_object.status, "pending")
        self.assertEqual(test_object.result, None)
