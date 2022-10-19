

import os,sys,time,random
op=open('op.txt' , 'r').read ().split()
c=0
for o in op:
	  c+=1
	  cc='+91' +o
	  pc=random.randint(100000,999999)
	  number=cc+str(pc)
	  print(c,number,len(number))
	  open('numbers-generated.txt' , 'a').write(f'{c}]     '+number+'\n')
