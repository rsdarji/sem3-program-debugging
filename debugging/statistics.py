def average(grades):
    total = sum(grades)
    n = len(grades)
    return total / n

def remove_fail(grades):
    new_grades = []
    for grade in grades:
        if grade >= 60:
            new_grades.append(grade)
    return new_grades

if __name__ == '__main__':
    list_of_grades = []

    while True:
        user_input = input('Enter a grade from 0 to 100, when done write done: ')

        if user_input.isnumeric():
            list_of_grades.append(float(user_input))
        elif user_input == 'done':
            break
        else:
            print('Invalid input')
    list_of_grades = remove_fail(list_of_grades)
    if list_of_grades:
        avr = average(list_of_grades)
        print('The average of students who passed is:', avr)
    else:
        print('No student passed...')

