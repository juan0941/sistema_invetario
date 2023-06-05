from pydantic import BaseModel, Field
from typing import Optional

class Supplies(BaseModel):
    id : Optional[int] = None
    Supplier_id : Optional[int] = None
    Product_id :Optional[int] = None
    Purchase_Price : float =Field(ge=1, description = "Precio total de la compra")

    class Config:
        schema_extra = {
            "example":{
                "Supplier_id" : 1,
                "Product_id" :2,
                "Purchase_Price" :500000


            }
        }