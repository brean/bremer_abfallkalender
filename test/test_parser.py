"""Test data parsing and formating."""
from bremer_abfallkalender.parser import parse_csv, print_nice


TEST_DATA = open('./test/data.csv', 'r', encoding='ISO-8859-1').read()


def test_parser():
    """Assure that data from local file gets parsed correctly."""
    data = parse_csv(TEST_DATA)
    assert data['2020-01-03'] == ['recycle']
    assert data['2020-01-08'] == ['bio', 'trash']
    assert data['2021-01-09'] == ['christmas']


def test_print_nice():
    """Make sure the output is printed nicely."""
    text = '2. Dezember 2020: Papier und Gelber Sack (♺)\n' \
        '4. Dezember 2020: Papier und Gelber Sack (♺)\n' \
        '9. Dezember 2020: Biomüll (🌿) und Restmüll (🗑)\n' \
        '16. Dezember 2020: Papier und Gelber Sack (♺)\n' \
        '18. Dezember 2020: Papier und Gelber Sack (♺)\n' \
        '22. Dezember 2020: Biomüll (🌿) und Restmüll (🗑)\n' \
        '30. Dezember 2020: Papier und Gelber Sack (♺)\n' \
        '2. Januar 2021: Papier und Gelber Sack (♺)\n' \
        '6. Januar 2021: Biomüll (🌿) und Restmüll (🗑)\n' \
        '9. Januar 2021: Tannenbaum (🎄)\n' \
        '13. Januar 2021: Papier und Gelber Sack (♺)\n' \
        '15. Januar 2021: Papier und Gelber Sack (♺)\n' \
        '20. Januar 2021: Biomüll (🌿) und Restmüll (🗑)\n' \
        '27. Januar 2021: Papier und Gelber Sack (♺)\n' \
        '29. Januar 2021: Papier und Gelber Sack (♺)\n' \
        '3. Februar 2021: Biomüll (🌿) und Restmüll (🗑)\n'
    data = parse_csv(TEST_DATA)
    assert text in print_nice(data)
