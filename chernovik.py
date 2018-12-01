pl = '  /planet Neptune   '
print(str(pl.strip().split()[-1]))

# **********************************LISTS***************************************

mylist = ["Вася", "Маша", "Петя", "Саша"]

print(mylist)
print(len(mylist))
mylist.append("Mu")
print(mylist)
mylist.pop()
print(mylist)
mylist.append("Mu")
print(mylist)
print(mylist.count("а"))
print(mylist.count("Маша"))
print(mylist)
print(mylist.index("Петя"))
print(mylist[::-1])
print(mylist[1],'-', mylist[2])
print('Вася' in mylist)
del mylist[2]
print(mylist)
mylist.append('Маша')
print(mylist)
mylist.remove('Маша')
print(mylist)


print('_____________________________________________________________________________')
# **********************************DICTIONARIES***************************************

user = {'name': 'Маша', 'age': 25, 'have_airplane': True}
print(user)
print(str(user['age']))
user['class'],user['income']='A','high'
print(user)
user ['age']= 76
print(user)
print(user.get('age'))
print(user.get('gender', 'Male'))
del user['class']
print(user)
 # List of dictionaries

all_users = [
   {'name': 'Маша', 'age': 25, 'have_airplane': True},
    {'name': 'Вася', 'age': 8, 'have_airplane': False},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
]

print(all_users)
print(all_users[0]['age'])


