
#CP1
def alpha():
    for i in range(65, 91):
        print(chr(i), end = '')
    print()
    for i in range(97, 123):
        print(chr(i), end = '')
    print()
    i=65
    while i<91:
        print(chr(i), end= '')
        i = i+1
    print()
    i=97
    while i<123:
        print(chr(i), end= '')
        i = i+1
    
alpha()


#CP2
def print_multiplication_table(number):
    print(f"Multiplication Table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

num = int(input("Enter a number to print its multiplication table: "))

print_multiplication_table(num)


#CP3
def count_alphabets_digits(text):
    alphabets = 0
    digits = 0
    for char in text:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
    return alphabets, digits

user_input = input("Enter a string: ")


#CP4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

num = int(input("Enter a number: "))

print(f"\nChecking number: {num}")
print("Prime:", "Yes" if is_prime(num) else "No")
print("Perfect:", "Yes" if is_perfect(num) else "No")
print("Armstrong:", "Yes" if is_armstrong(num) else "No")
print("Palindrome:", "Yes" if is_palindrome(num) else "No")
print("Automorphic:", "Yes" if is_automorphic(num) else "No")

alpha_count, digit_count = count_alphabets_digits(user_input)

print("Number of alphabets:", alpha_count)
print("Number of digits:", digit_count)


#CP5
def generate_pythagorean_triplets(limit):
    print(f"Pythagorean Triplets with side length ≤ {limit}:")
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):  
            c = (a*2 + b2)*0.5
            if c.is_integer() and c <= limit:
   
generate_pythagorean_triplets(30)


#CP6
def print_24_hour_labels():
    for hour in range(24):
        if hour == 0:
            label = "12 AM - Midnight"
        elif hour == 12:
            label = "12 PM - Noon"
        elif hour < 12:
            label = f"{hour} AM"
        else:
            label = f"{hour - 12} PM"
        print(label)

print_24_hour_labels()


#CP7
import math
def nCr(n, r):
    return math.comb(n, r)  

def nPr(n, r):
    return math.perm(n, r)  

n = int(input("Enter n: "))
r = int(input("Enter r: "))

print(f"\n{n}C{r} = {nCr(n, r)}")
print(f"{n}P{r} = {nPr(n, r)}")


#CP8
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))

print(f"Factorial of {num} is: {factorial(num)}")


#CP9
def print_reverse_natural_numbers(n):
    for i in range(n, 0, -1):
        print(i, end=" ")

num = int(input("Enter N: "))

print_reverse_natural_numbers(num)


#CP10
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

num = int(input("Enter the number of Fibonacci numbers to generate: "))

fib_sequence = fibonacci(num)
print(f"First {num} Fibonacci numbers: {fib_sequence}")



#CP11
import math
def sin_x(x, terms=10):
    result = 0
    for n in range(terms):
        # Taylor series term: (-1)^n * x^(2n+1) / (2n+1)!
        result += ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return result

x = float(input("Enter the value of x (in radians): "))

result = sin_x(x)
print(f"sin({x}) = {result}")
