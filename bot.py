#https://medium.com/como-programar-em-1-dia/como-fazer-um-chatbot-em-1-dia-bcb07c48ec5e
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

STATE1 = 1
STATE2 = 2

def welcome(update, context):
    message = "Olá, " + update.message.from_user.first_name + "!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def especialidades(update, context):
    message = '''Qual recurso vc gostaria? \n
                1 - Insert \n
                2 - Read'''
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
    return STATE1

def inputEspecialidades(update, context):
    especialidade = (update.message.text)
    print(especialidade)
    if (especialidade==1 or especialidade=='insert' or especialidade=='inserir' or especialidade=='create'):
        message = "xpto = inserir"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    elif (especialidade==2 or especialidade=='read' or especialidade=='consultar'):
        message = "Muito obrigada pelo seu feedback!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2


def inputAssunto(update, context):    
    message = "Muito obrigado em breve novidades!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def cancel(update, context):
    return ConversationHandler.END


def main():
    token = '1142244274:AAErdE14-eKg0P6h3cMgfITnIvCNk7p50dw'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('especialidades', especialidades)],
        states={
            STATE1: [MessageHandler(Filters.text, inputEspecialidades)],
            STATE2: [MessageHandler(Filters.text, inputAssunto)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)

    updater.start_polling()
    print('Oi, eu sou o updater'+str(updater))
    updater.idle()

if __name__ == '__main__' : 
    main()
