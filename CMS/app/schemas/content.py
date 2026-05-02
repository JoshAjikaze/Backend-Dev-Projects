from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class ContentStatus(str, Enum):
    draft = "draft"
    published = "published"
    archived = "archived"

class ContentCreate(BaseModel):
    title: str
    body: str
    status: ContentStatus = ContentStatus.draft
    slug: str

class ContentUpdate(BaseModel):
    title: str | None = None
    body: str | None = None
    status: ContentStatus | None = None

class ContentOut(BaseModel):
    id: int
    title: str
    body: str
    slug: str
    status: ContentStatus
    author_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}