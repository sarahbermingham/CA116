#!/usr/bin/env python

header = raw_input()

start = 0
end = 0
i = 0

while i < len(header):
    end = start + 1
    while end < len(header) and header[end] != ",":
        end = end + 1
    if start < len(header):
        print header[start:end]
    start = end + 1
    i = i + 1
