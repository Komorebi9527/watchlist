'''
@Project ：Dimension_reduction.py 
@File    ：wsgi.py
@IDE     ：PyCharm 
@Author  ：成佳闻
@Date    ：2023/9/24 23:56 
'''
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
load_dotenv(dotenv_path)
from watchlist import app