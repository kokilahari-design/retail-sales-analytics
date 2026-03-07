import os

# Database Connection Configuration

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "kokila"),
    "database": os.getenv("DB_NAME", "retail_analytics")
}



