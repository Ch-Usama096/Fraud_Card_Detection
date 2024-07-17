# import the important modules
import logging
import os
from datetime import datetime

log_file = f"{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.log"
log_path = os.path.join(os.getcwd() , "logs" , log_file)
os.makedirs(log_path , exist_ok = True)

log_file_path = os.path.join(log_path , log_file)

logging.basicConfig(
    filename = log_file_path,
    format = "Date & Time : [%(asctime)s] - Line Number : %(lineno)s - Name : %(name)s - Message : %(message)s",
    level = logging.INFO,
)