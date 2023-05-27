from pydantic import (
    BaseModel,
)


class QueryModel(BaseModel):
    prompt: str

class QueryResponseModel(BaseModel):
    response: str