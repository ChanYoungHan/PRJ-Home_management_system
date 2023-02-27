import logging
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

Base = declarative_base()


class CreditCradInfo(Base):
    __tablename__ = "credit_card_info"

    id = Column(Integer, primary_key=True)
    bank_name = Column(String)
    data = Column(String)
    user_info = relationship("UserInfo")


class UserInfo(Base):
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True)
    credit_card_id = Column(ForeignKey("credit_card_info.id"))
    name = Column(String)


class DB_SQLAlchemy:
    def __init__(self) -> None:
        RDS_HOSTNAME = "db_postgres"
        RDS_PORT = "5432"
        RDS_DB_NAME = "postgres"
        RDS_USERNAME = "postgres"
        RDS_PASSWORD = "example"
        database_url = f"postgresql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_HOSTNAME}:{RDS_PORT}/{RDS_DB_NAME}"
        e = create_engine(database_url, echo=False)
        Base.metadata.create_all(e)

        self.session = Session(e)

        self.session.add_all(
            [
                CreditCradInfo(
                    bank_name="sin-han", user_info=[UserInfo(name="ChanYoung")]
                ),
                CreditCradInfo(
                    bank_name="woo-ri", user_info=[UserInfo(name="SangMin")]
                ),
            ]
        )

        self.session.commit()

    def get_user_info(self, name):
        data_list = self.session.query(UserInfo).filter(UserInfo.name == name).all()
        return data_list[0]

    def get_credit_card_info(self, id):
        data_list = (
            self.session.query(CreditCradInfo)
            .filter(UserInfo.id == id)
        ).all()
        return data_list[0]
