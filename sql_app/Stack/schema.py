from pydantic import BaseModel

class StackCreate(BaseModel):
    stack_name : str
    description : str
    img : str
    type : str

class StackSelect(BaseModel):
    stack_id : int
    stack_name : str
    description: str
    img: str
    type: str