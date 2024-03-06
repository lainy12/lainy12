import telebot
import openai
from config import OpenAiKey
from config import TgKey

openai.api_key = OpenAiKey
bot = telebot.TeleBot(TgKey)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, какой у тебя вопрос?')

@bot.message_handler(content_types=['text'])
def talk(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=5000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.5
    )
    gpt_text = response['choices'][0]['text']
    bot.send_message(message.chat.id, gpt_text)


bot.polling(none_stop=True)