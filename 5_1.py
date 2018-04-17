import collections
fin=open('article.txt','r')
lines=fin.readlines()


def word_list():
    flag="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    wordlines=''
    for line in lines:
        word=''
        for ch in line:
            if ch in flag:
                word=word+ch
            else:
                word+=' '
        wordlines=wordlines+word
    return wordlines.split()

from collections import Counter

def word_count(t):
    cnt=Counter()
    for i in t:
        cnt[i]+=1
    return cnt

    '''
    idict=dict()
    for i in range(len(t)):
        idict[t[i]]=idict.get(t[i],0)+1
    _idict=dict(reversed(sorted(idict.items(),key=lambda items:items[1])))
    return _idict
    '''

word_dict=word_count(word_list())
result=word_dict.most_common(len(word_dict))
for x in result:
    print('%-20s%d'%(x[0],x[1]))

#for key,value in word_dict.items():
 #   print('%-20s%d'%(key,value))

fin.close()