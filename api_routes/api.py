from fastapi import APIRouter
from .expense import expense_router


router = APIRouter()


router.include_router(expense_router, prefix = "/expenses", tags=["TODOS"], )
