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

fruitsList = ['mango', 'kiwi', 'mango', 'apple', 'cocunout']

fruitsList.sort(reverse=True)

fruitsList.reverse()

newList = fruitsList.copy()
newList = list(fruitsList)

newList.extend(fruitsList)

print(fruitsList[-1])

list1 = ['e', 'b','c', 'd', 'e','f', 'g', 'h']
list2 = [1,2,3,4,5,6,7]

for x in list1:
    list2.append(x)

print(list2)


newTuple2 = (1,4,6,8,9,12,0)
newTuple = ('win', 'go', 'allow', 'ejiro', 'obus', 'ayo')

y = list(newTuple)
y[1] = 'dan'
print(y)


fruit = ('apple', 'banana', 'cherry', 'mango', 'raspberry', 'cocunut', 'peach')

(one,two, *three ) = fruit


print(three)


thisSet = {"apple", "banana", "cherry", "mango"}

anotherSet = {'tropical', 'data', 'allow', 'free', 'life'}

tropical = {'data', 'vql', 'etc'}

tropical.add('wahala, wahala')

anotherSet.update(tropical)

intersection = anotherSet.intersection(tropical)


x = anotherSet.pop()

for x in anotherSet:
    print(x)

print(x)


print(intersection)

thisDict = {
    "car": "ford",
    "model": "mustang",
    "year": 1964,
    "color": ['red', 'blue', 'green'],
    "price": 5000,
    "price": 15000,
}

x = thisDict.get('model')
y = thisDict.keys()

thisDict['color'] = 'black'

print(x, y)
print(len(thisDict))

print(type(thisDict))

z = thisDict.items()
print(z)

if 'model'  in thisDict:
    print('yes, model is one of the keys in thisDict')
   
thisDict['year'] = 2020

thisDict.update({'price': 28000})

thisDict.update({'buyer': 'ejiro'})

print(thisDict)

for x, y in thisDict.items():
    print(x, y)

myFamily = {
    "rukky":{
        "name": "rukky",
        "year": 2010
    },
    "ejiro": {
        "name": "ejiro",
        "year": 2005
    },
    "obus" :{
        "name": "obus",
        "year": 2003
    },
    "esiri":{
        "name": "esiri",
        "year": 2012
    }
}

for x in myFamily:
    print(myFamily[x])

for x, obj in myFamily.items():
    print(x, obj)


a = 200
b = 33
c =40
if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')
else:
    print('a is greater than b')

if a > b and c > a:
    print('both conditions are true')
else:
    print('one or both conditions are false')

i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i+=1  

def my_function(a,b):
   return a * b

print(my_function(3,4))

def my_function(*kids):
    print(kids)
    print('the youngest child is ' + kids[2])

my_function('emeka', 'ejiro', 'dan')

def my_function(**kid):
    print(kid)
    print('his last name is ' + kid['lname'])  

my_function(fname = 'ejiro', lname = 'obus')

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

tri_recursion(6)