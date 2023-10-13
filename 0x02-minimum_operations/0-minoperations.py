#!/usr/bin/python3
''' minimum operations challenge '''
def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    # starting with the smallest possible divisor
    divisors = 2  

    while n > 1:
        while n % divisors == 0:
            # check if 'divisor' is a factor of 'n',
            # copy 'divisor' times
            n //= divisors
            operations += divisors
        divisors += 1
        
    return operations
