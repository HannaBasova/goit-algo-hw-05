

'''
a function that creates and uses a cache to store
and reuse already calculated Fibonacci numbers
'''


def caching_fibonacci():
    #create an empy dictionary  for memorization (cache)
    cache = {}

    # function which calls itself
    def fibonacci(n):
        #base case: if n is 0 or less, return it
        if n <= 0:
            return 0
        # base case: if n is 1  return 1
        elif n == 1:
            return 1
        #if we have already counted it, get it from memory (cache)
        elif n in cache:
            return cache[n]
        else:
            ## if we haven't counted yet, count and remember the result
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
        # call the internal function and return the result
    return fibonacci
fib = caching_fibonacci()
print(fib(15))