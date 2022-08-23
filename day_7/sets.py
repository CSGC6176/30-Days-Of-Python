from logging import StringTemplateStyle
from stat import FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
import xdrlib


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# 1
print(len(it_companies))

# 2
it_companies.add('Twitter')
print(it_companies)

# 3
more_companies={'Cognizant','Wipro','TCS','Infosys'}
it_companies.update(more_companies)
print(it_companies)

# 4
it_companies.remove('Wipro')
print(it_companies)

# 5
it_companies.discard('TCS')
print(it_companies)

# Level 2
# 1

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))

# 2
print(A.intersection(B))

# 3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

# 5
A.update(B)
print(A)

B.update(A)
print(B)

# 6
print(A.symmetric_difference(B))

# 7
del A
print(A)

del B
print(B)

# Level 3
# 1
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set=set(age)
print(ages_set)

print('Comparing Lengths')
print(len(age))
print(len(ages_set))
print('Age list size is bigger')  if len(age) > len(ages_set) else  print('Age set len is bigger')
    
# 2
# String : String are surrounded by double quotes.Strings are immutable .We can work on Strings
# List:List are mutable data types.We can add or remove elements.It size is not fixed
# Tuples:Tuples are immutable datat types
# Set:Set are collection of unique items.

# 3
sent='I am a teacher and I love to inspire and teach people'
x= sent.split(" ")
print(x)
print(set(x))
print("Unique word in sentence " , len(set(x)))