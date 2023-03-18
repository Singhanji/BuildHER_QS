# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# TC: O(s) where s is the length of the string 


def Maximalword(s):
    count = 0
    s = s.strip()
    for i in s[::-1]:
        if i == ' ':
            break
        else:
            count += 1
    return count


# OR (we can also solve it in one line code)

def Maximalword2(s):

    return len(s.strip().split(' ')[::-1][0])
    
    

#s = "Hello World"
# = "   fly me   to   the moon  "
s = "luffy is still joyboy"
#print(Maximalword(s))
print(Maximalword2(s))
