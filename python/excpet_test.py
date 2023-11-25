class BaseException(Exception):
   """Base class for other exceptions"""
   pass

class AutomationException(BaseException): 
    # Constructor or Initializer 
    def __init__(self, msg=None, value=1): 
        self.value = value 
  
    # __str__ is to print() the value 
    def __str__(self): 
        return(repr(self.value)) 


class Error(AutomationException):
   pass
 
class TestError(AutomationException):
   pass
 
class DataError(AutomationException):
   pass

  
try: 
    raise DataError
except DataError as error: 
    print('A custom AMP exception occured: ', error.value) 