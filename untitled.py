#!/usr/bin/env python

s = raw_input()
a = []

while s != "end":
	a.append(s)
	s = raw_input()

n = input()

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

print s[start:end]