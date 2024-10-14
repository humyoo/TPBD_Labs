from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from db_setup import Base

class Subscription(Base):
    __tablename__ = 'Subscriptions'
    SubscriptionID = Column(Integer, primary_key=True, autoincrement=True)
    Type = Column(String(50), nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)

    # Relationship with Users
    users = relationship("User", back_populates="subscription")

    def __repr__(self):
        return f"Subscription(ID={self.SubscriptionID}, Type='{self.Type}', Price={self.Price})"
