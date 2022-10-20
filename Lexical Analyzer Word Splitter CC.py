import re

# Below is the code of file reading
print("File is given below:")
a = open("textFile.txt","r")
b = a.read()
print(b)

word = []
lexem = "";
i = 0
punctuators = [" ", ",", ";"]
operators = ['+', '-', '*', '=', '!', '>', '<']
while(i<len(b)):
    # Punctuators wagera ai tou split krda:
    if(b[i] in punctuators):
        word.append(lexem)
        lexem = ""

    # For parenthesis:
    elif(b[i] in ["(", ")", "{", "}", "[", "]" ]):
        word.append(b[i])
        word.append(lexem)
        lexem = ""

    # For (0-9).(0-9) & (A-Z).(0-9) & (A-Z).(A-Z) & (0-9).(A-Z)
    elif(b[i] == "."):
        if((b[i-1].isnumeric()) and (b[i+1].isnumeric())):
            lexem+=b[i]
        else:
            word.append(lexem)
            word.append(b[i])
            lexem = ""
            
    # For single line comment:
    elif(b[i] == '/' and b[i+1] == '/'):
        while(b[i] != "\n"):
            lexem+=b[i]
            i+=1
            
     # For multi line comment:
    elif(b[i] == '/' and b[i+1] == '*'):
         while(b[i]!= "*" and b[i+1]!="/"):
             lexem+=b[i]
             i+=1
           


    elif(b[i] == '\n'):
        lexem = ""
        word.append(lexem)
        lexem = ""
    
    # For double operators
    elif((b[i] in operators) and (b[i+1] in operators)):
        join_word_list = []
        join_word_list.append(b[i])
        join_word_list.append(b[i+1])
        x = ''.join(join_word_list)
        lexem+=x
        word.append(lexem)
        lexem= ""
        i+=1

        
    else:
        lexem+=b[i]
    i+=1
print(" The orignal word list is = ",word)

# Python3 program for the above approach

# Function to check if the given
# string is a comment or not
def isComment(line):

	# If two continuous slashes
	# precedes the comment
	if (line[0] == '/' and line[1] == '/' and line[2] != '/'):
		print("It is a single-line comment")
		return

	if (line[len(line) - 2] == '*' and line[len(line) - 1] == '/' and line[0] == '/' and line[1] == '*'):
		print("It is a multi-line comment")
		return

	print("It is not a comment")

# Driver Code
if __name__ == '__main__':

	# Given string
	line = "// Love Pakistan";
	
	# Function call to check whether then
	# given string is a comment or not
##	isComment(line)
	


##ans = list(filter(None,word))
##print("Modified Word list is = ",ans)
##

##k = 0
##while("" in word):
##    word.remove("")

##word1 = []
##j = 0
##while(j<len(c)):
##     if(c[j] in ['#']):
##        while(c[j] not in ['#']):
##            j+=1
##
##     word1.append(c[j])     
##     j+=1
##print("Word list after comment -->",word1)         

##i = 0
##while(i < len(b)):
##    if(b[i] in [" ", "," , ";","\n"]):
##        #space wagera ai tou split krda
##        word.append(lexem)
##        lexem = ""
##        
##    elif(b[i] in ["(" , ")", "+", "-", "="]):
##        
##        word.append(b[i])
##        lexem = ""
##
##    else:
##        lexem+=b[i]
##    i+=1
##print(word)
 
    
