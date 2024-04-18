from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import UUID
import uuid

from config.config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    currency = Column(String, nullable=False)
    date_ = Column(DateTime, nullable=False)
    price = Column(Float, nullable=False)


Base.metadata.create_all(engine)
