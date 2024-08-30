# To print n natural numbers
def printN(n):
    if n > 0:
        printN(n-1)
        print(n)
# printN(5)

# To print n natural numbers in reverse
def printN_reverse(n):
    if n != 0:
        print(n)
        printN_reverse(n-1)
# printN_reverse(7)

# To print n odd numbers
def print_n_odd_numbers(n):
    if n > 0:
        print_n_odd_numbers(n-1)
        print(2 * n -1)
# print_n_odd_numbers(10)

# To print n even numbers
def print_n_even_numbers(n):
    if n > 0:
        print_n_even_numbers(n-1)
        print(2*n)
# print_n_even_numbers(10)

# To print n odd numbers in reverse
def print_n_odd_numbers_reverse(n):
    if n > 0:
        print(n * 2 - 1)
        print_n_odd_numbers_reverse(n-1)
# print_n_odd_numbers_reverse(10)

# To print n even numbers in reverse
def print_n_even_numbers_reverse(n):
    if n > 0:
        print(n*2)
        print_n_even_numbers_reverse(n-1)
# print_n_even_numbers_reverse(10)

# To sum n natural numbers
def sum_n_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_n_natural_numbers(n-1)
# print(sum_n_natural_numbers(5))

# To get sum of n odd numbers
def sum_of_n_odd_numbers(n):
    if n == 1:
        return 1
    else:
        return n*2-1 + sum_of_n_odd_numbers(n-1)
# print(sum_of_n_odd_numbers(5))

# To get sum of n even numbers
def sum_of_n_even_numbers(n):
    if n==1:
        return 2
    else:
        return n*2 + sum_of_n_even_numbers(n-1)
# print(sum_of_n_even_numbers(5))

# To get factorial of n natural numbers
def fact_of_n_natural_numbers(n):
    if n == 1:
        return n
    else:
        return n * fact_of_n_natural_numbers(n-1)
# print(fact_of_n_natural_numbers(5))

# To calculate sum of squares of n numbers
def sum_of_squares_of_n_numbers(n):
    if n == 1:
        return n
    else:
        return n*n + sum_of_squares_of_n_numbers(n-1)
print(sum_of_squares_of_n_numbers(5))
