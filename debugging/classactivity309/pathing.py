import sys

# This checks for the Python version
if sys.version_info.major < 3:
    print("WARNING: you are using Python2. Switch to Python3.")
    exit(1)


def push_to_stack(stack, direction):
    """
    Push to the stack and simplify entry.
    Simplification:
        LEFT RIGHT -> ''
        RIGHT LEFT -> ''
        UP DOWN -> ''
        DOWN UP -> ''
    """
    if not stack:
        stack.append(direction)
    elif stack[-1] == inverse(direction):
        stack.pop()
    else:
        stack.append(direction)

def pop_from_stack(stack):
    """Pop from the stack and return None if the stack is empty"""
    if stack:
        return stack.pop()
    else:
        return None


def inverse(direction):
    """Return the inverse of a direction"""
    if direction == "UP":
        return "DOWN"
    elif direction == "DOWN":
        return "UP"
    elif direction == "LEFT":
        return "RIGHT"
    elif direction == "RIGHT":
        return "LEFT"
    else:
        raise ValueError("Allowed values: UP, DOWN, LEFT, RIGHT")

def reverse_stack(stack):
    output = []

    for i in range(0, len(stack)):
        item = pop_from_stack(stack)
        output.append(item)

    return output


def main():
    path = []
    stack = []

    command = input("Enter a direction [UP/DOWN/LEFT/RIGHT/END]: ").upper()
    while command != 'END':
        if command not in ('UP', 'DOWN', 'LEFT', 'RIGHT'):
            print('Invalid direction...')
        else:
            inverse_direction = inverse(command)
            path.append(command)
            push_to_stack(stack, inverse_direction)
        command = input("Enter a direction [UP/DOWN/LEFT/RIGHT/END]: ").upper()


    reversed_stack = reverse_stack(stack)

    print('Path:          ', ', '.join(path))
    print('Inverse path:  ', ', '.join(reversed_stack))

if __name__ == "__main__":
    main()
