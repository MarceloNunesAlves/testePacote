from commons.teste import print_1
import time
import logging

logger = logging.getLogger('Projeto de testes')

if __name__ == '__main__':
    logger.error('Execução da rotina de print - Projeto 1')
    print_1()
    logger.error('Logging...')

    #time.sleep(30)
