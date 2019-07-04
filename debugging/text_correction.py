import re

conversion_table = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
}

def convert_number(num):
    return conversion_table.get(num)

def apply_correction(text):
    # split the text into words and spaces
    splitted_text = re.findall(r"[\.,:;\s]+|[^\.,:;\s]+", text)

    for i, word in enumerate(splitted_text):
        print(type(word))
        try:
            if(word.isdigit()):
                value = int(word)
                print(value)
                if value < len(conversion_table):
                    splitted_text[i] = convert_number(value)
        except ValueError:
            # The word is not an integer
            pass

    return "".join(splitted_text)

if __name__ == "__main__":
    file_name = input("Enter a file name to convert: ")
    with open(file_name, "r") as f:
        file_content = f.read()

    converted_content = apply_correction(file_content)

    with open(file_name + ".corrected", "w") as f:
        f.write(converted_content)

