 
iName='ICT1007101010111012101410151.txt'
oName=iName+'.out'
outStr=''

with open(iName, 'r+') as f:    
    for line in f:
        #~ print line
        tempD={}       
        vals=line.split()
        count=1
        for i in vals:
            if count%8==0:
                outStr+=i+'\n'
            else:
                outStr+=i+' '
            count+=1
                
with open(oName, 'a+') as f:
    f.write(outStr)
'''
with open(iName, 'r+') as f:    
    for line in f:
        #~ print line
        #~ tempD={}       
        vals=line.split()
        mystr=vals[0]+' '+vals[1]+' '+vals[8]+'\n'
        with open(oName, 'a+') as f:
    
'''
