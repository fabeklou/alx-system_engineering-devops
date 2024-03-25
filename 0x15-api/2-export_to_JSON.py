#!/usr/bin/python3

"""This module sends a GET request to a REST API and
prints the data, formated to the stdin
"""

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

    EMPLOYEE_NAME: str = user_info.get("name")
    USERNAME: str = user_info.get("username")
    USER_DATA = {USER_ID: []}

    for task in tasks:
        TITLE, STATUS = task.get("title"), task.get("completed")
        USER_DATA.get(USER_ID).append(
            {"task": TITLE, "completed": STATUS, "username": USERNAME})

    with open("{}.json".format(USER_ID), "w") as file:
        json.dump(USER_DATA, file)
