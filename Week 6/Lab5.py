import math as m

def countdown(n):
    if n == 0:
        return
    if n <= 0:
        return
    print(n)
    countdown(n-1)
countdown(5)
print(countdown)
def fact(u):
    if u ==0:
        return 1
    return u * fact(u-1)
print(fact(10))
from math import factorial
def factor(j):
    return m.factorial(j)
print(factor(5))
#1
def countdwn(n):
    if n == 0:
        print("Lift off")
        return
    if n <= 0:
        return
    print(n)
    countdwn(n-1)
countdwn(30)
print(countdwn)
#2
def range1(o,i):
    if o == i:
        return
    if o < 0:
        return
    print(o)
    range1(o+1,i)
range1(0,11)
print(range1)
#3

def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)
#4 + 3 + 2 + 1 = 10. 5th round, n = 0, func ends
print(sum(4))
print(sum)
#4
def countdwn_even(n):
    if n < 0:
        print("done")
        return
    if n % 2 == 0:
        print(n)
    countdwn_even(n - 1)
countdwn_even(8)
print(countdwn_even)
#5
def pow(n):
    if n == 0:
        return
    power = 2 * (n * n)
    print(power)
    pow(n-1)
pow(10)
print(pow)
#6
larger = lambda x,y:x if x > y else y
print(larger(5, 3))
#7
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_or_odd(4))
#8
add = lambda x,y:x+y
print(add(5, 3))
#9
area_of_circle = lambda r: m.pi * (r ** 2)
print(area_of_circle(5))