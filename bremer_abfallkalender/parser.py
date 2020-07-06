"""Parser for data."""
import datetime
import re
import urllib
import csv
import logging
import requests

from collections import OrderedDict

from io import StringIO


GARBAGE_TYPES = {
    'Res': 'trash',  # other garbage
    'Bio': 'bio',  # organic
    'Pap': 'recycle',  # paper & recycle
    'Tan': 'christmas'  # christmas trees
}

UTF8_ICONS = {
    'recycle': '♺',
    'trash': '🗑',
    'christmas': '🎄',
    'bio': '🌿'
}

MONTHS = [
    'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August',
    'September', 'Oktober', 'November', 'Dezember'
]

BASE_URL = 'https://web.c-trace.de/bremenabfallkalender/(A(A))/abfallkalender/csv?'

log = logging.getLogger(__name__)


def parse_csv(data):
    f = StringIO(data)
    reader = csv.reader(f, delimiter=';')
    ret = {}
    DATUM_COL = None
    ABFUHRART_COL = None
    for row in reader:
        if DATUM_COL is None:
            for index in range(len(row)):
                cur_row = row[index]
                if cur_row == 'Abfuhrart':
                    ABFUHRART_COL = index
                if cur_row == 'Datum':
                    DATUM_COL = index
            assert ABFUHRART_COL is not None\
                and DATUM_COL is not None
            continue
        date = '-'.join(reversed(row[DATUM_COL].split('.')))
        garbage_type = GARBAGE_TYPES[row[ABFUHRART_COL][0:3]]
        ret.setdefault(date, [])
        ret[date].append(garbage_type)
    log.info(f'imported {len(ret)} entries.')
    return ret


def print_nice(data: object):
    """Print data as a nice UTF-8 encoded string.

    Shows the current date a colon, the description and an
    UTF-8 icon (trash bin for general and recycle for
    recycling/paper).
    """
    texts = {}
    for date_str, icons in data.items():
        date = [int(d) for d in date_str.split('-')]
        date = datetime.datetime(*date)
        month = MONTHS[date.month-1]
        date_text = f'{date.day}. {month} {date.year}'
        utf8_texts = ''
        for idx, icon in enumerate(icons):
            utf8_icon = UTF8_ICONS[icon]
            utf8_text = {
                'trash': 'Restmüll',
                'recycle': 'Papier und Gelber Sack',
                'bio': 'Biomüll',
                'christmas': 'Tannenbaum'
            }[icon]
            utf8_texts += f'{utf8_text} ({utf8_icon})'
            if idx < len(icons)-2:
                utf8_texts += ', '
            elif idx < len(icons)-1:
                utf8_texts += ' und '
        texts[date_str] = f'{date_text}: {utf8_texts}'
    sort_txt = OrderedDict(sorted(texts.items(), key=lambda t: t[0]))
    return '\n'.join(sort_txt.values())


def get_from_website(municipal: str, strasse: str, number: int, now: datetime = None):
    """Download the actual data from the Webserver."""
    strasse = urllib.parse.quote_plus(strasse)
    url = f'{BASE_URL}Gemeinde={municipal}&Strasse={strasse}&Hausnr={number}&abfall='
    log.debug(url)
    r = requests.get(url)
    return parse_csv(r.text)