create database bank1;
use bank1;

#For Creating User details table
create table user_table(username varchar(25) primary key,password varchar(4) not null,phone_no varchar(12) not null);

#For creating customer_detail
create table customer_detail(account_no int(20) primary key,account_name varchar(40) NOT NULL,phone_no varchar(12),place varchar(20),amount int(30) NOT NULL);

#For Creating transaction_detail_credit
create table transaction_detail_credit(account_no int(20) NOT NULL,date date NOT NULL,amount_added int(30) NOT NULL,foreign key (account_no) references customer_detail (account_no) on delete cascade);

#For Creating transaction_detail_debit
create table transaction_detail_debit(account_no int(20) NOT NULL,date date NOT NULL,withdrawal_amount int(30)NOT NULL,foreign key (account_no) references customer_detail (account_no) on delete cascade);

#For Creating low_bala_account
create table Low_bala_account(account_no int(20) primary key,account_name varchar(40) NOT NULL,phone_no varchar(12),place varchar(20),amount int(30) NOT NULL,foreign key (account_no) references customer_detail (account_no) on delete cascade);

#for loans
create table loan(account_no int(20) NOT NULL,loan_type varchar(20),loan_amount int(8) NOT NULL,date date NOT NULL,intrest_rate varchar(2) not null,foreign key (account_no) references customer_detail (account_no) on delete cascade);



select * from user_table;
select * from low_bala_account;
select * from transaction_detail_credit;
select * from customer_detail;
select * from transaction_detail_debit;
select * from loan;
