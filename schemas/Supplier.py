from pydantic import BaseModel, Field
from typing import Optional

class Supplier(BaseModel):
    id : Optional[int] = None
    Name : str = Field(max_length=100, min_length=2,description = "Nombre del cliente")
    Address :str = Field(max_length=100, min_length=2, description = "Direccion del cliente")
    Phone : float =Field(ge=1, description = "Telefono del cliente")
    Email :str =Field(max_length=100, min_length=2, description = "cooreo electronico del cliente")

    class Config:
        schema_extra = {
            "example":{
                "id" : 1,
                "Name" : "pepito perez",
                "Address": "calle70 #20-154",
                "Phone" : 3013402114,
                "Email" : "valencia78@gmail.com"

            }
        }