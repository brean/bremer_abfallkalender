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
3. Januar 2020: Papier und Gelber Sack (♺)
4. Januar 2020: Papier und Gelber Sack (♺)
8. Januar 2020: Biomüll (🌿) und Restmüll (🗑)
15. Januar 2020: Papier und Gelber Sack (♺)
17. Januar 2020: Papier und Gelber Sack (♺)
22. Januar 2020: Biomüll (🌿) und Restmüll (🗑)
29. Januar 2020: Papier und Gelber Sack (♺)
31. Januar 2020: Papier und Gelber Sack (♺)
5. Februar 2020: Biomüll (🌿) und Restmüll (🗑)
...
```

informs about christmas tree (🎄), organic (🌿), recycling (♺) and residual waste (🗑)
