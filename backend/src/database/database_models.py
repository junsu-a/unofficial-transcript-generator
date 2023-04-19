from sqlalchemy import Column, Integer, String
from .database import Base

class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    code = Column(String)
    title = Column(String)

class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    value = Column(Integer)





# from sqlalchemy import Column, Integer, String, event
# from .database_init import Base, SessionLocal

# class Courses(Base):
#     __tablename__ = "courses"

#     id = Column(Integer, primary_key=True, index=True)
#     course_code = Column(String, unique=True, index=True)
#     course_title = Column(String, unique=True, index=True)

# class UsedCounts(Base):
#     __tablename__ = "used_counts"

#     counts = Column(Integer, index=True)

# def insert_default_used_counts(mapper, connection, target):
#     """ Set used count as 0 when `used_count` table is newly created"""
#     default_used_counts = UsedCounts(counts=0)
#     with SessionLocal() as session:
#         session.add(default_used_counts)
#         session.commit()

# event.listen(UsedCounts.__table__, "after_create", insert_default_used_counts)
