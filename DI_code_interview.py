#*************************************************************************
#
# Python script that calculates the Fibonacci sequence of even numbers
# 
# This script is created to support my application to the Data Incubator
# fellowship program.
# 
# Created by: Esteban Velez R 
# Date: November 14th, 2023.
#
#**************************************************************************

import time

class even_Fib_class:
    '''
    Class that computes the mth term of the even Fibonacci sequence using memoization
    '''
    
    # Init method: Initial values of the Fibonacci sequence
    def __init__(self):
        self.memo = [0, 2]
    
    # Call method: calculates F_n using recursion. The previous values in the sequence are stored in the chache memory
    def __call__(self, m):
        
        if m < len(self.memo):
            return self.memo[m]
        else:
            fib_number = 4*self(m - 1) + self(m - 2)
            self.memo.append(fib_number)

        return self.memo[m]


even_fib_class = even_Fib_class()

start = time.time()
fib_value = even_fib_class(11)
fib_list = even_fib_class.memo
end = time.time()

print("", f"Sum of even numbers in the Fibonacci sequence that do not exceed 4000000 is: {sum(fib_list)}",
      "", f"The total time spent in the computation was: {end - start}", "" , sep='\n')    
