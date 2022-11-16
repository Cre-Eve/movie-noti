import telegram

# how to use bot

bot = telegram.Bot(token = ' ')

for i in bot.getUpdates():
    print(i.message)

bot.send_animation(chat_id = 3213123, text = "테스트입니다.")