#!/usr/bin/python3
'''
Script to gather employee data and TODO list progress from an API.

Usage:
    python3 script.py <employee_id>

Arguments:
    <employee_id>: Integer ID of the employee whose TODO progress to fetch.

API Endpoint:
    https://jsonplaceholder.typicode.com

Example:
    python3 script.py 2
'''

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])
            
            # Fetch employee data
            user_response = requests.get(f'{REST_API}/
                                         users/{employee_id}')
            if user_response.status_code != 200:
                print(f"Error fetching user data 
                      for employee ID {employee_id}")
                sys.exit(1)

            user_data = user_response.json()
            emp_name = user_data.get('name')

            # Fetch all todos and filter for the specific employee
            todos_response = requests.get(f'{REST_API}/
                                          todos?userId={employee_id}')
            if todos_response.status_code != 200:
                print(f"Error fetching TODO data 
                      for employee ID {employee_id}")
                sys.exit(1)

            todos_data = todos_response.json()
            total_tasks = len(todos_data)
            completed_tasks = [task for task in todos_data
                                if task.get('completed')]

            # Display the results
            print(f'Employee {emp_name} is done with tasks
                  ({len(completed_tasks)}/{total_tasks}):')
            for task in completed_tasks:
                print(f'\t {task.get("title")}')
        else:
            print("Employee ID must be an integer.")
    else:
        print("Usage: python3 script.py <employee_id>")
