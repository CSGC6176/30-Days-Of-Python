# Level 1
# 1
age = int(input('Enter your age  :'))
if age>=18:
    print('You are old enough to learn to drive')
else:
    print('You need ' , abs(age-18) ,' more years to learn to drive.')


# 2
my_age=int(input('Enter my age '))
your_age =int(input('Enter your age '))
if my_age<your_age:
    print('You are  ' , abs(your_age-my_age) , ' years older than me ')
else:
    print('I am ' , abs(your_age-my_age) , ' years older than you ')

# 3
a = int(input('Enter number one : '))
b = int(input('Enter number two : '))
if a> b:
    print('a is greater than b')
elif a==b:
    print('a and b are equal ')
else:
    print('a is less than b')


# Level 2
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

# 1
marks = int(input("Enter marks  : "))
if marks>=80 and marks <=100:
    print('A')
elif marks>=70 and marks <=89:
    print('B')
elif marks>=60 and marks<=79:
    print('C')
elif marks>=50  and marks<=59:
    print('D')
else:
    print('F')


# 2
month=input('Enter month : ')

if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn')
elif month == 'December' or  month == 'January' or month == 'February':
    print('The season is Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('The season is Spring')
elif month == 'June'  or   month == 'July' or  month == 'August':
    print('The season is Summer')

# 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input("Enter fruit to be added : ")
if  not fruit in fruits :
    fruits.append(fruit)
    print(fruits)
else:
    print('That fruit already exist in the list')


# Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person.keys():
    print(person['skills'][len(person['skills'])//2])
if 'skills' in person.keys():
    if 'Python'  in person['skills']:
        print(True)

if   'JavaScript' and 'React' in person['skills']:
    print('He is a front end developer')
if 'Node' and ' Python' and 'MongoDB' in person['skills']:
    print('He is a backend developer')
if 'React' and 'Node' and 'MongoDB' in person['skills']:
    print('He is a backend developer')
else:
     print('unknown title')

if person['is_marred']==True and person['country'] =='Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')
