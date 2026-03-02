import logging
import os
from datetime import datetime

def get_logger():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(
        log_dir,
        f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    )

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    #Creates a handler that writes logs into the file.
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    #Connects file handler to logger.
    logger.addHandler(file_handler)
    return logger