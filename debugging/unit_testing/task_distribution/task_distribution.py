def parse_file_content(content):
    """
    Parse the content of a file into a list of tasks.
    Each task is represented by a tuple (name <string>, time <int>)

    Example:
    Input:

    Buy milk   2
    Cook diner 3

    Output:
    [('Buy milk', 2), ('Cook diner', 3)]
    """
    tasks = []

    for line in content.splitlines():
        line = line.strip()
        if line:
            task_line = line.rsplit(maxsplit=1)
            name = task_line[0].strip()
            time = int(task_line[-1])
            tasks.append((name, time))

    return tasks


def distribute_tasks(tasks, n):
    """
    Split the tasks evenly between n workers
    Each worker is represented by a pair [tasks <list>, time <int>]

    Example:
    Input:
    [('Buy milk', 2), ('Cook diner', 3), ('Clean dishes', 1)], 2

    Output:
    [
        [[('Cook diner', 3)], 3]
        [[('Clean dishes', 1), ('Buy milk', 2)], 3],
    ]

    Algorithm: The distribution algorithm first sorts the tasks from smallest to biggest and then always inserts the
    next task into the less busy worker
    """

    tasks = sorted(tasks, key=lambda x: x[1], reverse=True)
    workers = [[[], 0] for _ in range(n)]

    for task in tasks:
        least_worker = min(workers, key=lambda x: x[1])
        least_worker[0].append(task)
        least_worker[1] += task[1]

    return workers


def distribution_to_string(workers):
    """
    Converts a list of workers to a printable string

    Example:
    Input:
    [
        [[('Cook diner', 3)], 3]
        [[('Clean dishes', 1), ('Buy milk', 2)], 3],
    ]

    Output:

    '''Worker #1
    Cook diner .............. 3h
    Total time: 3h

    Worker #2
    Buy milk ................ 2h
    Clean dishes ............ 1h
    Total time: 3h

    '''
    """
    content = ''
    for i, worker in enumerate(workers, start=1):
        content += 'Worker #{}\n'.format(i)
        for task, time in worker[0]:
            content += '{} {}h\n'.format((task + ' ').ljust(25, '.'), time)

        content += 'Total time: {}h\n\n'.format(time)

    return content


def main():
    filename = input('Enter the task list filename: ')

    with open(filename, 'r') as file:
        content = file.read()
        tasks = parse_file_content(content)

    n = int(input('Between how many workers should the tasks be split? '))

    workers = distribute_tasks(tasks, n)
    distribution_filename = input('Enter the team output filename: ')

    with open(distribution_filename, 'w') as file:
        content = distribution_to_string(workers)
        file.write(content)

    print('Done! Open {} to see the task distribution.'.format(distribution_filename))


if __name__ == '__main__':
    main()
