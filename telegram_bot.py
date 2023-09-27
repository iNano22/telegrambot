from typing import Final
from telegram import Update, Bot, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN: Final = '6661733237:AAFsw7Fe8nsCnfbV_sAeXlbWAuSYZGZax9o'
BOT_USERNAME: Final = '@inano_bot'


def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am Nano's Bot!")


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Help! I am Nano's Bot!")


def custom_command(update: Update, context: CallbackContext):
    update.message.reply_text("Custom I am Nano's Bot!")


# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    if 'how are you' in processed:
        return 'I am good!'
    if 'i love python' in processed:
        return 'Remember to subscribe!'

    return 'I do not understand what you wrote...'


def handle_message(update: Update, context: CallbackContext):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    update.message.reply_text(response)


def error(update: Update, context: CallbackContext):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')

    bot = Bot(token=TOKEN)
    updater = Updater(bot=bot, use_context=True)

    # Commands
    updater.dispatcher.add_handler(CommandHandler('start', start_command))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('custom', custom_command))

    # Messages
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Errors
    updater.dispatcher.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    updater.start_polling()
