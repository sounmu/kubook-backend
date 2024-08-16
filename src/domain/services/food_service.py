from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from domain.schemas.food_schemas import Food, FoodCreation
from repositories import food_repository
from routes.request.create_food_request import CreateFoodRequest


async def get_food_list(db: Session) -> list[Food]:
    foods = db.query(food_repository.Food).all()
    print(foods)
    print(foods)
    print(foods)
    return [Food.from_orm(food) for food in foods]


async def create_food(request: CreateFoodRequest, db: Session) -> Food:
    food_creation = FoodCreation.from_request(request)
    food = food_repository.Food(
        food_name=food_creation.food_name,
        food_type=food_creation.food_type,
        food_price=food_creation.food_price,
        food_description=food_creation.food_description,
        food_image_url=food_creation.food_image_url
    )
    db.add(food)
    db.commit()
    db.refresh(food)
    return Food.from_orm(food)
