""" module to utils function """

from datetime import datetime, timedelta


def str2datetime(str):
    """ convert string to datetime obj """
    return datetime.strptime(str, "%H:%M:%S.%f")


def str2float(str):
    """ convert string to float obj """
    return float(str.replace(",", "."))


def str2timedelta(str):
    """ convert string to timedelta obj """
    t = datetime.strptime(str, "%M:%S.%f")
    return timedelta(minutes=t.minute, seconds=t.second)


def printTable(myDict, colList=None, keys_list=None):
    """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson - Use it as you want but don't blame me.
   """
    if not colList:
        colList = list(myDict[0].keys() if myDict else [])
    if not keys_list:
        keys_list = list(myDict[0].keys() if myDict else [])

    myList = [colList]  # 1st row = header
    for item in myDict:
        myList.append([str(item[col] or "") for col in keys_list])

    colSize = [max(map(len, col)) for col in zip(*myList)]
    formatStr = " | ".join(["{{:<{}}}".format(i) for i in colSize])
    myList.insert(1, ["-" * i for i in colSize])  # Seperating line
    for item in myList:
        print(formatStr.format(*item))


def read_data_file(filename):
    """ read file and organize data in dictionary """

    data = {}
    file = open(filename, "r")
    for line in file.readlines()[1:]:  # remove first line
        line = line.split()  # split line in list of 'words'
        line.pop(2)  # Removes '-' character

        if line[1] not in data:  # Check code of pilot in dict
            data[line[1]] = []

        data[line[1]].append(
            {
                "hour": str2datetime(line[0]),
                "name": line[2],
                "number_lap": line[3],
                "time_lap": str2timedelta(line[4]),
                "speed_lap": str2float(line[5]),
            }
        )

    file.close()
    return data


def print_result_race(pilots_data):
    """ print report data in shell """

    head_list = [
        "Posição Chegada",
        "Código Piloto",
        "Nome Piloto",
        "Qtde Voltas Completadas",
        "Tempo Total de Prova",
        "Velocidade Média",
        "Melhor Volta",
        "Tempo Apos Ganhador",
    ]

    keys_list = [
        "position",
        "code",
        "name",
        "qtd_laps",
        "time_total",
        "avg_speed",
        "best_lap_str",
        "time_after_first",
    ]

    printTable(pilots_data, head_list, keys_list)


def print_best_lap_race(best_lap_data):
    """ print best_lap_data """

    print(
        "A melhor volta da corrida do piloto %(code)s - %(name)s com tempo %(best_lap_time)s."
        % best_lap_data
    )
