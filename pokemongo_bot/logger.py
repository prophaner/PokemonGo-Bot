import time
import logging
#logging.basicConfig(filename='..\\log.log', level=logging.DEBUG)

logging.debug("test2")

def log(string, color='white'):
    color_hex = {
        'green': '92m',
        'yellow': '93m',
        'red': '91m'
    }
    if color not in color_hex:
        print('[' + time.strftime("%Y-%m-%d %H:%M:%S") + '] '+ string)
        logging.debug(string)
    else:
        print(u'\033[' + color_hex[color] + '[' + time.strftime("%Y-%m-%d %H:%M:%S") + '] ' + string.decode('utf-8') + '\033[0m')
        logging.info(string)