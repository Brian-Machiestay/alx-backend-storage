#!/usr/bin/env python3
"""schools by topics"""


def schools_by_topic(mongo_collection, topic):
    """find schools by topics"""
    schools = []
    result = mongo_collection.find()
    for doc in result:
        if topic in doc.topics:
            schools.append(doc.name)
    return schools
