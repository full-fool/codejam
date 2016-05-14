
def findTail(reverseDict, currentList):
	lastEle = currentList[-1]
	isend = True
	largeTail = 0
	#print reverseDict
	#print lastEle
	if not reverseDict.has_key(lastEle):
		return len(currentList)
	for ele in reverseDict[lastEle]:
		if not ele in currentList:
			isend = False
			tmpLargeTail = findTail(reverseDict, currentList + [ele])
			if tmpLargeTail > largeTail:
				largeTail = tmpLargeTail
	if isend:
		return len(currentList)
	else:
		return largeTail



def largestNum(inputList):
	reverseDict = {}
	for i in range(len(inputList)):
		inputList[i] -= 1

	for i in range(len(inputList)):
		if reverseDict.has_key(inputList[i]):
			reverseDict[inputList[i]].append(i)
		else:
			reverseDict[inputList[i]] = [i]
	resultLength = 0
	openList = []
	closeList = []
	twoCloseList = []
	loopList = []
	for i in range(len(inputList)):

		tmpList = [i]
		crrVal = i
		while not inputList[crrVal] in tmpList:
			tmpList.append(inputList[crrVal])
			crrVal = inputList[crrVal]


		index = tmpList.index(inputList[tmpList[-1]])
		if index != len(tmpList)-2:
			#twoCloseList.append(tmpList[index:])
			closeList.append(tmpList[index:])
			if len(tmpList[index:]) > resultLength:
				resultLength = len(tmpList[index:])
		else:
			largeTail = findTail(reverseDict, tmpList)
			if largeTail > resultLength:
				resultLength = largeTail
	return resultLength




#print largestNum([7, 8, 10, 10, 9, 2, 9, 6, 3, 3])

#largestNum([2,3,4,1])

#exit()










if __name__ == "__main__":
	inputfile = open('input.in').read().split('\n')
	filehandler = open('small1.out', 'w')

	inputLen = len(inputfile)

	currentLine = 1
	currentRound = 1
	casesNum = int(inputfile[0])
	while currentLine <= inputLen - 1:
		if len(inputfile[currentLine]) == 0:
			break
		#print len(inputfile[currentLine])
		listlen = int(inputfile[currentLine])
		inputList = inputfile[currentLine+1].split()
		inputList = map(int, inputList)

		result = largestNum(inputList)

		print 'Case #%s: %s' % (currentRound, result)
		filehandler.write('Case #%s: %s\n' % (currentRound, result))
		currentRound += 1
		currentLine += 2
	filehandler.close()






	# filehandler = open('A-big-practice.out', 'w')
	# casesNum = int(raw_input())
	# for i in range(casesNum):
	# 	valueSum = int(raw_input())
	# 	itemNum = int(raw_input())

	# 	itemList = raw_input()
	# 	itemList = itemList.split()
	# 	itemList = map(int, itemList)
	# 	# for j in range(itemNum):
	# 	# 	tmpValue = int(raw_input())
	# 	# 	itemList.append(tmpValue)
	# 	index1, index2 = findTwo(valueSum, itemList)
	# 	print 'Case #%s: %s %s' % (i+1, index1, index2)
	# 	filehandler.write('Case #%s: %s %s\n' % (i+1, index1, index2))
	# filehandler.close()

