def fibGen():
    """
    Generates(/Yields) fibonacci numbers as per user's choice
    Usage: Run file. Go to console. Type fib.__next__() to generate number(s)
    starting from third in the sequence
    """
    
    # initial numbers of fibonacci sequence
    fib_a = 0
    fib_b = 1
    
    while True:
        # add previous two numbers to get new one in the sequence
        fib_c = fib_a + fib_b
        # yield that number
        yield fib_c
        
        # update values for next iteration
        fib_a = fib_b
        fib_b = fib_c

# calling fibGen() to start the process
fib = fibGen()