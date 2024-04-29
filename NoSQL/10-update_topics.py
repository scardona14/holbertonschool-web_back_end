#!/usr/bin/env python3
""" MongoDB operations with Python """


def update_topics(mongo_collection, name, topics):
    """ Update all documents based on the name """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
