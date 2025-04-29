from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID

class AnimalResponseSchema(BaseModel):
    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )
    model_config = ConfigDict(from_attributes=True)


class AnimalDetailSchema(BaseModel):
    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )

    processed_image: UUID = Field(
        ...,
        description="The unique code assigned to the animal image",
    )
    model_config = ConfigDict(from_attributes=True)
