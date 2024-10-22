import datetime
import random


def random_list():
    list1 = list()
    for id in range(random.randint(3,34)):
        list1.append(random.randint(1,784))
    return list1
    

def time_dekor(func):
    def inner (*args, **qwargs):
        time_start = datetime.datetime.now()
        func(*args,**qwargs)
        end_time = datetime.datetime.now()
        rezult = end_time-time_start
        return print(rezult)
    return inner


@time_dekor
def maxElement(list):
    a = list[0]
    for element in list:
        if a < element:
            a = element
    return print(a)


test_list = random_list()
print(test_list)
maxElement(test_list)

