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
        
def textToJson(iName,oName,subList):
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
    writeJson(tempList,oName)
            
def calcGpaGpvRank(dName):
    subCredits={'ENH1010':0, 'SCS2001':4, 'SCS2010':3, 'ENH1020':0, 'SCS1005':3, 'SCS1004':3, 'SCS1007':3, 'SCS1006':4, 'SCS1001':3, 'SCS2005':3, 'SCS1003':3, 'SCS1002':4, 'SCS2003':3, 'SCS1009':3,'SCS1008':4,'SCS2011':1,'SCS2006':2}
    gradeCreditsClass={'A+':4.25,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,'rA+':2.00,'rA':2.00,'rA-':2.00,'rB+':2.00,'rB':2.00,'rB-':2.00,'rC+':2.00,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75,'rE':0}
    gradeCredits={'A+':4,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,'rA+':4.00,'rA':4.00,'rA-':3.75,'rB+':3.25,'rB':3.00,'rB-':2.75,'rC+':2.25,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75,'rE':0}
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
            if subGrade in ('AB','--','NC','MC','ab'):
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
    found=0
    for oldEntry in lOldList:
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
    gradeCreditsClass={'A+':4.25,'A':4,'A-':3.75,'B+':3.25,'B':3,'B-':2.75,'C+':2.25,'C':2,'C-':1.75,'D+':1.25,'D':1,'D-':0.75,'E':0,'AB':0,'--':0,'NC':0,'MC':0,'rA+':2.00,'rA':2.00,'rA-':2.00,'rB+':2.00,'rB':2.00,'rB-':2.00,'rC+':2.00,'rC':2,'rC-':1.75,'rD+':1.25,'rD':1,'rD-':0.75}
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
                    if gradeCreditsClass[v]<gradeCreditsClass[oldEntry[k]]:
                        rEntry[k]=v
                    else:
                        rEntry[k]='r'+v
        updatedEntry= dict(oldEntry.items() + rEntry.items())
        updatedList.append(updatedEntry)
    
    return updatedList    

