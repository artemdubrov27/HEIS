from fastapi import FastAPI
from contextlib import asynccontextmanager

from .database import create_tables, init_db_from_csv
from .routes import router
from . import models   

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    init_db_from_csv()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)
