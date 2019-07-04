import sys

# This checks for the Python version
if sys.version_info.major < 3:
    print("WARNING: you are using Python2. Switch to Python3.")
    exit(1)


def kilogram_to_pound(k):
    return 2.205 * k


def pound_to_kilogram(p):
    return 0.4536 * p


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


converter_table = [kilogram_to_pound,
                   pound_to_kilogram,
                   celsius_to_fahrenheit,
                   fahrenheit_to_celsius]

if __name__ == "__main__":
    print("Welcome! Let me help you convert some units.\n"
          "\n"
          "What conversion do you need?\n"
          "1. Kilograms   ->   Pounds\n"
          "2. Pounds      ->   Kilograms\n"
          "3. Celsius     ->   Fahrenheit\n"
          "4. Fahrenheit  ->   Celsius")

    while True:
        option = int(input('>>> '))
        if option in (1, 2, 3, 4):
            break
        else:
            print('Invalid input...')

    converter = converter_table[option - 1]

    qty = float(input("Enter a value to convert: "))
    conversion = converter(qty)

    print("Output: {}".format(conversion))
