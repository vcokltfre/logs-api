from pydantic import BaseModel
from typing import Optional

class NewData(BaseModel):
    text: str
    name: Optional[str]
    timeout: Optional[int]