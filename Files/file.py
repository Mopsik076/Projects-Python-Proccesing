start = input('Вход или Регистрация?\n')

if start == 'Регистрация':
    login = input('Login: ')
    password = input('Password: ')
    with open('Files/database.txt', 'w') as f:
        f.write(login + ' ' + password)

if start == 'Вход':
    login = input('Login: ')
    password = input('Password: ')
    with open('Files/database.txt', 'r') as f:
        string = ''
        while 
            string = f.readline()
            string.split(' ')
        
