import sys

def wordcount(S):
    N = len(S.strip().split())
    return N


fileename = sys.argv[0]
try:
    f = open(arg,'r')
    text = f.read()
    print(wordcount(text))
    f.close()
except:
    print("File not available!")


A = "python is a great language"
print(wordcount(A))                                
    
