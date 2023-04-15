#!/usr/bin/env python3
"""sort students by average score"""


def top_students(mongo_collection):
    """sort top students"""
    results = mongo_collection.find()
    top_students = []
    for stu in results:
        avScore = 0
        count = 0
        for topic in stu['topics']:
            avScore += topic['score']
            count += 1
        if avScore != 0:
            avScore = avScore/count
        stu['averageScore'] = avScore
        top_students.append(stu)
    return sorted(top_students, key=lambda x: x['averageScore'], reverse=True)
