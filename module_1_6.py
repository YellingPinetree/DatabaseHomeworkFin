my_dict = {'Name' : 'Sophia', 'Age' : 26, 'Hobbies' : ['cooking', 'drawing', 'writing']}
print(my_dict)
my_dict['Favorite color'] = 'blue'
print(my_dict['Age'])
print(my_dict['Favorite color'])
my_dict.update({'Favorite book' : 'The Witcher',
                'Occupation' : 'Student'})
del my_dict['Hobbies']
print(my_dict)

my_set = {1, 2, 3, 4, 5, 1, 2, 4, 5, 3, 5}
print(my_set)
my_set.add(True)
my_set.add('cat')
my_set.add(('meow', 'bark', 'chirp'))
my_set.discard(1)
print(my_set)