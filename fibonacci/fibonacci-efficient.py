def fib(n, d):
    '''
    n: int, nth index in fibonacci sequence
    d: dictionary, to store values being calculated and some pre-defined
    values
    returns: Term at nth index in fibonacci sequence
    
    starting point of sequence i.e. initial term is considered as 1
    fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21...
    '''
    
    if n in d:
        return d[n]
    else:
        ans = fib(n - 1, d) + fib(n - 2, d)
        d[n] = ans
        return ans

# initialise dictionary with some base case values
d = {1: 1, 2: 1, 3: 2}
# prompt user for input
n = int(input('Enter an index: '))
# print result
print('Term at index ' + str(n) + ': ' + str(fib(n, d)))