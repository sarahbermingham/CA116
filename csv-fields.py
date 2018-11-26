#!/usr/bin/env python

header = raw_input()
i = 0

while i < len(header) and header[i] != ",":
    i = i + 1
    print header[:i]
