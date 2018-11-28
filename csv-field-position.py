#!/usr/bin/env python

import sys

field = sys.argv[1]
s = raw_input()
a = []

start = 0
end = 0
i = 0
while i < len(s):
    end = start + 1
    while end < len(s) and s[end] != ",":
        end = end + 1
    if start < len(s):
        a.append(s[start:end])
    start = end + 1
    i += 1

i = 0
while i < len(a):
    if a[i] == field:
        print i
    i += 1
