from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_current_active_user, get_db
from domain.services import food_service
from routes.request.create_food_request import CreateFoodRequest
from routes.response.food_response import FoodResponse

router = APIRouter(
    prefix="/food",
    tags=["food"]
)


@router.get(
    "/",
    summary="음식 목록 조회",
    response_model=List[FoodResponse],
    response_description="음식 목록을 조회합니다.",
    status_code=200
)
async def list_foods(
        db: Session = Depends(get_db),
        # current_user=Depends(get_current_active_user)
):
    foods = await food_service.get_food_list(db)
    return [food.to_response() for food in foods]


@router.post(
    "/",
    summary="음식 등록",
    response_model=FoodResponse,
    response_description="음식을 등록합니다.",
    status_code=201
)
async def create_food(
        request: CreateFoodRequest,
        db: Session = Depends(get_db),
        # current_user=Depends(get_current_active_user)
):
    food = await food_service.create_food(request, db)
    return food.to_response()
