#!/usr/bin/env python3
"""list all documents in mogodb collection"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """list all documents in mongodb collection"""
    return mongo_collection.find()
