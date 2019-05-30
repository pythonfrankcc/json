#higher order functions are functions that operate on other functions by taking other functions as the arguement or
#by returning another function
#looking at an example using a normal loop
integers = range(0, 20)  
even = [] 
for i in integers:     
    if i % 2 == 0:         
        even.append(i)
print('even:',even)
#however we can reduce this to one line of code using filter ()
'''This takes a function and and iterable as arguements and constructs a new iterable by applying the function
to every element in the list''' 
integers = range(0, 20)  
#even = []
even1= filter(lambda x: x % 2 == 0, integers)
print('even1:\n',even1)
'''the lambda is convenient for for short and adhoc funnctions'''
#or
integers = range(0, 20)
def is_even(x):     
    return x % 2 == 0  
even3 = filter(is_even, integers)
print('even3:\n',even3)
#using list comprehensions
#is the best way to represent or compress functions when using the lambda filter and def(both of which are higher order comprehensions) they return objects
even4 = [x for x in integers if x % 2 == 0]
print('even4:\n',even4)
#so far we are looking at functions that consume lists and return lists lets look at another list comprehensions
integers = range(0, 10)
multi = [x * x for x in integers]
print(multi)
#list of comprehensions always returns a list and never a single value
#list of comprehensions can reduce different functions and even return a single value
#the lambda shows only the variables that are going to be fed to a specific task
from functools import reduce
integers=range(1,10)
a = reduce(lambda x, y: x * y, integers)
print(a)
#higher order sum function
integers = range(1, 10)
b = sum(integers)
print(b)
#using higher order True,False and any
integers = range(1, 10)
any(x % 2 == 0 for x in integers) 
