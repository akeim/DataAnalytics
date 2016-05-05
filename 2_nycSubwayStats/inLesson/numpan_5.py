import numpy
from pandas import DataFrame, Series


def add_full_name(path_to_csv, path_to_new_csv):

    data = pandas.read_csv(path_to_csv)
    data['nameFull'] = data['nameFirst'] + ' ' + data['nameLast']
    data.to_csv(path_to_new_csv)


if __name__ == "__main__":
    path_to_csv = ""
    path_to_new_csv = ""
    add_full_name(path_to_csv, path_to_new_csv)
