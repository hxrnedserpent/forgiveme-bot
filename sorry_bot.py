import telebot
import os

api = os.environ.get('sorry_bot_api')
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.reply_to(message,'Hey, apakabar? Ini aku, Ghaizain, versi bot. Untuk melanjutkan, silahkan klik ini \'/apasih\'')

@bot.message_handler(commands=['apasih'])
def send_welcome(message):
 bot.reply_to(message,'Jadi aku buat bot ini pake python sebagai tanda permintaan maaf. Aku minta maaf karena udah nyebelin dan bikin kamu kecewa. Aku harap kamu bisa maafin aku :( so, \'/iya_dimaafin\' atau \'/enggak_ah\'')

@bot.message_handler(commands=['iya_dimaafin'])
def send_welcome(message):
 bot.reply_to(message,'Thanks yaaaa <3 I really miss you. Ayoo kita mulai lagi dari awal! Chat aku di personal chat kalo kamu udah maafin aku heheheheheh okay?')

@bot.message_handler(commands=['enggak_ah'])
def send_welcome(message):
 bot.reply_to(message,'Yah :( please tell me what should I do so you can forgive me? I am really really sorry........ please???? \'/ih_apasi\'')

@bot.message_handler(commands=['ih_apasi'])
def send_welcome(message):
 bot.reply_to(message,'Pleaseeee... pleaseeee forgive meeeeee.... There is one thing I want more right now that to make this right. Please forgive mee :(:(?? \'/yaudah_iya\'')

@bot.message_handler(commands=['yaudah_iya'])
def send_welcome(message):
 bot.reply_to(message,'Thanks yaaaa <3 I really miss you. Ayoo kita mulai lagi dari awal! Chat aku di personal chat kalo kamu udah maafin aku heheheheheh okay?')

print('bot start running')
bot.polling()