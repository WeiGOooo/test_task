import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()

APPLICATION_ID = os.getenv('APPLICATION_ID')
URL = 'https://api.worldoftanks.ru/wot/account/list/{}'


logging.basicConfig(
    level=logging.INFO,
    filename='main.log',
    format='%(asctime)s  %(levelname)s  %(message)s',
    filemode='a'
)
logger = logging.getLogger(__name__)
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
c_format = logging.Formatter(
    '%(asctime)s  %(levelname)s  %(message)s')
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)


def find_account_id(search):
    url = URL.format('?application_id={}&search={}'.format(
        APPLICATION_ID, search))
    try:
        request_url = requests.get(url)
        if request_url.status_code == 200:
            return request_url.json()
    except Exception as e:
        logger.exception(f'Something went wrong : {e}')


def parse_status(result):
    statues = ['SEARCH_NOT_SPECIFIED', 'NOT_ENOUGH_SEARCH_LENGTH',
               'SEARCH_LIST_LIMIT_EXCEEDED', 'APPLICATION_ID_NOT_SPECIFIED']
    try:
        if result['status'] == 'error':
            if result['error']['message'] in statues:
                logger.info(f"Error received : {result['error']['message']}")
                return 'The error message corresponds to the documentation.'
            logger.info(f"Error received : {result['error']['message']}")
            return 'There is no such message in the documentation'
        return result.get('data')[0]['account_id']
    except Exception as e:
        logger.exception(f'Something went wrong : {e}')


def main():
    logger.info('Go!')
    search = input('Enter nickname: ')
    logger.info(f'Received: {search}')
    result = (find_account_id(search))
    print(parse_status(result))


if __name__ == '__main__':
    main()
