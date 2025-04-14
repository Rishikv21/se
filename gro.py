import mysql.connector as sql 
conn=sql.connect(host='localhost',user='root',passwd='1234',database='project') 
if conn.is_connected(): 
print('successfully connected') 
c=conn.cursor() 
print('grocery shop management system') 
print('1.login') 
print('2.exit') 
choice=int(input('enter your choice:')) 
if choice==1: 
user_name=input('enter your user name=') 
password=input('enter your password=') 
while user_name=="bhuvanesh" and password=="bhuvi" : 
print('connected successfully') 
print('grocery shop') 
print('1.see all customer details') 
print('2.see all product details') 
print('3.see all worker details') 
print('4.add product details') 
print('5.add customers details') 
print('6.add worker details') 
print('7.see one customer details') 
print('8.see one product details') 
print('9.see one worker details') 
print("10.for exit") 
choice=int(input('enter the choice')) 
if choice == 1 : 
t=conn.cursor() 
t.execute('select * from costumers') 
record=t.fetchall() 
for i in record: 
print(i)   
elif choice==2: 
                t=conn.cursor() 
                t.execute('select * from products') 
                record=t.fetchall() 
                for i in record: 
                    print(i)   
        elif choice==3: 
                    
                   t=conn.cursor() 
                   t.execute('select * from employees') 
                   record=t.fetchall() 
                   for i in record: 
                        print(i) 
  
        elif choice==4: 
                product_name=input('enter product name=') 
                product_cost=float(input('enter the cost=')) 
                sql_insert="insert into products values(""'"+(product_name)+"',"+str(product_cost)+")" 
                c.execute(sql_insert) 
                conn.commit() 
                print('data is updated') 
 
        elif choice==5: 
                cust_name=input('enter your name=') 
                phone_no=int(input('enter your phone number=')) 
                cost=float(input('enter your cost=')) 
                sql_insert="insert into costumers 
values('"+(cust_name)+"',"+str(phone_no)+","+str(cost)+")" 
                c.execute(sql_insert) 
                 
                conn.commit() 
                print('data is updated') 
        elif choice==6: 
                    worker_name=input('enter your name=') 
                    worker_work=input('enter your work=') 
                    worker_age=int(input('enter your age=')) 
                    worker_salary=float(input('enter your salary=')) 
                    phone_no =int(input('enter your phone number=')) 
                    sql_insert="insert into employees values(""'"+(worker_name)+"',""'"+(worker_work)+"',"+str(worker_age)+","+str(worker_salary)+","+str(phone_no)+ ")" 
                    c.execute(sql_insert) 
                    conn.commit() 
                    print('data is updated') 
        elif choice==7: 
                   a=input('enter your name') 
                   t='select*from costumers where name=("{}")'.format(a) 
                   c.execute(t) 
                   v=c.fetchall() 
                   for i in v: 
                         print(v) 
        elif choice==8: 
                    a=input('enter your product_name') 
                    t='select*from products where product=("{}")'.format(a) 
                    c.execute(t) 
                    v=c.fetchall() 
                    for i in v: 
                            print(v) 
        elif choice==9: 
                  a=input('enter your name') 
                  t='select*from employees where name=("{}")'.format(a) 
                  c.execute(t) 
                  v=c.fetchall() 
                  for i in v: 
                         print(v) 
        elif choice==10: 
                   password="hi" 
else:   
    print("please try again")
