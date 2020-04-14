import csv
from collections import OrderedDict

with open('data77.csv', 'rt') as f:
    r = csv.reader(f)
    dict2 = {row[0]: row[1:] for row in r}

with open('users77.csv', 'rt') as f:
    r = csv.reader(f)
    dict1 = OrderedDict((row[0], row[1:]) for row in r)

result = OrderedDict()
for d in (dict1, dict2):
    for key, value in d.items():
         result.setdefault(key, []).extend(value)

with open('combined.csv', 'w') as f:
    w = csv.writer(f)
    for key, value in result.items():
        w.writerow([key] + value)
