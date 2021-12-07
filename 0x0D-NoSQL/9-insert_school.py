#!/usr/bin/python3
"""
This inserts a new doumnet into collection based of kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a document in collection
    """
    docs = mongo_collection.insert_one(kwargs)
    return docs.inserted_id
