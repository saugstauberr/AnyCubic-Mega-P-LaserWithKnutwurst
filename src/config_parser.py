import configparser

def read(key):
    config = configparser.ConfigParser()
    config.read('config.ini')
    key_result = config['DEFAULT'][key]
    return key_result