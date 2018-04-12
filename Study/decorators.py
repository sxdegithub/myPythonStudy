# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

# 没有完成的
from time import sleep
from functools import wraps
import logging

logging.basicConfig(
    filemode='w',
    filename=r'E:\python\helloWorld\hellologging.txt',
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.DEBUG
)
log = logging.getLogger("retry")


def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kargs):
        MAX_ATTEMPS = 5
    for attempt in range(1, MAX_ATTEMPS+1):
        try:
            return  f()