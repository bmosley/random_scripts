#!/usr/bin/python
# -*- coding: utf-8 -*-


class BaseClass(object):
    pass


class MyClass(BaseClass):

    def __init__(self):
        super(MyClass, self).__init__()
        self.some_var = None
        self.some_var2 = self.bar()

    def bar(self):
        print('\nassigned some_var: {}\n'.format(self.some_var))
        x = self.some_var
        return x

    def foo(self):
        print(self.some_var)
        print(self.some_var2)


class MySubClass(MyClass):

    def __init__(self):
        super(MySubClass, self).__init__()
        self.some_var = 'subclass'


my_class = MySubClass()
print('^^^^^ instance is called\n')
my_class.foo()
