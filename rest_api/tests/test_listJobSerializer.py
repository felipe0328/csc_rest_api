from django.test import TestCase
from rest_api.serializers import CreateJobSerializer, ListJobSerializer
from rest_api.models import Job


class ListJobSerializerTestCase(TestCase):
    def test_listJobSerializer_serializesDataCorrectly_returnsExpectedData(self):
        input_data = {
            "name": "test_name",
            "data": [1, 2, 3]
        }

        serialized_data = CreateJobSerializer(data=input_data)
        serialized_data.is_valid()
        serialized_data.save()

        job_object = Job.objects.get(pk=serialized_data.data["id"])
        list_job = ListJobSerializer(job_object)
        self.assertTrue(list_job.data.__contains__("id"))
        self.assertTrue(list_job.data.__contains__("name"))
        self.assertTrue(list_job.data.__contains__("data"))
        self.assertTrue(list_job.data.__contains__("result"))
        self.assertTrue(list_job.data.__contains__("status"))
