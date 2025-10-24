import csv

def auth(login, password):
    global data
    if data.get(login) == None:
        return False
    if data[login] == password:
        return True
    if data[login] != password:
        return False

def registration(login, password):
    global data
    if auth(login, password):
        return "Вы уже зарегистрированы "
    data[login] = password
    save_data(login, password)


def save_data(login, password):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([login, password])

filename = 'users.csv'


with open(filename, newline='', encoding='utf-8')as f:
    reader = csv.reader(f)
    data = {rows[0]: rows[1] for rows in reader}




while True:
    print("Желаете войти или зарегистрировать?(1/2)\nдля завершения работы выберите 0")
    decidion = int(input())
    if decidion == 1:
        login = input("Login: ")
        password = input("Password: ")
        auth(login, password)
        if auth(login, password) == False:
            print("Неверный логин или пароль")
        if auth(login, password) == True:
            print("вам доступен Странный переводчик")
            exec(open("strange.py", encoding='UTF-8').read())

    if decidion == 2:
        print("Введите данные для регистрации")
        login = input("Login: ")
        password = input("Password: ")
        registration(login, password)
    if decidion == 0:
        break
    print(data)

