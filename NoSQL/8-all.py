#!/usr/bin/env python3
""" MongoDB operations with Python """


def list_all(mongo_collection):
    """ List all documents in a collection """
    if not mongo_collection:
        return []
    return mongo_collection.find()