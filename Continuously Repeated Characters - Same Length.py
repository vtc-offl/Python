String S

Print the characters in a line until a character is continuosly repeated

Similarly, the program must print the other lines until the character is continuously repeated and also all the characters of str are printed

Pad * at the end of strings so that each line has same length

Sample I/O: abcdeeeemonopppppluck

Sample O/P:  abcdeeee*     // Length of 8, so padded with 4 asterisks.
             monoppppp     // Maximum among the other strings of length 9.
             luck*****     // Length of 4, so padded with 5 asterisks.
             
---------------------------------------------------------------------------------------------------------------------------------------------
             
S = input().strip()
lines = []                                              // To append the string having continuous repeated characters
                                                        
substr = ""

for i in range(len(S)):
    substr+=S[i]
    
    if i==len(S)-1:
        lines.append(substr)                            // Appends the substring if it reaches the end of the string S.
        
    elif i!=0 and S[i]==S[i-1] and S[i]!=S[i+1]:
        lines.append(substr)                            // Append the substring when it fails the character repetition condition.
        substr=""
        
maxlen = len(max(lines,key=len))                        // Gets the Maximum length of the string appended in the list "lines".
for word in lines:
    print(word.ljust(maxlen,'*'))                       // Aligns each word to the left and fills the leftover space with asterisks.
