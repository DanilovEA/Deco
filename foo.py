# -*- coding: utf-8 -*-
"""
Много строчный комментарий
"""
def my_dec(func):
    def wrapper(a, b):
        print u'We are here!'
        a = a*a
        b = b*b
    return wrapper

@my_dec
def foo(a, b):
    print a
    print b
    return a + b

print foo(12, 1)

def shout(word=u'да'):
    print u'Вызов shout'
    return word.capitalize()+u'!'
    

scream = shout

def doSomethingBefore(func):
    print u'Чота делаем до вызова декорируемой функции'
    func()

doSomethingBefore(scream)

def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        print u'Я код, который отрабатывает до вызова функции'
        a_function_to_decorate()
        print u'А я код, срабатывающий после'
    return the_wrapper_around_the_original_function

def a_stand_alone_function():
    print u'Я просто одинокая функция, ты ведь не посмеешь меня изменять?...'

a_stand_alone_function()
print u'-----------------'
a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
print u'-----------------'
a_stand_alone_function_decorated()

@my_shiny_new_decorator
def a_stand_alone_function_1():
    print u'Hello'

a_stand_alone_function_1()