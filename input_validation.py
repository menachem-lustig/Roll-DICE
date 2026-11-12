def valid_name():
    valid = False
    while not valid:
        name = input('Enter your name: ').strip()
        if name:
            valid = name
        else:
            print('Name cannot be empty.')
    return valid 


def valid_num(num,text):
    valid = False
    while not valid:
        try:
            num = int(input(text.strip()))
            if 0 < num < num + 1:
                valid = num
            else:
                print(f'Enter number only between 1-{str(num)}')
        except ValueError:
            print('Enter only number.')
    return valid
