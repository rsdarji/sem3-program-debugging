def print_account(account):
    year = account['year']
    amount = account['amount']
    print('After {} years, you have  {:.2f}$'.format(year, amount))
    account['year'] += 1

def compute_interests(account, rate=0.03):

    return account['amount'] * rate

def play_year(account):

    account['amount'] += compute_interests(account)
    print_account(bank_account)


if __name__ == '__main__':
    print('Welcome to bank simulator!')
    print('This program allows you to simulate interests of your personal finances.')

    while True:
        init_amount = input('Please enter the initial amount of your account ($): ')
        try:
            amount = float(init_amount)
            break
        except ValueError:
            print('This is not a valid amount. Try again.')

    bank_account = {
        'year': 1,
        'amount': amount
    }

    while True:
        play_year(bank_account)
        command = input('Enter exit to leave, anything else to continue')
        if command == 'exit':
            print('Thank you!')
            break
        else:
            play_year(bank_account)
