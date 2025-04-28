from pydantic import BaseModel, Field

class AnimalResponseSchema(BaseModel):
    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )
