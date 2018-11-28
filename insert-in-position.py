#!/usr/bin/env python

s = raw_input()
num = []
a = []

while s != "end":
    num.append(int(s))
    s = raw_input()

n = input()
i = 0
while n < len(num):
    if num[i] < n:
        print num[i]
        a.append(num[i])
    else:
        a.append(n)
    i = i + 1

print num
print a

i = 0
while i < len(a):
    i = i + 1