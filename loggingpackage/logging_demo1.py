"""
Logging Demo 1
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.warning("This is a warning")
logging.info("This is an info")
logging.error("This is an error")
