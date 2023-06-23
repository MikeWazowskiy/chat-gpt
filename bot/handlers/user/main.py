from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ContentType, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

import openai


def register_user_handlers(dp: Dispatcher):

    @dp.message_handler(commands='start')
    async def start(message: Message):
        await message.answer('Hello there!')

    @dp.message_handler()
    async def message_from_user(message: Message):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.9,
            max_tokens=1090,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["You:"]
        )

        await message.answer(response['choices'][0]['text'])

