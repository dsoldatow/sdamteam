from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse

from app.action_handlers.vk import VkActionHandler
from app.api.models.vk_callback import VkGroupAction
from app.external.vk import VkApi


router = APIRouter()
# --- быдло код, зарефачить
vk_api = VkApi(
    'https://api.vk.com/method',
    '4c2ab9052cf12589768f89de82443c201308c139e47e82476eae707748feea17079f5d01b2f4611397af7',
    '5.103',
)
vk_handler = VkActionHandler(
    vk_api,
    '00c531ef',
)


@router.post('/vk_callback', response_class=PlainTextResponse)
async def handle_vk_action(action: VkGroupAction, request: Request):
    request.app
    return await vk_handler.handle_event(action)
