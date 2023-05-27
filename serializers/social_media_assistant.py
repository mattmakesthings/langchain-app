from pydantic import (
    BaseModel
)

from typing import Optional

class SocialMediaAssistantModel(BaseModel):
    product_description: str

class SocialMediaAssistantResponse(BaseModel):
    response: str
    images: Optional[list[str]] = None