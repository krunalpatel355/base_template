import os
from datetime import timedelta

class Config:
    # Basic Flask Config
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    
    # MongoDB Config
    MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
    MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))
    MONGO_DB = os.getenv('MONGO_DB', 'flask_app')
    MONGO_USER = os.getenv('MONGO_USER', '')
    MONGO_PASS = os.getenv('MONGO_PASS', '')
    
    @property
    def MONGODB_URI(self):
        if self.MONGO_USER and self.MONGO_PASS:
            return f"mongodb+srv://{self.MONGO_USER}:{self.MONGO_PASS}@{self.MONGO_HOST}/{self.MONGO_DB}"
        return f"mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}/{self.MONGO_DB}"

    # AWS Config
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    EC2_INSTANCE_IP = os.getenv('EC2_INSTANCE_IP')
