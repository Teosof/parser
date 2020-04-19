from sqlalchemy import Column, INTEGER, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employee(Base):
    """
    Модель, описывающего таблицу Работник
    """
    __tablename__: str = "Employee"

    id = Column(INTEGER, primary_key=True)
    surname = Column(INTEGER)
    name = Column(INTEGER)
    patronymic = Column(TEXT)
    birth_month = Column(TEXT)
    birth_year = Column(INTEGER)
    department = Column(TEXT)
    telephone = Column(TEXT)
    electronic_mail = Column(TEXT)

    def __init__(self, surname, name, patronymic, birth_month, birth_year, department, telephone, electronic_mail):
        """
        Инициализация полей таблицы
        :param surname: фамилия
        :param name: имя
        :param patronymic: отчество
        :param birth_month: месяц рождения
        :param birth_year: год рождения
        :param department: отдел
        :param telephone: номер телефона
        :param electronic_mail: электронная почта
        """
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.department = department
        self.telephone = telephone
        self.electronic_mail = electronic_mail

    def __repr__(self):
        """
        Переопределение функции print() для возможности вывода в консоль
        :return: демонстрация данных в консоль
        """
        return f"Surname: {self.surname}," \
               f"Name: {self.name}," \
               f"Patronymic: {self.patronymic}," \
               f"Birth Month: {self.birth_month}," \
               f"Birth Year: {self.birth_year}," \
               f"Department: {self.department}," \
               f"Telephone: {self.telephone}," \
               f"E-mail: {self.electronic_mail}"
