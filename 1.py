import datetime
import random

def randomList():
    list1 = list()
    for id in range(random.randint(3,34)):
        list1.append(random.randint(1,784))
    return list1
    

def timeDekor(func):
    def inner (*args, **qwargs):
        time_start = datetime.datetime.now()
        func(*args,**qwargs)
        end_time = datetime.datetime.now()
        rezult = end_time-time_start
        return print(rezult)
    return inner

@timeDekor
def maxElement(list):
    a = list[0]
    for element in list:
        if a < element:
            a = element
    return print(a)

test_list = randomList()
print(test_list)
maxElement(test_list)

