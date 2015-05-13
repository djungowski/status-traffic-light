class Status:
    COLOR_GREEN = "green"
    COLOR_YELLOW = "yellow"
    COLOR_RED = "red"
    COLOR_BLUE = "blue"  # Blue = green in Jenkins

    __jobs = None

    def __init__(self, jobs):
        self.__jobs = jobs

    def __is_job_failed(self, job):
        return job["color"] == self.COLOR_RED

    def __is_job_unstable(self, job):
        return job["color"] == self.COLOR_YELLOW

    def get(self):
        status = self.COLOR_GREEN
        for job in self.__jobs:
            if self.__is_job_failed(job):
                status = self.COLOR_RED

            if self.__is_job_unstable(job):
                status = self.COLOR_YELLOW
        return status