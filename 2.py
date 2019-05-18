import random
import string


aList = []
dupList = []

def buat_random(param):
	
	for x in range(param):
		x = ''.join(random.choice(string.ascii_letters) for x in range(32))
		aList.append(x)
	return aList


def cek_duplicate():
	for num in aList:
		if num not in dupList:
			dupList.append(num)
	return dupList

buat_random(5)
print (cek_duplicate())