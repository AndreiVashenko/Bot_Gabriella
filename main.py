import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a Gabriella, please talk to me!")

async def _help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I can talk fun story. click /FunStory")

async def fun_story(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="You wonna amuse God  - tell him about your plan for life :)")


if __name__ == '__main__':
    application = ApplicationBuilder().token('6414293222:AAHaU0kLcmya5GIqyhWZYcdiYCLf3O0c_rg').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    help_handler = CommandHandler('help', _help)
    application.add_handler(help_handler)

    fun_story_handler = CommandHandler('FunStory', fun_story)
    application.add_handler(fun_story_handler)

    application.run_polling()
