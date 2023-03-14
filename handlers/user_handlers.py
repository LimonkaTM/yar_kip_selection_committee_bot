from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile
from aiogram.methods import DeleteMessage, SendPhoto

from lexicon.lexicon import LEXICON_BUTTONS, LEXICON_COMMANDS, LEXICON_DATA
from keyboards.inline import create_inline_menu

router: Router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    try:
        photo = FSInputFile('logo_two_fix2.png')
        await SendPhoto(chat_id=message.chat.id,
                        photo=photo,
                        caption=LEXICON_DATA['1'],
                        reply_markup=create_inline_menu(
                                'start-admission',
                                'start-translate',
                                'faq'))
    except BaseException:
        await message.answer(LEXICON_DATA['1'],
                             reply_markup=create_inline_menu(
                                'start-admission',
                                'start-translate',
                                'faq'),
                             disable_web_page_preview=True)
    await DeleteMessage(chat_id=message.chat.id, message_id=message.message_id)


# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands='help'))
async def process_restart_command(message: Message):
    await DeleteMessage(chat_id=message.chat.id,
                        message_id=message.message_id-1)
    await message.answer(LEXICON_DATA['help'],
                         reply_markup=create_inline_menu(
                            'back'),
                         disable_web_page_preview=True)
    await DeleteMessage(chat_id=message.chat.id, message_id=message.message_id)


# @router.callback_query(Text(text='forward'))
# async def process_forward_press(callback: CallbackQuery):
#     if users_db[callback.from_user.id]['page'] < len(book):
#         users_db[callback.from_user.id]['page'] += 1
#         text = book[users_db[callback.from_user.id]['page']]
#         await callback.message.edit_text(
#             text=text,
#             reply_markup=create_pagination_keyboard(
#                     'backward',
#                     f'{users_db[callback.from_user.id]["page"]}/{len(book)}',
#                     'forward'))
#     await callback.answer()