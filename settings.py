'''env and other config vars'''
import os
import logging
from dotenv import load_dotenv

# Env vars
load_dotenv()

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, 'app.log')

# Logging config (File logging only)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s || %(levelname)s || %(message)s',
    handlers=[logging.FileHandler(LOG_FILE, encoding='utf-8')]
)

logger = logging.getLogger('arabic-eval')
