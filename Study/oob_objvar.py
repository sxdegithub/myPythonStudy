# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
class Robot:
    """表示一个带有名字的机器人."""
    # 一个类变量,用来统计机器人的数量
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Initializing {})'.format(self.name))

        # 当有人被创建时,机器人数量加1
        Robot.population += 1

    def die(self):
        """机器人挂了"""
        print("{} is being destroyed".format(self.name))

        Robot.population -= 1
        if Robot.population == 0:
            print('{} is the last one'.format(self.name))

        else:
            print("There are still {:d} robots".format(Robot.population))

    def say_hi(self):
        """来自机器人的问候
        没问题你做得到"""
        print('Hello,my name is {}'.format(self.name))

    @classmethod
    def how_many(cls):
        """打印当前人口数量"""
        print('There are {:d} robots'.format(cls.population))


droid1 = Robot('WALL')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('E')
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
Robot.how_many()
