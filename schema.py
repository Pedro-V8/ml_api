from pydantic import BaseModel

class Manga(BaseModel):
    title: str
    img: str
    description: str

    class Config:
        orm_mode = True