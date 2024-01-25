from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU

# Init keyboard
_start_kb = ReplyKeyboardBuilder()

_start_button = KeyboardButton(text=LEXICON_RU['start_game_btn'])
_help_button = KeyboardButton(text=LEXICON_RU["rules_btn"])

_start_kb.row(_start_button, _help_button)
keyboard = _start_kb.as_markup(resize_keyboard=True, one_time_keyboard=True)

# Game keyboard
game_kb = ReplyKeyboardBuilder()

rock_btn = KeyboardButton(text=LEXICON_RU["rock"])
paper_btn = KeyboardButton(text=LEXICON_RU["paper"])
scissors_btn = KeyboardButton(text=LEXICON_RU["scissors"])

game_kb.row(rock_btn, paper_btn, scissors_btn, width=3)
game_keyboard = game_kb.as_markup(resize_keyboard=True)