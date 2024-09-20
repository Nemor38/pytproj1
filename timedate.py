import datetime
print('Hi, What is your name?')
name = input('My name is:')
print('Nice to see you, ', name, 'what u want to know?')
print('1- Whats time')
print('2- Whats date')

choise = int(input(''))
date_time = datetime.datetime.now()

if choise == 1:
    print(date_time.time())

if choise == 2:
    print(date_time.date())