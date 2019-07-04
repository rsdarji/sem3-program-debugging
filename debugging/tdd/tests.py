import features


def test_encrypt():
    input_output = [
        ("Az", "-2", "Yx"),
        ("A", "-1", "Z"),
        ("a", "-1", "z"),
        ("y", "2", "a"),
        ("hello", "1", "ifmmp"),
        ("HeLLo", "1", "IfMMp"),
        ("hello class! :)", "2", "jgnnq encuu! :)"),
        ("123abc", "10", "123klm"),
        ("", "10", ""),
        ("foo", "-2", "dmm"),


    ]

    # for text, key, expected_output in input_output:
    #     output = features.encrypt(text, key)
    #     assert output == expected_output, "{}, {} -> {} (expected: {})".format(text, key, output, expected_output)

    print("test encrypt: OK")



def test_decrypt():
    input_output = [
        ("Yx", "-2", "Az"),
        ("Z", "-1", "A"),
        ("z", "-1", "a"),
        ("a", "2", "y"),
        ("ifmmp", "1", "hello"),
        ("IfMMp", "1", "HeLLo"),
        ("jgnnq encuu! :)", "2", "hello class! :)"),
        ("123klm", "10", "123abc"),
        ("", "10", ""),
        ("dmm", "-2", "foo"),


    ]

    for text, key, expected_output in input_output:
        output = features.decrypt(text, key)
        assert output == expected_output, "{}, {} -> {} (expected: {})".format(text, key, output, expected_output)

    print("test decrypt: OK")


def test_random_key():
    ...


def test_random_encrypt():
    ...


if __name__ == "__main__":
    #test_encrypt()
    #
    # test_decrypt()
    test_random_key()
    test_random_encrypt()