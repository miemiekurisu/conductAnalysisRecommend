#-*-encoding:utf-8-*-
import time
import logging
import setting
import logging.handlers
import sys
import datetime


fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
logging.basicConfig(level=logging.INFO,format=fmt)

def timeit(func):
    def handle_args(*args, **kwargs): 
        if(setting.aspect_level=='on'):
            logging.info( func.__name__+' start:')
            start = time.time()
            try:
                ret = func(*args, **kwargs)
                logging.info( func.__name__+' is end, used: %s'%(time.time()  - start))
                return ret
            except:
                logging.error(func.__name__+"Unexpected error:%s"%sys.exc_info()[1])
        else:
            try:
                ret = func(*args, **kwargs)
                return ret
            except:
                logging.error(func.__name__+"Unexpected error:%s"%sys.exc_info()[1])
    return handle_args
