# encoding: utf-8
# author: fanko24@gmail.com


import sys
import logging


# class log




if __name__ == "__main__":
    log_file_1 = "./nomal_logger.log"
    log_file_2 = "./nomal_logger.log.wf"
    log_level_1 = logging.DEBUG
    log_level_2 = logging.WARN

    logger_1 = logging.getLogger("loggingmodule.NomalLogger")
    logger_2 = logging.getLogger("loggingmodule.wfLogger")
    handler_1 = logging.FileHandler(log_file_1)
    handler_2 = logging.FileHandler(log_file_2)
    formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")

    handler_1.setFormatter(formatter)
    handler_2.setFormatter(formatter)
    logger_1.addHandler(handler_1)
    logger_2.addHandler(handler_2)
    logger_1.setLevel(log_level_1)
    logger_2.setLevel(log_level_2)

    logger_1.debug("this is a debug msg!")
    logger_1.info("this is a info msg!")
    logger_1.warn("this is a warn msg!")
    logger_1.error("this is a error msg!")
    logger_1.critical("this is a critical msg!")

    logger_2.debug("this is a debug msg!")
    logger_2.info("this is a info msg!")
    logger_2.warn("this is a warn msg!")
    logger_2.error("this is a error msg!")
    logger_2.critical("this is a critical msg!")
