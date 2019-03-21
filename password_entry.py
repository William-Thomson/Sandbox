""" William Thomson """

password = input('Enter password: ')
while len(password) <= 3:
    password = input('Invalid password. Enter Password')

print('*' * len(password))
