# 1
dog={}
print(dog)

# 2
dog={'Name':'Tom','breed':'labrador','legs':4,'age':3}
print(dog)

# 3
stud_dict={'first_name':'John','last_name':'Doe','gender':'male','age':23, 'marital_status':'umarried', 
            'skills':['Java','Python','C','Redux','HTML'], 
            'country':'US', 'city':'Washington',
            'address':{
                'street':'Space Street',
                'zip_code':'110011'
            }}

# 4
print(len(stud_dict))

# 5
print(stud_dict['skills'])
print(type(stud_dict['skills']))

# 6
stud_dict['skills'].append('CSS')
print(stud_dict)

# 7
print(stud_dict.keys())

# 8
print(stud_dict.values())

# 9
print(stud_dict.items())

# 10
del stud_dict['city']
print(stud_dict)

# 11
del stud_dict['address']
print(stud_dict)



