from sqlalchemy import Column, Integer, String, Float

from config.database import Base

class Supplier(Base):

    __tablename__ ="Supplier"

    id=Column(Integer, primary_key=True)
    Name = Column(String)
    Address = Column (String)
    Phone = Column (Float)
    Email = Column (String)