# encoding: utf-8
# author: fanko24@gmail.com


import sys
import os
import time
import logging


# class log
class Log:
    def __init__(self, module_name, file_path, min_level):
        # set the level
        self.log_level_dict = {"DEBUG":logging.DEBUG, "INFO":logging.INFO, "WARNING":logging.WARNING, "ERROR":logging.ERROR, "CRITICAL":logging.CRITICAL}

        # set the formatter
        self.formatter = logging.Formatter("[%(levelname)s] [%(asctime)s] [%(filename)s] [%(funcName)s] [%(lineno)d] [%(message)s]")

        # set file name, logger, handler and level for normal log
        self.log_file_di = os.path.join(file_path, module_name+".log")
        self.handler_di = logging.FileHandler(self.log_file_di)
        self.handler_di.setFormatter(self.formatter)
        self.log_di = logging.getLogger("loggingmodule.NomalLogger")
        self.log_di.addHandler(self.handler_di)
        if self.log_level_dict[min_level] > logging.DEBUG:
            self.log_level_di = self.log_level_dict[min_level]
        else:
            self.log_level_di = logging.DEBUG
        self.log_di.setLevel(self.log_level_di)

        # set file name, logger, handler and level for wf log
        self.log_file_wf = os.path.join(file_path, module_name+".log.wf")
        self.handler_wf = logging.FileHandler(self.log_file_wf)
        self.handler_wf.setFormatter(self.formatter)
        self.log_wf = logging.getLogger("loggingmodule.wfLogger")
        self.log_wf.addHandler(self.handler_wf)
        if self.log_level_dict[min_level] > logging.WARNING:
            self.log_level_wf = self.log_level_dict[min_level]
        else:
            self.log_level_wf = logging.WARNING
        self.log_wf.setLevel(self.log_level_wf)


if __name__ == "__main__":
    log = Log("test", ".", "DEBUG")
    log_di.debug("this is a debug msg!")
    log_di.info("this is a info msg!")
    log_wf.warning("this is a warn msg!")
    log_wf.error("this is a error msg!")
    log_wf.critical("this is a critical msg!")
