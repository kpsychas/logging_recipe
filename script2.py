import logging
import logging.config

import mylib.module2 as m2
from mylib.module2 import foo as f2

logging.config.fileConfig('app_logging.conf')
module_logger = logging.getLogger('script2')

module_logger.debug('debug message scr2')
module_logger.info('info message scr2')
module_logger.warn('warn message scr2')


def foo():
    module_logger.debug('debug message scr2 foo')
    module_logger.info('info message scr2 foo')
    module_logger.warn('warn message scr2 foo')


def main():
    foo()
    f2()

    foo_obj = m2.FooClass()
    foo_obj.cls_foo()

    module_logger.debug('debug message scr2 main')
    module_logger.info('info message scr2 main')
    module_logger.warn('warn message scr2 main')

if __name__ == '__main__':
    main()
