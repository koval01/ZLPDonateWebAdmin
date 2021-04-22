from requests import post
from .covid.config import USER_AGENT
from json import loads
import logging

logger = logging.getLogger(__name__)


def get_result(type_) -> str:
    """
    Отримуємо випадкову цитату або факт
    :param type_: 0 fact 1 quote
    :return: response dict
    """
    if type_:
        url = 'https://randstuff.ru/saying/generate/'
    else:
        url = 'https://randstuff.ru/fact/generate/'
    for i in range(3):
        try:
            headers = {
                "User-Agent": USER_AGENT,
                "X-Requested-With": "XMLHttpRequest"
            }
            r = post(url, headers=headers)
            if r.status_code == 200:
                y = loads(r.text)
                if type_:
                    x = dict(
                        author=y['author'],
                        text=y['text'],
                    )
                else:
                    x = dict(
                        text=y['text']
                    )
                return x
        except Exception as e:
            logger.error(e)