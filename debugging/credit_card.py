import re

# Regular expressions to recognize credit card types
mastercard_pattern = r'5[1-5]\d{14}'
visa_pattern = r'4\d{12}(\d{3})?'
amex_pattern = r'3[47]\d{13}'


def is_mastercard_number(cc):
    if re.fullmatch(mastercard_pattern, cc):
        return True
    else:
        return False


def is_visa_number(cc):
    if re.fullmatch(visa_pattern, cc):
        return True
    else:
        return False


def is_amex_pattern(cc):
    if re.fullmatch(amex_pattern, cc):
        return True
    else:
        return False


def get_credit_card_type(cc):
    if is_mastercard_number(credit_card_number):
        return 'mastercard'
    elif is_visa_number(credit_card_number):
        return 'visa'
    elif is_amex_pattern(credit_card_number):
        return 'amex'
    else:
        return None


def hide_credit_card_number(cc):
    # Make a copy of the credit card number
    hidden_cc = cc[:]

    # Hide all characters with * except the three last ones
    for i in range(len(cc) - 3):
        hidden_cc[i] = '*'

    return hidden_cc


if __name__ == "__main__":
    while True:
        credit_card_number = input("Credit Card Number: ")
        credit_card_type = get_credit_card_type(credit_card_number)

        if credit_card_type is not None:
            break
        else:
            print('This is not a valid credit card number...')

    hidden_credit_card_number = hide_credit_card_number(credit_card_number)
    print('You entered a valid {} number: {}'.format(credit_card_type, hidden_credit_card_number))
