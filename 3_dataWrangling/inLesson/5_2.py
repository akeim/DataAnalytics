#!/usr/bin/env python

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [{"$match": {"user.time_zone": "Brasilia","user.statuses_count": {"$gte": 100}}},
                {"$project": {"followers": "$user.followers_count","screen_name": "$user.screen_name","tweets": "$user.statuses_count"}},
               {"$sort": {"followers": -1}},
               {"$limit": 1}]
    return pipeline

def aggregate(db, pipeline):
    result = db.tweets.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result)
    assert len(result["result"]) == 1
    assert result["result"][0]["followers"] == 17209
