#!/usr/bin/env python


from autos import process_file


def insert_autos(infile, db):
    data = process_file(infile)
    for car in data:
        db.autos.insert(car)


if __name__ == "__main__":
    # Code here is for local use on your own computer.
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos('autos-small.csv', db)
    print db.autos.find_one()
