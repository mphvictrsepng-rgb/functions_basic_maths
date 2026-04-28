# ---------------------------------------------------------
# MATH & OOP PYTHON QUIZ
# ---------------------------------------------------------

# 1. Write a function named 'add' that takes two numbers and returns their sum.
def add(a, b):                  # or can be done this way, but I think the 1st method looks cleaner    # def add(a, b): 
    results_1 = a + b                                                                                  #    return a + b
    return print(f'QUESTION 1: {results_1}')                                                           # results_1 = add(1, 2)
add(1, 3)        # e.g                                                                                 # print(f'QUESTION 1: {results_1}')

# 2. Write a function named 'minus' that takes two numbers and returns the result.
def minus(a, b):
    results_2 = a - b
    return print(f'QUESTION 2: {results_2}')
minus(4, 1)     # e.g

# 3. Write a function named 'multiply' that takes two numbers and returns the result.
def multiply(a, b):
    results_3 = a*b
    return print(f'QUESTION 3: {results_3}')
multiply(3, 2)    # e.g

# 4. Write a function named 'divide' that takes two numbers and returns the result.
def divide(a, b):
    results_4 = a / b                                # I saw that answer returns as float, so I came with 2 ways to get a whole number
    return print(f'QUESTION 4: {results_4:.0f}')     #print(f'{results_4:.0f}') or int(divide(4, 2)) to return int not float.
divide(4, 2)        # e.g                                  

# 5. Write a function named 'solve_y' that takes m, x, and b, and returns (m * x + b).
def solve_y(m, x, b):
    results_5 = m*x + b
    return print(f'QUESTION 5: {results_5}')
solve_y(2,1,2)      #e.g

# 6. Write a function named 'square' that takes one number and returns that number times itself.
def square(number):
    results_6 = number*number      # * allows the number to multiply by itself.
    return print(f'QUESTION 6: {results_6}')
square(2)


# 7. Create a class named 'MathStudent' that can store a 'name' attribute.

# 8. Inside the 'MathStudent' class, create a method named 'get_area' for a rectangle.

# 9. Create a class named 'Calculator' with a starting attribute 'total' set to 0.

# 10. Inside the 'Calculator' class, create a method named 'add_to_total' to update the total.