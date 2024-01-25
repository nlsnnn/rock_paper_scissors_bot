import random
from lexicon.lexicon import LEXICON_RU


def get_bot_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def _normalize_user_answer(user_answer):
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key


def get_winner(bot_choice, user):
    user_choice = _normalize_user_answer(user)
    rules = {'rock': 'scissors',
             'scissors': 'paper',
             'paper': 'rock'}

    if user_choice == bot_choice:
        return 'nobody_won'
    if rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'