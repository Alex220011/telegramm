﻿import telebot
import constants , datetime

bot = telebot.TeleBot(constants.token)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, str(message.datetime))


if __name__ == '__main__':
    bot.polling(none_stop=True)
