#!/usr/bin/env python

if __name__ == "__main__":
    a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]

small = a[0]
pos = 0
i = 1

while i < len(a):
    if a[i] < small:
        small = a[i]
        pos = i
    i = i + 1

print pos
