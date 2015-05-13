__author__ = 'Dominik Jungowski'

from jenkinsapi.jenkins import View


class ViewMonkeypatch:
    def apply(self):
        def jenkins_api_view_get_jobs(self):
            jobs = []
            if 'jobs' in self._data:
                for job in self._data["jobs"]:
                    jobs.append(job)

            return jobs

        View.get_jobs = jenkins_api_view_get_jobs
