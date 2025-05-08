# name = input("Enter you name: ")

# weight = int(input("Enter your weight in pounds: "))

# height = int(input("Enter your height in inches: "))

#  BMI = (10000 * weight_kg) / (height_cm ** 2)

# print(BMI)

# if BMI>0:
#     if(BMI<18.5):
#         print(name +", you are underwight.")
#     elif (BMI<=24.9):
#         print(name +", you are normal weight.")
#     elif (BMI<29.9):
#         print(name +", you are overweight. You need to exercise more and stop sitting and writing so many python tutorials.")
#     elif (BMI<34.9):
#         print(name +", you are obese.")
#     elif (BMI<39.9):
#         print(name +", you are severely obese.")
#     else:
#         print(name +", you are morbidly obese.")
# else:
#     print("Enter valid input")

# Ask the user for their name
name = input("Enter your name: ")

# Ask for weight in kilograms
weight_kg = float(input("Enter your weight in kilograms: "))

# Ask for height in centimeters
height_cm = float(input("Enter your height in centimeters: "))

# Calculate BMI using the formula for kg and cm
BMI = (10000 * weight_kg) / (height_cm ** 2)

# Print the calculated BMI
print(f"{name}, your BMI is: {round(BMI, 2)}")

# Check the BMI category
if BMI > 0:
    if BMI < 18.5:
        print(name + ", you are underweight.")
    elif BMI <= 24.9:
        print(name + ", you are normal weight.")
    elif BMI <= 29.9:
        print(name + ", you are overweight.")
    elif BMI <= 34.9:
        print(name + ", you are obese.")
    elif BMI <= 39.9:
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are morbidly obese.")
else:
    print("Please enter valid input.")
