from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:user@fastapi_docker_db:3306/FASTAPI_DB"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
