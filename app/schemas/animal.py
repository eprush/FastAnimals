from pydantic import BaseModel, Field, ConfigDict, field_validator
from uuid import UUID
from datetime import datetime

class AnimalSchema(BaseModel):
    """ A scheme of animal. """

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
    """ A scheme for showing animal fields. """

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

class AllAnimalsSchema(BaseModel):
    animals: tuple[AnimalDetailSchema, ...] = Field(
        ...,
        description="",
    )


class AnimalTypeSchema(BaseModel):
    """ The scheme for obtaining the type of animal. """

    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )

    @field_validator("animal_type", mode="before")
    @classmethod
    def validate_animal_type(cls, value: str) -> str | None:
        if value is None:
            return value
        available_animal_types = ("dog", "cat", "fox")
        if value not in available_animal_types:
            raise ValueError("Invalid animal type")
        return value

    model_config = ConfigDict(from_attributes=True)
