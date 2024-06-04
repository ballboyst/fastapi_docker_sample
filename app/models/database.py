from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlalchemy.url = mysql://mysql:mysql@fastapi_docker_db/mysql?charset=utf8mb4&collation=utf8mb4_unicode_ci"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sessionlocal = sessionmaker(autocommit=False, autoflash=False, bind=engine)

base = declarative_base()
