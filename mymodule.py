class CallClassName:
    def __init__(self, name):
        self.name = name
    def myFunc(self):
        print(f'hello my name is {self.name}')
pass

try:
    print(x)
except NameError:
    print('A variable x is not defined')
except: 
    print('Something else went wrong')

try:
    print('hello')
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('The try except is finished')

x = -1  


# y = 'hello'

# if not type(y) is int:
#     raise TypeError('Only integers are allowed')

username = input('Enter username: ')
print('Username is: ' + username)