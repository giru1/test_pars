import uuid
from datetime import datetime

from pydantic import BaseModel


class RmkSchemas(BaseModel):
    id: uuid.UUID
    status: str
    queue: str
    message: str
    send_time: datetime

    class Config:
        from_attributes = True
