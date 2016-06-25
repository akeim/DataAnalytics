#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'


def fix_area(area):

    if area == "NULL" or area == "":
        area = None


    elif (area[0:1] == "{"):
        area = area.split('|')
        value1 = area[0].replace('{','')
        value2 = area[1].replace('}','')

        less1, reject1 = value1.split('+')
        less2, reject2 = value2.split('+')

        if len(less1) > len(less2):
            value = value1
        else:
            value = value2
        area = float(value)
    else:
        area = float(area)

    return area


def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(5,8):
        pprint.pprint(data[n]["areaLand"])

    assert data[3]["areaLand"] == None
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0


if __name__ == "__main__":
    test()
