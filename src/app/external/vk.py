from typing import Optional
from datetime import datetime

import aiohttp
import logging
from yarl import URL


class VkApi:
    """Класс для работы с api vk."""

    def __init__(self, url: str, token: str, api_version: str):
        self._url = URL(url)
        self._api_token = token
        self._api_version = api_version
        self._session = aiohttp.ClientSession()

    async def send_message(self, user_id: str, message_text: str) -> Optional[str]:
        send_message_url = self._url / 'messages.send'
        payloads = {
            'peer_id': user_id,
            'random_id': datetime.now().microsecond,
            'message': message_text,
            'access_token': self._api_token,
            'v': self._api_version,
        }
        try:
            response = await self._session.get(send_message_url, params=payloads)
        except Exception as e:
            logging.warning(e)
        else:
            json_response = await response.json()
            print(json_response)
            error_message = json_response.get('error')
            if not error_message:
                return json_response.get('message_id')
            logging.warning(error_message)
