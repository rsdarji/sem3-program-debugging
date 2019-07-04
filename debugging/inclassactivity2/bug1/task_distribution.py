def read_file(filename):
    """Extract the tasks and their expected time from a file"""
    tasks = []
    with open(filename, 'r') as file:
        for line in file:
            line.strip()
            if line:
                task_line = line.rsplit()
                name = task_line[0]
                for i in range(1,len(task_line)-1):
                    name = name + " "+task_line[i]
                time = int(task_line[-1])
                tasks.append((name, time))

    return tasks

def distribute_tasks(tasks, n):
    """Split the tasks evenly between n workers"""
    tasks = sorted(tasks, key=lambda x: x[1], reverse=True)
    workers = [[[], 0] for _ in range(n)]

    for task in tasks:
        least_worker = min(workers, key=lambda x: x[1])
        least_worker[0].append(task)
        least_worker[1] += task[1]

    return workers


def write_distribution_to_file(workers, filename):
    """Write the task distribution to the file and write the total time for eack worker"""
    content = ''
    for i, worker in enumerate(workers, start=1):
        content += 'Worker #{}\n'.format(i)
        for task, time in worker[0]:
            content += '{} {}h\n'.format((task+' ').ljust(25, '.'), time)

        content += 'Total time: {}h\n\n'.format(worker[1])

    with open(filename, 'w') as file:
        file.write(content)


def main():
    filename = input('Enter the task list filename: ')

    tasks = read_file(filename)

    n = int(input('Between how many workers should the tasks be split? '))

    workers = distribute_tasks(tasks, n)
    distribution_filename = input('Enter the team output filename: ')

    write_distribution_to_file(workers, distribution_filename)

    print('Done! Open {} to see the task distribution.'.format(distribution_filename))


if __name__ == '__main__':
    main()
