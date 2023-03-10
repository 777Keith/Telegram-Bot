import telebot, wikipedia, re
from telebot import types
bot = telebot.TeleBot('5879052171:AAFL64yx4XSpC_jhogomQ4CtRFzAMC8zmnY')
wikipedia.set_lang('ru')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/wiki")
    markup.add(btn1)
    # bot.send_message(message.chat.id, text="Дарова ".format(message.from_user),reply_markup=markup)
    bot.send_message(message.chat.id, text="Hello, {0.first_name}! click on the wiki button to find the word ".format(message.from_user),reply_markup=markup)

def getwiki(s):
    try:
        ny = wikipedia.page(s)

        wikitext=ny.content[:1000]

        wikimas=wikitext.split('.')

        wikimas = wikimas[:-1]

        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):

                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break


        return wikitext2

    except Exception as e:
        return 'No information found'


@bot.message_handler(commands=["wiki"])
def wiki(m, res=False):
    bot.send_message(m.chat.id, 'Write me any word and I will find its meaning on Wikipedia')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


bot.polling(none_stop=True, interval=0)