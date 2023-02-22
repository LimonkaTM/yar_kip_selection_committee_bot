from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, Chat
from aiogram.methods.delete_message import DeleteMessage

from lexicon.lexicon import LEXICON_BUTTONS, LEXICON_COMMANDS, LEXICON_DATA
from keyboards.inline import create_inline_menu

router: Router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON_DATA['start'],
                         reply_markup=create_inline_menu(
                            'start-admission',
                            'start-translate',
                            'faq'))


# Этот хэндлер будет срабатывать на команду "/restart"
# @router.message(Command(commands='restart'))
# async def process_restart_command(message: Message):
#     await DeleteMessage(chat_id=message.chat.id, message_id=message.message_id)
#     # await message.answer(LEXICON_DATA['start'],
#     #                      reply_markup=create_inline_menu(
#     #                         'start-admission',
#     #                         'start-translate',
#     #                         'faq'))