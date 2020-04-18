from csv import DictWriter
from russian_names import RussianNames
from datetime import datetime
from random import randint


def set_birth_month() -> str:
    month: list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    return month[randint(a=0, b=len(month) - 1)]


def set_birth_year() -> int:
    return datetime.now().year - randint(a=0, b=100)


def set_department() -> str:
    return "IT"


def set_telephone() -> str:
    return f"8495{randint(a=0, b=999)}{randint(a=0, b=99)}{randint(a=0, b=99)}"


with open(file='employees.csv', mode='w') as csv_file:
    fieldnames: list = ['surname', 'name', 'patronymic', 'birth_month', 'birth_year', 'department', 'telephone',
                        'electronic_mail']
    writer = DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for e in range(2000000):
        full_name: list = RussianNames(surname=True, name=True, patronymic=True,
                                       transliterate=True).get_person().lower().split(' ')
        surname: str = full_name[2]
        name: str = full_name[0]
        patronymic: str = full_name[1]
        writer.writerow({'surname': surname,
                         'name': name,
                         'patronymic': patronymic,
                         'birth_month': set_birth_month(),
                         'birth_year': set_birth_year(),
                         'department': set_department(),
                         'telephone': set_telephone(),
                         'electronic_mail': f'{surname}@yandex.ru'})
