import html
import random
import EmikoRobot.modules.ramalan_string as ramalan_string
from EmikoRobot import dispatcher
from telegram import ParseMode, Update, Bot
from EmikoRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


def ramalan(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(ramalan_string.RAMALAN))


def ramal(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(ramalan_string.RAMAL))


RAMALAN_HANDLER = DisableAbleCommandHandler("ramalan", ramalan, run_async=True)
RAMAL_HANDLER = DisableAbleCommandHandler("ramal", ramal, run_async=True)

dispatcher.add_handler(RAMALAN_HANDLER)
dispatcher.add_handler(RAMAL_HANDLER)
