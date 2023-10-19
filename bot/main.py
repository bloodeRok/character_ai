import asyncio

from aiogram import Dispatcher
from aiogram.filters import Command

from bot.scenarios import WelcomeScenario
from bot.utils.bot_init import bot


async def start():
    dp = Dispatcher()
    dp.startup.register(WelcomeScenario.start_bot)

    # Welcome scenario
    dp.message.register(
        WelcomeScenario.send_welcome,
        Command("start")
    ),
    dp.message.register(
        WelcomeScenario.send_help,
        Command("help")
    )

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
