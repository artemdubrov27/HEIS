from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import create_tables, init_db_from_csv
from .routes import router

# === Lifespan: виконується при старті та завершенні програми ===
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()        # створює таблиці, якщо їх немає
    init_db_from_csv()     # заповнює базу з CSV, якщо вона порожня
    yield                  # тут можна додати код для завершення (shutdown)

# === Ініціалізація FastAPI з lifespan ===
app = FastAPI(lifespan=lifespan)

# === Підключення роутів ===
app.include_router(router)
