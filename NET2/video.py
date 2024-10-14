from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db_setup import Base

class Video(Base):
    __tablename__ = 'Videos'
    VideoID = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String(200), nullable=False)
    Description = Column(String(500))
    GenreID = Column(Integer, ForeignKey('Genres.GenreID'))
    Duration = Column(Integer)

    # Relationship with Genre
    genre = relationship("Genre", back_populates="videos")

    # Relationship with Views (video can have many views)
    views = relationship("View", back_populates="video")

    def __repr__(self):
        return f"Video(ID={self.VideoID}, Title='{self.Title}', GenreID={self.GenreID}, Duration={self.Duration})"
