# Lab 00

"""
Instructions

Please read this CAREFULLY since this is the first lab! I know functions are new especially
if you have not used python before, but we are going to jump right into it! Functions
are simple if you break it down. Essentially, they are snippets of code that you can use
over and over again later in code. They can contain parameters, which are optional, and can return
values if you tell them to. I HIGHLY recommend all of your functions return something

I will walk you through a very basic example function and then you will have a few to
do on your own!
"""

def add_together(num_1, num_2):
    """
    Docstrings! Where I am typing now is called a doc string and this is where you
    describe what your function does. Essentially, a colleague or whoever is reading 
    your code should be able to refer to this and understand what the function does and
    what it returns

    Params: parameter section, what is being passed into the function. For this example,
    the paramaters are num_1 and num_2 with types integer
    Returns: what is the function returning. For this example, we are retuning the addition
    of two numbers that is assigned to the variable "result"
    """

    result = num_1 + num_2 # addition in python
    return result # return the result

print(add_together(3, 4)) # you can see here I am calling the function, but in order to see the result you need to print!

### YOUR TURN!!!!!!

"""
This next function I want you to code multiplication. The function expects two numbers as
parameters and returns one variable, the result of multiplication of two numbers. INCLUDE DOCSTRINGS!!!
"""

def multiply(num_1, num_2):
    result = num_1 * num_2
    return result

print(multiply(10, 12))

"""
This next function I want you to implement raising a number to a certain power. Example: 2^2 = 4
"""

def power(num, power_raise):
    result = num ** power_raise
    return result

print(power(3, 2))

"""
For practice, make any function you want! Write the function on your own and tell me what it
does in the docstrings. Include test calls!!!
"""

def dogYears(num_1, num_2):
  """
  this is painfully basic but I failed miserably at my first attempt of "99 bottles of beer" while loop"
  """
  age = num_1 * num_2
  return age

print(dogYears(1.3, 7))


# def sing(num):
#   # num = 99
#   while num > 0:
#     lyric = str(num) + " bottles of beer on the wall" + "\n"
#     num = num - 1
#     lyric2 = str(num) + " bottles of beer on the wall"
#     return lyric + lyric2

# print(sing(8))