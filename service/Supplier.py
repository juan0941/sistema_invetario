from models.Supplier import Supplier as SupplierModel
from schemas.Supplier import Supplier

class SupplierService():
    def __init__(self,db):
        self.db = db

    def get_supplier(self):
        result = self.db.query(SupplierModel).all()
        return result
    
    def create_supplier(self,Supplier:SupplierModel):
        new_Supplier = SupplierModel(
            Name = Supplier.Name,
            Address = Supplier.Address,
            Phone = Supplier.Phone,
            Email = Supplier.Email

        )
        self.db.add(new_Supplier)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(SupplierModel).filter(SupplierModel.id == id).first()
        return result
    
    def update_supplier(self,id:int,data:Supplier):
        Supplier = self.db.query(SupplierModel).filter(SupplierModel.id == id).first()
        Supplier.Name = data.Name
        Supplier.Address = data.Address
        Supplier.Phone = data.Phone
        Supplier.Email = data.Email
        self.db.commit()
        return
    
    def delete_supplier(self,id:int):
        self.db.query(SupplierModel).filter(SupplierModel.id == id).delete()
        self.db.commit()
        return