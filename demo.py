'''def compose(f,g,x):
    return f(g(x))
compose(print, len, 'Hello, world!')



import random
def random_power():
    def f(x):
        return x ** 2
    def g(x):
        return x ** 3
    def h(x):
        return x ** 4
    functions = [f, g, h]
    return random.choice(functions)

for i in range(10):
    p = random_power()
    print(p(3))
 # syntactic sugar  



import time

def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        stop_time = time.time()
        dt = stop_time - start_time
        print(dt)
        
    return wrapper
    
def prime_factorization(n):
    #start_time = time.time
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    #stop_time = time.time()
    print(f"t = {stop_time - start_time}")        
    return factors'''


