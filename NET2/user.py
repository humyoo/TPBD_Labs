from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db_setup import Base

class User(Base):
    __tablename__ = 'Users'
    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    Password = Column(String(100), nullable=False)
    SubscriptionID = Column(Integer, ForeignKey('Subscriptions.SubscriptionID'))

    # Relationship with Subscription
    subscription = relationship("Subscription", back_populates="users")

    # Relationship with Views (user can have many views)
    views = relationship("View", back_populates="user")

    def __repr__(self):
        return f"User(ID={self.UserID}, Name='{self.Name}', Email='{self.Email}')"
