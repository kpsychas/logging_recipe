import logging
import logging.config

try:
    logging.config.fileConfig('mylib_logging.conf')
except:
    pass

module_logger = logging.getLogger(__name__)

# not a good practise to log here
# module may be imported and this code will be executed
# before logging is configured
module_logger.debug('debug message m1')
module_logger.info('info message m1')
module_logger.warn('warn message m1')


def foo():
    module_logger.debug('debug message m1 foo')
    module_logger.info('info message m1 foo')
    module_logger.warn('warn message m1 foo')


def foo2():
    module_logger.debug('debug message m1 foo2')
    module_logger.info('info message m1 foo2')
    module_logger.warn('warn message m1 foo2')


class FooClass():
    def __init__(self):
        # This logger is child of module's logger
        # so it will be handled the same way as its parent
        # (since we don't provide a handler for it).
        # It is used so that tracing of origin of messages
        # is a bit more granular. We could also have separate
        # loggers for module's functions but it is rarely
        # useful.
        self.logger = logging.getLogger('{}.FooClass'.format(__name__))

    def cls_foo(self):
        self.logger.debug('debug message m1 foocls')
        self.logger.info('info message m1 foocls')
        self.logger.warn('warn message m1 foocls')

        foo2()

if __name__ == '__main__':
    # we could have something similar to module2 here
    pass
