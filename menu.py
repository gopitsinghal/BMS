import mysql.connector as sqltor
import sys
import datetime as dt
sql_data=sqltor.connect(host='localhost',user='root',password='123456',database='bank1')
sql_cur=sql_data.cursor()
print('=======================================================Bank Management System=======================================================')
if sql_data.is_connected():
    print('Your database is Successfully connected')
else:
    print('Your database is not connected')
    sys.exit()



'''For creating customer_detail
sql_cur.execute('create table customer_detail(account_no varchar(20) primary key,account_name varchar(40) NOT NULL,phone_no varchar(10),place varchar(20),amount varchar(30) NOT NULL);')
'''

#function for Creating Bank Account
cba_query='insert into customer_detail values(%s,%s,%s,%s,%s)'
def create_bank_account():
    cbaaccno=input('Enter New Bank Account Number:')
    cbaname= input('Enter Your Name:')
    cbaphone=input('Enter Your Phone Number:')
    cbaplace=input('Enter Your Place :')
    cbamoney=input('Enter The Amount You Want to Deposit:')
    cba_values=(cbaaccno,cbaname,cbaphone,cbaplace,cbamoney)
    sql_cur.execute(cba_query,cba_values)
    sql_data.commit()
    print('========================Account Successfully Created========================')

'''For Creating transaction_detail
sql_cur.execute('create table transaction_detail(account_no varchar(20) NOT NULL,date date NOT NULL,withdrawal_amount varchar(30)NOT NULL,amount_added varchar(30) NOT NULL);')
'''

#Function for Transaction
tr_query='select * from customer_detail where account_no=%s;'
tr_query1='update customer_detail set amount=amount+%s where account_no=%s;'
tr_query2='insert into transaction_detail_credit values(%s,%s,%s);'
tr_query4='insert into transaction_detail_debit values(%s,%s,%s);'
tr_query3='update customer_detail set amount=amount-%s where account_no=%s;'
tr_wdamount=''
tr_values=''
tr_values1=''
tr_addamount=''

def transaction():
    tr_acc=input('Enter Your Account Number:')
    tr_accno=(tr_acc,)
    sql_cur.execute(tr_query,tr_accno)
    if sql_cur.fetchone() is None:
        print('Invalid Account Number')
    else:
        print('============================================================================================================================================')
        print('1. ADD AMOUNT')
        print('2. WITHDRAWAL AMOUNT')
        print('============================================================================================================================================')
        tr_choice=input('Enter Your Choice:')
        tr_choice=tr_choice.upper()
        if tr_choice=='1' or tr_choice=='ADD AMOUNT':
            tr_addamount=input('Enter The Amount You Want To Add:')
            tr_wdamount='0'
            tr_values=(tr_addamount,tr_acc)
            sql_cur.execute(tr_query1,tr_values)
            tr_values1=(tr_acc,dt.datetime.today(),tr_addamount)
            sql_cur.execute(tr_query2,tr_values1)
            sql_data.commit()
            print('====================================Amount Successfully Added=====================================')
        elif tr_choice=='2' or tr_choice=='WITHDRAWAL AMOUNT':
            tr_wdamount=input('Enter The Amount You want To Withdraw:')
            tr_addamount='0'
            tr_values=(tr_wdamount,tr_acc)
            sql_cur.execute(tr_query3,tr_values)
            tr_values1=(tr_acc,dt.datetime.today(),tr_wdamount)
            sql_cur.execute(tr_query4,tr_values1)
            sql_data.commit()
            print('====================================Amount Successfully withdrawn=================================')
#Function For Customer Details
cd_query='select * from customer_detail where account_no=%s ;'
def customer_details():
    cd_acc=input('Enter the Account Number:')
    cd_accno=(cd_acc,)
    sql_cur.execute(cd_query,cd_accno)
    cd_data=sql_cur.fetchone()
    print('Account Number:',cd_data[0],"Account Holder's Name:",cd_data[1],'Phone Number:',cd_data[2],'City:',cd_data[3],'Current Amount:',cd_data[4])
    sql_data.commit()


