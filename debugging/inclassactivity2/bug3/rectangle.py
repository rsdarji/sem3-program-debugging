def make_square(x, y):
    row = '*' * x

    rows = [row]

    while len(rows) < y:
        rows.append(row)

    return '\n'.join(rows)


def main():
    print('I will draw a rectangle for you.')

    x, y = int(input('Width of the rectangle: ')), int(input('Height of the rectangle: '))

    square = make_square(x, y)

    print('\n' + square)

    print('\nDone! Thank you!')


if __name__ == '__main__':
    main()
