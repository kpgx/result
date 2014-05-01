import json,csv,ast

def readJson(fname):
    with open(fname,'r') as f:        
        mydict=json.load(f)
        #~ result=
        return ast.literal_eval(json.dumps(mydict))

def readCsv(fname):
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        mydict = dict((rows[0],rows[1]) for rows in reader)
        return ast.literal_eval(json.dumps(mydict))    
    
def writeJson(dName,fname):
    with open(fname,'w') as f:
        json.dump(dName,f)
        
def writeCsv(dName,fname):
    keys=dName[0].keys()
    with open(fname, 'w') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writer.writerow(keys)
        dict_writer.writerows(dName)
        
def textToJson(iName,subList):
    """
    1st entry of sublist has to be 'index'
    """
    tempList=[]
    with open(iName, 'r') as f:    
        for line in f:
            tempD={}       
            vals=line.split()
            
            vals=vals[1:]
            #~ print vals
            count=0
            for i in vals:
                tempD[subList[count]]=i
                count+=1
            tempList.append(tempD)
    return tempList
            
def calcGpaGpvRank(dName):
    subCredits={'ENH1010':0, 'SCS2001':4, 'SCS2010':3, 'ENH1020':0, 'SCS1005':3, 'SCS1004':3, 'SCS1007':3, 'SCS1006':4, 'SCS1001':3, 'SCS2005':3, 'SCS1003':3, 'SCS1002':4, 'SCS2003':3, 'SCS1009':3,'SCS1008':4,'SCS2011':1,'SCS2006':2,'ICT1013':2, 'ICT1012':2, 'ICT1011':3, 'ICT1010':3, 'ICT1015':1, 'ICT1014':1, 'ICT2005':2, 'ICT2006':1, 'ICT2001':3, 'ICT2003':3, 'ICT2002':3, 'ICT2009':2, 'ICT2008':2, 'ICT1001':3, 'ICT1002':3, 'ICT1003':2, 'ICT1004':2, 'ICT1005':2, 'ICT1006':1, 'ICT1007':1, 'ICT1008':1, 'ICT1009':1}
    gradeCreditsClass={'A+':4.25,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,'rA+':2.00,'rA':2.00,'rA-':2.00,'rB+':2.00,'rB':2.00,'rB-':2.00,'rC+':2.00,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75,'rE':0,'-':0,'F':0}
    gradeCredits={'A+':4,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,'rA+':4.00,'rA':4.00,'rA-':3.75,'rB+':3.25,'rB':3.00,'rB-':2.75,'rC+':2.25,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75,'rE':0,'-':0,'F':0}
    rList=[]
    fList=[]
    ffList=[]
    for i in dName:        
        fullSummary={}
        totalCredit,GPVClass,GPAClass,GPV,GPA=0,0,0,0,0

        for sub in i.iterkeys():
            if sub not in subCredits.keys():
                continue
            subCredit=subCredits[sub]
            subGrade=i[sub]
            subGradeValClass=gradeCreditsClass[subGrade]   
            subGradeVal=gradeCredits[subGrade]     
            if subGrade in ('AB','--','NC','MC','ab''-'):
                pass
            else:
                totalCredit+=subCredit
            GPVClass+=subCredit*subGradeValClass
            GPV+=subCredit*subGradeVal
        try:
            GPAClass=GPVClass/totalCredit
            GPA=GPV/totalCredit
        except(ZeroDivisionError):
            print 'ZeroDivisionError: integer division or modulo by zero'
        fullSummary['index'],fullSummary['GPAClass'],fullSummary['GPVClass'],fullSummary['credit'],fullSummary['GPA'],fullSummary['GPV']=i['index'],GPAClass,GPVClass,totalCredit,GPA,GPV
        i['GPAClass'],i['GPVClass'],i['credit'],i['GPA'],i['GPV']=GPAClass,GPVClass,totalCredit,GPA,GPV
        rList.append(i)

    rList.sort(key=lambda item: (item['GPAClass']),reverse=True)
    rankClass=1
    for j in rList:
        j['rankClass']=rankClass
        rankClass+=1
        fList.append(j)    
    
    fList.sort(key=lambda item: (item['GPA']),reverse=True)
    rank=1
    for j in fList:
        j['rank']=rank
        rank+=1
        ffList.append(j)
    return ffList

