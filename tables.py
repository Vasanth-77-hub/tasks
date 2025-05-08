# def print_table(num):
#     print(f"Multiplication of table :{num}")
#     for i in range(1,30):
#      print(f"{num} * {i} = {num*i}")

# n = int(input("Enter a number: "))
# print_table(n)



def add_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num
