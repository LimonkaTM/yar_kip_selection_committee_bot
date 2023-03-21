from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.methods import DeleteMessage, SendPhoto
from magic_filter import F

from services.Message import get_message, get_start_message, get_help_message
from keyboards.inline import create_msg_menu


router: Router = Router()

prev_msgs = {}

# /start command handler
@router.message(CommandStart())
async def process_start_cmd(message: Message) -> None:
    msg = await get_start_message()
    if msg:
        if msg.photo:
            photo = FSInputFile(msg.photo)
            mes = await SendPhoto(chat_id=message.chat.id,
                            photo=photo,
                            caption=msg.content,
                            reply_markup=await create_msg_menu(msg.id))
            if message.from_user.id in prev_msgs:
                await DeleteMessage(chat_id=message.chat.id,
                                    message_id=prev_msgs[message.from_user.id])
            prev_msgs[message.from_user.id] = mes.message_id
        else:
            await message.answer(text=msg.content,
                                reply_markup=await create_msg_menu(msg.id),
                                disable_web_page_preview=True)
        await DeleteMessage(chat_id=message.chat.id,
                            message_id=message.message_id)


# /help command handler
@router.message(Command(commands='help'))
async def process_help_cmd(message: Message) -> None:
    msg = await get_help_message()
    if msg:
        mes = await message.answer(msg.content,
                             reply_markup=await create_msg_menu(msg.id),
                             disable_web_page_preview=True)
        if message.from_user.id in prev_msgs:
            await DeleteMessage(chat_id=message.chat.id,
                                message_id=prev_msgs[message.from_user.id])
        prev_msgs[message.from_user.id] = mes.message_id
        await DeleteMessage(chat_id=message.chat.id,
                            message_id=message.message_id)


# /home command handler
@router.message(Command(commands='home'))
async def process_home_cmd(message: Message) -> None:
    msg = await get_start_message()
    if msg:
        if msg.photo:
            photo = FSInputFile(msg.photo)
            mes = await SendPhoto(chat_id=message.chat.id,
                            photo=photo,
                            caption=msg.content,
                            reply_markup=await create_msg_menu(msg.id)) 
            if message.from_user.id in prev_msgs:
                await DeleteMessage(chat_id=message.chat.id,
                                    message_id=prev_msgs[message.from_user.id])
            prev_msgs[message.from_user.id] = mes.message_id
        else:
            mes = await message.answer(text=msg.content,
                                 reply_markup=await create_msg_menu(msg.id),
                                 disable_web_page_preview=True)
        await DeleteMessage(chat_id=message.chat.id,
                            message_id=message.message_id)


# open_msg callback handler
@router.callback_query(Text(startswith='open_msg:'))
async def open_msg(callback: CallbackQuery) -> None:
    id_msg = callback.data.removeprefix('open_msg:')
    msg = await get_message(int(id_msg))
    if msg:
        await DeleteMessage(chat_id=callback.message.chat.id,
                            message_id=callback.message.message_id)
        if msg.photo:
            photo = FSInputFile(msg.photo)
            mes = await SendPhoto(chat_id=callback.message.chat.id,
                            photo=photo,
                            caption=msg.content,
                            reply_markup=await create_msg_menu(id_msg))
            prev_msgs[callback.from_user.id] = mes.message_id
            await callback.answer()
        else:
            mes = await callback.message.answer(text=msg.content,
                                          reply_markup=await create_msg_menu(id_msg),
                                          disable_web_page_preview=True)
            prev_msgs[callback.from_user.id] = mes.message_id
            
    else:
        await callback.answer(text='Что-то пошло не так!\nПопробуйте перезагрузить бота',
                              show_alert=True)
