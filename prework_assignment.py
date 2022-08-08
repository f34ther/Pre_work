# question 1.  write a function to print "hello_USERNAME!"
# where USERNAME is the input of the function. the first line of the code is:
# def hello_name(user_name):


def hello_name(user_name):
    user = str(user_name)
    print("\nHello, " + user.upper())


hello_name("username")

# 2: write a python function, first_odds, that prints the odd numbers from
# 1-100 and returns nothing:
# first line:
# def first_odds():


def first_odds():
    while first_odds:
        if first_odds % 2 == 0:
            continue
        else:
            return first_odds


odds = first_odds(range(0-101))
print(odds)
# 3: write function, max_num_in_list to return the max number of a given list
# first line of code: def max(alist)


def max_num(alist):
    return max(alist)


ali = max_num(alist=[1, 2, 3, 5, 3, 4, 5])
print(ali)
# 4:Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
# def is_leap_year(a_year):

# #
# def leap(y):
#     return True if y % 4 == 0 or (y % 100 == 0 and y % 400 == 0) else False


# year = leap(1190)
# print(year)
# year = leap(1996)
# print(year)
# year = leap(4000)
# print(year)


# 5: Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# what is a consecutive number? a number, followed by another direct number
# aka: mathematically written: n, n+1, n+2, n+3
# so, how do we take that and apply it to a function with limitless length?
# obviously, we can

# #
# def is_con(n):
#     """Check for consecutive numbers"""
#     for numbers in sorted(n):
#         if numbers + 1 == n.index(+1):
#             return True
#         else:
#             return False
# UnboundLocalError: local variable 'numbers' referenced before assignment
#     # if numbers + 1 == n.index(+1):
#     for numbers in sorted(n):
#         return True
#     else:
#         return False

def is_con(n):
    for numbers in n:
        if numbers + 1 == n[+1]:
            return True
        else:
            return False


number = is_con(n=[1, 2, 3, 5, 4, 6])

print(number)
number = is_con(n=[1, 2, 3, 4, 5])
print(number)
number = is_con(n=[1, 15, 3])
print(number)
