from dotenv import load_dotenv
from pathlib import Path

load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
