import html_formatter


def test_is_closing_tag():

    input=[("</p>",True),("</body>",True),("some text",False),("</",False)]
    for input,expected_output in input:

        output = html_formatter.is_closing_tag(input)

        assert output == expected_output, "input: {} -> Expected output: {}".format(input,output)




    print("test parse file content: OK")


def test_is_opening_tag():
    input=[("<a option=value>",True),("</body>",False),("some text",False),("<",False)]
    for input,expected_output in input:

        output = html_formatter.is_closing_tag(input)

        assert output == expected_output, "input: {} -> Expected output: {}".format(input,output)




    print("test parse file content: OK")


def test_format_with_indentation():
    ...


if __name__ == "__main__":
    test_is_closing_tag()
    test_is_opening_tag()
    test_format_with_indentation()
