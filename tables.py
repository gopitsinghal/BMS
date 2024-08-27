import mysql.connector as sqltor
import sys
sql_data=sqltor.connect(host='localhost',user='root',password='123456',database='bank1')
sql_cur=sql_data.cursor()

if sql_data.is_connected():
    print('Your database is Successfully connected')
else:
    print('Your database is not connected')
    sys.exit()


#For Creating User details table
sql_cur.execute('create table user_table(username varchar(25) primary key,password varchar(4) not null,phone_no varchar(12) not null);')

#For creating customer_detail
sql_cur.execute('create table customer_detail(account_no int(20) primary key,account_name varchar(40) NOT NULL,phone_no varchar(12),place varchar(20),amount int(30) NOT NULL);')

#For Creating transaction_detail_credit
sql_cur.execute('create table transaction_detail_credit(account_no int(20) NOT NULL,date date NOT NULL,amount_added int(30) NOT NULL,foreign key (account_no) references customer_detail (account_no) on delete cascade);')

#For Creating transaction_detail_debit
sql_cur.execute('create table transaction_detail_debit(account_no int(20) NOT NULL,date date NOT NULL,withdrawal_amount int(30)NOT NULL,foreign key (account_no) references customer_detail (account_no) on delete cascade);')

#For Creating low_bala_account
sql_cur.execute('create table Low_bala_account(account_no int(20) primary key,account_name varchar(40) NOT NULL,phone_no varchar(12),place varchar(20),amount int(30) NOT NULL,foreign key (account_no) references customer_detail (account_no));')

#for loans
sql_cur.execute('create table loan(account_no int(20) NOT NULL,loan_type varchar(20),loan_amount int(8) NOT NULL,date date NOT NULL,intrest_rate varchar(2) not null,foreign key (account_no) references customer_detail (account_no));')



