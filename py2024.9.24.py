    
import math
import re
# print(len("good evening!"))
# a=eval(input("请输入:"))
# print(int(a/100))
# print(int(a/10%10))
# print(a%100)
# s=input("请输入一个高精度整数:")
# for i in range(len(s)):
#     print(s[i])
# import math
# print(math.pi)
# a=math.pow(1.001,365)
# b=math.pow(0.999,365)
# print(round(0.99**365,2))
# print(round(1.01**365,2))
# lst=[33,23,21,21,23,2,3]
# lst1=sorted(lst,reverse=True)
# lst2=reversed(lst1)
# print(lst1)
# print(f"start:{lst},desc_lst:{lst1},asc_lst{list(lst2)}")
# print("start:{},desc_lst:{}".format(lst,lst1))
# PM=input("PM:")
# if 0<PM<=35:
#     print("great")
# elif 35<PM<=75:
#     print("good")
# else:
#     print("bad")
lst1=['afsdf','bfsdf','cbfe','ddasw']
# lst2=[1,2,3,4]
# zipobj=zip(lst1,lst2)
# print(type(zipobj),list(zipobj))
# print(type(zipobj))
# for index,item in enumerate(lst1):
#     print(index,":",item)
# def fun(num):
#     return num%2==1
# obj=filter(fun,range(1,10))
# print(list(obj))
def upper(x):
    return x.upper()
obj=map(upper,lst1)
# print(list(obj))
# print(format("hello",'*<20'))
# print(format("hello",'*>20'))
# print(format("hello",'*^20'))
# print(format(3.138293082,'.2f'))
# print(format(100,'b'))
# print(format(100,'o'))
# print(format(100,'x'))
# print(lst)
pattern='\d.\d+'
s='i ndi2.1 san py3.9000'
match=re.split(pattern,s,re.I)
print(type(match),match)
def fun(age,name='666'):
    print("to ",name,age);
fun(88)
res=lambda a,b:a+b
print(res(10,20))
class Student:
    def __init__(self,a,b):
        self._name=a
        self.__age=b
    def _fun1(num):
        return num
    def __fun2():
        print("mmm")
#staticmethod and classmethod use classname
for i in range(1,101):
    if i%7==0 and i%5!=0:
        print(i)
stu1=Student("aaa",10)
print(stu1._name)
print(stu1._Student__age)
print(dir(Student))
for i in range(1,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j,end=" ")
    print("\n")