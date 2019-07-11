# ======================================================================================================================
# Enter team members here:
# Name: Harsh Patel
# ID: 1892720
# Name: Ravi Darji
# ID: 1892903
# ======================================================================================================================

import pytransact


def test_is_visa():
    input=[
        ("4123-8956-7584-5263", True),
        ("41#3-89%6-75.4-52d3", False), # with special char and alphbatical char
        ("4-8956-7584-5263", True),
        ("4 8956 7584 5263", True),
        ("4895675845263", True),
        ("1-8956-7584-5263", False),
        ("14-8956-7584-5263", False), #with 14 digit with - and not start with 4
        ("41-8956-7584-5263", False), #with 14 digit with -
        ("4123-8956-7584-5263", True),

    ]

    for key, expected_output in input:
        output = pytransact.is_visa(key)
        assert output == expected_output, "({} -> {}), expected output ->  ({})".format(key,output,expected_output)

    print("test passed for is visa function...")

def test_is_valid_expiration():
    input=[
        ("01/23", True),
        ("01/023", False),
        ("1/23", False),
        ("0123", False),
        ("01 23", False),
        ("01 %$.23", False),
        ("01c23", False),
        ("13/23", False),
        ("01/00", False),
        ("13/23", False),
        ("13/100", False)
    ]

    for key, expected_output in input:
        output = pytransact.is_valid_expiration(key)
        assert output == expected_output, "({} -> {}), expected output ->  ({})".format(key,output,expected_output)

    print("test passed for test_is_valid_expiration function...")

def test_random_visa():
    random_cc = pytransact.random_visa()

    assert len(random_cc)==13 or len(random_cc)==16, "(Length of random cc({}) is {}. It should be either 13 or 16)".format(random_cc,len(random_cc))
    assert random_cc.startswith("4"), "((random_cc -> {}) -> random_cc should start with 4)".format(random_cc)
    assert random_cc.isdigit(), "((random_cc -> {}) -> random_cc should contains only digits, No char and No space.)".format(random_cc)
    assert '' in random_cc, "((random_cc -> {}) -> random_cc should not have any space)".format(random_cc)

    assert pytransact.is_visa(random_cc)

    print("test passed for test_random_visa function...")
if __name__ == "__main__":
    test_is_visa()
    test_is_valid_expiration()
    test_random_visa()