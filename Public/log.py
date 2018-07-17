# -*- coding: utf-8 -*-
# @Date    : 2017-10-14 15:35:17
# @Author  :
import os
import logbook
from logbook.more import ColorizedStderrHandler
from functools import wraps
from config import path




filestream = False
if not os.path.exists(path.logdir):
    os.makedirs(path.logdir)
    filestream = True
def get_logger(name='pctestjiekou', file_log=filestream, level=''):
    """ get logger Factory function """
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
        path.logpath,
        date_format='%Y%m-%d-%H%M%S', bubble=True, encoding = 'utf-8').push_thread()
    return logbook.Logger(name)

# LOG = get_logger( level='INFO')
LOG = get_logger(file_log=filestream, level='INFO')

def logger(param):
    """ fcuntion from logger meta """
    def wrap(function):
        """ logger wrapper """
        @wraps(function)
        def _wrap(*args, **kwargs):
            """ wrap tool """
            LOG.info("模块 {}".format(param))
            LOG.info("args , {}".format(str(args)))
            LOG.info("kwargs , {}".format(str(kwargs)))
            return function(*args, **kwargs)
        return _wrap
    return wrap



#
# if __name__ == '__main__':
#     logger({'securityToken': 'c063c4d327282264257d60163da3a33e'})