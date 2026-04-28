from pydantic import BaseModel

class TodoSchema(BaseModel):
    title: str
    is_done: bool = False

    class Config:
        from_attributes = True