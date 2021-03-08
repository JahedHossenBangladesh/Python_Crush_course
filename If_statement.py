cars = ['audi','bmw','subaru','toyota']

for cars in cars:
    if cars == 'bmw':
        print(cars.upper())
    else:
        print(cars.title())


requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies')

age = 22
money = 1000
if age <= 23:
    print('he is less then me')
else:
    print('he is elder then me')


if age <= 23 and money >= 5000:
    print('i can make her girl friend')
else:
    print('i wont make her girl friend')



looking ='bed'
having_respect = True

if looking == 'nice' or having_respect == True :
    print('i do friendship with you')
else:
    print('i dont do  friendship with you')

banned_users = ['andrew','carolina','david']
user = 'marie'
if user in banned_users:
    print(f'{user} is  in the list')
else:
    print(f'{user} is in not the list')

user ='jahed'

if user not in banned_users:
    print(f'{user} is not in the list')
else:
    print(f'{user} is in list')

car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

age =17

if age>=18:
    print('you are old enough to vote')
    print('Have you registered to vote yet')
else:
    print('sorry,you are not enough to vote')
    print(f'contact {18-age} year later')

if age < 4:
    print('you are child')
elif age < 18:
    print('you are young')
elif age < 19:
    print('you vote')
else:
    print('you are voter')

if 'andrew' in banned_users:
    print("andrew is in list")

if 'jahed' in banned_users:
    print('jahed is in the list')

banned_users.append('shahed')

if 'shahed' in banned_users:
    print('Sahed is in the list')

if 'andrew' in banned_users:
    print('andrew is in list')
elif 'jahed' in banned_users:
    print('jahed is in list')
elif 'sahed' in banned_users:
    print('shahed is in the list')

print('\nFinishing the line')

# Task 5-3
alien_color = ['green','yellow','red']

if alien_color == 'green':
    print('The player earned 5 points')
else:
    print('')

# Task 5-4
if alien_color != 'green':
    print('The player earn 10')
else:
    print('the color is not match')

# Task 5-5
alien_color.append('perpal')

if alien_color == 'green':
    print('Player earned 5 points')
elif alien_color == 'yellow':
    print('Player earned 10 points')
elif alien_color == 'red':
    print('player earned 15 points')

# Task 5-6
age = 20

if age < 2:
    print('person is a baby')
elif age == 2 and age < 4:
    print('The person is a toddler')
elif age == 4 and age <13:
    print('The person is kid')
elif age == 13 and age <20:
    print('The person is teenager')
elif age == 20 and age < 65:
    print('The person is an adult')
elif age >= 65 :
    print('The person is elder')

# 5-7

fruit = ['apple','banana','pinapple','jack fruit']

if fruit =='apple':
    print('I like apple')
elif fruit =='banana':
    print('I like banana')
elif fruit =='pinapple':
    print('This is pinapple')
elif fruit =='jack fruit':
    print('this is jack fruit')
else:
    print('the code is not working')

for i in fruit:
    if i == 'apple':
        print('this is apple')
    elif i == 'banana':
          print('this is banana')
    else:
        print('this is nothing')

my_fruint = ['apple','banana','Jamrul']

if my_fruint in fruit:
    print('yes , the food is in my list')
else:
    print('no that is not in my list')
    

if 'apple' in fruit:
    print('yes,apple in the list')
elif 'banana' in fruit:
    print('yes, banana in the list')
else:
    print('no, it is not in the list')

requested_topping =['mushrooms','green peppers','extra cheese']
for requested_topping in requested_topping:
    print(f'Adding {requested_topping}')

print('\n Finishing line')

requested_topping =['mushrooms','green peppers','extra cheese']
for requested_topping in requested_topping:
    if requested_topping == 'green peppers':
        print('soory green peppers is out of stock')
    else:
        print(f'Adding {requested_topping}')
    
    print('\n the line is finished')


requested_topping=[]
if requested_topping:
    for requested_topping in requested_topping:
        print(f'adding {requested_topping}')
        print('\n adding new line')
else:
    print('Are you sure you want a planin pizza?')

available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
request = ['mushrooms', 'french fries', 'extra cheese']
for request in available_toppings:
    if request in available_toppings:
        print(f'adding {request}')
    else:
        print(f'Sorry,we dont have {request}')
              
print('\n Finishing making your pizza')



user = ['admin','user','buyer','seller','owner','worker']
for user in user:
    if user == 'admin':
        print(f'welcome mr {user}')
    else:
        print(f'hello, {user} thank you for logging')

users = []
if users == []:
    print('we need to fined some one')
else:
    print('this is not empty')
