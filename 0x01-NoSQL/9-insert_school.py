#!/usr/bin/env python3
"""insert a document into a db collection"""


def insert_school(mongo_collection, **kwargs):
    """insert a pymongo document through python"""
    status = mongo_collection.insert_one(kwargs)
    return status.inserted_id
