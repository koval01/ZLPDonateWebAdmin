from requests import get, exceptions
from bs4 import BeautifulSoup
from .config import USER_AGENT, API_URL, API_URL_RU
import logging, re


def __main__(country='UA') -> str:
    error_http = False;
    error_parse = False;
    error_decode = False
    headers = {"user-agent": USER_AGENT}
    array = []

    if country == 'UA':
        try:
            http_response = get(API_URL, headers=headers)
        except exceptions.RequestException:
            error_http: True

        if not error_http:
            try:
                soup = BeautifulSoup(http_response.text)
                fields_all = soup.find_all('div', {"class": "one-field", "class": "info-count"})
            except Exception as e:
                logging.error(e)
                error_parse: True

            for i in fields_all:
                try:
                    soup_local = BeautifulSoup(str(i))
                    array.append(soup_local.find('div', {"class": "field-value"}).text.replace('\n', ''))
                except Exception as e:
                    logging.error(e)
                    error_decode: True

            def ukr_month_to_russian(string) -> str:
                """local function mont translate"""
                ua_month = ['січня', 'лютого', 'березня', 'квітня', 'травня', 'червня', 'липня', 'серпня',
                            'вересня', 'жовтня', 'листопада', 'грудня']
                ru_month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября',
                            'октября', 'ноября', 'декабря']
                for i, e in enumerate(ua_month):
                    if e in string:
                        return string.replace(e, ru_month[i])

            date = soup.find('span', {'style': 'color: #999999;'}).text
            date = ukr_month_to_russian(date)
            array.append(date.replace(
                'Інформація станом на', 'По состоянию на'
            ))

            if len(array) != 6:
                error_decode: True

        if error_http or error_parse or error_decode:
            logging.error(f'Error http: {error_http}; Error parsing: {error_parse}; Error decode: {error_decode};')
            return 0

    elif country == 'RU':
        try:
            http_response = get(API_URL_RU, headers=headers)
        except exceptions.RequestException:
            error_http: True

        if not error_http:
            try:
                soup = BeautifulSoup(http_response.text)
                fields_all = soup.find_all('div', {"class": "cv-countdown__item"})
            except Exception as e:
                logging.error(e)
                error_parse: True

            for i in fields_all:
                try:
                    soup_local = BeautifulSoup(str(i))
                    x = soup_local.find('div', {"class": "cv-countdown__item-value"}).text.replace('> ', '').replace(
                        ' млн', '00 000').replace(',', ' ')
                    array.append(x)
                except Exception as e:
                    logging.error(e)
                    error_decode: True

            date = soup.find('div', {'class': 'cv-banner__description'}).text
            array.append(re.sub(r'\d\d[:]\d\d', '', date))

            if len(array) != 6:
                error_decode: True

        if error_http or error_parse or error_decode:
            logging.error(f'Error http: {error_http}; Error parsing: {error_parse}; Error decode: {error_decode};')
            return 0

    return array