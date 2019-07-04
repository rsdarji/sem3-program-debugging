import unittest

import task_distribution

content = ""
filename = "list.txt"
with open(filename, 'r') as file:
    content = file.read()
def test_parse_file_content():
    # input_ = """
    # Buy Milk 2
    # Cook diner 3"""


    expected_output = [('Buy milk', 2), ('Cook diner', 3), ('Clean dishes', 1)]

    output = task_distribution.parse_file_content(content)

    assert len(output) == 3, "Missing tasks"
    assert output[0][0] == "Buy milk", "Wrong task name: {}".format(output[0][0])
    assert output[0][1] == 2, "Wrong task time"

    assert output == expected_output, "{} -> {}".format(content,output)

    print("test parse file content: OK")

def test_distribution_to_string():
    #n = int(input('Between how many workers should the tasks be split? '))

    #workers = task_distribution.distribute_tasks(content, 2)
     input_ = """
    # [
    #     [[('Cook diner', 3)], 3]
    #     [[('Clean dishes', 1), ('Buy milk', 2)], 3],
    # ]"""
    #
    # output = task_distribution.distribution_to_string(input_)
    # expected_output = """Worker #1
    # Cook diner .............. 3h
    # Total time: 3h
    #
    # Worker #2
    # Buy milk ................ 2h
    # Clean dishes ............ 1h
    # Total time: 3h
    #
    # """
    #
    # assert output == expected_output, "{} -> {}".format(workers,output)
    #
    # print("test parse file content: OK")

def test_distribute_tasks():


    input_ = [('Buy milk', 2), ('Cook diner', 3), ('Clean dishes', 1)]

    expected_output = [[[('Cook diner', 3)], 3],[[('Buy milk', 2), ('Clean dishes', 1)], 3]]

    output = task_distribution.distribute_tasks(input_,2)

    assert output == expected_output

    print("test parse file content: OK")


if __name__ == "__main__":
    #test_parse_file_content()
    #test_distribution_to_string()
    test_distribute_tasks()
