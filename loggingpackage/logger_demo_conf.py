"""
Logger Demo
"""

import logging
import logging.config


class LoggerDemoConf():

    def testLog(self):
        # Create Logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConf.__name__)

        # Logging messages
        logger.debug('Debug message')
        logger.info('Info message')
        logger.warning('Warning message')
        logger.error('Error message')
        logger.critical('Critical message')


demo = LoggerDemoConf()
demo.testLog()
