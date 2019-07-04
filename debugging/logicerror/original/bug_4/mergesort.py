def merge(left, right):
    output = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1

    output.extend(left[r:])
    output.extend(right[r:])

    return output


def mergesort(lst):
    if len(lst) <= 1:
        return lst[:]

    mid = len(lst) // 2

    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])

    return merge(left, right)


if __name__ == '__main__':
    numbers = []
    print('Merge Sort is a O(nlog(n)) recursive sorting algorithm. Here is a demonstration.')
    while True:

        n = input("Enter a number (or press ENTER stop): ")

        if not n:
            break
        else:
            numbers.append(int(n))

    sorted_numbers = mergesort(numbers)

    print('Here are the sorted numbers:', *sorted_numbers)
