import os
import itertools


def scantree(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            yield entry
            yield from scantree(entry.path)
        else:
            yield entry


listing = scantree('C:/temp')
for l in listing:
    print('DIR ' if l.is_dir() else 'FILE', l.path)

listing = scantree('C:/temp')
listing = sorted(listing, key=lambda e: e.is_dir())

for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))