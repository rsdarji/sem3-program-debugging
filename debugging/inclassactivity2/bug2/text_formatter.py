DEFAULT_WIDTH = 80


def join_lines(lines):
    lines = [' '.join(line) for line in lines]
    text = '\n'.join(lines)
    return text


def get_lines_of_length(words, length):
    lines = []
    current_line = []
    last_line=[]
    line_length = 0
    for word in words:
        if line_length > length:
            lines.append(current_line)
            current_line = []
            line_length = 0

        line_length += len(word) + 1
        current_line.append(word)














def create_new_filename(filename):
    new_filename = filename.split('.')
    new_filename.insert(1, 'format')
    new_filename = '.'.join(new_filename)
    return new_filename


def main():
    filename = input('Enter a filename to format: ')
    with open(filename, 'r') as file:
        content = file.read()

    words = content.split()

    splitted_lines = get_lines_of_length(words, DEFAULT_WIDTH)

    formatted_text = join_lines(splitted_lines)

    new_filename = create_new_filename(filename)

    with open(new_filename, 'w') as file:
        file.write(formatted_text)


if __name__ == "__main__":
    main()
