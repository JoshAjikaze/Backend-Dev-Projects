from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middlewares.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
app.middleware("http")(timing_middleware)
app.include_router(issues_router)
