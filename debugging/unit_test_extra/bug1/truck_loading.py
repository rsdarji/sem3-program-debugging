def read_file_content(content):
    """
    Extract the tasks and their expected time from a file content
    Example:
    '''
    Cement 500
    Wood 200
    '''
    Output:
    [('Cement', 500), ('Wood', 200)]
    """
    items = []

    for line in content.splitlines():
        line = line.strip()
        if line:
            item_line = line.rsplit(maxsplit=1)
            name = item_line[0]
            weight = int(item_line[1])
            items.append((name, weight))

    return items


def split_items(items, n):
    """
    Split the items evenly between n containers.
    The algorithm uses is a greedy algorithm which always add the biggest remaining item to the least loaded container

    Example:
        [('Cement', 500), ('Wood', 200), ('Plastic', 100)]
        2
    Output:
        [[[('Cement', 500)], 500], [[('Wood', 200), ('Plastic', 100)], 300]]

    The output contains containers represented by lists.
    Each container contains a list of items at index 0 and the total mass of items at index 1
    """
    items = sorted(items, key=lambda x: x[1], reverse=True)
    containers = [[[], 0] for _ in range(n)]

    for item in items:
        least_loaded_container = min(containers, key=lambda x: x[1])
        least_loaded_container[0].append(item)
        least_loaded_container[1] += item[1]

    return containers


def write_distribution_to_file(trucks, filename):
    """Write the item distribution to the file and write the total weight for each worker"""
    content = ''
    for i, container in enumerate(trucks, start=1):
        content += 'Container #{}\n'.format(i)
        for item, weight in container[0]:
            content += '{} {}kg\n'.format((item+' ').ljust(25, '.'), weight)

        content += 'Total: {}kg\n\n'.format(weight)

    with open(filename, 'w') as file:
        file.write(content)


def main():
    filename = input('Enter the items filename: ')

    with open(filename, 'r') as file:
        content = file.read()
        tasks = read_file_content(content)

    n = int(input('How many trucks will carry the load? '))

    containers = split_items(tasks, n)
    distribution_filename = input('Enter the output filename: ')

    write_distribution_to_file(containers, distribution_filename)

    print('Done! Open {} to see the item distribution.'.format(distribution_filename))


if __name__ == '__main__':
    main()
