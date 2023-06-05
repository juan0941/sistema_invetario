from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder

from service.Supplier import SupplierService 
from schemas.Supplier import Supplier
from config.database import Session

Supplier_router = APIRouter()
@Supplier_router.get('/Supplier', tags=['Supplier'],status_code=200)
def get_router():
    db = Session()
    result = SupplierService(db).get_supplier()
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@Supplier_router.get('/Supplier/{id}',tags=['Supplier'],status_code=200)
def get_Supplier_for_id(id:int):
     db = Session()
     result =SupplierService(db).get_for_id(id)
     return JSONResponse(content=jsonable_encoder(result),status_code=200)

@Supplier_router.post('/Supplier', tags=['Supplier'],status_code=201)
def create_supplier(Supplier:Supplier):
    db = Session()
    SupplierService(db).create_supplier(Supplier)
    return JSONResponse(content={"message":"Supplier created successfully", "status_code" : 201})

@Supplier_router.put('/Supplier{id}',tags=['Supplier'])
def update_supplier(id:int,data:Supplier):
     db = Session()
     result = SupplierService(db).get_for_id(id)
     if not result :
         return JSONResponse(content={"message":"Supplier don't found","status_code":404})    
     SupplierService(db).update_supplier(id,data)
     return JSONResponse(content={"message":"Supplier update succesfully","satus_code":202},status_code=202)

@Supplier_router.delete('/Supplier{id}',tags=['Supplier'])
def delete_supplier(id:int):
     db = Session()
     result = SupplierService(db).get_for_id(id)
     if not result :
         return JSONResponse(content={"message":"Supplier don't found","status_code":404})
     SupplierService(db).delete_supplier(id)
     return JSONResponse(content={"message":"Supplier delete succefully",'status_code':200},status_code=200)
