#!/usr/bin/python3

"""This module sends a GET request to a REST API and
prints the data, formated to the stdin
"""

import json
import requests

if __name__ == "__main__":
    USERS_URL: str = "https://jsonplaceholder.typicode.com/users"
    TODOS_URL: str = "https://jsonplaceholder.typicode.com/todos"
    users_info = requests.get(USERS_URL).json()
    tasks = requests.get(TODOS_URL).json()

    formated_tasks = {}
    for task in tasks:
        USER_ID = task.get("userId")
        TITLE = task.get("title")
        STATUS = task.get("completed")
        if not formated_tasks.get(USER_ID):
            formated_tasks[USER_ID] = []
        formated_tasks.get(USER_ID).append(
            {"task": TITLE, "completed": STATUS})

    for user_info in users_info:
        USER_ID = user_info.get("id")
        USERNAME = user_info.get("username")
        for task in formated_tasks.get(USER_ID):
            task.update({"username": USERNAME})

    with open("todo_all_employees.json", "w") as file:
        json.dump(formated_tasks, file)
