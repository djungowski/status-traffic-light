__author__ = 'Dominik Jungowski'

from jenkinsapi.jenkins import Jenkins
from jenkinsapi.jenkins import Requester
from lib.view_monkeypatch import ViewMonkeypatch
from lib.status import Status
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

# Use custom requester which ignores self-signed certificates
requester = Requester(config["jenkins"]["username"], config["jenkins"]["password"], ssl_verify=False)
jenkins = Jenkins(config["jenkins"]["base_url"], requester=requester)


# Monkeypatch the jenkinsapi provided view
ViewMonkeypatch().apply()

view_url = config["jenkins"]["base_url"] + "/view/" + config["jenkins"]["view"]
view = jenkins.get_view_by_url(view_url)
jobs = view.get_jobs()
status = Status(jobs)
print(status.get())