from enum import StrEnum, auto
from typing import Any

from pydantic import BaseModel, Field


class MessageModel(BaseModel):
    role: str = Field(..., description="角色")
    avatar: str | None = Field(..., description="頭貼")
    content: Any = Field(..., description="內容")


class Role(StrEnum):
    system = auto()
    human = auto()
    ai = auto()


class Avatar(StrEnum):
    system = "⚙️"
    human = "😊"
    ai = "🤖"
