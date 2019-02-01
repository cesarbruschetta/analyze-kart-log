""" module to utils test """

import sys
import io
import os
from unittest import TestCase
from datetime import datetime, timedelta

from analyze_kart_log import utils


class TestUtils(TestCase):
    """" test class to utils module """

    def test_str2datetime(self):
        """ test method str2datetime """

        obj = utils.str2datetime("23:49:08.277")
        self.assertIsInstance(obj, datetime)

    def test_str2float(self):
        """ test method str2float """

        obj = utils.str2float("44,275")
        self.assertIsInstance(obj, float)

    def test_str2timedelta(self):
        """ test str2timedelta """

        obj = utils.str2timedelta("1:02.852")
        self.assertIsInstance(obj, timedelta)

    def test_read_data_file(self):
        """ test to method read data file """
        
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        data = utils.read_data_file(os.path.join(root_path, "kart_run.log"))
        self.assertEqual(data["038"][0]["name"], "F.MASSA")

    def test_print_best_lap_race(self):
        """ test method to print best lap race """

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        data = {"code": "038", "name": "F.MASSA", "best_lap_time": "1:02.852"}
        utils.print_best_lap_race(data)

        sys.stdout = sys.__stdout__
        self.assertIn("A melhor volta da corrida do piloto", capturedOutput.getvalue())

    def test_print_result_race(self):
        """ test method print result race """

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        data = [
            {
                "code": "038",
                "name": "F.MASSA",
                "qtd_laps": 4,
                "time_total": timedelta(0, 249),
                "avg_speed": "44.25 Km/h",
                "best_lap_time": timedelta(0, 62),
                "best_lap_str": "4 volta em 0:01:02",
                "position": 1,
                "time_after_first": timedelta(0),
            },
            {
                "code": "002",
                "name": "K.RAIKKONEN",
                "qtd_laps": 4,
                "time_total": timedelta(0, 253),
                "avg_speed": "43.63 Km/h",
                "best_lap_time": timedelta(0, 63),
                "best_lap_str": "4 volta em 0:01:03",
                "position": 2,
                "time_after_first": timedelta(0, 4),
            },
            {
                "code": "033",
                "name": "R.BARRICHELLO",
                "qtd_laps": 4,
                "time_total": timedelta(0, 255),
                "avg_speed": "43.47 Km/h",
                "best_lap_time": timedelta(0, 63),
                "best_lap_str": "3 volta em 0:01:03",
                "position": 3,
                "time_after_first": timedelta(0, 6),
            },
            {
                "code": "023",
                "name": "M.WEBBER",
                "qtd_laps": 4,
                "time_total": timedelta(0, 256),
                "avg_speed": "43.19 Km/h",
                "best_lap_time": timedelta(0, 64),
                "best_lap_str": "4 volta em 0:01:04",
                "position": 4,
                "time_after_first": timedelta(0, 7),
            },
            {
                "code": "015",
                "name": "F.ALONSO",
                "qtd_laps": 4,
                "time_total": timedelta(0, 293),
                "avg_speed": "38.07 Km/h",
                "best_lap_time": timedelta(0, 67),
                "best_lap_str": "2 volta em 0:01:07",
                "position": 5,
                "time_after_first": timedelta(0, 44),
            },
            {
                "code": "011",
                "name": "S.VETTEL",
                "qtd_laps": 3,
                "time_total": timedelta(0, 386),
                "avg_speed": "25.75 Km/h",
                "best_lap_time": timedelta(0, 78),
                "best_lap_str": "3 volta em 0:01:18",
                "position": 6,
                "time_after_first": "Não terminou a prova",
            },
        ]
        utils.print_result_race(data)

        sys.stdout = sys.__stdout__
        self.assertIn("Posição Chegada", capturedOutput.getvalue())
