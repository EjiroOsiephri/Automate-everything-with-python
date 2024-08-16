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

txt = 'The best things in life are free'

if 'free' in txt:
    print('yes, free is in the text')

if 'expensive' not in txt:
    print('yes, expensive is not in the text')

print(txt[10:12])
print(txt.upper())
print(txt.lower())

data = " i am a boy "
print(data.strip())

val = 'hello, world'
print(val.replace('w', 'z'))
print(val.split(','))

price = 59
txt = f'The price is {price} dollars'
print(txt)

x =9
print(f"the value of x is {x:.2f}")
print("we are the so called \"Vikings\" from the north")

test = 'hello'
print(test.encode())

a = 200
b =33

if b > a:
    print('B is greater than a')
else:
    print('A is greater than b')

print(bool(a))

tuple = ('Ejiro', 'dan', 'mike', 'idiot')
print(type(tuple))

print(len(tuple))

x = ""
print(5 > 3)
print(isinstance(x, int))

listt = list(('ejiro', 'dan', 'mike', 'idiot'))
print((listt[-4:-1]))

thisList = ['apple', 'banana', 'cherry', 'mango']  
thisList[0:2] = ['ejiro', 'dan']

otherList = ['mike', 'idiot']

thisList.insert(3, 'mike')

thisList.append('idiot')
thisList.extend(otherList)

print(thisList)

print(thisList.remove('idiot'))
del thisList[0]

thisList.pop(3)

for x in thisList:
    print(x)

for i in range(len(thisList)):
    print(i)

i = 0
while i < len(thisList):
    print(thisList[i])
    i+=1

fruits = ['apple', 'banana', 'cherry', 'mango']
newList = []

for x in fruits:
    if 'a' in x:
        newList.append(x)
        print(newList)
    

value = range(1,10)

data = [x**2 for x in value if x > 3 ]
print(data)

print([x for x in fruits if x != 'banana'])
print([x for x in range(10)])