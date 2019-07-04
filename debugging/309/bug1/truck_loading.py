def read_file(filename):
    """Extract the tasks and their expected time from a file"""
    items = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                item_line = line.rsplit(maxsplit=1)
                name = item_line[0]
                weight = int(item_line[1])
                items.append((name, weight))

    return items


def split_items(items, n):
    """Split the tasks evenly between n containers"""
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

    tasks = read_file(filename)

    n = int(input('How many trucks will carry the load? '))

    containers = split_items(tasks, n)
    distribution_filename = input('Enter the output filename: ')

    write_distribution_to_file(containers, distribution_filename)

    print('Done! Open {} to see the item distribution.'.format(distribution_filename))


if __name__ == '__main__':
    main()
