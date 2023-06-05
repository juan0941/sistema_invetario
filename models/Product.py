from sqlalchemy import Column, Integer, String, Float

from config.database import Base

class Product(Base):
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Brand = Column(String)
    Description = Column(String)
    Price = Column(Float)
    Entry_Date = Column(String)
    Availability = Column(String)
    Available_Quantity = Column(Integer)