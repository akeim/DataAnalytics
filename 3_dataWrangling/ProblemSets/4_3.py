#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import csv
import json
import pprint

DATAFILE = 'arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'binomialAuthority_label': 'binomialAuthority'}


def add_field(filename, fields):

    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for line in reader:
            if ("(" not in line['rdf-schema#label']):
                entity = {
                    "label": line['rdf-schema#label'],
                    "classification": {
                    "binomialAuthority": line['binomialAuthority_label']}}
                data.append(entity)
    return data


def update_db(data, db):
    for line in data:
        new_line = db.arachnid.find_one({'label': line['label']})
        new_line['classification']['binomialAuthority'] = line['classification']['binomialAuthority']
        db.arachnid.save(new_line)


def test():

    data = add_field(DATAFILE, FIELDS)
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    update_db(data, db)

    updated = db.arachnid.find_one({'label': 'Opisthoncana'})
    assert updated['classification']['binomialAuthority'] == 'Embrik Strand'
    pprint.pprint(data)



if __name__ == "__main__":
    test()
