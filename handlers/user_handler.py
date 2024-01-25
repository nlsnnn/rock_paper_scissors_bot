from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
#
from lexicon.lexicon import LEXICON_RU
from keyboards import keyboard
from services.services import get_bot_choice, get_winner

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAEDElFlsiicm-pCEIsMP-AJ41xwvb1hjwAC4BwAAnbQcUvyswPrqKIEgzQE')
    await message.answer(LEXICON_RU['/start'],
                         reply_markup=keyboard.keyboard)


@router.message(F.text == LEXICON_RU["rules_btn"])
async def rules_cmd(message: Message):
    await message.answer(LEXICON_RU['/help'],
                         reply_markup=keyboard.keyboard)


@router.message(F.text == LEXICON_RU["start_game_btn"])
async def start_game(message: Message):
    await message.answer(text=LEXICON_RU["start_game"],
                         reply_markup=keyboard.game_keyboard)


@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['scissors']]))
async def game(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(f'{LEXICON_RU["bot_choice"]} '
                         f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(bot_choice, message.text)
    await message.answer(LEXICON_RU[winner], reply_markup=keyboard.keyboard)
    await message.answer_sticker(r"CAACAgIAAxkBAAEDElNlsijLGL-0RqZb3zBMq09891XtrwAClyAAAt88OUtsjjyKWQ5bXjQE")