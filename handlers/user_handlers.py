from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU

router: Router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON_RU['buttons'][message.text])
