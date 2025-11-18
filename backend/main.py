from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.core.db import create_db_and_tables
from src.api.cafe.routes import router as cafe_router
from src.api.item.routes import router as item_router
# from .src.core.db import 


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# include routes
app.include_router(cafe_router)
app.include_router(item_router)