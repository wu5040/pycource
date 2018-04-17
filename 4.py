f=open('words.txt','r')
fx=open('result.txt','w')
fx.truncate()
line_list=[li.strip('\n') for li in f]
for line in line_list:
    if line[::-1]!=line and line[::-1] in line_list:
        print(line)
        fx.write(line+'\n')
f.close()
fx.close()

