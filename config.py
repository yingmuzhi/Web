'''
配置SQLite数据库
'''
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # 配置 SQLite 数据库路径
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'personal_website.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False