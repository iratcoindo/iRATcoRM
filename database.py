from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import bcrypt
import os

# Pastikan folder data ada
os.makedirs("data", exist_ok=True)

engine = create_engine("sqlite:///data/irm.db")

Base = declarative_base()

Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True)

    password = Column(String)

    fullname = Column(String)

    role = Column(String)


Base.metadata.create_all(engine)


def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


def verify_password(password, hashed):
    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )


def create_default_admin():

    session = Session()

    admin = session.query(User).filter_by(username="admin").first()

    if admin is None:

        admin = User(
            username="admin",
            password=hash_password("admin123"),
            fullname="Administrator",
            role="Admin"
        )

        session.add(admin)
        session.commit()

    session.close()
