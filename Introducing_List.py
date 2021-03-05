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



