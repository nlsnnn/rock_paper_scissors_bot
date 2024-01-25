from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

router = Router()


@router.message()
async def other_msg(message: Message):
    await message.answer(text=LEXICON_RU['other'])