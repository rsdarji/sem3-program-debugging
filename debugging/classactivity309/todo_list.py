from collections import deque
import sys

# This checks for the Python version
if sys.version_info.major < 3:
    print("WARNING: you are using Python2. Switch to Python3.")
    exit(1)

def tasks_already_exists(task, queue):
    if task in queue:
        return True
    else:
        return False

def get_task(queue):
    if queue:
        return queue.pop()
    else:
        return None

def add_task(task, queue):
    if tasks_already_exists(task, queue):
        return False
    else:
        queue.appendleft(task)
        return True


if __name__ == "__main__":
    queue = deque()

    print("Welcome to TODO!")
    print("Let me help you organize by keeping track fo your todo tasks.")
    print("You can ADD a task, GET the next task or EXIT.")

    while True:
        command = input('Command [add/get/exit]: ').lower()
        while command not in ('add', 'get', 'exit'):
            print('Invalid command...')
            command = input('Command [add/get/exit]: ').lower()

        if command == 'add':
            task = input('What task do you want to add?\n>>> ')
            res = add_task(queue, task)
            if res:
                print('Done!')
            else:
                print('ERROR: The task already exists in the todo list...')
        elif command == 'get':
            next_task = get_task(queue)
            if next_task is not None:
                print('The next task on the list is:', next_task)
            else:
                print('The todo-list is empty... You are done working!')
        elif command == 'exit':
            print('Thank you!')
            break
