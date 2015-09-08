# coding=utf-8

class Person(object):
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count += 1
        
# john = Person('john',40)
# print john.name
# print john.age
# print Person.count
# 
# jessica = Person('jessica',35)
# print jessica.name
# print jessica.age
# print Person.count



class Teacher:
    def __init__(self,name):
        self.name = name

t = Teacher('Andy')
print t.name







