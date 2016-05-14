def findTwo(valueSum, itemList):
	itemDict = {}
	lNum = len(itemList)
	for i in range(lNum):
		if itemDict.has_key(itemList[i]):
			itemDict[itemList[i]].append(i)
		else:
			itemDict[itemList[i]] = [i]
	for eachKey in itemDict.keys():
		if eachKey * 2 == valueSum and len(itemDict[eachKey]) >= 1:
			minIndex = min(itemDict[eachKey][0], itemDict[eachKey][1])
			maxIndex = max(itemDict[eachKey][0], itemDict[eachKey][1])
			return minIndex + 1, maxIndex + 1
		elif itemDict.has_key(valueSum - eachKey):
			minIndex = min(itemDict[eachKey][0], itemDict[valueSum - eachKey][0])
			maxIndex = max(itemDict[eachKey][0], itemDict[valueSum - eachKey][0])
			return minIndex + 1, maxIndex + 1
		else:
			continue
	return None, None




if __name__ == "__main__":
	inputfile = open('A-large-practice.in').read().split('\n')
	filehandler = open('A-large-practice.out', 'w')

	inputLen = len(inputfile)

	currentLine = 1
	currentRound = 1
	casesNum = int(inputfile[0])
	while currentLine <= inputLen - 1:
		if len(inputfile[currentLine]) == 0:
			break
		#print len(inputfile[currentLine])
		valueSum = int(inputfile[currentLine])
		itemNum = int(inputfile[currentLine + 1])
		itemList = inputfile[currentLine + 2]
		itemList = itemList.split()
		itemList = map(int, itemList)
		index1, index2 = findTwo(valueSum, itemList)
		print 'Case #%s: %s %s' % (currentRound, index1, index2)
		filehandler.write('Case #%s: %s %s\n' % (currentRound, index1, index2))
		currentRound += 1
		currentLine += 3
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

