import telebot

# Замініть 'YOUR_TOKEN' на ваш реальний токен
bot = telebot.TeleBot('7728543578:AAEU4tyMq1KYyCqV7vkQ2kqJMfWHs3GYA28')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()