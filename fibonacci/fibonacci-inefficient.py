def fib(n):
    '''
    n: int, nth index in fibonacci sequence
    returns: Term at nth index in fibonacci sequence
    
    starting point of sequence i.e. initial term is considered as 1
    fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21...
    '''
    
    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)

# prompt user for input
n = int(input('Enter an index: '))
# print result
print('Term at index ' + str(n) + ': ' + str(fib(n)))