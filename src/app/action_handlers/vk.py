import logging

from app.api.models.vk_callback import VkGroupAction
from app.external.vk import VkApi


CONFIRMATION_EVENT_TYPE = 'confirmation'
MESSAGE_EVENT_TYPE = 'message_new'
FLOW = ['введи ВУЗ', 'введи предмет', 'опиши задание и прикрепи файлы, если имеются', 'заказ создан']


class VkActionHandler:
    """Обработчик событий vk."""

    def __init__(self, api: VkApi, confirmation_secret: str):
        self._vk_api = api
        self._confirmation_secret = confirmation_secret
        self._user_states = {}

    async def handle_event(self, event: VkGroupAction) -> str:
        if event.type == CONFIRMATION_EVENT_TYPE:
            return self._confirmation_secret
        if event.type == MESSAGE_EVENT_TYPE:
            return await self._handle_message(event.object)

    async def _handle_message(self, obj: dict) -> str:
        logging.info(f'obj: {obj}')
        message = obj.get('message', {})
        user_id = message.get('from_id')
        message_text = message.get('text', '').lower()
        current_step = (self._user_states.get(user_id, -1) + 1) % len(FLOW)
        if user_id:
            await self._vk_api.send_message(user_id, FLOW[current_step])
            self._user_states[user_id] = current_step
            return 'ok'
        logging.warning('bad message object detected')
