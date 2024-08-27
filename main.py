import mysql.connector as sqltor
import sys
from os import system

sql_data=sqltor.connect(host='localhost',user='root',password='123456',database='bank1')
sql_cur=sql_data.cursor()
print('=======================================================Bank Management System=======================================================')
if sql_data.is_connected():
    print('Your database is Successfully connected')
else:
    print('Your database is not connected')
    sys.exit()



'''For Creating User details table  
sql_cur.execute('create table user_table(username varchar(25) primary key,password varchar(4) not null,phone_no varchar(12) not null);')
'''
try:
    # Function For register
    nu_query = 'insert into user_table values(%s,%s,%s)'


    def register():
        newuser = input('Enter the new user name:')
        password = input('Enter a 4 digit password:')
        phoneno = input('Enter your phone number:')
        nu_values = (newuser, password, phoneno)
        sql_cur.execute(nu_query, nu_values)
        print('User Successfully created')
        #    system('cls')
        sql_data.commit()


    # Function For Login
    lg_query = "select * from user_table where username=%s and password=%s;"


    def login():
        exuser = input('Enter your User Name:')
        expassword = input('Enter your 4 digit password:')
        lg_values = (exuser, expassword)
        sql_cur.execute(lg_query, lg_values)
        if sql_cur.fetchone() is None:
            print('Invalid User name or Password')
        else:
            print(
                '=======================================================Successfully Login=======================================================')
            import menu.py


    # taking User Choice
    choice = '0'
    while choice != '3' or choice != 'EXIT':
        print(
            '============================================================================================================================================')
        print('1. REGISTER')
        print('2. LOGIN')
        print('3. EXIT')
        print(
            '============================================================================================================================================')
        choice = input('Enter Your Choice:')
        choice = choice.upper()
        if choice == 'REGISTER' or choice == '1':
            register()
        elif choice == 'LOGIN' or choice == '2':
            login()
        elif choice == 'EXIT' or choice == '3':
            sys.exit()
        else:
            print('Invalid Choice')
            break
    sql_data.close()
except Exception as e:
    err_str=str(e)
    print(e)
    err_str=err_str.split()
    if err_str[0]=='1415':
        print("Cannot proceed due to trigger Withdrawa`l amount too high.")

