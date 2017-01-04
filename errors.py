'''
This moduel contains the set custom exceptions
'''
class Error(Exception):
    '''Base class for exceptions in this module.'''
    pass

class ResponseError(Error):
    '''Raised when return status from API is different than 200'''
    pass