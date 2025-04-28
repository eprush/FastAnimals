from pydantic import BaseModel, Field

class AnimalResponseSchema(BaseModel):
    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )

    download_link: str = Field(
        ...,
        description="The link where you can get a photo of the animal.",
        examples=["https://perchance.org/cat-img-gen"],
    )
