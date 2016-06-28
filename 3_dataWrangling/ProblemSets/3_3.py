#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import csv
import pprint

CITIES = 'cities.csv'


def fix_name(name):

    if (name == "NULL") or (name == ""):
        name = []

    elif (name.startswith("{")):
        name1, name2 = name.split('|')
        name1 = name1.replace('{','').replace('[','')
        name2 = name2.replace('}','').replace(']','')
        name = [str(name1), str(name2)]
    else:
        name = [str(name)]

    print name
    return name


def process_file(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #skipping the extra metadata
        for i in range(3):
            l = reader.next()
        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "name" in line:
                line["name"] = fix_name(line["name"])
            data.append(line)
    return data


def test():
    data = process_file(CITIES)

    print "Printing 20 results:"
    for n in range(20):
        pprint.pprint(data[n]["name"])

    assert data[14]["name"] == ['Negtemiut', 'Nightmute']
    assert data[9]["name"] == ['Pell City Alabama']
    assert data[3]["name"] == ['Kumhari']

if __name__ == "__main__":
    test()
