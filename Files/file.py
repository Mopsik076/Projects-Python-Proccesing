while True:
    start = input('Sign in or Sign up?\n')

    if start == 'Sign up':
        login = input('Login: ')
        password = input('Password: ')
        with open('C:/Users/Креайтивика/Desktop/Projects Python Proccesing/Files/database.txt', 'w') as f:
            f.write(login + '\n' + password)

    if start == 'Sign in':
        flag = 1
        login = input('Login: ').rstrip()
        password = input('Password: ').rstrip()
        with open('C:/Users/Креайтивика/Desktop/Projects Python Proccesing/Files/database.txt', 'r') as f:

            doc = f.read()
            strings = doc.split('\n')
            for k in strings:
                tmp = k.split(' ')
                print(tmp)
                if tmp[0] == login and tmp[1] == password:
                    flag = 0
        if flag == 1:
            print('Not correct')
        else:
            print('amazing')


