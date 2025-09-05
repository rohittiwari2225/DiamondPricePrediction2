import logging
import os
from datetime import datetime
# log file name with timestamp to avoid overwriting
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"#creating log file name
# directory to store log files
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)#creating logs directory
os.makedirs(logs_path,exist_ok=True)#creating logs directory if not exists
log_file_path=os.path.join(logs_path,LOG_FILE)#creating log file path

# setting up logging configuration
logging.basicConfig(
    filename=log_file_path,#specifying log file path
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",#log format
    level=logging.INFO #Logging level
)