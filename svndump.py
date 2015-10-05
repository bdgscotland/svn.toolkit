#!/bin/python
import subprocess, shlex, itertools

def ranges(i):
        for a, b in itertools.groupby(enumerate(i), lambda (x, y): y - x):
                b = list(b)
                yield b[0][1], b[-1][1]

with open('good_revisions.txt') as f:
        revlist = f.read().splitlines()
revlist = map(int, revlist)
print revlist

print list(ranges(revlist))

