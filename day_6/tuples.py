# Level 1
# 1
empty_tuple=()
print(empty_tuple)

# 2
brothers_t=('John','Mack','Rony')
print(brothers_t)
sisters_t=('Emma','June','Kelly')
print(sisters_t)

# 3
siblings=brothers_t+sisters_t
print(siblings) 

# 4
print("No of siblings " , len(siblings))

# 5
parents_t=('Kevin','Mary')
family_t=parents_t+siblings
print(family_t)


# Level 2
# 1
father,mother,*siblings=family_t
print(father)
print(mother)
print(siblings)

# 2
fruits=('Mango','Banana','Apple','Grapes','Orange')
vegetables=('Potato','Cabbage','Brocolli','Spinach','Pumpkin')
animal_products=('Cheese','Milk','Meat','Egg','Beef')
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)

# 3
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)

# 4
print(food_stuff_tp[len(food_stuff_tp)//2])

# 5
print(food_stuff_tp[0:3],food_stuff_tp[-3:])

# 6
del food_stuff_tp
# print(food_stuff_tp)

# 7.1
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries )

#7.2
print('Iceland' in nordic_countries )


