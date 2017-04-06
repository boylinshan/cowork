# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import logging
from Singleton import Singleton
from logging.handlers import RotatingFileHandler

KYEL = "\x1B[33m"
RST = "\x1B[0m"

class LogManager(object):
	__metaclass__ = Singleton

	'''
	Global LogManager
	'''
	def __init__(self):
		super(LogManager ,self).__init__()
		self._root_logger = None
		self._init_root_logger()

	def _init_root_logger(self):
		'''
		Initial root logger's configuration
		'''
		self._root_logger = logging.getLogger()
		self._root_logger.setLevel(logging.DEBUG)
		ch = logging.StreamHandler(sys.stderr)
		ch.setLevel(logging.DEBUG)
		formatter = logging.Formatter(KYEL + "%(asctime)s -linshan- %(name)s - %(levelname)s : %(message)s" + RST)
		ch.setFormatter(formatter)
		self._root_logger.addHandler(ch)

	def get_logger(self, log_name, log_level=logging.DEBUG):
		'''
		Return a logger for caller
		:param log_name: the name of return logger.
		:param log_level: the initial log level of return logger.
		'''
		logger = logging.getLogger(log_name)
		logger.setLevel(log_level)
		return logger

if __name__ == '__main__':
	##example
	a = LogManager().get_logger('test')

	b = logging.StreamHandler(sys.stdout)
	b.setLevel(logging.WARNING)
	formatter = logging.Formatter("%(asctime)s -linshan- %(name)s - %(levelname)s : %(message)s")
	b.setFormatter(formatter)
	a.addHandler(b)

	a.warning('page')



