from vkbottle import GroupEventType, GroupTypes, Keyboard, Text, VKAPIError
from vkbottle.bot import Bot, Message

class Keyboard_:

    def __init__(self):
        pass

    def get_json(self):
        pass

KEYBOARD_START = (
    Keyboard(one_time=False, inline=False)
        .add(Text("Заказать", {"cmd": "create_task"}))
        .add(Text("Поддержка", {"cmd": "help"}))
        .add(Text("Мои заказы", {"cmd": "my_tasks"}))
).get_json()

KEYBOARD_TASK = (
    Keyboard(one_time=False, inline=False)
        .add(Text("Матан", {"cmd": "create_task"}))
        .add(Text("Экономика", {"cmd": "help"}))
        .add(Text("Мои заказы", {"cmd": "my_tasks"}))
).get_json()
KEYBOARD_FILES = (
    Keyboard(one_time=False, inline=False)
        .add(Text("Матан", {"cmd": "create_task"}))
        .add(Text("Экономика", {"cmd": "help"}))
        .add(Text("Мои заказы", {"cmd": "my_tasks"}))
).get_json()

KEYBOARD_TASK = (
    Keyboard(one_time=False, inline=False)
        .add(Text("Матан", {"cmd": "create_task"}))
        .add(Text("Экономика", {"cmd": "help"}))
        .add(Text("Мои заказы", {"cmd": "my_tasks"}))
).get_json()

KEYBOARD_TASK = (
    Keyboard(one_time=False, inline=False)
        .add(Text("Матан", {"cmd": "create_task"}))
        .add(Text("Экономика", {"cmd": "help"}))
        .add(Text("Мои заказы", {"cmd": "my_tasks"}))
).get_json()



subject = ['Мат. Анализ', "Экономика"]