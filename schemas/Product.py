from pydantic import BaseModel, Field
from typing import Optional
class Product(BaseModel):
    id : Optional[int] = None
    Name : str = Field(max_length=15, min_length=2, description = "Nombre del producto")
    Brand : str = Field(max_length=15, min_length=2, description = "Marca del producto")
    Description : str = Field(max_length=100, min_length=2, description = "Descripcion del producto")
    Price : float = Field(ge=100, description = " Precio del producto")
    Entry_Date : str = Field(max_length=100000000, min_length=1, description = "Fecha de entrada del producto")
    Availability : str = Field(max_length=100, min_length=3, description = "Disponibilidad del producto")
    Available_Quantity : int = Field(ge=1,description = "Cantidad disponible del producto" )

    class Config:
        schema_extra = {
            "example":{
                "id" :1,
                "Name" :"TENIS",
                "Brand" :"NIKE",
                "Description" : "ZAPATOS",
                "Price" : 350000,
                "Entry_Date" : "10/05/2023",
                #poner esta disponible o no esta disponible
                "Availability" : "ESTA DISPONIBLE",
                "Available_Quantity" : 5


            }
        }