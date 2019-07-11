def is_visa(cc):
    cc = cc.replace(' ', '').replace('-', '')

    if len(cc) == 13 or len(cc) == 16:
        if cc.startswith('4'):
            return True
        else:
            return False
    else:
        return False


def is_valid_expiration(date):
    ...


def random_visa():
    ...
