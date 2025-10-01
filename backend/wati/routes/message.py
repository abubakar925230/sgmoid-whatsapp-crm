

from fastapi import APIRouter, Query
from backend.wati.services.message_generator import generate_message

router = APIRouter()

@router.get("/generate-message/")
async def get_generated_message(prompt: str = Query(..., description="The message prompt")):
    message = generate_message(prompt)
    return {"generated_message": message}
