#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
	"""
	read two ints
	s a string
	return a list of two ints, representing the beginning and end of a range, [i, j]
	"""
	a = s.split()
	return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
	"""
	i the beginning of the range, inclusive
	j the end       of the range, inclusive
	return the max cycle length of the range [i, j]
	"""
	#knownValues = []

	for n in range (i,j+1):
		
		i = n
		count = 1
		if i % 2 == 0:
			i = (i / 2)
			count += 1
		elif i % 2 != 0:
			i = (i + (i>>1) + 1)
			count += 2
		
		if count not in knownValues:
			#knownValues[n] = count



	return 1

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
	"""
	print three ints
	w a writer
	i the beginning of the range, inclusive
	j the end       of the range, inclusive
	v the max cycle length
	"""
	w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
	"""
	r a reader
	w a writer
	"""
	for s in r:
		i, j = collatz_read(s)
		v = collatz_eval(i, j)
		collatz_print(w, i, j, v)
