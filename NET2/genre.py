from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db_setup import Base

class Genre(Base):
    __tablename__ = 'Genres'
    GenreID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)

    # Updated relationship with Videos
    videos = relationship("Video", back_populates="genre")

    def __repr__(self):
        return f"Genre(ID={self.GenreID}, Name='{self.Name}')"
