from pandas import read_csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configure import db_string_connect
from model import Employee

df = read_csv('employees.csv')

engine = create_engine(db_string_connect, echo=False, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()
for surname, name, patronymic, birth_month, birth_year, department, telephone, electronic_mail in \
        df['surname'], df['name'], df['patronymic'], df['birth_month'], df['birth_year'], df['department'], \
        df['telephone'], df['electronic_mail']:
    employee = Employee(surname=surname, name=name, patronymic=patronymic, birth_month=birth_month,
                        birth_year=birth_year, department=department, telephone=telephone,
                        electronic_mail=electronic_mail)
    print(employee)
    session.add_all(employee)
    # results
    # for out in session.query(Employee).order_by(Employee.id):
    #     print(out)
session.commit()
session.close()
