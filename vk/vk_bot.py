from vkbottle.bot import Bot


import logging
import os
import random
from typing import Optional

from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError
from vkbottle.bot import Bot, Message
from vkbottle.bot import rules
from typing import Union

from keyboards import *
class MyRule(rules.ABCMessageRule):
    def __init__(self, payload_key: str):
        if not isinstance(payload_key, str):
            raise ValueError
        self.payload_key = payload_key

    async def check(self, message: Message) -> Union[dict, bool]:
        return self.payload_key in message.payload


bot = Bot("4c2ab9052cf12589768f89de82443c201308c139e47e82476eae707748feea17079f5d01b2f4611397af7")

@bot.on.message(text='Начать')
async def on_start(message: Message) -> str:
    await message.answer('Привет', keyboard=KEYBOARD_START)

# @bot.on.message(text='Заказать')
# async def on_create_task(message: Message) -> str:
#     await message.answer('Введи номер предмета из списка (например: 1) или введи свой предмет (например: автоматизация процессов), если его нет в списке:', keyboard=KEYBOARD_TASK)

@bot.on.message(MyRule('create_task'))
async def on_start(message: Message) -> str:
    await message.answer('xuy', keyboard=KEYBOARD_START)



bot.run_forever()