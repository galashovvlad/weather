import telebot
import pyowm

owm = pyowm.OWM('6137b99a0989ef3be9e73ef6f8af184e', language = "ru")




bot = telebot.TeleBot("871015912:AAF_0MczX7VPsC-ugyyKJKs5H7rnymE9CuY")
@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	answer = "В городе сейчас" + temp
	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )
