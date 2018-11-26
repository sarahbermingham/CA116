#!/usr/bin/env python

s = raw_input()
a = []

a.append(s)

while s != "end":
    i = 0
    dup = 0
    while i < len(a):
        if a[i] == s:
            dup = dup + 1
        i = i + 1
    if 0 == dup:
        a.append(s)
    s = raw_input()

print a
i = 0
while i < len(a):
    print a[i]
    i = i + 1
