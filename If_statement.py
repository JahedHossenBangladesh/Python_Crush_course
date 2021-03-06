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
