alien_0 ={'color':'blue','point':5}

print(alien_0['color'])
print(alien_0['point'])

alien_0['color'] = 'red'

print(alien_0['color'])

new_points = alien_0['point']
print(f'the point of alien_0 is {new_points}')

alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['point'] = 4
print(f'{alien_1}')

print(f"the color is {alien_1['color']}")


alien_2 = {'x':0,'y': 25,'speed':'medium'}
print(f"orginal position:{alien_2['x']}")

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 

alien_2['x'] = alien_2['x'] + x_increment

print(f"new position: {alien_2['x']}")

del alien_0['point']
print(alien_0)

favorite_language ={
    'Jahed':'python',
    'hossen': 'JavaScript',
    'Jebon': 'C'
}

languages = favorite_language['hossen'].upper()
print(f'hossen favorite_language is {languages}')

# get method for dictionary adding 
alien_3 ={'color':'pink','speed':'slow'}
point_value = alien_3.get('points','there is no points')
print(f'the points value is {point_value}')

# Task 6-10

person ={
    'first_name':'jahed',
    'last_name':'hossen',
    'age':33,
    'city':'chittagong'
}

print(f"{person['first_name']}")
# items method
for key, value in person.items():
    print(f"\nkey:{key}")
    print(f"Value:{value}")



for name,language in favorite_language.items():
    print(f"\n{name.upper()} is like {language.lower()}")


for name in favorite_language.keys():
    print(name.title())

print('\n')
favorite_language ={
    'jen':'python',
    'sarah': 'c',
    'edward' : 'ruby',
    'phil': 'python'
}
friends= ['phil','sarah']
# for name in favorite_language.keys():
#     print(name.title())

# for name in favorite_language.keys():
#   if name in friends:
#     language = favorite_language[name].title()
#     print(f"\t{name.title()}, I see you love {language}")

for name in favorite_language.keys():
    if name in friends:
        language = favorite_language[name]
        print(f"\t{name} likes {language}")


for name in sorted(favorite_language.keys()):
    print(f"Shorted name of {name.upper()}")

for language in favorite_language.values():
    print(f"\tthe language is {language}")



# This is 6-4

programming_words ={
    'items': 'it is includes the key and value',
    'keys': 'key is the item where it items name call something',
    'values': 'value say the quantity or meaning of that ',
    'uppper()': 'The word is upper',
    'shorted()': 'It is show with the serioul',
    'list' : 'is a kind or array as javascript',
    'dictionary': 'is like as Object of javascript'
}

for words,defination in programming_words.items():
    print(f"\t{words} meaning is {defination}")

rivers = {
    "Padma":"Rajshahi",
    "Surma":"Sylhet",
    "Sangu": "Chittagong"
}

for river_name,location in rivers.items():
    print(f"\n\t{river_name} runs through {location}")

for river_name in rivers.keys():
    print(f"\nriver name is {river_name}")

for location in rivers.values():
    print(f"\nriver located in {location}")


# Task 6-6

favorite_language_list = ['jen','sarah','edward','phil','sarah']

del favorite_language['phil']
print(favorite_language)

for name in favorite_language_list:
    if name in favorite_language.keys():
        print(f"{name} thank you take the poll")
    else:
        print(f"\n{name} invite him to join the class")

# Nesting dictionary

aliens =[alien_0,alien_1,alien_3]

for alien in aliens:
    print(alien)


aliens=[]
for alien_number in range(20):
    new_alien = {'color':'red','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
    print('....')
    


for alien in aliens[:3]:
    if alien['color'] == 'red':
        alien['color'] = 'Yellow'
        alien['speed'] = 'medium'
        alien['points'] =10 
        print(alien)

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
}

print(f"you order a {pizza['crust']} -crust pizza with  the folling toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


favorite_language = {
    'jen' : ['python','c'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil' : ['python','haskell']
}

for name,language in favorite_language.items():
    print(f"\n{name.title()}'s favourite language is :")
    for language in language:
        print(f"\t {language.title()}")

print('\n')

users = {
    'aeinstein' : {'first' : 'albert','last' : 'einstein','location' : 'princeton',},'mcurie' : {'first' : 'marie','last' : 'curle','location' : 'paris',},
}

for username, user_info in users.items():
  print(f"\nUsername: {username}")
  full_name = f"{user_info['first']} {user_info['last']}"
  location = user_info['location']

  print(f"\tfull name :{full_name.title()}")
  print(f"\tLocation:{location.title()}")
  
# 6-7 task

humaiyun = {
    'first_name':'Humaiyun',
    'last_name' : 'Akbar',
    'location': 'kumira',
}
shahed ={
    'first_name':'Shahed',
    'last_name':'hossen',
  'location':'Monsurabad',
    }
noyon = {
   'first_name': 'Kamrul',
    'last_name': 'hassan',
    'location' : 'goni mension',
}

people =[humaiyun,shahed,noyon]

for user in people:
    # print(f"userName:{user}")
    full_name = f"{user['first_name']} {user['last_name']}"
    location = f"{user['location']}"
    
    print(f"\nthe full name is : {full_name.title()} \n location in {location.upper()}")
cat = {
        'name':'meow',
        'owner':'pi',
}
dog ={
     'name':'don',
     'owner':'villain',
}
tiger = {
       'name': 'Messi',
        'owner': 'Naimer',
}
pets = [cat,dog,tiger]
 
for pet in pets:
    pet_name = pet['name']
    pet_owner = pet['owner']
      
    print(f"{pet_name} owner is {pet_owner}")

favorite_places = {
     'jahed':['cowx,s bazar','sentmartin','Bandorbon','kagrachori'],
     'nipa' : ['newziland','france','mokka','madina'],
      'ma'   : ['babarBari','shoshur bari','bonerBari','nanarBari']
}
 
for name,places in favorite_places.items():
     print(f"\nthe name is {name} likes:")
     for place in places:
         print(f"{place}")   
         
favorite_number = {
    'ami':[5,6],
    'tumi':[8,0],
    'she': [2,9],
    'he' : [34,87],
}

for name,number in favorite_number.items():
    print(f"\n{name}")
    for num in number:
        print(f"favorite number is {num}")

cities = {
    'ctg':{
        'country':'Bangladesh',
        'population': 23445,
        'fact':'give the call name',
    },
   'dhaka': {
        'country':'Bangladesh',
        'population':34344,
        'fact': 'give',
    },
    'shelate':{
        'country':'Bangladesh',
        'population':23423423,
        'fact': 'give',
    }
}

for name,info in cities.items():
    country = info['country'].title()
    population = info['population']
    fact = info['fact'].title()
    print(f"\nThe city name is {name}")
    for info in info:
        print(f"The country of the city is {country} and the population is {population} and the fact is {fact}")
