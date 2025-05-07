from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
from datetime import datetime

class AnimalResponseSchema(BaseModel):
    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )

    processed_image: UUID = Field(
        ...,
        description="The unique code assigned to the animal image.",
    )

    model_config = ConfigDict(from_attributes=True)


class AnimalDetailSchema(BaseModel):
    id: int = Field(
        ...,
        description="The unique photo number",
        examples=[1],
    )

    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )

    processed_image: UUID = Field(
        ...,
        description="The unique code assigned to the animal image.",
    )

    created_at: datetime = Field(
        ...,
        description="The time when the photo was added."
    )

    model_config = ConfigDict(from_attributes=True)
