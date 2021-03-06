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
