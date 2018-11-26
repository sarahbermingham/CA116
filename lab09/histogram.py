#!/usr/bin/env python

s = raw_input()
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while s != "end":
    if s == "0":
        a[0] = a[0] + 1
    elif s == "1":
        a[1] = a[1] + 1
    elif s == "2":
        a[2] = a[2] + 1
    elif s == "3":
        a[3] = a[3] + 1
    elif s == "4":
        a[4] = a[4] + 1
    elif s == "5":
        a[5] = a[5] + 1
    elif s == "6":
        a[6] = a[6] + 1
    elif s == "7":
        a[7] = a[7] + 1
    elif s == "8":
        a[8] = a[8] + 1
    else:
        a[9] = a[9] + 1
    s = raw_input()

print "0", a[0] * "*"
print "1", a[1] * "*"
print "2", a[2] * "*"
print "3", a[3] * "*"
print "4", a[4] * "*"
print "5", a[5] * "*"
print "6", a[6] * "*"
print "7", a[7] * "*"
print "8", a[8] * "*"
print "9", a[9] * "*"
