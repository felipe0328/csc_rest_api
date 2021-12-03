import threading
from .models import Job
import environ

env = environ.Env()
environ.Env.read_env()


class PendingJobsHandler:
    JobHandlerTime = None
    JobPendingState = "pending"
    JobProcessedState = "processed"

    isRunning = False

    def process_pending_jobs(self):
        if self.JobHandlerTime is None:
            self.JobHandlerTime = int(env('PROCESS_JOB_DELAY_TIME'))

        self.isRunning = True
        timer = threading.Timer(self.JobHandlerTime, self.run_pending)
        timer.start()

    def run_pending(self):
        pending_job = Job.objects.filter(status=self.JobPendingState).first()
        string_data = ''.join(map(str, pending_job.data))
        pending_job.result = string_data
        pending_job.status = self.JobProcessedState
        pending_job.save()
        self.isRunning = False
        if Job.objects.filter(status=self.JobPendingState).exists():
            self.process_pending_jobs()
