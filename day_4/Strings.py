# 1
conc="Thirty " + "Days " + "Of " + "Python "
print(conc)

#2
conc2='Coding ' + 'For ' + 'All'
print(conc2)

#3
company= "Coding For All"

#4
print(company)

#5
print(len(company))

#6
print(company.upper())

#7
print(company.lower())

#8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9
print(company[0:6])

#10
print(company.index('Coding'))
print(company.rindex('Coding'))
print(company.find('Coding'))
print(company.rfind('Coding'))

#11 
print(company.replace('Coding','Python'))

#12
word='Python for Everyone'
print(word)
print(word.replace('Everyone','All'))

#13
print(company.split())

#14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

#15
print(company[0])

#16
print(company[len(company)-1])

#17
print(company[10])

#18
print("".join(e[0] for e in word.split(' ')).upper())

#19
acronym=''
for x in company.split(' '):
    acronym+=(x[0].upper())

print(acronym)

#20
print(company.find('C'))

#21
print(company.find('F'))

#22
print(company.rfind('I'))

#23
print("You cannot end a sentence with because because because is a conjunction".find('because'))

#24
print("You cannot end a sentence with because because because is a conjunction".rfind('because'))

#25
sent="You cannot end a sentence with because because because is a conjunction"
print(sent[sent.index('because'):sent.rindex('e')+1])

#26
print(sent.find('because'))

#27
#same as 25

#28
print(company.startswith('Coding'))

#29
print(company.endswith('coding'))

#30
print('   Coding For All      ' .strip())

#31
print('30DaysOfPython'.isidentifier())

#32
print('thirty_days_of_python'.isidentifier())

#33
print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

#34
print('I am enjoying this challenge.\nI just wonder what is next.')

#35
print('Name\t\t\tAge\t\tCountry\t\tCity\nAsabeneh\t\t250\t\tFinland\t\tHelsinki')

# radius = 10
#area = 3.14 * radius ** 2

#36
radius = 10
print('radius = {} '.format(radius))
print('area = {} * radius ** {}'.format(3.14,2))
print('The area  of  a circle with radius {} is {:.0f} meters square'.format(radius,3.14*radius**2))

#37
a=8
b=6
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))

