#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
import json
import jsondb


def main():
    db_file = 'test.db'
        
    with jsondb.JsonDB(db_file) as db:
        print("Create DB table")
        db.create_table("persons")
        db.commit()

        print("Insert data to the table")
        data = {"name": "Alice", "age": 10}
        db.set("persons", 1, data)

        data = {"name": "Bob", "age": 25}
        db.set("persons", 2, data)
        
        data = {"name": "Charlie", "age": 19}
        db.set("persons", None, data)

        print("Get data by ID")
        row = db.get("persons", 3)
        print(row)

        print("Find data by condition")
        where = {"name": "Bob"}
        for row in db.find("persons", where):
            print(row["id"])
            print(row["data"])

if __name__ == "__main__":
    main()
