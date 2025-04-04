import logging
import os
from datetime import datetime

# Create logs folder if it doesn't exist
LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "test-logs"))
os.makedirs(LOG_DIR, exist_ok=True)

# Create a timestamped log file
log_file_path = os.path.join(LOG_DIR, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# Configure logger
logger = logging.getLogger("airalo_test_logger")
logger.setLevel(logging.INFO)

# Prevent duplicate logs if re-imported
if not logger.handlers:
    # File handler
    file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
