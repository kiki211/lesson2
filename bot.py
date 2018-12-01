from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

API_KEY = "747629397:AAG6RpN5OjKkIFc5DZXKIBnLIE3rr1VEgME"

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Privet {}! Ti napisal: {}" .format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def planet(bot, update,args):
    print('Command /planet was called')
    current_time = datetime.datetime.now()
    #input_planet = str(update.message.text.strip().split()[-1])
    input_planet = args[0].strip().title()
    all_planets = {'Pluto': ephem.Pluto(),
               'Mercury': ephem.Mercury(),
               'Venus': ephem.Venus(),
               'Mars': ephem.Mars(),
               'Jupiter': ephem.Jupiter(),
               'Saturn': ephem.Saturn(),
               'Uranus': ephem.Uranus(),
               'Neptune': ephem.Neptune()
               }
    answer = ''


    def constel_answer(planet):
        planet.compute(current_time)
        return ('Planet\'s info: %s %s %s' % (planet.ra, planet.dec, planet.mag),
                'The current constellation is: {}'.format(ephem.constellation(planet)[1]))


    if input_planet in all_planets:
        answer = constel_answer(all_planets[input_planet])
    elif input_planet == 'Earth':
        answer = 'Earth is our planet!'
    else:
        answer = 'Please enter a planet of the Solar system the after the command /planet.'
    update.message.reply_text(answer)


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()
