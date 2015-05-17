__author__ = 'samsung'
import sys
i = 0
for line in sys.stdin:
        for token in line.strip().split():
            print(token + "\t 1")
            i = i+1
            if i>50:
		 break
