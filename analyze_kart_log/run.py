""" module to methods to run  """

import argparse
import sys
import os
from datetime import timedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyze_kart_log import utils


def build_result_race(data):
    """ build the result of rance data """
    result = []
    for c_pilot, laps in data.items():
        time_total = timedelta(0)
        avg_speed = 0.0
        qtd_laps = len(laps)
        best_lap_number = laps[0]["number_lap"]
        best_lap_time = laps[0]["time_lap"]

        for lap in laps:
            time_total += lap["time_lap"]
            avg_speed += lap["speed_lap"]

            if lap["time_lap"] <= best_lap_time:
                best_lap_time = lap["time_lap"]
                best_lap_number = lap["number_lap"]

        avg_speed = avg_speed / qtd_laps

        result.append(
            {
                "code": c_pilot,
                "name": laps[0]["name"],
                "qtd_laps": qtd_laps,
                "time_total": time_total,
                "avg_speed": "%.2f Km/h" % avg_speed,
                "best_lap_time": best_lap_time,
                "best_lap_str": "%s volta em %s" % (best_lap_number, best_lap_time),
            }
        )

    result = sorted(result, key=lambda k: (-k["qtd_laps"], k["time_total"]))
    for index, resultado in enumerate(result):
        resultado["position"] = index + 1

        if not index:
            resultado["time_after_first"] = "-"

        if resultado["qtd_laps"] == result[0]["qtd_laps"]:
            resultado["time_after_first"] = (
                resultado["time_total"] - result[0]["time_total"]
            )
        else:
            resultado["time_after_first"] = "Não terminou a prova"

    return result


def get_best_lap_race(result_race):
    """ get the bast lap from the data race result """

    return min(result_race, key=lambda k: k["best_lap_time"])


def main():
    """ method to main process """

    parser = argparse.ArgumentParser(
        description="Process log file of a kart race and returns winners report"
    )

    parser.add_argument(
        "--path_file",
        "-p",
        default="./kart_run.log",
        help="Caminho para o arquivo de log",
    )

    args = parser.parse_args()

    data_race = utils.read_data_file(args.path_file)
    result_race = build_result_race(data_race)

    SPACE = 20

    print("\n", "#" * SPACE, "RESULTADO DA CORRIDA", "#" * SPACE)
    utils.print_result_race(result_race)

    print("\n", "#" * SPACE, "MELHOR VOLTA DA CORRIDA", "#" * SPACE)
    utils.print_best_lap_race(get_best_lap_race(result_race))


if __name__ == "__main__":
    main()
