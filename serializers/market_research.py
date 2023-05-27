from pydantic import (
    BaseModel,
)

class MarketResearchModel(BaseModel):
    companies: list[str]
