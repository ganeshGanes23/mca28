import csv 
'''with open('mca.csv','w',newline='') as csvfile:
    data=csv.writer(csvfile)
    data.writerow(['id','name','mobile','email'])
    data2=[
        [1,'john',9876543210,'gam@mail.com'],
        [2,'jin',9844743210,'jam@mail.com'],
        [4,'jam',9825543210,'jim@mail.com']
    ]
    data.writerows(data2)'''

''' with open('mca.csv','r,') as csvfile:
    data=csv.reader(csvfile)
    for i in data:
        print(i)'''

'''with open('mca1.csv','w',newline='') as csvfile:
    filednames=['id','name','moblie','email']
    data=csv.DictWriter(csvfile,filednames)
    data.writeheader()
    rows=[
        {'id':1,'name':'suresh','moblie':9876543210,'email':'s@gmail.com'},
        {'id':4,'name':'naresh','moblie':9876544566,'email':'t@gmail.com'},
        {'email':'t@gmail.com.','moblie':9876544566,'id':4,'name':'naresh'}
    ]
    data.writerows(rows)'''


with open('mca1.csv','r') as csvfile:
    data=csv.DictReader(csvfile)
    for row in data:
        print(row['email'])