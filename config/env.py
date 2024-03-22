from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = Path(BASE_DIR) / 'app'

load_dotenv(Path(BASE_DIR) / '.env')
