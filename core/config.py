from dotenv import load_dotenv
import os
load_dotenv()
USERNAME = os.getenv("DB_USERNAME", "postgres")
PASSWORD = os.getenv("DB_PASSWORD", "AcademyRootPassword")
HOSTNAME = os.getenv("DB_HOSTNAME", "localhost")
PORT = os.getenv("DB_PORT", "5432")
DATABASE = os.getenv("DB_DATABASE", "final_backendpaw")
