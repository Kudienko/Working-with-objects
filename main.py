import colorama
import pickle
colorama.init()
from colorama import Fore, Back, Style
# pip install colorama
# persons = {
#     "Александр": {
#         'Возраст': 27,
#         'Телефон': 89129051090,
#         'Почта': 'Kudienko2016@mail.ru',
#         'Тип': 'Дневной',
#         'Тренер': False,
#         'Занятия': ['Тайский бокс','Аэробика','Плавнание']
#     },
#     "Ольга": {
#         'Возраст': 18,
#         'Телефон': 89227666339,
#         'Почта': 'Abudabi777@yandex.ru',
#         'Тип': 'Безлимит',
#         'Тренер': False,
#         'Занятия': ['Стретчинг','Аэробика']
#     },
#     "Денис": {
#         'Возраст': 50,
#         'Телефон': 89123456789,
#         'Почта': 'Big_Denis@gmail.com',
#         'Тип': 'Безлимит',
#         'Тренер': True,
#         'Занятия': ['Стретчинг','Стрип-пластика']
#     },
#     "Александра": {
#         'Возраст': 22,
#         'Телефон': 89987654321,
#         'Почта': 'Alex1999@yandex.ru',
#         'Тип': 'Дневной',
#         'Тренер': True,
#         'Занятия': ['Вольная борьба']
#     },
#     "Георгий": {
#         'Возраст': 33,
#         'Телефон': 89195732922,
#         'Почта': 'Mamba3000@mail.ru',
#         'Тип': 'Безлимит',
#         'Тренер': True,
#         'Занятия': ['Сальса']
#     }
# }
with open('data.pickle', 'rb') as f:
    persons = pickle.load(f)
emotion = input(Fore.CYAN +"""
Список клиентов -> нажмите 1
Поиск клиента -> нажмите 2 
Добавление клиента -> нажмите 3
Удаление клиента -> нажмите 4 
Показать только тех, у кого есть личный тренер -> нажмите 5
Средний возраст клиентов  -> нажмите 6  
""" + Style.RESET_ALL)
if emotion == "1":
    persons = {}
    with open('data.pickle', 'rb') as f:
        persons = pickle.load(f)
    for username,userinfo in persons.items():
        print(Fore.GREEN + f"Имя клиента: {username}" + Style.RESET_ALL)
        print('-' * 20)
        print(Fore.BLUE + f"Возраст клиента: {userinfo['Возраст']}")
        print(f"Телефон клиента: {userinfo['Телефон']}")
        print(f"Почта клиента: {userinfo['Почта']}")
        print(f"Тип абонемента клиента: {userinfo['Тип']}")
        print(f"Занятия клиента:")
        for value in userinfo['Занятия']:
            print(value)
        if userinfo['Тренер'] == True:
            print("У данного клиента есть личный тренер" + Style.RESET_ALL)
        else:
            print("У данного клиента нет личного тренера" + Style.RESET_ALL)
        print('-' * 30 + '\n')
elif emotion == "5":
    for username, userinfo in persons.items():
        if userinfo['Тренер'] == True:
            print(Fore.LIGHTMAGENTA_EX + username + Style.RESET_ALL)
elif emotion == "6":
        i = len(persons)
        summa = 0
        for username, userinfo in persons.items():
             summa += int(userinfo['Возраст'])
        avgAge = summa / i
        print(Fore.LIGHTMAGENTA_EX + f"Средний возраст всех клиентов: {round(avgAge)}" + Style.RESET_ALL)
elif emotion == "2":
    klient = input(Fore.CYAN + "Введите имя клиента с заглавной буквы о котором хотите получить информацию:\n" + Style.RESET_ALL)
    if persons.get(klient) != None:
        print(persons.get(klient)['Возраст'])
        print(Fore.GREEN + f"Имя клиента: {klient}" + Style.RESET_ALL)
        print('-' * 20)
        print(Fore.BLUE + f"Возраст клиента: {persons.get(klient)['Возраст']}")
        print(f"Телефон клиента: {persons.get(klient)['Телефон']}")
        print(f"Почта клиента: {persons.get(klient)['Почта']}")
        print(f"Тип абонемента клиента: {persons.get(klient)['Тип']}")
        print(f"Занятия клиента:")
        for value in persons.get(klient)['Занятия']:
            print(value)
        if persons.get(klient)['Тренер'] == True:
            print("У данного клиента есть личный тренер" + Style.RESET_ALL)
        else:
            print("У данного клиента нет личного тренера" + Style.RESET_ALL)
        print('-' * 30 + '\n')
    else:
        print(Fore.RED + "Данного клиента не существует" + Style.RESET_ALL)
elif emotion == "3":
    klient = input(Fore.CYAN + "Введите имя клиента\n" + Style.RESET_ALL).title()
    age = input(Fore.CYAN + "Введите его возраст\n" + Style.RESET_ALL)
    mobile = input(Fore.CYAN + "Введите его телефон\n" + Style.RESET_ALL)
    email = input(Fore.CYAN + "Введите его почту\n" + Style.RESET_ALL).title()
    type = input(Fore.CYAN + """
    Какой тип абонемента у клиента?
    Дневной -> нажмите 1
    Безлимит -> нажмите 2
    """ + Style.RESET_ALL)
    if type == "1":
        type = "Дневной"
    else:
        type = "Безлимит"
    couch = input(Fore.CYAN + """
    Есть ли тренер у клиента?
    Да -> нажмите 1
    Нет -> нажмите 2
    """ + Style.RESET_ALL)
    if couch == "1":
        couch = True
    else:
        couch = False
    spisok = input(Fore.CYAN + "Введите через запятую занятия, на которые будет ходить клиент:\n" + Style.RESET_ALL).split(',')
    persons[klient] = {}
    persons[klient]['Возраст'] = age
    persons[klient]['Телефон'] = mobile
    persons[klient]['Почта'] = email
    persons[klient]['Тип'] = type
    persons[klient]['Тренер'] = couch
    persons[klient]['Занятия'] = spisok
    with open('data.pickle', 'wb') as f:
        pickle.dump(persons, f)
    for username, userinfo in persons.items():
        print(Fore.GREEN + f"Имя клиента: {username}" + Style.RESET_ALL)
        print('-' * 20)
        print(Fore.BLUE + f"Возраст клиента: {userinfo['Возраст']}")
        print(f"Телефон клиента: {userinfo['Телефон']}")
        print(f"Почта клиента: {userinfo['Почта']}")
        print(f"Тип абонемента клиента: {userinfo['Тип']}")
        print(f"Занятия клиента:")
        for value in userinfo['Занятия']:
            print(value)
        if userinfo['Тренер'] == True:
            print("У данного клиента есть личный тренер" + Style.RESET_ALL)
        else:
            print("У данного клиента нет личного тренера" + Style.RESET_ALL)
        print('-' * 30 + '\n')
elif emotion == "4":
    with open('data.pickle', 'rb') as f:
        persons = pickle.load(f)
    print(Fore.CYAN + "Имена клиента:" + Style.RESET_ALL)
    for value in persons.keys():
        print(Fore.GREEN + f"{value}" + Style.RESET_ALL)
    name = input("Введите имя клиента которого хотите удалить")
    try:
        persons.pop(name)
    except:
        print(Fore.RED + "Такого клиента не существует" + Style.RESET_ALL)
    with open('data.pickle', 'wb') as f:
        pickle.dump(persons, f)
    print(Fore.CYAN + "Клиент успешно удален" + Style.RESET_ALL)
else:
    print( Fore.RED + "Такой команды не существует" + Style.RESET_ALL)