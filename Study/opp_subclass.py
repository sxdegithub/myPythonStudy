# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
class SchoolMember:
    """代表任何学校成员"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember:{})'.format(self.name))

    def tell(self):
        """告诉我有关细节"""
        print('Name:{} Age:{}'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    """代表老师"""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('\n')
        print('salary is {}'.format(self.salary))


class Student(SchoolMember):
    """代表学生"""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('\n')
        print('marks is {}'.format(self.marks))


t = Teacher('Lao mao', 45, 50000)
s = Student('xx', 16, 100)

members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()
