import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig:
    @staticmethod
    def get_db_url():
        return os.getenv("DB_URL")
    
    @staticmethod
    def get_db_name():
        return os.getenv("DB_NAME")
    
    @staticmethod
    def get_username():
        return os.getenv("USERNAME")
    
    @staticmethod
    def get_user_password():
        return os.getenv("USER_PASSWORD")
    
    @staticmethod
    def get_db_port():
        return os.getenv("DB_PORT")
    
    @staticmethod
    def get_app_port()-> float:
        return os.getenv("APP_PORT")
    
    @staticmethod
    def get_app_host():
        return os.getenv("HOST")