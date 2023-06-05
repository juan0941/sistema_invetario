from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder

from service.Supplies import SuppliesService 
from schemas.Supplies import Supplies
from config.database import Session

Supplies_router = APIRouter()
@Supplies_router.get('/supplies', tags=['supplies'],status_code=200)
def get_router():
    db = Session()
    result = SuppliesService(db).get_supplies()
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@Supplies_router.get('/supplies/{id}',tags=['supplies'],status_code=200)
def get_Supplies_for_id(id:int):
     db = Session()
     result =SuppliesService(db).get_for_id(id)
     return JSONResponse(content=jsonable_encoder(result),status_code=200)

@Supplies_router.post('/supplies', tags=['supplies'],status_code=201)
def create_Supplies(Supplies:Supplies):
    db = Session()
    SuppliesService(db).create_Supplies(Supplies)
    return JSONResponse(content={"message":"Supplies created successfully", "status_code" : 201})

@Supplies_router.put('/supplies{id}',tags=['supplies'])
def update_Supplies(id:int,data:Supplies):
     db = Session()
     result = SuppliesService(db).get_for_id(id)
     if not result :
         return JSONResponse(content={"message":"Supplies don't found","status_code":404})    
     SuppliesService(db).update_Supplies(id,data)
     return JSONResponse(content={"message":"Supplies update succesfully","satus_code":202})

@Supplies_router.delete('/supplies{id}',tags=['supplies'])
def delete_Supplies(id:int):
     db = Session()
     result = SuppliesService(db).get_for_id(id)
     if not result :
         return JSONResponse(content={"message":"Supplies don't found","status_code":404})
     SuppliesService(db).delete_Supplies(id)
     return JSONResponse(content={"message":"Supplie delete succefully",'status_code':200},status_code=200)