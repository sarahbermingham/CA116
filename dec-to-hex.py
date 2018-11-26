#!/usr/bin/env python

digits = "0123456789abcdef"
base = len(digits)
n = input()
s = ""

while 0 < n:
    s = digits[n % base] + s
    n = n / base

print s
