import logging
import logging.config
import os
from datetime import datetime

path = os.path.dirname(__file__)

logging.config.fileConfig(os.path.join(path, "logging_config.ini"))
# create logger
logger = logging.getLogger(__name__)

# init new logger file every time

log_file = os.path.join(path, 'log/{:%Y%m%d-%H%M}.log'.format(datetime.now()))
fh = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s [%(process)d] %(name)-5s %(levelname)s: %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.setLevel(logging.INFO)

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("paramiko").setLevel(logging.WARNING)


if __name__ == "__main__":
    print os.path.join(path, "log")

