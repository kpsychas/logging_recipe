import logging
import logging.config

import mylib.module1 as m1
from mylib.module1 import foo as f1

logging.config.fileConfig('app_logging.conf')
module_logger = logging.getLogger('script1')

module_logger.debug('debug message scr1')
module_logger.info('info message scr1')
module_logger.warn('warn message scr1')


def foo():
    module_logger.debug('debug message scr1 foo')
    module_logger.info('info message scr1 foo')
    module_logger.warn('warn message scr1 foo')


def main():
    foo()
    f1()

    foo_obj = m1.FooClass()
    foo_obj.cls_foo()

    module_logger.debug('debug message scr1 main')
    module_logger.info('info message scr1 main')
    module_logger.warn('warn message scr1 main')

if __name__ == '__main__':
    main()
