 
iName='1007'
oName='scs1007'
outStr=''
with open(iName, 'r+') as f:    
    for line in f:
        #~ print line
        tempD={}       
        vals=line.split()
        count=1
        for i in vals:
            if count%3==0:
                outStr+=i+'\n'
            else:
                outStr+=i+' '
            count+=1
                
with open(oName, 'a+') as f:
    f.write(outStr)
