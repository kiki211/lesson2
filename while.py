# Напишите функцию ask_user(), которая с помощью input()
# спрашивает пользователя “Как дела?”,
#  пока он не ответит “Хорошо”
def ask_user():
    while True:
        user_say = input('Kak dela?: ')
        if user_say == 'Good':
            print ("The answer {} is correct, bye bye now!" .format(user_say))
            break

print(ask_user())


# Создайте словарь типа "вопрос": "ответ", например:
# {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
# Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре,
# программа давала ему соотвествующий ответ. Например:
# Пользователь: Что делаешь?  Программа: Программирую

my_dic = {"How are you?" : "Good",
          "Whatcha duin?" : "Coding",
          "Are you hungry?": "Just ate, thx",
          "Need some cash?" : "Would be great",
          "H": 'aga'}

def ask_user2():
    while True:
        try:
            user_ask = str.capitalize(input("Ask a question:"))
            for k, v in my_dic.items():
                if k == user_ask:
                    print(v)
                    break
                if user_ask == 'Bye' or user_ask == 'Goodbye':
                    print("If you want {} then bye bye now!" .format(user_ask))
                    quit()
            else:
                print("Sorry, I don't get this question: {}   Can you ask something else?"
                      .format(user_ask.strip()))
        except KeyboardInterrupt:
            print("Sorry you are leaving and had to use keyboard interruption")
            quit()
print(ask_user2())



