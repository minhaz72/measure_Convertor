import database
from database import * 

print('----- welcome , to our terminal -------- ')
print('=== this is a convertor software-==== ')
print('=== you  can convert some things here : -==== ')
print('you can make your respose view terminal , like  , \n y for start \n  n for exit ')
am= str(input('input your response '))
if am== 'n':
    print('exiting==========  ')
    print('end ')
elif am=='y':
    print('which measurment do  you want to convert ; ')
    print('you can make your response from follwing some steps like , \n 1.kilogram to gram \n 2. gram to kilogram \n 3. miligram to killogram \n 4. killogram to miligram \n 5. gram to miligram \n 6. miligram to gram \n 7. meter to centimeter \n 8. centimeter to meter \n 9.milimeter to centimetre \n 10. centimeter to milimeter \n 11.meter to milimeter \n 12.milimeter to meter   ')
    y= int(input('enter your measuring response : '))
    n=float(input('enter the measuring  value  '))
    if y== 1:
        database.kg_to_gm(n)
    elif y==2:
        database.gm_to_kg(n)
    elif y==3 :
        database.mili_to_kg(n)
    elif y==4 :
        database.kg_to_mili(n)
    elif y==5 :
        database.gm_to_mili(n)
    elif y==6 :
        database.mili_to_gm(n)
    elif y==7 :
        database.m_to_c(n)
    elif y==8 :
        database.c_to_m(n)
    elif y==9 :
        database.mili_to_c(n)
    elif y==10 :
        database.c_to_mili(n)
    elif y==11 :
        database.m_to_mili(n)
    elif y==12 :
        database.mili_to_meter(n)
    else:
        print('invalid')
    
else:
    print('invalid input : ')
