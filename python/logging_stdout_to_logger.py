import logging
import sys

class LoggerWriter:
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, message):
        if message != '\n':
            self.logger.log(self.level, message)

logging.basicConfig(
   level=logging.DEBUG,
   format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
)

stdout_logger = logging.getLogger(__name__)
sl = LoggerWriter(stdout_logger, logging.INFO)
sys.stdout = sl

stderr_logger = logging.getLogger('STDERR')
sl = LoggerWriter(stderr_logger, logging.ERROR)
sys.stderr = sl

print('hi')