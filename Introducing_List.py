# This is capter 3

bicycles = ["trek","cannondale",'redline','specialize']
print(bicycles)

print(bicycles[1])

print(bicycles[0].upper())
print(bicycles[-1])
print(bicycles[-2].title())

message = f"My first bicycles is {bicycles[-3].lower()}"
print(message)


friends =['Tuhin','Shahed','Tohid','Munna']
print(friends[3].upper())
message = "Hello"
message2 = f"hi and {message} {friends[0].upper()}"

print(message2)

myVachel =['car','Hunda','neno']
message = f"I would like to take {myVachel[2]}"
print(message)

motorcycles = ['honda','yamaha','suzuki']

motorcycles[0] ='ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles.insert(2,'ducati')
print(motorcycles)
del motorcycles[2]
print(motorcycles)
popend_motorcycles = motorcycles.pop()
print(motorcycles)
print(popend_motorcycles)

print(f"The last pop is {popend_motorcycles}")

motorcycles.append('nano')
print(motorcycles)

first_delete = motorcycles.pop(0)
print(first_delete)

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)

# task ..

dinner_list =["Noyon","Jony","Munna","Tohid","Tuhin","Jonak"]
message = f'please {dinner_list[0]} come in the birthday'
print(message)
not_attend = dinner_list.pop()
print(not_attend)
dinner_list.append('Efan')
print(dinner_list)
pop_end = dinner_list.pop()
print(f'please come {pop_end.upper()}')
dinner_list.insert(0,'Sahed')
print(dinner_list)
dinner_list.insert(3,'Bipu')
print(dinner_list)
dinner_list.append('Humaiyun')
message =f'Please come {dinner_list.pop()} in the party'
print(message)
message = f'please {dinner_list[0]} and {dinner_list[4]} come to the dinner'
print(message)
del dinner_list[0]
print(dinner_list)

dinner_list.remove('Tuhin')
print(dinner_list)

dinner_list.sort()
print(dinner_list)
dinner_list.sort(reverse = True)
print('\nHerer is the orginal list:')
print(dinner_list)
print('\n Here is the sorted list:')
short_list = sorted(dinner_list)
print(short_list)
short_list.reverse()
print(f'the reverse is not working {dinner_list} ')

invited_person = len(dinner_list)
print(f'the invited person is {invited_person}')

# Task 3-8 
wanna_visit = ["Kashmir","Makka","Madinatul Munabra","Finland"]
print('The orginal lis :')
print(wanna_visit)

sort_visit = sorted(wanna_visit)
print(f'shorted list {sort_visit}')
sort_visit.reverse()
print(f'the reverse is not working {sort_visit} ')
print(f'orginal list: {wanna_visit}')
wanna_visit.sort()
print(wanna_visit)
wanna_visit.reverse()
print(wanna_visit)
wanna_visit.sort()
print(wanna_visit)
visted_place = len(wanna_visit)
print(f'total place {visted_place}')

# Avoiding index error when working with lists 

motorcycles =['honda','yamaha','sukuki']
print(motorcycles[2])
print(motorcycles[-1])

