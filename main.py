import 299cproject
from 299cproject import sine_tone
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
	with open(sys.argv[1], "r") as f:
		text = file.read(n)
		text = text.lower()
		text = re.sub("[^a-z ]")
		curr = ""
		for t in text:
			curr += t
			print(curr)
			if (t != ' '):

				a = ord(t)
				ch = a - ord('a') + 1

				if (t == 'm' or t == 'n'):
					sine_tone(a4, 4)
				elif (ch < 13):
					sine_tone(a4/(halfstep**(13 - ch)), 4)
				else:
					sine_tone(a4*(halfstep**(ch - 14)), 4)





