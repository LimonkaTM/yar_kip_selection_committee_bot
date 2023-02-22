from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from lexicon.lexicon import LEXICON_BUTTONS, LEXICON_COMANDS, LEXICON_DATA

router: Router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON_COMANDS[message.text])
