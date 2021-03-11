# name= input('what is your name?')
# print(f"name is {name}")

# prompt = "if you tell us your name.we can print it"
# prompt += "\n what is your first name? "

# name = input(prompt)

# height = input("what is your height? ")
# height =int(height)

# if height >= 5:
#     print('you are able to get that')
# else:
#     print('you are not able')

# number = input("Enter a number ")
# number = int(number)

# if number % 2 == 0:
#     print(f"The number  {number} is even")
# else:
#     print(f"The number {number} is odd")

#     task 7-1 
# car = input("Let me see if I can find you a subaru")

# question = input("how many people are in  dinner group?")
# question = int(question)

# if question >= 8:
#     print("the will have to wait for a table")
# else:
#     print("Their table is ready")

numbers = {
    'jahed' : [3,4,5],
    'hossen' : [6,7,3],
    'jebon' : [22,33,66],
}

for name,number in numbers.items():
    print(f'the name is {name}')
    for num in number:
        print(" " + str(num))

current_number = 1

while current_number <= 5:
    print(current_number)
    current_number +=1
