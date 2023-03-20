from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.methods import DeleteMessage, SendPhoto

from services.Message import get_message, get_start_message, get_help_message
from keyboards.inline import create_msg_menu


router: Router = Router()


# /start command handler
@router.message(CommandStart())
async def process_start_cmd(message: Message) -> None:
    msg = get_start_message()
    if msg:
        if msg.photo:
            photo = FSInputFile(msg.photo)
            await SendPhoto(chat_id=message.chat.id,
                            photo=photo,
                            caption=msg.content,
                            reply_markup=create_msg_menu(msg.id))
        else:
            await message.answer(text=msg.content,
                                 reply_markup=create_msg_menu(msg.id),
                                 disable_web_page_preview=True)
        await DeleteMessage(chat_id=message.chat.id,
                            message_id=message.message_id)


# /help command handler
@router.message(Command(commands='help'))
async def process_help_cmd(message: Message) -> None:
    msg = get_help_message()
    if msg:
        await DeleteMessage(chat_id=message.chat.id,
                            message_id=message.message_id)
        await message.answer(msg.content,
                             reply_markup=create_msg_menu(msg.id),
                             disable_web_page_preview=True)
    await DeleteMessage(chat_id=message.chat.id,
                        message_id=message.message_id-1)


# /home command handler
@router.message(Command(commands='home'))
async def process_home_cmd(message: Message) -> None:
    msg = get_start_message()
    if msg:
        await DeleteMessage(chat_id=message.chat.id,
                            message_id=message.message_id)
        if msg.photo:
            photo = FSInputFile(msg.photo)
            await SendPhoto(chat_id=message.chat.id,
                            photo=photo,
                            caption=msg.content,
                            reply_markup=create_msg_menu(msg.id))
        else:
            await message.answer(text=msg.content,
                                 reply_markup=create_msg_menu(msg.id),
                                 disable_web_page_preview=True)
        await DeleteMessage(chat_id=message.chat.id,
                            message_id=message.message_id-1)


# open_msg callback handler
@router.callback_query(Text(startswith='open_msg:'))
async def open_msg(callback: CallbackQuery) -> None:
    id_msg = callback.data.removeprefix('open_msg:')
    msg = get_message(id_msg)

    if msg:
        await DeleteMessage(chat_id=callback.message.chat.id,
                            message_id=callback.message.message_id)
        if msg.photo:
            photo = FSInputFile(msg.photo)
            await SendPhoto(chat_id=callback.message.chat.id,
                            photo=photo,
                            caption=msg.content,
                            reply_markup=create_msg_menu(id_msg))
        else:
            await callback.message.answer(text=msg.content,
                                          reply_markup=create_msg_menu(id_msg),
                                          disable_web_page_preview=True)
    else:
        await callback.answer(text='Что-то пошло не так!\nПопробуйте перезагрузить бота',
                              show_alert=True)
