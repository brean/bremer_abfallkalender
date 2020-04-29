# Bremer Abfallkalender

[![Build Status](https://travis-ci.org/brean/bremer_abfallkalender.svg?branch=master)](https://travis-ci.org/brean/bremer_abfallkalender)

Get data from Stadtreinigung Bremen

# Installation and usage
Install the required libraries using `pipenv install` or `pip install -r requirements.txt`

You can then use the CLI to get data:
```
python bremer_abfallkalender/cli.py -s Bahnhofstraße -n 1
```

The output should look like this:
```
1. April 2020: Bio- und Restmüll (🗑)
8. April 2020: Papier und Gelber Sack (♺)
15. April 2020: Bio- und Restmüll (🗑)
22. April 2020: Papier und Gelber Sack (♺)
29. April 2020: Bio- und Restmüll (🗑)
6. Mai 2020: Papier und Gelber Sack (♺)
13. Mai 2020: Bio- und Restmüll (🗑)
20. Mai 2020: Papier und Gelber Sack (♺)
27. Mai 2020: Bio- und Restmüll (🗑)
```
