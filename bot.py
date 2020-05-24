import pyowm
import telebot

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")
bot = telebot.TeleBot("1230024109:AAHoslqnQcmS1B9EuHM4k4SG7bV0KZ1B13w")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе" + message.text + "сейчас" + w.get_detailed_status() + "/n"
	answer += "Температура около" + str(temp) + "/n/n"
	if temp < 10:
   		answer += "В такую погоду нужно одеться потеплее"
	elif temp < 20:
		answer += "В такую погоду можно не утепляться"
	else: answer += "Погода отменная. Одевайся как хочешь"
		
	bot.send_message(message.chat.id, answer)

bot.polling ( none_stop = True ) 