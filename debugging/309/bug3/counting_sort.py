def list_from_count(count, lo, hi):
    new_lst = []

    x = lo
    while x <= hi:
        if count[x - lo] >= 0:
            new_lst.extend(x for _ in range(count[x - lo]))
        else:
            continue

        x += 1

    return new_lst


def counting_sort(lst):
    lo, hi = min(lst), max(lst)
    count = [0 for _ in range(lo, hi + 1)]

    for x in lst:
        count[x - lo] += 1

    new_lst = list_from_count(count, lo, hi)

    return new_lst


def main():
    user_input = input('Enter a list of numbers separated by spaces: ')

    nums = []

    for x in user_input.split():
        nums.append(int(x))

    sorted_nums = counting_sort(nums)

    print('Sorted numbers:', *sorted_nums)


if __name__ == '__main__':
    main()


#wrong input
#1 6 9 8 3
#9 6 5 10 15 4
#88 65 32 22 0 2 25
#99 8 55 54 75 63 4

#correct input
#1 , 1 2 , 2 1 , 3 2 1