while True:
import mysql.connector as b
a= b.connect(host="localhost", user="root",
password="root",database="covid")
mycursor = a.cursor()
mycursor.execute("create table COVAXIN_1(C_CODE int PRIMARY KEY,C_NAME
varchar(30),PINCODE int,AREA varchar(30),NOD12TO18 int,NOD18TO45
int,NOD45ABOVE int)")
mycursor.execute("create table COVISHIELD_1(C_CODE int PRIMARY
KEY,C_NAME varchar(30),PINCODE int,AREA varchar(30),NOD12TO18
int,NOD18TO45 int,NOD45ABOVE int)")
mycursor.execute("create table COVAXIN_2(C_CODE int PRIMARY KEY,C_NAME
varchar(30),PINCODE int,AREA varchar(30),NOD12TO18 int,NOD18TO45
int,NOD45ABOVE int)")
mycursor.execute("create table COVISHIELD_2(C_CODE int PRIMARY
KEY,C_NAME varchar(30),PINCODE int,AREA varchar(30),NOD12TO18
int,NOD18TO45 int,NOD45ABOVE int)")
mycursor.execute("create table COVAXIN_BOOSTER(C_CODE int PRIMARY
KEY,C_NAME varchar(30),PINCODE int,AREA varchar(30),NOD12TO18
int,NOD18TO45 int,NOD45ABOVE int)")
mycursor.execute("create table COVISHIELD_BOOSTER(C_CODE int PRIMARY
KEY,C_NAME varchar(30),PINCODE int,AREA varchar(30),NOD12TO18
int,NOD18TO45 int,NOD45ABOVE int)")
mycursor.execute("create table RECORD(AADHAR_NO int PRIMARY KEY,NAME
varchar(30),AGE int,GENDER varchar(1),MOBILE_NO
varchar(10),VACCINE_NAME char(20),FD char(3),SD char(3),BD char(3))")
print("--------------------------------------------------------------WELCOME TO
COVISAFE-----------------------------------------------------------------------------")
print("Help us know whether you are programmer or user")
print()
print("IF YOU ARE PROGRAMMER ENTER P")
print("IF YOU ARE USER ENTER U")
print("IF YOU WANT TO LEAVE ENTER L")
print()
enter = input("Enter: ")
print()
print("----------------------------------------------------------------------------------------------
---------------------------------------------")
# coding for changing the records by the programmer
if enter == 'P':
progid = 'prog@123'
login_id= input("Enter the programmer id:")
if login_id == progid:
u = 'yes'
while u== "yes":
print()
print("ENTER 1 FOR UPDATING RECORDS FOR COVISHIELD DOSE#1")
print("ENTER 2 FOR UPDATING RECORDS FOR COVISHIELD DOSE#2")
print("ENTER 3 FOR UPDATING RECORDS FOR COVAXIN DOSE#1")
print("ENTER 4 FOR UPDATING RECORDS FOR COVAXIN DOSE#2")
print("ENTER 5 FOR UPDATING RECORDS FOR COVISHIELD BOOSTER
DOSE")
print("ENTER 6 FOR UPDATING RECORDS FOR COVAXIN BOOSTER
DOSE")
ch= int(input("Enter your choice:"))
if ch == 1:
a= b.connect(host="localhost", user="root",
password="root",database="covid")
mycursor = a.cursor()
print("Enter 1 to update existing record")
print("Enter 2 to add a new record")
print("Enter 3 to delete a record")
entry = int(input("Enter choice : "))
if entry == 1:
code = int(input("enter the vaccination centre code to be updated:"))
age = int(input("enter 12 for 12-18,enter 18 for 18-45 and 45 for 45
and above:"))
if age == 12:
slots = int(input("Enter the number of slots left:"))
mycursor.execute("update covishield_1 set NOD12TO18='{}' where
c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif age==18:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covishield_1 set NOD18TO45='{}' where
c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
else:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covishield_1 set NOD45ABOVE='{}'
where c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif entry == 2:
code=int(input("Enter the vaccination centre code:"))
name=input("Enter the vaccination centre name:")
pin=int(input("Enter the pin code of the area:"))
area=input("Enter the area of the centre:")
slots_12to18=int(input("Enter the slots left for 12 to 18:"))
slots_18to45=int(input("Enter the slots left for 18 to 45:"))
slots_45above=int(input("Enter the slots left for 45 and above:"))
mycursor.execute("insert into covishield_1
values({},'{}',{},'{}',{},{},{})".format(code,name,pin,area,slots_12to18,slots_18to45,s
lots_45above))
a.commit()
print("ADDITION SUCCESSFUL")
elif entry == 3:
code=int(input("enter the vaccination centre code:"))
mycursor.execute("delete from covishield_1 where
c_code={}".format(code))
a.commit()
print("DELETION SUCCESSFUL")
if ch == 2:
a= b.connect(host="localhost", user="root",
password="root",database="covid")
mycursor = a.cursor()
print("Enter 1 to update existing record")
print("Enter 2 to add a new record")
print("Enter 3 to delete a record")
entry = int(input("Enter choice : "))
if entry == 1:
code = int(input("enter the vaccination centre code to be updated:"))
age = int(input("enter 12 for 12-18,enter 18 for 18-45 and 45 for 45
and above:"))
if age == 12:
slots = int(input("Enter the number of slots left:"))
mycursor.execute("update covishield_2 set NOD12TO18='{}' where
c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif age==18:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covishield_2 set NOD18TO45='{}' where
c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
else:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covishield_2 set NOD45ABOVE='{}'
where c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif entry == 2:
code=int(input("Enter the vaccination centre code:"))
name=input("Enter the vaccination centre name:")
pin=int(input("Enter the pin code of the area:"))
area=input("Enter the area of the centre:")
slots_12to18=int(input("Enter the slots left for 12 to 18:"))
slots_18to45=int(input("Enter the slots left for 18 to 45:"))
slots_45above=int(input("Enter the slots left for 45 and above:"))
mycursor.execute("insert into covishield_2
values({},'{}',{},'{}',{},{},{})".format(code,name,pin,area,slots_12to18,slots_18to45,s
lots_45above))
a.commit()
print("ADDITION SUCCESSFUL")
elif entry == 3:
code=int(input("enter the vaccination centre code:"))
mycursor.execute("delete from covishield_2 where
c_code={}".format(code))
a.commit()
print("DELETION SUCCESSFUL")
if ch == 3:
a= b.connect(host="localhost", user="root",
password="root",database="covid")
mycursor = a.cursor()
print("Enter 1 to update existing record")
print("Enter 2 to add a new record")
print("Enter 3 to delete a record")
entry = int(input("Enter choice : "))
if entry == 1:
code = int(input("enter the vaccination centre code to be updated:"))
age = int(input("enter 12 for 12-18,enter 18 for 18-45 and 45 for 45
and above:"))
if age == 12:
slots = int(input("Enter the number of slots left:"))
mycursor.execute("update covaxin_1 set NOD12TO18='{}' where
c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif age==18:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covaxin_1 set NOD18TO45='{}' where
c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
else:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covaxin_1 set NOD45ABOVE='{}' where
c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif entry == 2:
code=int(input("Enter the vaccination centre code:"))
name=input("Enter the vaccination centre name:")
pin=int(input("Enter the pin code of the area:"))
area=input("Enter the area of the centre:")
slots_12to18=int(input("Enter the slots left for 12 to 18:"))
slots_18to45=int(input("Enter the slots left for 18 to 45:"))
slots_45above=int(input("Enter the slots left for 45 and above:"))
mycursor.execute("insert into covaxin_1
values({},'{}',{},'{}',{},{},{})".format(code,name,pin,area,slots_12to18,slots_18to45,s
lots_45above))
a.commit()
print("ADDITION SUCCESSFUL")
elif entry == 3:
code=int(input("enter the vaccination centre code:"))
mycursor.execute("delete from covaxin_1 where
c_code={}".format(code))
a.commit()
print("DELETION SUCCESSFUL")
if ch == 4:
a= b.connect(host="localhost", user="root",
password="root",database="covid")
mycursor = a.cursor()
print("Enter 1 to update existing record")
print("Enter 2 to add a new record")
print("Enter 3 to delete a record")
entry = int(input("Enter choice : "))
if entry == 1:
code = int(input("enter the vaccination centre code to be updated:"))
age = int(input("enter 12 for 12-18,enter 18 for 18-45 and 45 for 45
and above:"))
if age == 12:
slots = int(input("Enter the number of slots left:"))
mycursor.execute("update covaxin_2 set NOD12TO18='{}' where
c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif age==18:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covaxin_2 set NOD18TO45='{}' where
c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
else:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covaxin_2 set NOD45ABOVE='{}' where
c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif entry == 2:
code=int(input("Enter the vaccination centre code:"))
name=input("Enter the vaccination centre name:")
pin=int(input("Enter the pin code of the area:"))
area=input("Enter the area of the centre:")
slots_12to18=int(input("Enter the slots left for 12 to 18:"))
slots_18to45=int(input("Enter the slots left for 18 to 45:"))
slots_45above=int(input("Enter the slots left for 45 and above:"))
mycursor.execute("insert into covaxin_2
values({},'{}',{},'{}',{},{},{})".format(code,name,pin,area,slots_12to18,slots_18to45,s
lots_45above))
a.commit()
print("ADDITION SUCCESSFUL")
elif entry == 3:
code=int(input("enter the vaccination centre code:"))
mycursor.execute("delete from covaxin_2 where
c_code={}".format(code))
a.commit()
print("DELETION SUCCESSFUL")
if ch == 5:
a= b.connect(host="localhost", user="root",
password="root",database="covid")
mycursor = a.cursor()
print("Enter 1 to update existing record")
print("Enter 2 to add a new record")
print("Enter 3 to delete a record")
entry = int(input("Enter choice : "))
if entry == 1:
code = int(input("enter the vaccination centre code to be updated:"))
age = int(input("enter 12 for 12-18,enter 18 for 18-45 and 45 for 45
and above:"))
if age == 12:
slots = int(input("Enter the number of slots left:"))
mycursor.execute("update covishield_booster set NOD12TO18='{}'
where c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif age==18:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covishield_booster set NOD18TO45='{}'
where c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
else:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covishield_booster set
NOD45ABOVE='{}' where c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif entry == 2:
code=int(input("Enter the vaccination centre code:"))
name=input("Enter the vaccination centre name:")
pin=int(input("Enter the pin code of the area:"))
area=input("Enter the area of the centre:")
slots_12to18=int(input("Enter the slots left for 12 to 18:"))
slots_18to45=int(input("Enter the slots left for 18 to 45:"))
slots_45above=int(input("Enter the slots left for 45 and above:"))
mycursor.execute("insert into covishield_booster
values({},'{}',{},'{}',{},{},{})".format(code,name,pin,area,slots_12to18,slots_18to45,s
lots_45above))
a.commit()
print("ADDITION SUCCESSFUL")
elif entry == 3:
code=int(input("enter the vaccination centre code:"))
mycursor.execute("delete from covishield_booster where
c_code={}".format(code))
a.commit()
print("DELETION SUCCESSFUL")
if ch == 6:
a= b.connect(host="localhost", user="root",
password="root",database="covid")
mycursor = a.cursor()
print("Enter 1 to update existing record")
print("Enter 2 to add a new record")
print("Enter 3 to delete a record")
entry = int(input("Enter choice : "))
if entry == 1:
code = int(input("enter the vaccination centre code to be updated:"))
age = int(input("enter 12 for 12-18,enter 18 for 18-45 and 45 for 45
and above:"))
if age == 12:
slots = int(input("Enter the number of slots left:"))
mycursor.execute("update covaxin_booster set NOD12TO18='{}'
where c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif age==18:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covaxin_booster set NOD18TO45='{}'
where c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
else:
slots=int(input("Enter the number of slots left:"))
mycursor.execute("update covaxin_booster set NOD45ABOVE='{}'
where c_code='{}'".format(slots,code))
a.commit()
print("UPDATION SUCCESSFUL")
elif entry == 2:
code=int(input("Enter the vaccination centre code:"))
name=input("Enter the vaccination centre name:")
pin=int(input("Enter the pin code of the area:"))
area=input("Enter the area of the centre:")
slots_12to18=int(input("Enter the slots left for 12 to 18:"))
slots_18to45=int(input("Enter the slots left for 18 to 45:"))
slots_45above=int(input("Enter the slots left for 45 and above:"))
mycursor.execute("insert into covaxin_booster
values({},'{}',{},'{}',{},{},{})".format(code,name,pin,area,slots_12to18,slots_18to45,s
lots_45above))
a.commit()
print("ADDITION SUCCESSFUL")
elif entry == 3:
code=int(input("enter the vaccination centre code:"))
mycursor.execute("delete from covaxin_booster where
c_code={}".format(code))
a.commit()
print("DELETION SUCCESSFUL")
u=input("Do you wish to continue as programmer?")
else:
print("OOPS! programmer_id is incorrect")
if enter == 'U':
print('ENTER #1 IF YOU HAVE NOT TAKEN THE FIRST DOSE')
print('ENTER #2 IF YOU HAVE TAKEN THE FIRST DOSE')
print('ENTER #3 IF YOU HAVE TAKEN THE SECOND DOSE')
entry=int(input("Enter your choice:"))
a = b.connect(host="localhost", user="root",
password="root",database="covid")
mycursor = a.cursor()
if entry==1:
i=input("Enter the name of the vaccine you wish to
take(covaxin/covishield)")
pin=int(input("enter the pincode of the area where you want the centre to
be:"))
if i == 'covishield':
mycursor.execute("select * from covishield_1 where
pincode='{}'".format(pin))
r=mycursor.fetchall()
for c in r:
print(c)
d=int(input("enter the vaccination centre code you prefer:"))
name=input("enter your name:")
age=int(input("enter your age:"))
adhar=int(input("enter your aadhar number:"))
mob=input("enter mobile number:")
gender=input("Enter F for female and M for male")
vaccine_name= "COVISHIELD"
FD='YES'
SD="NO"
BD="NO"
if age == 12 or age >12 and age <18:
mycursor.execute("update covishield_1 set NOD12TO18 =
NOD12TO18-1 where c_code='{}'".format(d))
a.commit()
elif age == 18 or age >18 and age <45:
mycursor.execute("update covishield_1 set NOD18TO45 =
NOD18TO45-1 where c_code='{}'".format(d))
a.commit()
else:
mycursor.execute("update covishield_1 set NOD45ABOVE =
NOD45ABOVE-1 where c_code='{}'".format(d))
a.commit()
mycursor.execute("insert into record
values({},'{}',{},'{}','{}','{}','{}','{}','{}')".format(adhar,name,age,gender,mob,vaccine_
name,FD,SD,BD))
a.commit()
print("SUCCESSFULLY REGISTERED")
elif i == 'covaxin':
mycursor.execute("select * from covaxin_1 where
pincode='{}'".format(pin))
r=mycursor.fetchall()
for c in r:
print(c)
d=int(input("enter the vaccination centre code you prefer:"))
name=input("enter your name:")
age=int(input("enter your age:"))
adhar=int(input("enter your aadhar number:"))
mob=input("enter mobile number:")
gender=input("Enter F for female and M for male")
vaccine_name= "COVAXIN"
FD='YES'
SD="NO"
BD="NO"
if age == 12 or age >12 and age <18:
mycursor.execute("update covaxin_1 set NOD12TO18 = NOD12TO18-1
where c_code='{}'".format(d))
a.commit()
elif age == 18 or age >18 and age <45:
mycursor.execute("update covaxin_1 set NOD18TO45 = NOD18TO45-1
where c_code='{}'".format(d))
a.commit()
else:
mycursor.execute("update covaxin_1 set NOD45ABOVE =
NOD45ABOVE-1 where c_code='{}'".format(d))
a.commit()
mycursor.execute("insert into record
values({},'{}',{},'{}','{}','{}','{}','{}','{}')".format(adhar,name,age,gender,mob,vaccine_
name,FD,SD,BD))
a.commit()
print("SUCCESSFULLY REGISTERED")
elif entry==2:
i=input("Enter the name of the vaccine you took(covaxin/covishield)")
pin=int(input("enter the pincode of the area where you want the centre to
be:"))
if i == 'covishield':
mycursor.execute("select * from covishield_2 where
pincode='{}'".format(pin))
r=mycursor.fetchall()
for c in r:
print(c)
d=int(input("enter the vaccination centre code you prefer:"))
name=input("enter your name:")
age=int(input("enter your age:"))
adhar=int(input("enter your aadhar number:"))
mob=input("enter mobile number:")
gender=input("Enter F for female and M for male")
vaccine_name= "COVISHIELD"
FD="NO"
SD='YES'
BD="NO"
if age == 12 or age >12 and age <18:
mycursor.execute("update covishield_2 set NOD12TO18 =
NOD12TO18-1 where c_code='{}'".format(d))
a.commit()
elif age == 18 or age >18 and age <45:
mycursor.execute("update covishield_2 set NOD18TO45 =
NOD18TO45-1 where c_code='{}'".format(d))
a.commit()
else:
mycursor.execute("update covishield_2 set NOD45ABOVE =
NOD45ABOVE-1 where c_code='{}'".format(d))
a.commit()
mycursor.execute("insert into record
values({},'{}',{},'{}','{}','{}','{}','{}','{}')".format(adhar,name,age,gender,mob,vaccine_
name,FD,SD,BD))
a.commit()
print("SUCCESSFULLY REGISTERED")
elif i == 'covaxin':
mycursor.execute("select * from covaxin_2 where
pincode='{}'".format(pin))
r=mycursor.fetchall()
for c in r:
print(c)
d=int(input("enter the vaccination centre code you prefer:"))
name=input("enter your name:")
age=int(input("enter your age:"))
adhar=int(input("enter your aadhar number:"))
mob=input("enter mobile number:")
gender=input("Enter F for female and M for male")
vaccine_name= "COVAXIN"
FD="NO"
SD='YES'
BD="NO"
if age == 12 or age >12 and age <18:
mycursor.execute("update covaxin_2 set NOD12TO18 = NOD12TO18-1
where c_code='{}'".format(d))
a.commit()
elif age == 18 or age >18 and age <45:
mycursor.execute("update covaxin_2 set NOD18TO45 = NOD18TO45-1
where c_code='{}'".format(d))
a.commit()
else:
mycursor.execute("update covaxin_2 set NOD45ABOVE =
NOD45ABOVE-1 where c_code='{}'".format(d))
a.commit()
mycursor.execute("insert into record
values({},'{}',{},'{}','{}','{}','{}','{}','{}')".format(adhar,name,age,gender,mob,vaccine_
name,FD,SD,BD))
a.commit()
print("SUCCESSFULLY REGISTERED")
elif entry==3:
i=input("Enter the name of the vaccine you took(covaxin/covishield)")
pin=int(input("enter the pincode of the area where you want the centre to
be:"))
if i == 'covishield':
mycursor.execute("select * from covishield_booster where
pincode='{}'".format(pin))
r=mycursor.fetchall()
for c in r:
print(c)
d=int(input("enter the vaccination centre code you prefer:"))
name=input("enter your name:")
age=int(input("enter your age:"))
adhar=int(input("enter your aadhar number:"))
mob=input("enter mobile number:")
gender=input("Enter F for female and M for male")
vaccine_name= "COVISHIELD"
FD="NO"
SD="NO"
BD='YES'
if age == 12 or age >12 and age <18:
mycursor.execute("update covishield_booster set NOD12TO18 =
NOD12TO18-1 where c_code='{}'".format(d))
a.commit()
elif age == 18 or age >18 and age <45:
mycursor.execute("update covishield_booster set NOD18TO45 =
NOD18TO45-1 where c_code='{}'".format(d))
a.commit()
else:
mycursor.execute("update covishield_booster set NOD45ABOVE =
NOD45ABOVE-1 where c_code='{}'".format(d))
a.commit()
mycursor.execute("insert into record
values({},'{}',{},'{}','{}','{}','{}','{}','{}')".format(adhar,name,age,gender,mob,vaccine_
name,FD,SD,BD))
a.commit()
print("SUCCESSFULLY REGISTERED")
elif i == 'covaxin':
mycursor.execute("select * from covaxin_booster where
pincode='{}'".format(pin))
r=mycursor.fetchall()
for c in r:
print(c)
d=int(input("enter the vaccination centre code you prefer:"))
name=input("enter your name:")
age=int(input("enter your age:"))
adhar=int(input("enter your aadhar number:"))
mob=input("enter mobile number:")
gender=input("Enter F for female and M for male")
vaccine_name= "COVAXIN"
FD="NO"
SD="NO"
BD='YES'
if age == 12 or age >12 and age <18:
mycursor.execute("update covaxin_booster set NOD12TO18 =
NOD12TO18-1 where c_code='{}'".format(d))
a.commit()
elif age == 18 or age >18 and age <45:
mycursor.execute("update covaxin_booster set NOD18TO45 =
NOD18TO45-1 where c_code='{}'".format(d))
a.commit()
else:
mycursor.execute("update covaxin_booster set NOD45ABOVE =
NOD45ABOVE-1 where c_code='{}'".format(d))
a.commit()
mycursor.execute("insert into record
values({},'{}',{},'{}','{}','{}','{}','{}','{}')".format(adhar,name,age,gender,mob,vaccine_
name,FD,SD,BD))
a.commit()
print("SUCCESSFULLY REGISTERED")
if enter == 'L':
break