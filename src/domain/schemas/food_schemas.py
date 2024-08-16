from datetime import datetime

from pydantic import BaseModel

from repositories.food_repository import Food as FoodModel
from routes.request.create_food_request import CreateFoodRequest
from routes.response.food_response import FoodResponse


class Food(BaseModel):
    id: int | None = None
    food_name: str
    food_type: str
    food_price: int
    food_description: str
    food_image_url: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    @classmethod
    def from_orm(cls, food: FoodModel):
        return cls(
            id=food.id,
            food_name=food.food_name,
            food_type=food.food_type,
            food_price=food.food_price,
            food_description=food.food_description,
            food_image_url=food.food_image_url,
            created_at=food.created_at,
            updated_at=food.updated_at
        )

    def to_response(self) -> FoodResponse:
        return FoodResponse(
            id=self.id,
            food_name=self.food_name,
            food_type=self.food_type,
            food_price=self.food_price,
            food_description=self.food_description,
            food_image_url=self.food_image_url,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class FoodCreation(BaseModel):
    food_name: str
    food_type: str
    food_price: int
    food_description: str
    food_image_url: str

    @classmethod
    def from_request(cls, request: CreateFoodRequest):
        return cls(
            food_name=request.food_name,
            food_type=request.food_type,
            food_price=request.food_price,
            food_description=request.food_description,
            food_image_url=request.food_image_url
        )
