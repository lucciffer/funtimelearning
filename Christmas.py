from random import randint
from time import sleep
md2=randint(1,30)
def  genTree():
        print('\033c')
        for x in range(1,30,2):
            md1=randint(1,md2)
            if x==1:
                ch="A"
            elif md1%4==0:
                ch="o"
            elif md1%3==0:
                ch="i"
            else:
                ch="*"
            print("{:^33}".format(ch*x))
        print("{:^33}".format("||||"))
        print("{:^33}".format("||||"))
        sleep(.75)
while True:
    genTree()



"""
This project of Christmas Tree was coded by #Lucciffer
This program, in order to run shall require randint and time libraries of python
"""
