from pydantic import (
    BaseModel
)

from typing import Optional

class SocialMediaPromptModel(BaseModel):
    product_description: str

class SocialMediaCaptionResponse(BaseModel):
    response: str

class SocialMediaImageResponse(BaseModel):
    images: Optional[list[str]] = None
