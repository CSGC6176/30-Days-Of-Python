# 1 

empty_list=[]
print(empty_list)

# 2
fruits=['Banana','Apple','Mango','Papaya','Lemon']
print(fruits)

# 3
print(len(fruits))

# 4
print(fruits[::2])

# 5
mixed_data_types=['John',25,165,'Single','Mumbai']
print(mixed_data_types)

#6
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']

# 7
print(it_companies)

# 8
print('No of Companies : ' , len(it_companies))

# 9
print(it_companies[0:len(it_companies)+1:3])

# 10
it_companies[4]='Infosys'
print(it_companies)

# 11
it_companies.append('TCS')
print(it_companies)

# 12
it_companies[len(it_companies)//2]='Cognizant'
print(it_companies)

# 13
it_companies[3]=it_companies[3].upper()
print(it_companies)

#14
print('# '.join(it_companies))

# 15
print('Microsoft' in it_companies)

# 16
it_companies.sort()
print(it_companies)

# 17
it_companies.reverse()
print(it_companies)

# 18
print(it_companies[0:3])

# 19
print(it_companies[-3:])

# 20
print(it_companies[len(it_companies)//2])

# 21
del it_companies[0]
print(it_companies)

# 22
del it_companies[len(it_companies)//2]
print(it_companies)

# 23
del it_companies[len(it_companies)-1]
print(it_companies)

# 24
print(it_companies.clear())

# 25
del it_companies
# print(it_companies)

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
main_end= front_end + back_end
print(main_end)

# 27
full_stack=main_end.copy()
full_stack.insert(full_stack.index('Node'),'Python')
full_stack.insert(full_stack.index('Node'),'SQL')
print(full_stack)

# Level 2
# 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
# Min
print(min(ages))

# Max
print(max(ages))

ages.append(min(ages))
ages.append(max(ages))
print(ages)
ages.sort()
print(ages)

# Median
median = (ages[len(ages)//2-1] + ages[len(ages)//2]) // 2
print(median)

# Average age
average_age = sum(ages)/len(ages)
print(average_age)

# Range
range_of_age=(max(ages)-min(ages))
print(range_of_age)

# Compare
range_min=(min(ages)-average_age)
range_max=(max(ages)-average_age)
print(range_min==range_max)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(countries[len(countries)//2])

countries1=countries[0:len(countries)//2]
print(countries1)

countries2=countries[len(countries)//2:]
print(countries2)

countries3=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch,rs,us,*scandic=countries3
print(ch)
print(rs)
print(us)
print(scandic)