DEFAULT_WIDTH = 80


def join_lines(lines):
    """
    Takes in a list of list, each list represent a line and contains words
    Format back the list of list to a readable string

    Example
    Input [['Hello', 'world!'], ['How', 'are', 'you?']]

    Output:
    '''Hello world!
    How are you?'''
    """
    lines = [' '.join(line) for line in lines]
    text = '\n'.join(lines)
    return text


def get_lines_of_length(words, length):
    """
    Takes a list of words as input and a maximum length
    split the words into lists containing approximately the 'length' number of characters
    The output is a list of list, each list representing a line

    Example:
    Input: ['Test', 'text', 'for', 'formatter'], 8
    Output: [['Test', 'text'], ['for', 'formatter']]
    """
    lines = []
    current_line = []
    line_length = 0
    for word in words:
        if line_length > length:
            lines.append(current_line)
            current_line = []
            line_length = 0

        line_length += len(word) + 1
        current_line.append(word)
    lines.append(current_line)
    return lines


def create_new_filename(filename):
    """
    Create the output file name from the input file name by adding format as second extension
    Example:

    Input: 'file.txt'
    Output: 'file.format.txt
    """
    new_filename = filename.split('.')
    new_filename.append('format')
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
