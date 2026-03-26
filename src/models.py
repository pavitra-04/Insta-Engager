
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from src.database import Base
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    instagram_id = Column(String)

class Post(Base):
    __tablename__ = "posts"
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    post_time = Column(DateTime)
    post_type = Column(String)
    like_count = Column(Integer)
    comment_count = Column(Integer)
    view_count = Column(Integer)

class Comment(Base):
    __tablename__ = "comments"
    comment_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.post_id"))
    comment_text = Column(String)
    like_count = Column(Integer)