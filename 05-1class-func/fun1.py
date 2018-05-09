def factorial(n):
    '''return n!'''
    if(n < 2):
        return 1
    else:
        return n * factorial(n - 1)
