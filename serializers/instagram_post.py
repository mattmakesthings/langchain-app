from pydantic import (
    BaseModel,
    validator,
    root_validator,
)

from typing import Optional, List

class InstagramPostModel(BaseModel):
    caption: str
    image_urls: List[str]
    username: str
    password: str
    verification_code: Optional[str]
