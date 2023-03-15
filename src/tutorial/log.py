import logging

logging.basicConfig(filename='../../resource/myProgramLog.txt', level=logging.DEBUG,
                    format='%(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('Some debugging details.')

logging.info('The logging module is working.')

logging.warning('An error message is about to be logged.')

logging.error('An error has occurred.')

logging.disable(logging.CRITICAL)
logging.critical('The program is unable to recover!')






