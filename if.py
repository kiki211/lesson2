# # IF tasks
# 1 Task age
your_age = int(input("Please enter your age here: "))

def age_activity(age):
    if age <= 5:
        return "Kindergarden"
    elif age <18:
        return "School"
    elif 18 >= age <= 24:
        return "College"
    elif 25 >= age <= 150:
        return "Work"
    else:
        return "Please enter a valid age!"


activity_answer = age_activity(your_age)
print(activity_answer)


# 2 Task strings
def two_str(a,b):
    if isinstance(a, str) and isinstance(b, str):
        if a == b:
            return 1
        elif a != b:
            if b == 'learn':
                return 3
            elif len(a) > len(b):
                return 2
            else:
                return "Doesn't match any criteria"
    else:
        return 0


print(two_str('asdsdsd','bsdsd'))
print(two_str('ad','bsdsd'))
print(two_str('asdsdsd','learn'))
print(two_str('asd','learn'))
print(two_str('learn','learn'))
print(two_str('asdsdsd',23232))





