import mysql.connector
from tkinter import *

fileObject=open("connCache.txt","r")
connectStr=fileObject.read()
fileObject.close()
connectArr=connectStr.split(" ")
print(connectArr)
uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
curs=focus.cursor()

def makePurch(medNam,medPri,MediID):
    getitmdqu="select StckLimit from TestWarehouse where WareMedID='"+MediID+"'"
    print(getitmdqu)
    curs.execute(getitmdqu)
    finaMeds=curs.fetchall()[0][0]-1
    setfimdqu="update TestWarehouse set StckLimit="+str(finaMeds)+" where WareMedID='"+MediID+"'"
    print(setfimdqu)
    curs.execute(setfimdqu)
    focus.commit()
    trytoexe="insert into TestProfitTab(MedicNomen,EarnedCash) values ('"+medNam+"',"+str(medPri)+")"
    print(trytoexe)
    curs.execute(trytoexe)
    focus.commit()

def getMedNam(RequestID):
    curs.execute("select MedName from TestMedicines where MedicineID='"+RequestID+"'")
    result=curs.fetchall()[0][0]
    return result

def getTypNam(RequestID):
    result=""
    curs.execute("select IsAntiPytc from TestMedicines where MedicineID='"+RequestID+"'")
    if curs.fetchall()[0][0]==1:
        result="Anti-Pyretics"
    curs.execute("select IsAnalGesc from TestMedicines where MedicineID='"+RequestID+"'")
    if curs.fetchall()[0][0]==1:
        result="Analgesics"
    curs.execute("select IsAntiBiot from TestMedicines where MedicineID='"+RequestID+"'")
    if curs.fetchall()[0][0]==1:
        result="Anti-Biotics"
    curs.execute("select IsAntiSept from TestMedicines where MedicineID='"+RequestID+"'")
    if curs.fetchall()[0][0]==1:
        result="Anti-Septics"
    curs.execute("select IsMoodStab from TestMedicines where MedicineID='"+RequestID+"'")
    if curs.fetchall()[0][0]==1:
        result="Mood Stabilisers"
    curs.execute("select IsStimulan from TestMedicines where MedicineID='"+RequestID+"'")
    if curs.fetchall()[0][0]==1:
        result="Stimulants"
    curs.execute("select IsTranquil from TestMedicines where MedicineID='"+RequestID+"'")
    if curs.fetchall()[0][0]==1:
        result="Tranquilizers"
    return result

def getMfgDat(RequestID):
    curs.execute("select MfgDate from TestMedicines where MedicineID='"+RequestID+"'")
    result=curs.fetchall()[0][0]
    return result

def getExpDat(RequestID):
    curs.execute("select ExpDate from TestMedicines where MedicineID='"+RequestID+"'")
    result=curs.fetchall()[0][0]
    return result

def getMfgrID(RequestID):
    curs.execute("select MedMfgrID from TestMedicines where MedicineID='"+RequestID+"'")
    result=curs.fetchall()[0][0]
    return result

def getInveID(RequestID):
    curs.execute("select InvID from TestWarehouse where WareMedID='"+RequestID+"'")
    result=curs.fetchall()[0][0]
    return result

def getStkLim(RequestID):
    curs.execute("select StckLimit from TestWarehouse where WareMedID='"+RequestID+"'")
    result=curs.fetchall()[0][0]
    return result

def getMfgNam(RequestID):
    curs.execute("select MfgName from TestMedicines,TestManufacts where MedMfgrID=MfgrID and MedicineID='"+RequestID+"'")
    result=curs.fetchall()[0][0]
    return result

def getMedPri(RequestID):
    curs.execute("select TotalPric from TestMedPrices where MediID='"+RequestID+"'")
    result=curs.fetchall()[0][0]
    return result

def wipeTableStats(tabName):
    x = tabName.get_children()
    for item in x:
        tabName.delete(item)

def getIDfromMeds():
    userList=[]
    curs.execute("select MedicineID from TestMedicines")
    result=curs.fetchall()
    for item in result:
        userList.append(item[0])
    return userList

def getIDfromWare():
    userList=[]
    curs.execute("select WareMedID from TestWarehouse")
    result=curs.fetchall()
    for item in result:
        userList.append(item[0])
    return userList

def getMedListFroMeds():
    medList=[]
    trytoask="select MedicineID from TestMedicines"
    curs.execute(trytoask)
    received=curs.fetchall()
    for item in received:
        userList.append(item[0])
    return userList

def getUserList():
    userList=[]
    trytoask="select StoreUser from TestUserCreds"
    curs.execute(trytoask)
    received=curs.fetchall()
    for item in received:
        userList.append(item[0])
    return userList

def getAllMedicines():
    curs.execute("select * from TestMedicines")
    result=curs.fetchall()
    return result

def getAllManufacts():
    curs.execute("select * from TestManufacts")
    result=curs.fetchall()
    return result

def getAllTypeClass():
    curs.execute("select * from TestTypeClass")
    result=curs.fetchall()
    return result

def getAllWarehouse():
    curs.execute("select * from TestWarehouse")
    result=curs.fetchall()
    return result

def ViewAntiPytc():
    curs.execute("select * from TestMedicines where IsAntiPytc=1")
    result=curs.fetchall()
    return result

def ViewAnalGesc():
    curs.execute("select * from TestMedicines where IsAnalGesc=1")
    result=curs.fetchall()
    return result

def ViewAntiBiot():
    curs.execute("select * from TestMedicines where IsAntiBiot=1")
    result=curs.fetchall()
    return result

def ViewAntiSept():
    curs.execute("select * from TestMedicines where IsAntiSept=1")
    result=curs.fetchall()
    return result

def ViewMoodStab():
    curs.execute("select * from TestMedicines where IsMoodStab=1")
    result=curs.fetchall()
    return result

def ViewStimulan():
    curs.execute("select * from TestMedicines where IsStimulan=1")
    result=curs.fetchall()
    return result

def ViewTranquil():
    curs.execute("select * from TestMedicines where IsTranquil=1")
    result=curs.fetchall()
    return result

def RefreshMedi(searched):
    result=[]
    if searched=='':
        curs.execute("select * from TestMedicines")
        result=curs.fetchall()
    else:
        MediIDLike="MedicineID like '"+searched+"%' or MedicineID like '%"+searched+"%' or MedicineID like '%"+searched+"'"
        MedNamLike="MedName like '"+searched+"%' or MedName like '%"+searched+"%' or MedName like '%"+searched+"'"
        MedTypLike="MedTypeID like '"+searched+"%' or MedTypeID like '%"+searched+"%' or MedTypeID like '%"+searched+"'"
        MfgDatLike="MfgDate like '"+searched+"%' or MfgDate like '%"+searched+"%' or MfgDate like '%"+searched+"'"
        ExpDatLike="ExpDate like '"+searched+"%' or ExpDate like '%"+searched+"%' or ExpDate like '%"+searched+"'"
        trytoask="select * from TestMedicines where "+MediIDLike+" or "+MedNamLike+" or "+MedTypLike+" or "+MfgDatLike+" or "+ExpDatLike
        print(trytoask)
        curs.execute(trytoask)
        result=curs.fetchall()
    return result