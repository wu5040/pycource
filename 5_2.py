fa=open('text.txt','r')
fb=open('keyword.txt','r')
fc=open('keyword_result.txt','w')

import time
import re
from collections import Counter
cnt=Counter()
start=time.time()
basestr=fa.read()
keyword=(line.strip('\n') for line in fb)
pattern=r"[a-zA-Z0-9\-']+"
words=re.findall(pattern,basestr)
for word in words:
    cnt[word]+=1
s="\n".join("%s:%s"%(i,cnt[i]) for i in keyword)

fc.write(s)
print("耗时：%lf"%(time.time()-start))
fa.close()
fb.close()
fc.close()

