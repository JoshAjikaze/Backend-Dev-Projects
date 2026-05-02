import base64
from datetime import datetime, timedelta, timezone
import hashlib
from passlib.context import CryptContext
from jose import JWTError, jwt
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def _prepare_password(plain: str) -> str:
    """SHA-256 stretch before bcrypt to bypass the 72-byte limit."""
    digest = hashlib.sha256(plain.encode()).digest()
    return base64.b64encode(digest).decode()

def hash_password(plain: str) -> str:
    return pwd_context.hash(_prepare_password(plain))

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(_prepare_password(plain), hashed)

def create_access_token(data: dict) -> str:
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expire})
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_token(token: str) -> dict:
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])