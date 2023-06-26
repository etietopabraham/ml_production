import logging, os
from datetime import datetime

FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", FILE_NAME)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s'
)


# Test
# if __name__ == "__main__":
#     logging.info("Logger started")