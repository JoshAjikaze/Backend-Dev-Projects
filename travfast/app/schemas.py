from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

# Enum creation


class IssueStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"


class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


# Schema Creation
class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    priority: IssuePriority = IssuePriority.medium


class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=100)
    priority: Optional[IssuePriority] = None
    status: Optional[IssueStatus] = None


class IssueOut(BaseModel):
    id: str
    title: str
    description: str
    priority: IssuePriority
    status: IssueStatus


class UserType(str, Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    email: str = Field(min_length=3, max_length=100)
    password: str = Field(min_length=3, max_length=50)
    username: str = Field(min_length=1, max_length=20)
    user_type: UserType = UserType.user


class UserAuth(BaseModel):
    username: Optional[str] = Field(default=None, max_length=20)
    email: Optional[str] = Field(default=None, max_length=100)
    password: Optional[str] = Field(default=None, max_length=50)