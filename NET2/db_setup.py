from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

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
