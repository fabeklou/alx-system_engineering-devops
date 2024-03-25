#!/usr/bin/python3

"""This module sends a GET request to a REST API and
prints the data, formated to the stdin
"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    USER_ID: str = sys.argv[1]

    USER_INFO_URL: str = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(USER_ID)
    TODOS_URL: str = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(USER_ID)
    user_info = requests.get(USER_INFO_URL).json()
    tasks = requests.get(TODOS_URL).json()

    USERNAME: str = user_info.get("username")

    with open("{}.csv".format(USER_ID), "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        # writer.writeheader()
        for task in tasks:
            writer.writerow({"USER_ID": USER_ID, "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task.get("completed"),
                             "TASK_TITLE": task.get("title")})
