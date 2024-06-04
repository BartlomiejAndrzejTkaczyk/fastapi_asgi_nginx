from sqlalchemy import Column, Integer, String
from common.database import Base, engine
import json



class User(Base):
    __tablename__ = 'users'

    id_ = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nickname = Column(String, index=True, nullable=False)
    hash_password = Column(String, nullable=False)
    info = Column(String, nullable=True)

    def to_dict(self):
        return {
            "id_": self.id_,
            "nickname": self.nickname,
            "hash_password": self.hash_password,
            "info": self.info
        }

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)

Base.metadata.create_all(engine)