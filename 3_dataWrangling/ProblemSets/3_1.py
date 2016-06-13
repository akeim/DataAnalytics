#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal",
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long",
          "areaLand", "areaMetro", "areaUrban"]

def float_test(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def audit_file(filename, fields):
    fieldtypes = {}

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        for field in fields:
            fieldtypes[field] = []

        for row in reader:
            for field in fields:
                if (row[field] == "NULL")  or (row[field] == ""):
                    fieldtypes[field].append(type(None))
                elif (row[field][0:1] == "{"):
                    fieldtypes[field].append(type([]))
                elif (row[field].isdigit() == True):
                    fieldtypes[field].append(type(0))
                else:
                    try:
                        float(row[field])
                        fieldtypes[field].append(type(0.0))
                    except ValueError:
                        pass

    for field in fields:
        fieldtypes[field] = set(fieldtypes[field])

    return fieldtypes

def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    #pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])

if __name__ == "__main__":
    test()
