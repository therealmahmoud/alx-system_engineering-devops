#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
returns information about his/her TOdO list progress."""
import requests
import sys


if __name__ == '__main__':
    todo = requests.get(f'https://jsonplaceholder.typicode.com/users/\
{sys.argv[1]}/todos')
    users = requests.get(f'https://jsonplaceholder.typicode.com/users/\
{sys.argv[1]}')

    todoo = todo.json()
    user = users.json()

    p = 0
    for i in todoo:
        if i['completed'] is True:
            p = p + 1

    print(f"Employee {user['name']} is done with tasks({p}/{len(todoo)}):")

    for j in todoo:
        if j['completed'] is True:
            print(f"\t {j['title']}")
