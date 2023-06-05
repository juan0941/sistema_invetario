from models.Supplies import Supplies as SuppliesModel
from schemas.Supplies import Supplies

class SuppliesService():
    def __init__(self,db) :
        self.db = db

    def get_supplies(self):
        result = self.db.query(SuppliesModel).all()
        return result
    
    def create_Supplies(self,Supplies:SuppliesModel):
        new_supplies = SuppliesModel(
            Supplier_id = Supplies.Supplier_id,
            Product_id = Supplies.Product_id,
            Purchase_Price = Supplies.Purchase_Price
        )
        self.db.add(new_supplies)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(SuppliesModel).filter(SuppliesModel.id == id).first()
        return result
    
    
    def update_Supplies(self,id:int,data:Supplies):
        Supplies = self.db.query(SuppliesModel).filter(SuppliesModel.id == id).first()
        Supplies.Supplier_id = data.Supplier_id
        Supplies.Product_id = data.Product_id
        Supplies.Purchase_Price = data.Purchase_Price
        self.db.commit()
        return
    
    def delete_Supplies(self,id:int):
        self.db.query(SuppliesModel).filter(SuppliesModel.id == id).delete()
        self.db.commit()
        return