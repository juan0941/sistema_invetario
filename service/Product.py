from models.Product import Product as productModel
from schemas.Product import Product 

class ProductService():
    def __init__(self, db):
        self.db = db

    def get_product(self):
        result = self.db.query(productModel).all()
        return result
    
    def create_product(self,Product:productModel):
        new_product = productModel(
            Name = Product.Name,
            Brand = Product.Brand,
            Description = Product.Description,
            Price = Product.Price,
            Entry_Date = Product.Entry_Date,
            Availability = Product.Availability,
            Available_Quantity = Product.Available_Quantity
        )
        self.db.add(new_product)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(productModel).filter(productModel.id == id).first()
        return result
    
    def update_product(self,id:int,data:productModel):
        Product = self.db.query(productModel).filter(productModel.id == id).first()
        Product.Name = data.Name
        Product.Brand = data.Brand
        Product.Description = data.Description
        Product.Price = data.Price
        Product.Entry_Date = data.Entry_Date
        Product.Availability = data.Availability
        Product.Available_Quanriry = data.Available_Quantity

        self.db.commit()
        return
    
    def delete_Product(self,id:int):
        self.db.query(productModel).filter(productModel.id == id).delete()
        self.db.commit()
        return