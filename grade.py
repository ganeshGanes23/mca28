mrk=input('enter marks percentage ')
if mrk>90 and mrk==100:
    print('grade=A+')
elif mrk>=90 and mrk<80:
    print('grade=A')
elif mrk>=80 and mrk<70  :
    print('grade=B')
elif mrk>=70 and mrk<60 : 
    print('grade=C')
elif mrk>=60 and mrk<50 :
    print('grade=D')
elif mrk>=50 and mrk<40 :
    print('grade=PASS')
elif mrk>=0 and mrk<35 :
    print('grade=FAIL')
elif mrk>100 and mrk<0:
    print('invalid marks')
else:
    print('no more marks')