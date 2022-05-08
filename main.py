from player import playNote
import sys
import re

a4 = 440
halfstep = 2**(1/12)

if (len(sys.argv) < 2):
	print("Must have file argument")
else:
	n = 100
	if (len(sys.argv) == 3):
		n = int(sys.argv[2])
	with open(sys.argv[1], "r") as file:
		text = file.read(n)
		text = text.lower()
		text = re.sub("[^a-z ]","",text)
		curr = ""
		for t in text:
			curr += t
			print(curr)
			if (t != ' '):

				a = ord(t)
				ch = a - ord('a') + 1

				if (t == 'm' or t == 'n'):
					playNote(a4, 0.5)
				elif (ch < 13):
					playNote(a4/(halfstep**(13 - ch)), 1)
				else:
					playNote(a4*(halfstep**(ch - 14)), 1)





