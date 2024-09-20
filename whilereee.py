

true_log = 'dimasik'
true_pass = 'karasik'
user_log = input ( 'Введи логин: ')
user_pass = input( 'Введи пароль: ')
while user_log != true_log or user_pass != true_pass:
    print ( 'Неверный логин или пароль')
    user_1og = input ( 'Введи логин: ')
    user_pass = input( 'Введи пароль: ')
else:
    print ( 'Вход выполнен' )