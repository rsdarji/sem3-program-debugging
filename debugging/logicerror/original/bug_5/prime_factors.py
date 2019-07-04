def factors(number):
    """Returns a list of all prime factors of a given number"""
    x = 2
    while x <= number:
        output = [1]
        while number % x == 0:
            output.append(x)
            number //= x
        x += 1

    return output


if __name__ == "__main__":
    print('A prime number is a number which is only divisible by one and itself.\n'
          'Every number can be written as a product of prime factors. Example: 45 = 3 * 3 * 5.')

    while True:
        try:
            num = int(input("Enter a number to find its prime factorization: "))
            break
        except ValueError:
            print('Invalid input...')

    print('The factors of', num, 'are:', ', '.join(str(c) for c in factors(num)))

