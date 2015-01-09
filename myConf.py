# encoding: utf-8
# author: fanko24@gmail.com


import sys
import ConfigParser


# class Config
class Config:
    def __init__(self, path):
        self.path = path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)

    def get(self, field, key):
        result = None
        try:
            result = self.cf.get(field, key)
        except:
            pass
        return result

    def get_int(self, field, key):
        result = None
        try:
            result = self.cf.getint(field, key)
        except:
            pass
        return result

    def get_float(self, field, key):
        result = None
        try:
            result = self.cf.getfloat(field, key)
        except:
            pass
        return result

    def get_bool(self, field, key):
        result = None
        try:
            result = self.cf.getboolean(field, key)
        except:
            pass
        return result


if __name__ == "__main__":
    cf = Config("test.conf")
    print cf.get("mysql", "user")
    print cf.get_int("mysql", "port")
    print cf.get_bool("concur", "switch")
    print cf.get_float("value", "weight")

