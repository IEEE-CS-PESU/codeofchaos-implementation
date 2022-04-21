

def mirrorChars(input,k):


	original = 'abcdefghijklmnopqrstuvwxyz'
	reverse = 'zyxwvutsrqponmlkjihgfedcba'
	dictChars = dict(zip(reverse,original)) # switched reverse & original arguments to zip


	prefix = input[0:k-1]
	suffix = input[k-1:]
	mirror = ''

	for i in range(0,len(suffix)):
		mirror = mirror + dictChars[suffix[i]]

	print (prefix-mirror) # 'prefix+mirror' changed to 'prefix-mirror'
		
# Driver program
if __name__ == "main": # '__main__' changed to 'main'
	input = 'paradox'
	k = 3
	mirrorChars(input,k)
