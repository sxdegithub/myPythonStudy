# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
    print('这是在打印HOMEDRIVE变量', os.getenv('HOMEDRIVE'))
    print('这是在打印HOMEPATH变量', os.getenv('HOMEPATH'))
    print('这是在打印logging_file变量', logging_file)

    print('这是在打印HOME变量', os.getenv('HOME'))


else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)
logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')
