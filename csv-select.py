#!/usr/bin/env python

import sys

hv = sys.argv[1]
header = raw_input()
a = []

start = 0
end = 0
i = 0
while i < len(header):
    end = start + 1
    while end < len(header) and header[end] != ",":
        end = end + 1
    if start < len(header):
        a.append(header[start:end])
    start = end + 1
    i += 1

i = 0
while i < len(hv) and hv[i] != "=":
    i += 1
h = hv[:i]
v = hv[i + 1:]

i = 0
while i < len(a):
    if a[i] == h:
        n = i
    i += 1

s = raw_input()
while s != "end":
    start = 0
    i = 0
    while i < n:
        while start < len(s) and s[start] != ",":
            start = start + 1

        start = start + 1
        i = i + 1

    end = start + 1
    while end < len(s) and s[end] != ",":
        end = end + 1
    if s[start:end] == v:
        print s
    s = raw_input()
