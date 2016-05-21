#!/usr/bin/env python


def porsche_query():
    # Please fill in the query to find all autos manuafactured by Porsche.
    query = {"manufacturer": "Porsche"}
    return query


# Do not edit code below this line in the online code editor.
# Code here is for local use on your own computer.
def get_db(db_name):
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def find_porsche(db, query):
    # For local use
    return db.autos.find(query)


if __name__ == "__main__":
    # For local use
    db = get_db('examples')
    query = porsche_query()
    p = find_porsche(db, query)
