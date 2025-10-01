# backend/wati/database/database.py

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1️⃣ Load the .env file from project root
dotenv_path = Path(__file__).parents[3] / ".env"
load_dotenv(dotenv_path=dotenv_path)

# 2️⃣ Fetch database URL
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("Database URL not found. Check your .env file!")

print("Database URL loaded:", SQLALCHEMY_DATABASE_URL)  # Optional: check loading

# 3️⃣ Create async engine
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    pool_recycle=120,
    pool_pre_ping=True,
    pool_size=30
)

# 4️⃣ Create session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# 5️⃣ Base class for declarative models
Base = declarative_base()

# 6️⃣ Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
