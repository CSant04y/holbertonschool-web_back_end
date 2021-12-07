#!/usr/bin/env python3
"""[lists school having specific topics]
"""


def schools_by_topic(mongo_collection, topic):
    """
    This returns schools by topics
    """
    docs = mongo_collection.find({"topics": topic})
    return docs
