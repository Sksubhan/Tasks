from myproject import results
from myproject import logger
import time
logger.info('Execution Started.')
time.sleep(1)
try:
    a,b,c=map(int,input('Enter three subjects scores:').split())
    logger.debug(results(a,b,c))
except ValueError:
    logger.info('Give three values in integer format')
finally:
    logger.info('Execution ended.')