from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db_setup import Base

class View(Base):
    __tablename__ = 'Views'
    ViewID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    VideoID = Column(Integer, ForeignKey('Videos.VideoID'))
    ViewDate = Column(DateTime)

    # Relationships with User and Video
    user = relationship("User", back_populates="views")
    video = relationship("Video", back_populates="views")

    def __repr__(self):
        return f"View(ID={self.ViewID}, UserID={self.UserID}, VideoID={self.VideoID}, Date='{self.ViewDate}')"
