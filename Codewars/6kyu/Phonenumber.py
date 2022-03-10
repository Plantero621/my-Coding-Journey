import random
from tkinter import ON

n = [0, 7, 7, 4, 8,3, 3, 2, 1, 1]

def create_phone_number(n):
        a="".join([str(i) for i in n[0:3]])
        b="".join([str(i) for i in n[3:6]])
        c="".join([str(i) for i in n[6:10]])
        tel = "({}) {}-{}".format(a,b,c)
        return(tel)
def oneline(n):
        return"({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    
print(create_phone_number(n))
print(oneline(n))

