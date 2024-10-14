from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

# Зміни ці параметри відповідно до ваших налаштувань
DATABASE_URL = 'mysql+mysqlconnector://avnadmin:AVNS_H9XkQzsdnJUK3P_lk38@netflix-manya4560-9acc.j.aivencloud.com:21425/defaultdb?ssl_disabled=false'

engine = create_engine(DATABASE_URL)

# Конфігурація класу Session
Session = sessionmaker(bind=engine)

# Відображення метаданих таблиць, якщо вони вже існують
Base = declarative_base()

def create_session():
    # Створення сесії
    session = Session()
    return session

class Genre(Base):
    __tablename__ = 'Genres'
    GenreID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50), nullable=False)

    # Updated relationship with Videos
    videos = relationship("Video", back_populates="genre")

    def __repr__(self):
        return f"Genre(ID={self.GenreID}, Name='{self.Name}')"

class Subscription(Base):
    __tablename__ = 'Subscriptions'
    SubscriptionID = Column(Integer, primary_key=True, autoincrement=True)
    Type = Column(String(50), nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)

    # Relationship with Users
    users = relationship("User", back_populates="subscription")

    def __repr__(self):
        return f"Subscription(ID={self.SubscriptionID}, Type='{self.Type}', Price={self.Price})"

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
