from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import repositories.food_repository as food_repository


async def get_food_list(db: Session):
    food = db.query(food_repository.Food).all()
    return food


async def create_food(request, db: Session):
    food = food_repository.Food(
        food_name=request.food_name,
        food_type=request.food_type,
        food_price=request.food_price,
        food_description=request.food_description,
        food_image_url=request.food_image_url
    )
    db.add(food_repository.Food)
    db.commit()
    db.refresh(food)
    return food
