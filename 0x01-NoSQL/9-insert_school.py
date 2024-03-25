#!/usr/bin/env python3
"""
def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """ A function that inserts a doc into a collection """
    return mongo_collection.insert_one(kwargs)
