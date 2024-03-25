#!/usr/bin/env python3
"""
def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """ Function that returns all docs having a particular topic """
    return mongo_collection.find({"topics": topic})
