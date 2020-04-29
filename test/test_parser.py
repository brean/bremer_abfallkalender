"""Test data parsing and formating."""
import datetime

from bremer_abfallkalender.exceptions import MultipleMonthException
from bremer_abfallkalender.parser import parse_html, print_nice

import pytest

TEST_DATA = open('./test/data.html', 'r', encoding='ISO-8859-1').read()


def test_parse_html():
    """Assure that data from local file gets parsed correctly."""
    now = datetime.datetime(2020, 4, 29, 12, 1, 1, 0)
    data = parse_html(TEST_DATA, now=now)
    assert data == {
        '2020-4-01': 'trash',
        '2020-4-08': 'recycle',
        '2020-4-15': 'trash',
        '2020-4-22': 'recycle',
        '2020-4-29': 'trash',
        '2020-5-06': 'recycle',
        '2020-5-13': 'trash',
        '2020-5-20': 'recycle',
        '2020-5-27': 'trash'
    }


def test_parse_html_failing():
    """Make sure that an exception is thrown if a date is received twice."""
    now = datetime.datetime(2020, 4, 29, 12, 1, 1, 0)
    test_data = '<html><b>April 2020</b><b>April 2020</b></html>'
    with pytest.raises(MultipleMonthException):
        parse_html(test_data, now=now)


def test_print_nice():
    """Make sure the output is printed nicely."""
    now = datetime.datetime(2020, 4, 29, 12, 1, 1, 0)
    text = '1. April 2020: Bio- und Restmüll (🗑)\n' \
        '8. April 2020: Papier und Gelber Sack (♺)\n' \
        '15. April 2020: Bio- und Restmüll (🗑)\n' \
        '22. April 2020: Papier und Gelber Sack (♺)\n' \
        '29. April 2020: Bio- und Restmüll (🗑)\n' \
        '6. Mai 2020: Papier und Gelber Sack (♺)\n' \
        '13. Mai 2020: Bio- und Restmüll (🗑)\n' \
        '20. Mai 2020: Papier und Gelber Sack (♺)\n' \
        '27. Mai 2020: Bio- und Restmüll (🗑)'
    data = parse_html(TEST_DATA, now=now)
    assert text == print_nice(data)
