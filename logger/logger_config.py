import logging
import os
from logging.handlers import RotatingFileHandler

LOGGER_MB_LIMIT = 50
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
os.makedirs('/log_tests/', exist_ok=True)
info_handler = RotatingFileHandler(os.path.join('../log_tests/', "log_info.log"), mode='a',
                                   maxBytes=LOGGER_MB_LIMIT * 1024 * 1024, backupCount=1,
                                   encoding='utf-8', delay=False)
info_handler.setFormatter(formatter)
info_handler.setLevel(logging.INFO)
info_logger = logging.getLogger('info_logger')
info_logger.setLevel(logging.INFO)
info_logger.addHandler(info_handler)
