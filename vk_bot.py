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
        # if not isinstance(payload_key, str):
        #     raise ValueError
        self.payload_key = payload_key

    async def check(self, message: Message) -> Union[dict, bool]:
        return self.payload_key in message.payload
subjects = {
    '1': "Матан",
    '2': "История экономики",
    '3': "Физика",
    '4': "Теория Игр",
    '5': "Макроэкономика",
}
tasks = []


bot = Bot("4c2ab9052cf12589768f89de82443c201308c139e47e82476eae707748feea17079f5d01b2f4611397af7")

@bot.on.message(text='Начать')
async def on_start(message: Message) -> str:
    await message.answer('Привет', keyboard=KEYBOARD_START)

# @bot.on.private_message()
# async def on_start(message: Message) -> str:
#     await message.answer('xuy')
# @bot.on.message(text='Заказать')
# async def on_create_task(message: Message) -> str:
#     await message.answer('Введи номер предмета из списка (например: 1) или введи свой предмет (например: автоматизация процессов), если его нет в списке:', keyboard=KEYBOARD_TASK)

@bot.on.message(MyRule('create_task'))
async def create_task(message: Message) -> str:
    if tasks:
        await message.answer('У вас уже есть активный заказ, что хотите сделать?', keyboard=KEYBOARD_TASK_NEW)
    else:
        await create_task_new(message)

@bot.on.message(MyRule('create_task_new'))
async def create_task_new(message: Message) -> str:
    await message.answer('Выберите предмет по которому нужна помощь:', keyboard=keyboard_create(subjects))


@bot.on.message(MyRule('help'))
async def help(message: Message) -> str:
    await message.answer('Если у вас какие-то вопросы по работе с ботом, напишите ему @dsoldatow')

@bot.on.message(MyRule('my_tasks'))
async def my_tasks(message: Message) -> str:
    await message.answer(f'Список заданий {list}', keyboard=KEYBOARD_BACK)


@bot.on.message(MyRule('back'))
async def back(message: Message) -> str:
    await message.answer('Привет', keyboard=KEYBOARD_BACK)


bot.run_forever()