import random
def is_visa(cc):
    cc = cc.replace(' ', '').replace('-', '')

    if len(cc) == 13 or len(cc) == 16:
        if cc.startswith('4') and cc.isdigit():
            return True
        else:
            return False
    else:
        return False


def is_valid_expiration(date):
    date = date.split("/")

    if(len(date)==2):
        month = date[0]
        year = date[1]
        if month.isdigit() and year.isdigit() and len(month)==2 and len(year)==2 and int(month) in range(1,13) and int(year) in range(1,100):
            return True
        else:
            return False
    else:
        return False



def random_visa():

    list  = [12, 15]
    length = random.choice(list)

    a = ''.join([str(random.randint(0,9)) for _ in range(length)])
    final_str="4"+a
    return final_str
