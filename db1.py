import pymysql

conn=pymysql.connect(user='root',password='root',port=3306,database='pythonmysql')
cursor=conn.cursor()
'''def create_table():
    try:
        query="create table student_1(id int  primary key, name varchar(20), mob bigint unique,
        bal bigint);"
        cursor.execute(query)
    except pymysql.err.OperationalError as e:
        print(f'{e}')
def insert_record():
    query='insert into student_1(id,name,mob,bal) values(1,"suresh",987765434,23443)'
    cursor.execute(query)
    conn.commit()
insert_record()'''

'''def get_records():
    query='select *from student_1'
    cursor.execute(query)
    records=cursor.fetchall()
    for i in records:
        print(i)
get_records()'''


'''def insert_dynamic(id,name,mob,bal):
    record=(id,name,mob,bal)
    query="insert into student_1(id,name,mob,bal) values(%s,%s,%s,%s)"%record
    cursor.execute(query)
    conn.commit()'''

'''def drop_record(id):
    query=f'delete from student_1 where id={id}'
    cursor.execute(query)
    conn.commit()
    print('record removed')'''

'''def alter_record(mob):
    query=f'delete from student_1 where mob={mob}'
    cursor.execute(query)
    conn.commit()
    print('name removed')'''



