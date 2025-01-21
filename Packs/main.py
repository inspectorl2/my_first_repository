import logging
#import sys


#class ErrorLogFilter(logging.Filter):
#    def filter(self, record):
#        return record.levelname == 'ERROR' and 'важно' in record.msg.lower()
class EvenLogFilter(logging.Filter):
    def filter(self, record):
        return "важно"  in record.msg.lower()

#format_1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:'\
#          '%(lineno)d - %(name)s - %(message)s'
#format_2 = '[{asctime}] #{levelname:8} {filename}:'\
#           '{lineno} - {name} - {message}'

#formatter_1 = logging.Formatter(fmt=format_1)
#formatter_2 = logging.Formatter(
#   fmt=format_2,
#   style='{'
#)


logger = logging.getLogger(__name__)

#file_handler = logging.FileHandler('logs.log')
#file_handler.setFormatter(formatter_1)
#logger.addHandler(file_handler)
stderr_handler = logging.StreamHandler()
#stdout_handler = logging.StreamHandler(sys.stdout)

#stderr_handler.setFormatter(formatter_1)
#stdout_handler.setFormatter(formatter_2)

stderr_handler.addFilter(EvenLogFilter())

#logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

for i in range(1, 5):
    logger.warning('Важно! Это лог с предупреждением! %d', i, extra={'i': i})
#print(logger.handlers)

#logger.warning('Это лог с предупреждение!')


#logging.basicConfig(
#    level=logging.DEBUG,
#    format=format_1)
#


#logging.debug('Лог уровня DEBAG')
#logger.info('Важно! Это лог уровня INFO')
#logger.warning('Важно! Это лог уровня WARNING')
#logger.error('Важно! Это лог уровня ERROR')
#logging.critical('Это лог уровня CRITICAL')
#logger.error('Это лог какой то ошибки')

#print('Это основной модуль main.py, его имя в процессу выполнения программы:', __name__)

#from pack_1.file_11 import func_1
#from pack_1.file_12 import a
#from pack_1 import file_11
#from pack_2.pack_21 import file_211
#import pack_1
#import pack_2
#from pack_2 import pack_21

#print(func_1(a))
#print(dir())
#print(dir(pack_1))
#print(dir(pack_2))
#print(dir(pack_21))
#print('b =', pack_2.file_211.b)
#print('Словарь some_dict:', file_211.some_dict)
