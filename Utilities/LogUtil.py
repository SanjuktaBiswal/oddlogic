import logging
import time
import inspect

class Logger():

    def __init__(self,LogFileName, logger, file_level=logging.INFO):
        #loggerName=inspect.stack()[1][3]
        #self.logger = logging.getLogger(loggerName)
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(file_level)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        curr_time = time.strftime("%Y-%m-%d")

        self.LogFileName =LogFileName    # '..\\Logs\\logging_' + curr_time + '.txt'
        # Debug>Info>Warning>Error>Critical
        # "a" to append the logs in same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(self.LogFileName, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
