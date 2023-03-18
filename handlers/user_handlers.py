from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.methods import DeleteMessage, SendPhoto

from lexicon.lexicon import LEXICON_BUTTONS, LEXICON_COMMANDS, LEXICON_DATA
from keyboards.inline import create_inline_menu

router: Router = Router()


current_message = {}
prev_kb = {}

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
                                'paid-services',
                                # 'certificates-rating',
                                'faq'))
    except BaseException:
        await message.answer(LEXICON_DATA['1'],
                             reply_markup=create_inline_menu(
                                'start-admission',
                                'start-translate',
                                'paid-services',
                                # 'certificates-rating',
                                'faq'),
                             disable_web_page_preview=True)
    await DeleteMessage(chat_id=message.chat.id, message_id=message.message_id)


# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands='help'))
async def process_restart_command(message: Message):
    current_message[message.chat.id] = 'help'
    prev_kb[message.chat.id] = create_inline_menu(
                                'start-admission',
                                'start-translate',
                                'paid-services',
                                # 'certificates-rating',
                                'faq')
    await DeleteMessage(chat_id=message.chat.id,
                        message_id=message.message_id-1)
    await message.answer(LEXICON_DATA['help'],
                         reply_markup=create_inline_menu('back'),
                         disable_web_page_preview=True)
    await DeleteMessage(chat_id=message.chat.id, message_id=message.message_id)





# 1.1
@router.callback_query(Text(text='start-admission'))
async def process_start_admission(callback: CallbackQuery):
    current_message[callback.message.chat.id] = '1'
    prev_kb[callback.message.chat.id] = create_inline_menu(
                                'start-admission',
                                'start-translate',
                                'paid-services',
                                # 'certificates-rating',
                                'faq')
    print('Номер месседжа', current_message[callback.message.chat.id])
    # await DeleteMessage(chat_id=callback.message.chat.id,
    #                     message_id=callback.message.message_id-1)
    await callback.message.answer(text=LEXICON_DATA['1.1'],
                                  reply_markup=create_inline_menu(
                                      'destinations-list',
                                      'admission-rulle',
                                      'admission-dates',
                                      'document-submission',
                                      'special-rights',
                                      'back'),
                                  disable_web_page_preview=True)
    await DeleteMessage(chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id)
    # await callback.answer()

# 1.2
@router.callback_query(Text(text='start-translate'))
async def process_start_translate(callback: CallbackQuery):
    current_message[callback.message.chat.id] = '1'
    # await DeleteMessage(chat_id=callback.message.chat.id,
    #                     message_id=callback.message.message_id-1)
    await callback.message.answer(text=LEXICON_DATA['1.2'],
                                  reply_markup=create_inline_menu(
                                      'back'),
                                  disable_web_page_preview=True)
    await DeleteMessage(chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id)
    # await callback.answer()

# 1.3
@router.callback_query(Text(text='paid-services'))
async def process_paid_services(callback: CallbackQuery):
    current_message[callback.message.chat.id] = '1'
    # await DeleteMessage(chat_id=callback.message.chat.id,
    #                     message_id=callback.message.message_id-1)
    await callback.message.answer(text=LEXICON_DATA['1.3'],
                                  reply_markup=create_inline_menu(
                                      'back'),
                                  disable_web_page_preview=True)
    await DeleteMessage(chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id)
    # await callback.answer()

# 1.4
@router.callback_query(Text(text='faq'))
async def process_faq(callback: CallbackQuery):
    current_message[callback.message.chat.id] = '1'
    # await DeleteMessage(chat_id=callback.message.chat.id,
    #                     message_id=callback.message.message_id-1)
    await callback.message.answer(text=LEXICON_DATA['1.4'],
                                  reply_markup=create_inline_menu(
                                      'back'),
                                  disable_web_page_preview=True)
    await DeleteMessage(chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id)
    # await callback.answer()

# 1.1.1
@router.callback_query(Text(text='destinations-list'))
async def process_admission_rulle(callback: CallbackQuery):
    current_message[callback.message.chat.id] = '1.1'
    prev_kb[callback.message.chat.id] = create_inline_menu(
                                    'destinations-list',
                                    'admission-rulle',
                                    'admission-dates',
                                    'document-submission',
                                    'special-rights',
                                    'back')
    await callback.message.answer(text=LEXICON_DATA['1.1.1'],
                                  reply_markup=create_inline_menu(
                                      'back'),
                                  disable_web_page_preview=True)
    await DeleteMessage(chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id)
    # await callback.answer()



# callback back
@router.callback_query(Text(text='back'))
async def process_back(callback: CallbackQuery):
    # await DeleteMessage(chat_id=callback.message.chat.id,
    #                     message_id=callback.message.message_id-1)
    for mes in LEXICON_DATA:
        if current_message[callback.message.chat.id] == '1':
            photo = FSInputFile('logo_two_fix2.png')
            await SendPhoto(chat_id=callback.message.chat.id,
                            photo=photo,
                            caption=LEXICON_DATA['1'],
                            reply_markup=create_inline_menu(
                                'start-admission',
                                'start-translate',
                                'paid-services',
                                # 'certificates-rating',
                                'faq'))
            break
        elif mes == current_message[callback.message.chat.id]:
            await callback.message.answer(text=LEXICON_DATA[current_message[callback.message.chat.id]],
                                          reply_markup=prev_kb[callback.message.chat.id],
                                          disable_web_page_preview=True)
            break
    await DeleteMessage(chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id)
    # await callback.answer()
