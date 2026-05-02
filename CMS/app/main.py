from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, content

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CMS API")
app.include_router(auth.router)
app.include_router(content.router)