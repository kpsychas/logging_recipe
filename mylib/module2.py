import logging
import logging.config

import module1
from module1 import foo as foo_m1
from module1 import foo2 as foo2_m1

try:
    logging.config.fileConfig('mylib_logging.conf')
except:
    pass

module_logger = logging.getLogger(__name__)

# not a good practise to log here
# module may be imported and this code will be executed
# before logging is configured
module_logger.debug('debug message m2')
module_logger.info('info message m2')
module_logger.warn('warn message m2')


def foo():
    module_logger.debug('debug message m2 foo')
    module_logger.info('info message m2 foo')
    module_logger.warn('warn message m2 foo')


class FooClass():
    def __init__(self):
        self.logger = logging.getLogger('{}.FooClass'.format(__name__))

    def cls_foo(self):
        self.logger.debug('debug message m2 foocls')
        self.logger.info('info message m2 foocls')
        self.logger.warn('warn message m2 foocls')

        foo2_m1()


def main():
    # Adding
    class ModuleFilter(logging.Filter):
        def filter(self, record):
            record.name = record.name.replace('__main__', 'module2')
            return True

    f = ModuleFilter()
    main_logger = logging.getLogger()
    # Logger.handlers is not a documented field
    # filter can be added to logger or handler but
    # the name of record will not be the proper one
    # in the first case
    for handler in main_logger.handlers:
        handler.addFilter(f)

    def main_foo():
        # This is the place for functions used only by main
        # they cannot be accessed when module is imported
        # and at the same time they can access the local logger
        script_logger.debug('debug message m2 mainfoo')
        script_logger.info('info message m2 mainfoo')
        script_logger.warn('warn message m2 mainfoo')

    # this will be handled by script logger
    # script in module1 could have script.m1
    script_logger = logging.getLogger('script.m2')

    foo()
    foo_obj = FooClass()
    foo_obj.cls_foo()

    foo_m1()
    foo_obj2 = module1.FooClass()
    foo_obj2.cls_foo()

    script_logger.debug('debug message m2 main')
    script_logger.info('info message m2 main')
    script_logger.warn('warn message m2 main')

if __name__ == '__main__':
    main()
