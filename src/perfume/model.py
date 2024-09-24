from pydantic import BaseModel
from typing import Optional, List, Dict

class PerfumeInDB(BaseModel):
    id: Optional[str] = None
    name: str
    brand: str
    type: str
    price: dict
    description: list
    image: list


    def to_bson(self):
        return {
            "name": self.name,
            "brand": self.brand,
            "type": self.type,
            "price": self.price,
            "description": self.description,
            "image": self.image
        }