#Function For Transaction Details
t_query='select * from transaction_detail_credit where account_no=%s;'
t_query1='select * from transaction_detail_debit where account_no=%s;'
def transaction_details():
    t_acc=input('Enter Your Account Number:')
    print('============================================================================================================================================')
    print('1. Credit')
    print('2. Debit')
    print('============================================================================================================================================')
    td_choice = input('Enter Your Choice:')
    td_choice = td_choice.upper()
    if td_choice == '1' or td_choice == 'CREDIT':
        t_accno=(t_acc,)
        sql_cur.execute(t_query,t_accno)
        t_data=sql_cur.fetchall()
        t_count=sql_cur.rowcount
        print('===========================================================================================================================================')
        print('Transaction For Account Number:',t_accno[0])
        for t_row in t_data:
            print('Date:',t_row[1],'credited Amount:',t_row[2])
        print(' ')
        print('The Total Number Of Transactions are:',t_count)
        sql_data.commit()
    elif td_choice == '2' or td_choice == 'DEBIT':
        t_accno=(t_acc,)
        sql_cur.execute(t_query1,t_accno)
        t_data=sql_cur.fetchall()
        t_count=sql_cur.rowcount
        print('===========================================================================================================================================')
        print('Transaction For Account Number:',t_accno[0])
        for t_row in t_data:
            print('Date:',t_row[1],'DEBITED Amount:',t_row[2])
        print(' ')
        print('The Total Number Of Transactions are:',t_count)
        sql_data.commit()

#function to display all  the account with low balance
lb_query="select * from low_bala_account;"
def low_balance():
    sql_cur.execute(lb_query)
    lb_data=sql_cur.fetchall()
    for lb_row in lb_data:
        print('Account Number:',lb_row[0],"Account Holder's Name:",lb_row[1],'Phone Number:',lb_row[2],'City:',lb_row[3],'Current Amount:',lb_row[4])

    sql_data.commit()

#function For Delete Account
da_query='delete from customer_detail where account_no=%s '
def delete_account():
    da_acc=input('Enter The Account Number:')
    da_accno=(da_acc,)
    sql_cur.execute(da_query,da_accno)
    print('====================================Account Successfully Deleted=====================================')
    sql_data.commit()


#function for requesting loan
lo_query = 'select * from customer_detail where account_no = %s ;'
lo_query1 = 'insert into loan values(%s,%s,%s,%s,%s);'
lo_query2 = 'update customer_detail set amount=amount+%s where account_no=%s;'

def req_loan():
    lo_acc = input('Enter the account number:')
    lo_accno = (lo_acc, )
    sql_cur.execute(lo_query, lo_accno)
    if sql_cur.fetchone() is None:
        print('Invalid Account Number')
    else:
        print('=========================================================================')
        print('1. HOME LOAN INTREST RATE:7%')
        print('2. EDUCATION LOAN INTREST RATE:13%')
        print('3. PERSONAL LOAN INTREST RATE:9%')
        print('4. BUISNESS LOAN INTREST RATE:5%')
        lo_type = input('enter the loan type:')
        lo_irate = input('enter the intrest rate:')
        lo_amt = input('enter the amount required:')
        lo_values = (lo_acc, lo_type, lo_amt, dt.datetime.today(), lo_irate)
        sql_cur.execute(lo_query1, lo_values)
        lo_cred = (lo_amt, lo_acc)
        sql_cur.execute(lo_query2, lo_cred)
        print('=====================loan sanctioned=====================================')
        sql_data.commit()


#Taking User's Choice
menu_choice='0'

while menu_choice!='6' or menu_choice!='QUIT':
    print(
        '============================================================================================================================================')
    print('1. CREATE BANK ACCOUNT')
    print('2. TRANSACTION')
    print('3. CUSTOMER DETAILS')
    print('4. TRANSACTION DETAILS')
    print('5. LOAN')
    print('6. LOW BALANCE ACCOUNT')
    print('7. DELETE ACCOUNT')
    print('8. QUIT')
    print('============================================================================================================================================')
    menu_choice = input('Enter Your Choice:')
    menu_choice = menu_choice.upper()
    if menu_choice == '1' or menu_choice == 'CREATE BANK ACCOUNT':
        create_bank_account()
    elif menu_choice == '2' or menu_choice == 'TRANSACTION':
        transaction()
    elif menu_choice == '3' or menu_choice == 'CUSTOMER DETAILS':
        customer_details()
    elif menu_choice == '4' or menu_choice == 'TRANSACTION DETAILS':
        transaction_details()
    elif menu_choice == '5' or menu_choice == 'LOAN':
        req_loan()
    elif menu_choice == '6' or menu_choice == 'LOW BALANCE ACCOUNT':
        low_balance()
    elif menu_choice == '7' or menu_choice == 'DELETE ACCOUNT':
        delete_account()
    elif menu_choice == '8' or menu_choice == 'QUIT':
        sys.exit()
    else:
        print('Invalid Choice')
        break
