def add_ingredient(current_ingredients):
    ingredient = input('Ingredient: ').title()
    qty = input('Quantity: ')

    current_ingredients.append({'name': ingredient, 'qty': qty})


def format_recipe(ingredients):
    lines = []
    for item in ingredients:
        name = item['name']
        qty = item['qty']

        line = '{} {} {}'.format(name[:20], '.' * (40 - len(name[:20]) - len(qty)), qty)

        lines.append(line)

    return '=' * 17 + ' Recipe ' + '=' * 17 + '\n' + '\n'.join(lines)


def main():
    ingredients = []
    while True:

        add_ingredient(ingredients)

        command = input('Press ENTER to add another ingredient. Enter QUIT to quit.').lower()
        while command not in ('', 'quit'):
            print('Invalid command...')
            command = input('Press ENTER to add another ingredient. Enter QUIT to quit.').lower()

        if command != '':
            break

    printable_recipe = format_recipe(ingredients)
    filename = 'your_recipe.txt'
    print("\nThe following recipe will be saved to '{}':".format(filename))
    print(printable_recipe)
    with open(filename, 'w') as f:
        f.write(printable_recipe)


if __name__ == '__main__':
    main()
