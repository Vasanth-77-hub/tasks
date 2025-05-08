# # class Person:
# #     def greet(self):
# #         print("Hello!")

# # p = Person()
# # p.greet()

#examples
# class MyFunc:
#     def __call__(self, x):
#         return x * 2

# f = MyFunc()
# print(f(10))  # Output: 20

import math

try:
    val = int("abc")          # ValueError
except ValueError:
    print("ValueError: Invalid value for integer conversion.")

try:
    result = math.len(100)         # TypeError
except TypeError:
    print("TypeError: len() used on wrong type.")

try:
    data = [1, 2, 3]
    print(data[5])            # IndexError
except IndexError:
    print("IndexError: Index out of range.")

