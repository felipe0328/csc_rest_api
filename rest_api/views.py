from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .PendingJobsHandler import PendingJobsHandler
from .models import Job
from .serializers import CreateJobSerializer, ListJobSerializer
from rest_framework.authentication import get_authorization_header


class Jobs(APIView):
    jobsHandler = PendingJobsHandler()

    def get(self, request, status_value=None):
        if status_value is None:
            job_data = Job.objects.all()
            serialized_data = ListJobSerializer(job_data, many=True)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:
            job_data = Job.objects.filter(status=status_value)
            serialized_data = ListJobSerializer(job_data, many=True)
            return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request, status_value=None):
        if status_value is not None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        header_info = get_authorization_header(request).decode("utf-8")

        if header_info == "allow":
            new_job = CreateJobSerializer(data=request.data)
            if new_job.is_valid():
                new_job.save()

                if self.jobsHandler.isRunning is False:
                    self.jobsHandler.process_pending_jobs()

                created_object = Job.objects.get(pk=new_job.data["id"])
                serialized_object = ListJobSerializer(created_object)
                return Response(serialized_object.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_401_UNAUTHORIZED, status=status.HTTP_401_UNAUTHORIZED)
