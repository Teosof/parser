from pandas import read_csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configure import db_string_connect
from model import Employee

df = read_csv('employees.csv', delimiter=',',
              names=['surname', 'name', 'patronymic', 'birth_month', 'birth_year', 'department', 'telephone',
                     'electronic_mail'])
engine = create_engine(db_string_connect, echo=False, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()
for d in df:
    employee = Employee(surname=df['surname'], name=df['name'], patronymic=df['patronymic'],
                        birth_month=df['birth_month'], birth_year=df['birth_year'], department=df['department'],
                        telephone=df['telephone'], electronic_mail=df['electronic_mail'])
    session.add_all(employee)
    # results
    # for out in session.query(Employee).order_by(Employee.id):
    #     print(out)
session.commit()
session.close()
