from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder

from service.Product import ProductService
from schemas.Product import Product
from config.database import Session

Product_router = APIRouter()
@Product_router.get('/Product', tags=['Product'],status_code=200)
def get_router():
    db = Session()
    result = ProductService(db).get_product()
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@Product_router.get('/Product_for_id',tags=['Product'],status_code=200)
def get_Product_for_id(id:int):
     db = Session()
     result =ProductService(db).get_for_id(id)
     return JSONResponse(content=jsonable_encoder(result),status_code=200)

@Product_router.post('/Product', tags=['Product'],status_code=201)
def create_product(Product:Product):
    db = Session()
    ProductService(db).create_product(Product)
    return JSONResponse(content={"message":"product created successfully", "status_code" : 201})

@Product_router.put('/Product{id}',tags=['Product'])
def update_product(id:int,data:Product):
     db = Session()
     result = ProductService(db).get_for_id(id)
     if not result :
         return JSONResponse(content={"message":"Product don't found","status_code":404})    
     ProductService(db).update_product(id,data)
     return JSONResponse(content={"message":"Product update succesfully","satus_code":202})

@Product_router.delete('/Product{id}',tags=['Product'])
def delete_Product(id:int):
     db = Session()
     result = ProductService(db).get_for_id(id)
     if not result :
         return JSONResponse(content={"message":"Product don't found","status_code":404})
     ProductService(db).delete_Product(id)
     return JSONResponse(content={"message":"Product delete succefully",'status_code':200},status_code=200)