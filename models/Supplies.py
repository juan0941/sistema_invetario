from sqlalchemy import Column, Integer, String, Float

from config.database import Base

class Supplies(Base):

    __tablename__ ="Supplies"
    
    id = Column(Integer, primary_key = True, index=True)
    Supplier_id = Column(Integer)
    Product_id = Column(Integer)
    Purchase_Price = Column(Float)
