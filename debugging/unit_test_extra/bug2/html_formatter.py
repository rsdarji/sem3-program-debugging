def is_opening_tag(tag):
    """
    Return whether a tag (string) is an opening tag or not.

    Examples:
        "<p>" -> True
        "<a option=value>" -> True
        "</p>" -> False
        "Some text" -> False
    """
    return tag.startswith('<')


def is_closing_tag(tag):
    """
    Return whether a tag (string) is a closing tag or not.

    Examples:
        "</p>" -> True
        "<body>" -> False
        "Some text" -> False
    """
    return tag.startswith('</') and tag[-1]==">"


def format_with_indentation(tokens):
    """
    From a list of tokenized html tag, return an indented string.
    Example:
        ["<p>", "Some text", "</p>"]
    Output:
    '''
    <p>
      Some text
    </p>
    '''
    """
    indent = 0
    html_lines = []
    for token in tokens:
        if is_opening_tag(token):
            html_lines.append('  ' * indent + token)
            indent += 1
        elif is_closing_tag(token):
            indent -= 1
            html_lines.append('  ' * indent + token)
        else:
            html_lines.append('  ' * indent + token)

    html = '\n'.join(html_lines)
    return html


def tokenize_html(html):
    """Turns an html file into a list of tags and text.
    Example
        <p>Some text</p>
    Output:
        ["<p>", "Some text", "</p>"]
    """
    tokens = []
    i = 0

    while i < len(html):
        char = html[i]
        if char == '<':
            closing_char_pos = html.index('>', i)
            tokens.append(html[i:closing_char_pos + 1])
            i = closing_char_pos + 1
        else:
            opening_char_pos = html.index('<', i)
            tokens.append(html[i:opening_char_pos])
            i = opening_char_pos

    return tokens


def format_html(html):
    tokenized_html = tokenize_html(html)
    formatted_html = format_with_indentation(tokenized_html)
    return formatted_html


def main():
    in_filename = input("Enter filename to format: ")
    out_filename = input("Enter output filename: ")

    with open(in_filename, 'r') as file:
        content = file.read()

    formatted_content = format_html(content)

    with open(out_filename, 'w') as file:
        file.write(formatted_content)

    print('Done! Please open {}'.format(out_filename))


if __name__ == "__main__":
    main()
