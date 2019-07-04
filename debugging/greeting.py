def capitalize_name(name):
    name_parts = name.split()
    name = ""
    for x in name_parts:
        name+= " "+x.capitalize()
    return name


if __name__ == '__main__':
    name = input('Hello, what is your name? ')
    capitalized_name = capitalize_name(name)
    print('Nice to meet you{}!'.format(capitalized_name))
