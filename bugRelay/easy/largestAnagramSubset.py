
from collections import Counter

def maxAnagramSize(input):

	input = input.split(" ")

	for i in range(0,len(input)):
		input[i]=''.join(sorted(input[i])) 


	freqDict = Counter(input)


	print (max(freqDict.keys())) # .values changed to .keys

output = 'hello world' # useless variabke

if name == "__main__": # '__name__' changed to 'name'
	input = 'ant magenta magnate tan gnamate'
	maxAnagramSize(output) # 'input' changed to 'output'
