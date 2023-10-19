from aiogram import Bot
from aiogram.types import Message

from bot.repositories.user_repository import UserRepository
from bot.services.user_services import UserService
from constants import WELCOME_MESSAGE, HELP_MESSAGE

from bot.utils.commands import set_commands


class WelcomeScenario:

    @staticmethod
    async def start_bot(bot: Bot):
        await set_commands(bot=bot)

    @staticmethod
    async def send_welcome(message: Message):

        user, was_in_db = UserService().start_actions(
            user_id=message.chat.id,
            username=message.chat.username,
            name=message.chat.first_name,
            surname=message.chat.last_name
        )
        await message.answer(WELCOME_MESSAGE)

    @staticmethod
    async def send_help(message: Message):
        await message.answer(HELP_MESSAGE)