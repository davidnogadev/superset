import os

# Clave secreta para la aplicación
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY', 'default_insecure_key')

# Construir la URL de conexión a la base de datos utilizando las variables de entorno
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOSTNAME = os.getenv('DB_HOSTNAME')
DB_PORT = os.getenv('DB_PORT', '5432')  # Puerto por defecto para PostgreSQL
DB_NAME = os.getenv('DB_NAME')

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}"

# Otras configuraciones opcionales de la base de datos
SQLALCHEMY_MAX_OVERFLOW = int(os.getenv('SQLALCHEMY_MAX_OVERFLOW', 10))
