# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:16:56 2021

@author: Umidjon Masnurov
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN =''	# You have to insert link there which is telegram botfather brought to you
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username
    answer = f"Hello {username}, You are welcome!"
    answer += "\nInsert your text"
    bot.reply_to(message, answer)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text 
    # reply = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    if msg.isascii():
        answer = to_cyrillic(msg)
    else:
        answer = to_latin(msg)
    bot.reply_to(message, answer)
    
bot.polling()