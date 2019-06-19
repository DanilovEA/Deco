# -*- coding: utf-8 -*-

def my_new_deco(my_func):
    def wrapper_bla_bla():
        print u'до функции'
        my_func()
        print u'после функции'
    return wrapper_bla_bla



def my_foo():
    print u'сама функция'

my_foo()

print my_new_deco(my_foo)
print("Test new git config")