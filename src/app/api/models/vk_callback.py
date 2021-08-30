from typing import Optional

from pydantic.main import BaseModel


class VkGroupAction(BaseModel):
    type: str
    object: Optional[dict]
    group_id: int
