from telegram.ext import Updater, CommandHandler

def welcome(update, context):
    message = "Olá, " + update.message.from_user.first_name + "!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    #https://medium.com/como-programar-em-1-dia/como-fazer-um-chatbot-em-1-dia-bcb07c48ec5e
    token = '1142244274:AAErdE14-eKg0P6h3cMgfITnIvCNk7p50dw'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    updater.start_polling()
    print('Oi, eu sou o updater'+str(updater))
    updater.idle()

if __name__ == '__main__' : 
    main()