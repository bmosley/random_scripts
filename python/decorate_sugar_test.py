import functools

def hello(test):
	if test == 'test':
		print('hello')

	return

def my_wrap(*args, **kwargs):
	print('do something')
	hello(targ)

	print('did something')
	return

hello = my_wrap(hello, *args)

hello('test')