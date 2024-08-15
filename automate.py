import sys
import random

print(random.randrange(1,50))

print(sys.version)
print('hello world')

if 5 > 2:
    print('5 is greater than 2')
if 5 > 2:
    print('5 is greater than 2')
    
a = 200
b = 'ejiro'
c = True
print(type(a))
print(type(b))
print(type(c))


x = int(3)
y = str(3)
z = float(3)

print(x)
print(y)
print(z)

x , y, z = 'ejiro', 'is', 'awesome'
print(x,y,z)

x = y = z = 'ejiro'

print(x)

fruits = ['apple', 'banana', 'cherry']

x,y,z = fruits

print(x,y,z)

val = 'awesome'

def myFunction():
    global val
    val = 'fantastic'
    print('hello from a function' + val)

myFunction()

   
print('hello from a function' + val)

print(type(1j))

data = 45

print(complex(data))

a = 'hello world'

print(a[0])

for x in "bananas":
    print(x)

print(len(a))