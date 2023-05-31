from pydantic import (
    BaseModel
)

from typing import Optional

class InstagramPostModel(BaseModel):
    caption: str
    image_url: str
    username: str
    password: str
