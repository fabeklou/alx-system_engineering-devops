#!/usr/bin/python3

"""This module sends a GET request to a REST API and
prints the data, formated to the stdin
"""

import requests
import sys
from typing import List

if __name__ == "__main__":
    USER_ID: int = sys.argv[1]

    USER_INFO_URL: str = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(USER_ID)
    TODOS_URL: str = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(USER_ID)
    user_info = requests.get(USER_INFO_URL).json()
    tasks = requests.get(TODOS_URL).json()

    SEP: str = "\t "
    EMPLOYEE_NAME: str = user_info.get("name")
    NUMBER_OF_DONE_TASKS: int = 0
    TOTAL_NUMBER_OF_TASKS: int = 0
    TASKS_COMPLETED: List[str] = []

    for task in tasks:
        if task.get("completed"):
            TASKS_COMPLETED.append(task.get("title"))
            NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in TASKS_COMPLETED:
        print("{}{}".format(SEP, task))
