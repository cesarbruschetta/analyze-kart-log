""" module to run test """

from unittest import TestCase
from datetime import datetime, timedelta

from analyze_kart_log import run, utils


class TestRun(TestCase):
    """ class to test run methods """

    def setUp(self):

        self.data_race = utils.read_data_file("./kart_run.log")

    def test_build_result_race(self):
        """ test method build_result_race """

        result_race = run.build_result_race(self.data_race)
        self.assertEqual(len(result_race), 6)

    def test_get_best_lap_race(self):
        """ test method get_best_lap_race """

        result_race = run.build_result_race(self.data_race)
        data = run.get_best_lap_race(result_race)

        self.assertEqual(data["name"], "F.MASSA")
