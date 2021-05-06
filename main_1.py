from commons.teste import print_1
import time
import sys
import logging

logger = logging.getLogger('Projeto de testes')
logger.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(FORMATTER)
logger.addHandler(console_handler)

if __name__ == '__main__':
    logger.info('Execução da rotina de print - Projeto 1')
    print_1()
    logger.info('Logging...')

    #time.sleep(30)
