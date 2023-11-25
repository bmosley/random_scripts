# decorator

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()

print('------')

# in a class

# decorator

class A(object):
	def make_pretty(func):
	    def inner(self):
	        print("I got decorated")
	        func(self)
	    return inner

	@make_pretty
	def ordinary(self):
	    print("I am ordinary")

AC = A()
AC.ordinary()

ordinary()