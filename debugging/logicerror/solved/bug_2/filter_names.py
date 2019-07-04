def format_words(words):
    """
    Sorts and capitalize all words
    """
    return sorted(words, key=str.lower)


def print_words(words):
    """
    Print the words to the screen for the user in a readable format
    """
    print('Here are the words you entered:')
    for i, word in enumerate(words, start=1):
        print('{}. {}'.format(i, word.title()))


def remove_words_with_letters(words, letters):
    for word in words:
        for letter in letters.lower():
            if letter in word.lower():
                words.remove(word)


if __name__ == '__main__':
    print('Enter a list of word. When done, type ENTER without entering anything:')
    words = list(iter(input, ''))

    # Sort words alphabetically
    formatted_words = format_words(words)

    # Remove words with letters input from the user
    letters = input('Enter any letters, the words containing these will be removed: ')
    remove_words_with_letters(formatted_words, letters)

    # Print the output
    print_words(formatted_words)
