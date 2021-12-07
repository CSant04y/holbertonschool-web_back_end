#!/usr/bin/env python3
"""
Function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    This lists all documents under a collection
    """
    docs = mongo_collection.find()
    return docs
