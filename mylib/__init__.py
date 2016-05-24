import logging


# Set default logging handler to avoid "No handler found" warnings.
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

# __name__ is mylib whenever mylib is imported
logging.getLogger(__name__).addHandler(NullHandler())