def updateListNew(lOldList,lNewList):
    updatedList=[]
    
    for oldEntry in lOldList:
        found=0
        oIndex=str(oldEntry['index'])
        #~ print oIndex
        for newEntry in lNewList:
            nIndex=str(newEntry['index'])
            if oIndex==nIndex:
                found=1
                #~ print nIndex
                break
        if found:
            updatedEntry= dict(oldEntry.items() + newEntry.items())
            #~ print updatedEntry
            updatedList.append(updatedEntry)
    
    return updatedList               

def updateListRepeat(lOldList,lNewList):
    gradeCreditsClass={'A+':4.25,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,'rA+':2.00,'rA':2.00,'rA-':2.00,'rB+':2.00,'rB':2.00,'rB-':2.00,'rC+':2.00,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75,'rE':0,'-':0,'F':0}
    updatedList=[]
    
    for oldEntry in lOldList:
        found=0
        oIndex=str(oldEntry['index'])
        for newEntry in lNewList:
            nIndex=str(newEntry['index'])
            if oIndex==nIndex:
                found=1
                break
        rEntry={}
        if found:
            print oIndex
            
            for k,v in newEntry.items():
                if not v in gradeCreditsClass.keys():
                    continue
                if oldEntry[k] in ['MC','AB','ab']:
                    rEntry[k]=v
                else:
                    if gradeCreditsClass[v]<=gradeCreditsClass[oldEntry[k]]:
                        continue
                    else:
                        rEntry[k]='r'+v
        updatedEntry= dict(oldEntry.items() + rEntry.items())
        updatedList.append(updatedEntry)
    
    return updatedList    

def check(l,n):
    count=0
    for i in l:
        if int(i['index'])==n:
            
            count+=1
    print count

#~ """
#~ Example
ictlist=textToJson('ICT1001_1006.txt.out',['index','ICT1001','ICT1006'])
#~ check(ictlist,11021004)
NEWLIST=updateListNew(ictlist,textToJson('ICT1002_1003_1004_1008.txt.out',['index','ICT1002','ICT1003','ICT1004','ICT1008']))
#~ check(NEWLIST,11021004)
NEWLIST=updateListNew(NEWLIST,textToJson('ICT1005.txt.out',['index','ICT1005']))
#~ check(NEWLIST,11021004)
NEWLIST=updateListNew(NEWLIST,textToJson('ICT1007.txt.out',['index','ICT1007']))
#~ check(NEWLIST,11021004)
#~ NEWLIST=updateListNew(NEWLIST,textToJson('ICT1007.txt.out',['index','ICT1007']))
NEWLIST=updateListNew(NEWLIST,textToJson('ICT1009.txt.out',['index','ICT1009']))
#~ check(NEWLIST,11021004)
NEWLIST=updateListNew(NEWLIST,textToJson('ICT1010.txt.out',['index','ICT1010']))
#~ check(NEWLIST,11021004)
NEWLIST=updateListNew(NEWLIST,textToJson('ICT1011.txt.out',['index','ICT1011']))
#~ check(NEWLIST,11021004)
NEWLIST=updateListNew(NEWLIST,textToJson('ICT1012.txt.out',['index','ICT1012']))
#~ check(NEWLIST,11021004)
NEWLIST=updateListNew(NEWLIST,textToJson('ICT1013.txt.out',['index','ICT1013']))
#~ check(NEWLIST,11021004)
NEWLIST=updateListNew(NEWLIST,textToJson('ICT1014.txt.out',['index','ICT1014']))
#~ check(NEWLIST,11021004)
NEWLIST=updateListNew(NEWLIST,textToJson('ICT1015.txt.out',['index','ICT1015']))
#~ check(NEWLIST,11021004)
NEWLIST=updateListNew(NEWLIST,textToJson('ICT2001_2002_2003_2005_2006_2008_2009.txt.out',['index','ICT2001','ICT2002','ICT2003','ICT2005','ICT2006','ICT2008','ICT2009']))

NEWLIST=updateListNew(NEWLIST,textToJson('ICT2007.txt.out',['index','ICT2007']))

NEWLIST=updateListNew(NEWLIST,textToJson('ICT1016.txt.out.out',['index','ICT1016']))

NEWLIST=updateListRepeat(NEWLIST,textToJson('ICT1007101010111012101410151.txt.out',['index','ICT1007','ICT1010','ICT1011','ICT1012','ICT1014','ICT1015']))

NEWLIST=updateListRepeat(NEWLIST,textToJson('ICT1001100310051006.txt.out',['index','ICT1001','ICT1003','ICT1005','ICT1006']))

flist=calcGpaGpvRank(NEWLIST)

writeCsv(flist,'ict')
#~ """
