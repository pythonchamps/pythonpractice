def listReverse(lst):
	'''
	function to reverse the string.
	'''

	nlst = []
	for x in range(len(lst)-1,-1,-1):
		nlst.append(lst[x])

	return nlst


