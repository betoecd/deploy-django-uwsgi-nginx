#!/usr/bin/python

import os
import sys

def log(*args, **kwargs):
	return print(*args, **kwargs, file=sys.stderr)

def to_bool(s:str)-> bool:
	return s.strip().upper()[0] in ('1', 'T', 'Y')

SECRET_KEY = os.environ.get('SECRET_KEY')
assert SECRET_KEY

DEBUG = os.environ.get('DEBUG', 'True')
ALLOWED_HOSTS_ENV = os.environ.get('ALLOWED_HOSTS_ENV')
