#!/usr/bin/env python3
"""schools by topics"""


def schools_by_topic(mongo_collection, topic):
    """find schools by topics"""
    schools = []
    result = mongo_collection.find()
    for doc in result:
        if 'topics' in doc.keys():
            if topic in doc['topics']:
                if 'name' in doc.keys():
                    schools.append(doc)
    return schools
