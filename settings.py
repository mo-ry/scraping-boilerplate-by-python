import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.python.env')
load_dotenv(dotenv_path)

LOGIN_URL = os.environ.get("LOGIN_URL")
TARGET_URL = os.environ.get("TARGET_URL")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
LOGIN_XPATH = os.environ.get("LOGIN_XPATH")
PASSWORD_XPATH = os.environ.get("PASSWORD_XPATH")
FORM_XPATH = os.environ.get("FORM_XPATH")
NEXT_PAGE_LINK_XPATH = os.environ.get("NEXT_PAGE_LINK_XPATH")
TARGET_XPATH = os.environ.get("TARGET_XPATH")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
TABLE_NAME = os.environ.get("TABLE_NAME")
