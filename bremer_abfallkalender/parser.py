"""Parser for data."""
import datetime
import re
import urllib
from collections import OrderedDict

from bs4 import BeautifulSoup

import requests

from .exceptions import MultipleMonthException

ICONS = {
    'trash': 'Rest',
    'recycle': 'Papier'
}

UTF8_ICONS = {
    'recycle': '♺',
    'trash': '🗑'
}

MONTHS = [
    'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August',
    'September', 'Oktober', 'November', 'Dezember'
]

BASE_URL = 'http://213.168.213.236/bremereb/bify/bify.jsp'


def parse_for_date(data: str, year: int, month: int):
    """Get the data for given month,year for given html-data."""
    m = re.search(rf'(?P<tag>(\w+))\W*{month} {year}', data)
    tag = m.groups('tag')[0]

    soup = BeautifulSoup(data, 'html.parser')

    bs = soup.find_all(tag)
    this_month = [b for b in bs if b.text.startswith(f'{month} {year}')]
    if len(this_month) > 1:
        raise MultipleMonthException()

    parent = str(this_month[0].parent)
    ret = {}
    for icon, name in ICONS.items():
        pattern = rf'(?P<day>(\d+))\.(?P<month>(\d+)).*{name}'
        for m in re.finditer(pattern, parent):
            ret[m.group('day')] = icon
    return ret


def parse_html(data: str, now: datetime = None):
    """Get data from HTML-tags, uses parse_for_data for individual tags."""
    if not now:
        now = datetime.datetime.utcnow()
    current_month = MONTHS[now.month-1]
    next_month = MONTHS[now.month]
    year = now.year
    ret = {}
    for day, icon in parse_for_date(data, year, current_month).items():
        ret[f'{year}-{now.month}-{day}'] = icon
    for day, icon in parse_for_date(data, year, next_month).items():
        ret[f'{year}-{now.month+1}-{day}'] = icon
    return ret


def print_nice(data: object):
    """Print data as a nice UTF-8 encoded string.

    Shows the current date a colon, the description and an
    UTF-8 icon (trash bin for general and recycle for
    recycling/paper).
    """
    texts = {}
    for date_str, icon in data.items():
        utf8_icon = UTF8_ICONS[icon]
        date = [int(d) for d in date_str.split('-')]
        date = datetime.datetime(*date)
        month = MONTHS[date.month-1]
        date_text = f'{date.day}. {month} {date.year}'
        utf8_text = {
            'trash': 'Bio- und Restmüll',
            'recycle': 'Papier und Gelber Sack'
        }[icon]
        texts[date_str] = f'{date_text}: {utf8_text} ({utf8_icon})'
    sort_txt = OrderedDict(sorted(texts.items(), key=lambda t: t[0]))
    return '\n'.join(sort_txt.values())


def get_from_website(strasse: str, hausnummer: int, now: datetime = None):
    """Download the actual data from the Webserver."""
    strasse = strasse.encode(encoding='ISO-8859-1', errors='strict')
    strasse = urllib.parse.quote_plus(strasse)
    r = requests.get(f'{BASE_URL}?strasse={strasse}&hausnummer={hausnummer}')
    return parse_html(r.text, now=now)
