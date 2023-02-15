#!/usr/bin/env python3
"""log nginx stats"""


from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    nginx = client.logs.nginx
    number_docs = nginx.count_documents({})
    get = nginx.count_documents({"method": "GET"})
    post = nginx.count_documents({"method": "POST"})
    put = nginx.count_documents({"method": "PUT"})
    patch = nginx.count_documents({"method": "PATCH"})
    delete = nginx.count_documents({"method": "DELETE"})
    stat = nginx.count_documents({"method": "GET", "path": "/status"})
    print("{} logs".format(number_docs))
    print("Methods:")
    print("\tmethod GET: {}".format(get))
    print("\tmethod POST: {}".format(post))
    print("\tmethod PUT: {}".format(put))
    print("\tmethod PATCH: {}".format(patch))
    print("\tmethod DELETE: {}".format(delete))
    print("{} status check".format(stat))
