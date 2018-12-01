#  Task 1
list= [1,2,3,4,5,6,7,8,9,10]
for dig in list:
    print(dig+1)

for dig in range(1,11,1):
    print(dig+1)

# Task 2
string = str(input("Please type something: "))
for l in string:
    print(l.upper())
# Task 3
# Посчитать и вывести средний балл по каждому классу.
# Посчитать и вывести средний балл по всей школе.
grades = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
         {'school_class': '4b', 'scores': [2,4,4,5,3]},
         {'school_class': '4c', 'scores': [5,5,5,5,4]},
         {'school_class': '4d', 'scores': [1,5,4,5,1]}]

class_avg = []
for g in grades:
    grade = sum(g['scores'])/len(g['scores'])
    class_avg.append(grade)
    print('The average grade in class {} is: {}' .format(g['school_class'], grade))

print("The average grade in school is: {}" .format(sum(class_avg)/len(class_avg)))










