def getScoreList(score, resultList):
	if not '?' in score:
		resultList.append(score)
		return
	
	questionIndex = score.find('?')

	for i in range(10):
		score = score[:questionIndex] + str(i) + score[questionIndex+1:]
		getScoreList(score[:questionIndex] + str(i) + score[questionIndex+1:], resultList)

def maxNum(score):
	print 'input', score
	if not '?' in score:
		return score
	score = score.replace('?', '9')
	print 'out', score
	return score

def minNum(score):
	if not '?' in score:
		return score
	score = score.replace('?', '0')
	return score


def maxDiff(cscore, jscore):
	if len(cscore) == 1 and len(jscore) == 1:

		if cscore[0] == '?' and jscore[0] == '?':
			return '0', '0'
		elif cscore[0] == '?' and jscore[0] != '?':
			return jscore, jscore
		elif cscore[0] != '?' and jscore[0] == '?':
			return cscore, cscore
		else:
			return cscore, jscore

	if cscore[0] != '?' and jscore[0] != '?':
		if cscore[0] < jscore[0]:
			return cscore[0] + maxNum(cscore[1:]), jscore[0] + minNum(jscore[1:])
		elif cscore[0] > jscore[0]:
			return cscore[0] + minNum(cscore[1:]), jscore[0] + maxNum(jscore[1:])
		else:
			subCscore, subJscore = maxDiff(cscore[1:], jscore[1:])
			return cscore[0] + subCscore, jscore[0] + subJscore
	elif cscore[0] == '?' and jscore[0] != '?':
		subCscore, subJscore = maxDiff(cscore[1:], jscore[1:])
		resultCScore = jscore[0] + subCscore
		resultJScore = jscore[0] + subJscore
		crrDiff = max(int(subCscore) - int(subJscore), int(subJscore) - int(subCscore))
		if jscore[0] > '0':
			cscore1 = str(int(jscore[0])-1)
			tmpcscore = cscore1 + maxNum(cscore[1:])
			tmpjscore = jscore[0] + minNum(jscore[1:])
			tmpDiff = max(int(tmpcscore) - int(tmpjscore), int(tmpjscore) - int(tmpcscore))
			if tmpDiff <= crrDiff:
				crrDiff = tmpDiff
				resultCScore = tmpcscore
				resultJScore = tmpjscore
		if jscore[0] < '9':
			cscore1 = str(int(jscore[0]) + 1)
			tmpcscore = cscore1 + minNum(cscore[1:])
			tmpjscore = jscore[0] + maxNum(jscore[1:])
			tmpDiff = max(int(tmpcscore) - int(tmpjscore), int(tmpjscore) - int(tmpcscore))
			if tmpDiff < crrDiff:
				crrDiff = tmpDiff
				resultCScore = tmpcscore
				resultJScore = tmpjscore

		return resultCScore, resultJScore

	elif cscore[0] != '?' and jscore[0] == '?':
		#print cscore, jscore
		subCscore, subJscore = maxDiff(cscore[1:], jscore[1:])
		resultCScore = cscore[0] + subCscore
		resultJScore = cscore[0] + subJscore
		crrDiff = max(int(subCscore) - int(subJscore), int(subJscore) - int(subCscore))
		if cscore[0] > '0':
			jscore1 = str(int(cscore[0])-1)
			tmpjscore = jscore1 + maxNum(jscore[1:])
			tmpcscore = cscore[0] + minNum(cscore[1:])
			tmpDiff = max(int(tmpcscore) - int(tmpjscore), int(tmpjscore) - int(tmpcscore))
			if tmpDiff <= crrDiff:
				crrDiff = tmpDiff
				resultCScore = tmpcscore
				resultJScore = tmpjscore
		if cscore[0] < '9':
			jscore1 = str(int(cscore[0]) + 1)
			tmpjscore = jscore1 + minNum(jscore[1:])
			#print 'before', cscore
			tmpcscore = cscore[0] + maxNum(cscore[1:])
			tmpDiff = max(int(tmpcscore) - int(tmpjscore), int(tmpjscore) - int(tmpcscore))
			#print jscore,cscore
			if tmpDiff < crrDiff:
				crrDiff = tmpDiff
				resultCScore = tmpcscore
				resultJScore = tmpjscore
		return resultCScore, resultJScore
	
	else:
		subCscore, subJscore = maxDiff(cscore[1:], jscore[1:])
		resultCScore = '0' + subCscore
		resultJScore = '0' + subJscore
		crrDiff = max(int(subCscore) - int(subJscore), int(subJscore) - int(subCscore))
		tmpCScore = '0' + maxNum(cscore[1:])
		tmpJScore = '1' + minNum(jscore[1:])
		tmpDiff = max(int(tmpCScore) - int(tmpJScore), int(tmpJScore) - int(tmpCScore))
		if tmpDiff < crrDiff:
			crrDiff = tmpDiff
			resultCScore = tmpCScore
			resultJScore = tmpJScore

		tmpCScore = '1' + minNum(cscore[1:])
		tmpJScore = '0' + maxNum(jscore[1:])
		tmpDiff = max(int(tmpCScore) - int(tmpJScore), int(tmpJScore) - int(tmpCScore))
		if tmpDiff < crrDiff:
			crrDiff = tmpDiff
			resultCScore = tmpCScore
			resultJScore = tmpJScore
		return resultCScore, resultJScore
		

#print maxDiff('?16', '381')
#exit()


# 89? ?33


def process(cscore, jscore):
	cScoreList = []
	getScoreList(cscore, cScoreList)
	jScoreList = []
	getScoreList(jscore, jScoreList)
	minDiff = 2147483645
	minCscore = '2147483647'
	minJscore = '2147483647'
	for eachCScore in cScoreList:
		for eachJScore in jScoreList:
			#print max(int(eachCScore) - int(eachJScore), int(eachJScore)-int(eachCScore))
			if max(int(eachCScore) - int(eachJScore), int(eachJScore)-int(eachCScore)) < minDiff:
				minDiff = max(int(eachCScore) - int(eachJScore), int(eachJScore)-int(eachCScore))
				minCscore = eachCScore
				minJscore = eachJScore
			elif max(int(eachCScore) - int(eachJScore), int(eachJScore)-int(eachCScore)) == minDiff:
				if eachCScore < minCscore:
					minCscore = eachCScore
				elif eachCScore == minCscore:
					if eachJScore < minJscore:
						minJscore = eachJScore
				else:
					pass
			else:
				pass
	return minCscore, minJscore
























if __name__ == "__main__":
	inputfile = open('B-large-practice.in').read().split('\n')
	filehandler = open('large.out', 'w')

	inputLen = len(inputfile)

	currentLine = 1
	currentRound = 1
	casesNum = int(inputfile[0])
	while currentLine <= inputLen - 1:
		if len(inputfile[currentLine]) == 0:
			break
		#print len(inputfile[currentLine])
		twoInputList = inputfile[currentLine]
		first = twoInputList.split()[0]
		second = twoInputList.split()[1]
		cscore, jscore = maxDiff(first, second)

		print 'Case #%s: %s %s' % (currentRound, cscore, jscore)
		filehandler.write('Case #%s: %s %s\n' % (currentRound, cscore, jscore))
		currentRound += 1
		currentLine += 1
	filehandler.close()





