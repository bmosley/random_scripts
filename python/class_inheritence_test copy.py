class AppBase(object):
	"""docstring for Family"""
	def __init__(self):
		super(AppBase, self).__init__()
		self.fam = "the AppBase class"
		self.whos_right = 'AppBase is right'
		

class AppBaseMac(AppBase):
	"""docstring for Family"""
	def __init__(self):
		super(AppBaseMac, self).__init__()
		self.father = "the AppBaseMac sub class"
		self.whos_right = 'AppBaseMac is right'

	def print_something(self):
		print('print_something AppBaseMac')


class AppBaseIOS(AppBase):
	"""docstring for Family"""
	def __init__(self):
		super(AppBaseIOS, self).__init__()
		self.mother = "the AppBaseIOS sub class"
		self.whos_right = 'AppBaseIOS is right'

	def print_something(self):
		print('print_something AppBaseIOS')


class MusicAppBase(AppBaseIOS, AppBaseMac):
	"""docstring for Family"""
	def __init__(self):
		super(MusicAppBase, self).__init__()
		self.boy = "the MusicAppBase sub sub class"


fc = MusicAppBase()

print(fc.fam)
print(fc.father)
print(fc.boy)
print(fc.whos_right)

fc.print_something()

print(MusicAppBase.__mro__)