from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.methods import DeleteMessage, SendPhoto

#! Temp database

from lexicon.msgs import msgs
from keyboards.inline import create_msg_menu

router: Router = Router()


current_message = {}
prev_kb = {}


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    current_message[message.chat.id] = '1.1'
    await message.answer(msgs['1.1']['content'],
                            reply_markup=create_msg_menu('1.1'),
                            disable_web_page_preview=True)
    await DeleteMessage(chat_id=message.chat.id, message_id=message.message_id)

# open_msg
@router.callback_query(Text(startswith='open_msg:'))
async def open_msg(callback: CallbackQuery):
    id_msg = callback.data.removeprefix('open_msg:')
    msg = msgs[id_msg]
    current_message[callback.message.chat.id] = id_msg

    await DeleteMessage(chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id)
    await callback.message.answer(text=msg['content'],
                                  reply_markup=create_msg_menu(id_msg),
                                  disable_web_page_preview=True)
