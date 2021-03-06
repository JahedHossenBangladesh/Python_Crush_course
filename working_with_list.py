z = ['a','b','c','d','e','f']
for z in z : 
    print(f"{z.upper()} is a alphabate")
    print(f"i dont know {z.title()}.\n")

print("Thank you for that")

magicians = ['alice','david','carolina']
for magicians in magicians:
 print(magicians)



pizza =['megdonal','donut','kfc','cheap']
for pizza in pizza:
   print(f'i like {pizza.upper()} pizza')
   print('how much you like pizza?')


animal = ['Monky','elephan','dog','Tiger']
for animal in animal:
    print(f'The animal name is {animal.upper()}')
    print(f'{animal.upper()} is a grate pet')


for value in range(1,5):
    print(value)


number = list(range(2,10))
print(number)


even_number =list(range(2,10,2))
print(even_number)


squares =[]
for value in range(1,11):
  squares.append(value**2)
print(squares)


min_digit = min(squares)
print(min_digit)


max_digit = max(squares)
print(max_digit)
print(sum(squares))


squares = [value**2 for value in range(1,11)]
print(squares)


list_data = []
for value in range(1,20):
    print(value)
# for vlaue in range(1,10000):
#     print(vlaue)

for value in range(3,30):
    print(value)


for value in range(1,10):
    list_data.append(value**3)
    print(list_data)


print(list_data[0:3])
print(list_data[1:3])
print(list_data[:4])
print(list_data[2:])
print(list_data[-3:])


player = ['i','you','they','ours']
for player in player[:3]:
    print(player.title())


my_foods =['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)


my_foods.append('cannoli')
friend_foods.append('ice cream')


print(my_foods)
print(friend_foods)


# Task 

message =["I","love",'you','so','much']
print(message[:3])
print(message[3:])
print(message[-3:])

pizza= ['a','b','c','d']
pizza.append('z')

print(pizza)

friend_pizza = pizza[:]
print(friend_pizza)

for pizza in pizza:
    print(f'my favourite pizza is: {pizza}')
  
for friend_pizza in friend_pizza:
    print(f'my friend pizza is : {friend_pizza}')

# Tuple

dimension = (100,200)
print(dimension[0])
print(dimension[1])

for dimension in dimension:
    print(f'this is orginal {dimension}')

dimension = (300,400)
for dimension in dimension:
    print(f'this is new {dimension}')

# Task
basic_food = ('rice','potato mixture','Dal','Hilsha Fish','Chicken')
for basic_food in basic_food :
    print(basic_food)

basic_food = ('rice','potato mixture','dal','loitta fish','shutki')
for basic_food in basic_food:
    print(basic_food)
