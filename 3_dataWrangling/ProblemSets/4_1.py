#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import csv
import json
import pprint
import re

DATAFILE = 'arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'URI': 'uri',
         'rdf-schema#comment': 'description',
         'synonym': 'synonym',
         'name': 'name',
         'family_label': 'family',
         'class_label': 'class',
         'phylum_label': 'phylum',
         'order_label': 'order',
         'kingdom_label': 'kingdom',
         'genus_label': 'genus'}


def process_file(filename, fields):

    process_fields = fields.keys()
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for line in reader:
            if (line['name'] == "NULL"):
                line['name'] = line['rdf-schema#label']
            if (line['synonym'] == "NULL"):
                line['synonym'] = "NULL"
            elif (line['synonym'].startswith("{")):
                line['synonym'] = line['synonym'].split("|")
            else:
                line['synonym'] = [line['synonym']]

            if ("(" in line['rdf-schema#label']):
                index = line['rdf-schema#label'].index("(")
                line['rdf-schema#label'] = line['rdf-schema#label'][:index-1]



            for i in process_fields:
                if line[i] == "NULL":
                    line[i] = None

            entry = {
                     "synonym": line['synonym'],
                        "name": line['name'],
                        "classification": {
                            "kingdom": line['kingdom_label'],
                            "family": line['family_label'],
                            "order": line['order_label'],
                            "phylum": line['phylum_label'],
                            "genus": line['genus_label'],
                            "class": line['class_label']
                        },
                        "uri": line['URI'],
                        "label": line['rdf-schema#label'],
                        "description": line['rdf-schema#comment']
                }
            data.append(entry)

    return data


def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return [v]


def test():
    data = process_file(DATAFILE, FIELDS)
    print "Your first entry:"
    pprint.pprint(data[0])
    first_entry = {
        "synonym": None,
        "name": "Argiope",
        "classification": {
            "kingdom": "Animal",
            "family": "Orb-weaver spider",
            "order": "Spider",
            "phylum": "Arthropod",
            "genus": None,
            "class": "Arachnid"
        },
        "uri": "http://dbpedia.org/resource/Argiope_(spider)",
        "label": "Argiope",
        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
    }

    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]

if __name__ == "__main__":
    test()
