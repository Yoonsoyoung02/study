import string
import sys

word = sys.stdin.readline().rstrip()
alpha = list(string.ascii_lowercase)
word_loc= [-1]*26

for i in word:
    if  i in alpha:
        word_loc[alpha.index(i)] = word.index(i)

sys.stdout.write(' '.join(map(str,word_loc))+'\n')