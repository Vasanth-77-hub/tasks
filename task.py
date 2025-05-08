# Name = if(input("Enter your name: "))
# #it will be print your name
# Height = if(input(float(int("Enter your height: "))))
# #it will be print your height
# weight =if(input)(float(int("Enter your weight: ")))

# name = input("Enter your name: ")

# height = input(float(int("Enter your height: ")))

# weight = input(float(int("Enter your weight")))

name = input("Enter your name: ")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)
print(f"{name}, your BMI is {bmi:.2f}")

# if BMI > 0:
#     if BMI < 18.5:
#         print(name + ", you are underweight.")
#     elif BMI <= 24.9:
#         print(name + ", you are normal weight.")
#     elif BMI <= 29.9:
#         print(name + ", you are overweight.")
#     elif BMI <= 34.9:
#         print(name + ", you are obese.")
#     elif BMI <= 39.9:
#         print(name + ", you are severely obese.")
#     else:
#         print(name + ", you are morbidly obese.")
# else:
#     print("Please enter valid input.")

def class_bmi(name, bmi):
    if bmi <= 0:
        return "Please enter valid input."
    elif bmi < 18.5:
        return f"{name}, you are underweight."
    elif bmi <= 24.9:
        return f"{name}, you are normal weight."
    elif bmi <= 29.9:
        return f"{name}, you are overweight."
    elif bmi <= 34.9:
        return f"{name}, you are obese."
    elif bmi <= 39.9:
        return f"{name}, you are severely obese."
    else:
        return f"{name}, you are morbidly obese."

print(class_bmi(name, bmi))
