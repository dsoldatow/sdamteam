from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError
from vkbottle.bot import Bot, Message


class Keyboard_:

    def __init__(self):
        pass

    def get_json(self):
        pass

#
# def keyboard_create_choose(items: list, value: str):
#     keyboard = Keyboard(one_time=False, inline=False)
#     for value in items:
#         keyboard.add(Text(text, {"cmd": value}))
#
#     return keyboard.get_json()


KEYBOARD_START = (
    Keyboard(one_time=False, inline=False)
        .add(Text("Заказать", {"cmd": "create_task"}))
        .add(Text("Поддержка", {"cmd": "help"}))
        .add(Text("Мои заказы", {"cmd": "my_tasks"}))
).get_json()

KEYBOARD_HELP = (
    Keyboard(one_time=False, inline=False)
        .add(Text("Заказать", {"cmd": "create_task"}))
        .add(Text("Поддержка", {"cmd": "help"}))
        .add(Text("Мои заказы", {"cmd": "my_tasks"}))
).get_json()

KEYBOARD_BACK = (
    Keyboard(one_time=False, inline=False)
        .add(Text("Вернуться", {"cmd": "back"}))
).get_json()

KEYBOARD_TASK_NEW = (
    Keyboard(one_time=False, inline=False)
        .add(Text("Сделать новый заказ", {"cmd": "create_task_new"}))
        .add(Text("Мои заказы", {"cmd": "my_tasks"}))
).get_json()

KEYBOARD_FILES = (
    Keyboard(one_time=False, inline=False)
        .add(Text("Матан", {"cmd": "create_task"}))
        .add(Text("Экономика", {"cmd": "help"}))
        .add(Text("Мои заказы", {"cmd": "my_tasks"}))
).get_json()

# KEYBOARD_TASK = (
#     Keyboard(one_time=False, inline=False)
#         .add(Text("Матан", {"cmd": "create_task"}))
#         .add(Text("Экономика", {"cmd": "help"}))
#         .add(Text("Мои заказы", {"cmd": "my_tasks"}))
# ).get_json()

KEYBOARD_TASK = (
    Keyboard(one_time=False, inline=False)
        .add(Text("Матан", {"cmd": "create_task"}))
        .add(Text("Экономика", {"cmd": "help"}))
        .add(Text("Мои заказы", {"cmd": "my_tasks"}))
).get_json()

subject = ['Мат. Анализ', "Экономика"]
