__author__ = 'Dominik Jungowski'

import unittest
from lib.status import Status

class StatusTest(unittest.TestCase):

    def test_green(self):
        jobs = [{"color": "blue"}, {"color": "blue"}, {"color": "blue"}]
        status = Status(jobs)
        self.assertEqual('green', status.get())

    def test_red(self):
        jobs = [{"color": "blue"}, {"color": "red"}, {"color": "blue"}]
        status = Status(jobs)
        self.assertEqual('red', status.get())

    def test_yellow(self):
        jobs = [{"color": "blue"}, {"color": "yellow"}, {"color": "blue"}]
        status = Status(jobs)
        self.assertEqual('yellow', status.get())