def cut_cake(parts):
    try:
        return 1/int(parts)
    except (ZeroDivisionError, TypeError, ValueError):
        return "Are you out of your mind?"

cake= cut_cake("23")
print(cake)


#                                           ******Tasks********

#1
answers = {"How are you?" : "Good",
          "Whatcha duin?" : "Coding",
          "Are you hungry?": "Just ate, thx",
          "Need some cash?" : "Would be great",
          "H": 'aga'}

def get_answer(question, answer):
    return answers.get(question)

def ask_user(answers):
    try:
        while True:
            user_input= str(input("Ask your question here: "))
            answer = get_answer(user_input, answers)
            print(answer)

            if user_input == 'Bye':
                break
    except KeyboardInterrupt:
            print("Poka, ti ostanovil programmu sam.")


print(ask_user(answers))



# 2
def get_summ(num_one, num_two):
    try:
        return int(num_one)+int(num_two)
    except ValueError:
        return("Ooops, you need to enter a number, try again.")

print(get_summ('aq',4.343))



