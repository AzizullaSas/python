# person = input("Stastus of the person:")

# if person == 'Student' or person == "school 10th" or person == "school 11th" :
#     print(f"He is more then 16 years old")
# else:
#     print(f"He is less then 16 years old")



age = int(input("Enter your age: "))


if 0 <= age <18:
    print("You are kid!")
elif 18 <= age <35:
    print("You are man or woman!")
elif 35 <= age <70:
    print("You are oldman or oldwoman")
elif age >= 70:
    print("You are old")
else:
    print("Incorrect age, please enter your age again")