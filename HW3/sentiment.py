#! /usr/bin/python3

import sys
import re

def getSentences( fileSet ):

	lines = fileSet.readlines()
	sentences = []
	for i in lines:
		#remove punctuation
		newLine = re.sub(ur"[^\w\d\s]+",'',i)
		newWords = newLine.split(" ")
		sentences.append(newWords)

	return sentences


def getVocabulary( sentences ): 

	vocab = []
	for curSent in sentences:
		for word in curSent:
			check = 0
			for i in vocab:
				if word.lower() == i:
					check = 1
					break
			if check == 0:
				vocab.append(word.lower())
	vocab.sort()

	return vocab


def getFeaturized( sentences, vocab ):

	fSet = []
	for curSent in sentences:
		fList = []
		for vocabWord in vocab:
			test = 0
			for i in range(0, len(curSent)-2):
				if vocabWord == curSent[i].lower():
					fList.append("1")
					test = 1
					break
			if test == 0:
				fList.append("0")
		fList.append(curSent[len(curSent)-2])
		fSet.append(fList)
	vocab.append("classlabel")
	fSet.insert(0, vocab)

	return fSet

def printPreprocess( fTrainingSet, fTestSet):
	
	wTrSet = open("preprocessed_train.txt", "w")
	wTeSet = open("preprocessed_test.txt", "w")

	wTrSet.truncate()
	wTeSet.truncate()
	for i in fTrainingSet:
		wTrSet.write(str(i))
		wTrSet.write('\n')
	for i in fTestSet:
		wTeSet.write(str(i))
		wTeSet.write('\n')

	return

def preprocess(usedSet):

	sentences = getSentences(usedSet)
	vocab = getVocabulary(sentences)
	fSet = getFeaturized(sentences, vocab)
	
	return fSet

def probabilityWord(word, usedSet, posOrNeg):

	totalApp = 0
	posOrNegApp = 0

	for i in range(0, len(usedSet[0])):
		if(word == usedSet[0][i]):
			pos = i
			break
	for line in usedSet:
		if(line[pos] == "1"):
			totalApp += 1
			if(line[len(line)-1] == str(posOrNeg)):
				posOrNegApp += 1

	return posOrNegApp / float(totalApp)

def probabilityPosOrNeg(usedSet, posOrNeg):

	totalApp = 0
	posOrNegApp = 0

	for i in range(1, len(usedSet)):
		totalApp += 1
		if(usedSet[i][len(usedSet)-1] == str(posOrNeg)):
			posOrNegApp += 1

	return posOrNegApp / float(totalApp)

def inVocab(word, usedSet):

	for i in usedSet[0]:
		if word == i:
			return 1
	
	return 0

def findWord(testSet, pos):

	return testSet[0][pos]

def findProbability(trainSet, testSet, line, posOrNeg):

	curProb = probabilityPosOrNeg(trainSet, posOrNeg)

	for i in range(0, len(line)-1):
		if line[i] == "1" and inVocab(findWord(testSet, i), trainSet):
			curProb *= probabilityWord(findWord(testSet, i), trainSet, posOrNeg)

	return curProb

def determineClass(trainSet, testSet, line):
	
	if(findProbability(trainSet, testSet, line, 1) >= findProbability(trainSet, testSet, line, 0)):
		return 1
	else:
		return 0

def classification(trainSet, testSet):

	generated = []
	actual = []
	skip = 0

	for line in testSet:
		if skip == 0:
			skip = 1
		else:
			generated.append(determineClass(trainSet, testSet, line))
			actual.append(line[len(line)-1])

	result = []
	result.append(generated)
	result.append(actual)

	return result

def calculatePercent(result):

	total = 0
	correct = 0

	for i in range(0, len(result[0])):
		total += 1
		if(str(result[0][i]) == str(result[1][i])):
			correct += 1

	return (correct / float(total)) * 100

def printResult(trainResult, testResult):
	R = open("result.txt", "w")
	R.truncate()

	R.write("Training Set: Training Set\n")
	R.write("Test Set: Training Set\n")
	R.write("Actual: " + str(trainResult[1]) + "\n")
	R.write("Generated: " + str(trainResult[0]) + "\n")
	R.write("Result: " + str(calculatePercent(trainResult)) + "%\n\n")

	R.write("Training Set: Training Set\n")
	R.write("Test Set: Test Set\n")
	R.write("Actual: " + str(testResult[1]) + "\n")
	R.write("Generated: " + str(testResult[0]) + "\n")
	R.write("Result: " + str(calculatePercent(testResult)) + "%\n\n")

	return

trainingSet = open("trainingSet.txt", "r")
testSet = open("testSet.txt", "r")

fTrainingSet = preprocess(trainingSet)
fTestSet = preprocess(testSet)

printPreprocess(fTrainingSet, fTestSet)

rTrainSet = classification(fTrainingSet, fTrainingSet)
rTestSet = classification(fTrainingSet, fTestSet)

printResult(rTrainSet, rTestSet)

#END

