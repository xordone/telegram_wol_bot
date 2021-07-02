import telebot
from telebot import types

import wakedown
from cfg.config import authorized_users
from cfg.config import token as teletoken

bot = telebot.TeleBot(token=teletoken)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
button1 = types.KeyboardButton('Wakeup')
button2 = types.KeyboardButton('Shutdown')
button3 = types.KeyboardButton('About')
markup.add(button1, button2, button3)


@bot.message_handler(regexp='Wakeup|Shutdown|About')
def send_welcome(message):
    process_select_step(message)


def process_select_step(message):
    if message.from_user.username in authorized_users:
        try:
            if message.text == 'Wakeup':
                bot.send_message(message.chat.id, wakedown.wakeup(), parse_mode='Markdown', reply_markup=markup)
            elif message.text == 'Shutdown':
                bot.send_message(message.chat.id, wakedown.shutdown(), parse_mode='Markdown', reply_markup=markup)
            elif message.text == 'About':
                bot.send_message(message.chat.id, wakedown.about(), reply_markup=markup)
        except Exception as e:

            bot.reply_to(message, '{}'.format(e))
    else:
        bot.send_message(message.chat.id, 'Пшёл на Х')


if __name__ == '__main__':
    bot.polling(none_stop=True)
