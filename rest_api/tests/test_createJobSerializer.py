from django.test import TestCase
from rest_api.serializers import CreateJobSerializer
from rest_api.models import Job


class CreateJobSerializerTestCase(TestCase):
    def test_jobSerializer_validateCorrectData_returnsTrue(self):
        input_data = {
            "name": "test_name",
            "data": [1, 2, 3]
        }

        serialized_data = CreateJobSerializer(data=input_data)
        self.assertTrue(serialized_data.is_valid())

    def test_jobSerializer_validDataCreatesCorrectDBObject_returnsExpectedData(self):
        input_data = {
            "name": "jobSerializer_test_name",
            "data": [1, 2, 3]
        }

        serialized_data = CreateJobSerializer(data=input_data)
        self.assertTrue(serialized_data.is_valid())
        serialized_data.save()

        database_element = Job.objects.get(pk=serialized_data.data["id"])
        self.assertEqual(database_element.name, "jobSerializer_test_name")
        self.assertEqual(database_element.data, [1, 2, 3])
        self.assertEqual(database_element.status, "pending")
        self.assertEqual(database_element.result, None)

    def test_jobSerializer_validateIncorrectData_returnsFalse(self):
        input_data = {
            "name": "test_name",
            "no_correct_object": [1, 2, 3]
        }

        serialized_data = CreateJobSerializer(data=input_data)
        self.assertFalse(serialized_data.is_valid())

    def test_jobSerializer_unableToModifyOtherDBFieldsWhenCreating_returnsExpectedData(self):
        input_data = {
            "name": "test_name",
            "data": [1, 2, 3],
            "status": "processed",
            "result": "123",
        }

        serialized_data = CreateJobSerializer(data=input_data)
        self.assertTrue(serialized_data.is_valid())
        serialized_data.save()

        database_element = Job.objects.get(pk=serialized_data.data["id"])
        self.assertEqual(database_element.name, "test_name")
        self.assertEqual(database_element.data, [1, 2, 3])
        self.assertEqual(database_element.status, "pending")
        self.assertEqual(database_element.result, None)
