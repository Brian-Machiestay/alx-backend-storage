#!/usr/bin/env python3
"""update topics of a school"""


def update_topics(mongo_collection, name, topics):
    """update topics of a school"""
    query = {"name" : name}
    newVals = {"$set" : {"topics" : topics}}
    mongo_collection.update_one(query, newVals)
