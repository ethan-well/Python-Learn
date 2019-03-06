print('Hello world!')
message = 'test traceback'
print(message)
str1 = " xxx \n "
print(str1)
print(str1.strip())
print('tttt')

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
bicycles[0] = 'trek2'
print(bicycles[0])

bicycles.insert(0, 'first')
print(bicycles)

del bicycles[0]
del bicycles[0]
print(bicycles)

poped = bicycles.pop()
print(poped)
print(bicycles)

arr = ['abc', 'acd', 'kk', 'ddd', 'lll']
print(sorted(arr))
print(arr)

for item in arr:
    print(item)
    print('xxxxx\n')

numbers = list(range(1, 6))
print(numbers)

squares = [value*2 for value in range(1, 11)]
print(squares)

car = "bmw"
print(car.upper())
print(car)

print('-*--'*3)
arr = [1]
for item in arr:
    print(item)

t = (1, 2, 3)
for i in t:
    print(i)
message = input("input some world:")
print(message)

string = "qWrddR"
print(string.title())

def describe_pet(animai_type, pet_name):
    """显示宠物信息"""
    print(animai_type + pet_name)

describe_pet('cat', 'little_cat')

def test(name='name', age=13):
    print(name)
    print(age)

test('name2', 14)


test_list = ['name1', 'age1']

def test(list):
    list[0] = 'name2'
test(test_list)
print(test_list)



