from tkinter import *
import mysql.connector
import receiveDat
import tkinter.messagebox as msgbox

fileObject=open("connCache.txt","r")
connectStr=fileObject.read()
fileObject.close()
connectArr=connectStr.split(" ")
print(connectArr)
uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
curs=focus.cursor()

def drawOptPlace(where,user):
    titleText=Label(where,font=("Liberation Sans",20,"bold"),text=user,fg="green").place(x=10,y=60)
    Describ=Label(where,text="PharmaDB Basic Plan",font=('Liberation Sans',9,'italic'),fg="black",justify=LEFT).place(x=10,y=95)
    FiltTex=Label(where,text="FILTERS",font=('Liberation Sans',10,'bold'),fg="black",justify=LEFT).place(x=10,y=150)

def drawWarTable(where):
    titleText=Label(where,font=("Liberation Sans",20,"normal"),text="Available Now",fg="green").place(x=900,y=60)
    Describ=Label(where,text="The following is a catalog of all pharmaceutical products available in your local warehouse for purchase and utility. You can request for products if not available.",wraplength=350,font=('Liberation Sans',9,'normal'),fg="black",justify=LEFT)
    WarTable=ttk.Treeview(where,height=12)
    WarTable['show']='headings'
    WarTable["column"]=("InvID","MedID","StkLim","MfgDat","ExpDat")
    WarTable.column("InvID",width=50)
    WarTable.column("MedID",width=50)
    WarTable.column("StkLim",width=70)
    WarTable.column("MfgDat",width=100)
    WarTable.column("ExpDat",width=100)
    WarTable.heading("InvID",text="InvID")
    WarTable.heading("MedID",text="MedID")
    WarTable.heading("StkLim",text="StkLim")
    WarTable.heading("MfgDat",text="MfgDat")
    WarTable.heading("ExpDat",text="ExpDat")
    receiveDat.wipeTableStats(WarTable)
    for recs in receiveDat.getAllWarehouse():
        WarTable.insert('',0, text='', value = recs)
    WarTable.place(x=900,y=150)
    Describ.place(x=900,y=95)

def drawMedTable(where):
    def fetchInputs():
        searched=searchMed.get()
        receiveDat.wipeTableStats(MedTable)
        for recs in receiveDat.RefreshMedi(searched):
            MedTable.insert('',0, text='', value = recs)

    def OnlyAntiPytc():
        receiveDat.wipeTableStats(MedTable)
        for recs in receiveDat.ViewAntiPytc():
            MedTable.insert('',0, text='', value = recs)

    def OnlyAnalGesc():
        receiveDat.wipeTableStats(MedTable)
        for recs in receiveDat.ViewAnalGesc():
            MedTable.insert('',0, text='', value = recs)

    def OnlyAntiBiot():
        receiveDat.wipeTableStats(MedTable)
        for recs in receiveDat.ViewAntiBiot():
            MedTable.insert('',0, text='', value = recs)

    def OnlyAntiSept():
        receiveDat.wipeTableStats(MedTable)
        for recs in receiveDat.ViewAntiSept():
            MedTable.insert('',0, text='', value = recs)

    def OnlyMoodStab():
        receiveDat.wipeTableStats(MedTable)
        for recs in receiveDat.ViewMoodStab():
            MedTable.insert('',0, text='', value = recs)

    def OnlyStimulan():
        receiveDat.wipeTableStats(MedTable)
        for recs in receiveDat.ViewStimulan():
            MedTable.insert('',0, text='', value = recs)

    def OnlyTranquil():
        receiveDat.wipeTableStats(MedTable)
        for recs in receiveDat.ViewTranquil():
            MedTable.insert('',0, text='', value = recs)

    ShowAntiPytc=Button(where,font=("Liberation Sans",9,"bold"),text="ANTIPYRETICS",bg="green",bd=0,fg="white",width=19,command=OnlyAntiPytc,height=1).place(x=10,y=180)
    ShowAnalGesc=Button(where,font=("Liberation Sans",9,"bold"),text="ANALGESICS",bg="green",bd=0,fg="white",width=19,command=OnlyAnalGesc,height=1).place(x=10,y=210)
    ShowAntiBiot=Button(where,font=("Liberation Sans",9,"bold"),text="ANTIBIOTICS",bg="green",bd=0,fg="white",width=19,command=OnlyAntiBiot,height=1).place(x=10,y=240)
    ShowAntiSept=Button(where,font=("Liberation Sans",9,"bold"),text="ANTISEPTICS",bg="green",bd=0,fg="white",width=19,command=OnlyAntiSept,height=1).place(x=10,y=270)
    ShowMoodStab=Button(where,font=("Liberation Sans",9,"bold"),text="MOOD STABILIZERS",bg="green",bd=0,fg="white",width=19,command=OnlyMoodStab,height=1).place(x=10,y=300)
    ShowStimulan=Button(where,font=("Liberation Sans",9,"bold"),text="STIMULANTS",bg="green",bd=0,fg="white",width=19,command=OnlyStimulan,height=1).place(x=10,y=330)
    ShowTranquil=Button(where,font=("Liberation Sans",9,"bold"),text="TRANQUILIZERS",bg="green",bd=0,fg="white",width=19,command=OnlyTranquil,height=1).place(x=10,y=360)
    topmoText=Label(where,font=("Liberation Sans",20,"normal"),text="PharmaDB Store",bg="white",fg="green").place(x=10,y=10)
    searchMed=Entry(where,font=("Liberation Sans",20,"normal"),width=20,bd=1,fg="green")
    searchMed.place(x=730,y=10)
    searchBtn=Button(where,font=("Liberation Sans",16,"normal"),text="SEARCH CATALOG",fg="white",bg="green",command=fetchInputs,bd=0).place(x=1045,y=10)
    titleText=Label(where,font=("Liberation Sans",20,"normal"),text="Global Catalog",fg="green").place(x=180,y=60)
    Describ=Label(where,text="The following is a catalog of all pharmaceutical products available under our PharmaDB service. There may be some products which are not available at some warehouses.",wraplength=350,font=('Liberation Sans',9,'normal'),fg="black",justify=LEFT)
    MedTable=ttk.Treeview(where,height=26)
    MedTable['show'] = 'headings'
    MedTable["column"]=("MedID","Titles","TypeID","MfgrID","MfgDate","ExpDate","AntiPytc","AnalGesc","AntiBiot","AntiSept","MoodStab","Stimulan","Tranquil")
    MedTable.column("MedID",width=50)
    MedTable.column("Titles",width=150)
    MedTable.column("TypeID",width=50)
    MedTable.column("MfgrID",width=50)
    MedTable.column("MfgDate",width=100)
    MedTable.column("ExpDate",width=100)
    MedTable.column("AntiPytc",width=30)
    MedTable.column("AnalGesc",width=30)
    MedTable.column("AntiBiot",width=30)
    MedTable.column("AntiSept",width=30)
    MedTable.column("MoodStab",width=30)
    MedTable.column("Stimulan",width=30)
    MedTable.column("Tranquil",width=30)
    MedTable.heading("MedID",text="MedID")
    MedTable.heading("Titles",text="Medicine Name")
    MedTable.heading("TypeID",text="TypID")
    MedTable.heading("MfgrID",text="MfgID")
    MedTable.heading("MfgDate",text="MfgDate")
    MedTable.heading("ExpDate",text="ExpDate")
    MedTable.heading("AntiPytc",text="AP")
    MedTable.heading("AnalGesc",text="AG")
    MedTable.heading("AntiBiot",text="AB")
    MedTable.heading("AntiSept",text="AS")
    MedTable.heading("MoodStab",text="MS")
    MedTable.heading("Stimulan",text="ST")
    MedTable.heading("Tranquil",text="TQ")
    for recs in receiveDat.getAllMedicines():
        MedTable.insert('',0, text='', value = recs)
    MedTable.place(x=180,y=150)
    Describ.place(x=180,y=95)

def drawPurcInit(where):
    medName=Label(where,font=("Liberation Sans",20,"normal"),text="No Product Selected!",fg="green").place(x=0,y=0)
    AvlStat=Label(where,font=("Liberation Sans",9,"bold"),text="OUT OF STOCK",fg="red").place(x=0,y=35)
    mfgDesc=Label(where,font=("Liberation Sans",9,"bold"),text="Manufacturer Name",fg="black").place(x=0,y=55)
    typDesc=Label(where,font=("Liberation Sans",9,"bold"),text="Product Type",fg="black").place(x=0,y=75)
    mfgDtDs=Label(where,font=("Liberation Sans",9,"bold"),text="Manufacturing Date",fg="black").place(x=0,y=95)
    expDtDs=Label(where,font=("Liberation Sans",9,"bold"),text="Expiry Date",fg="black").place(x=0,y=115)
    medIDDs=Label(where,font=("Liberation Sans",9,"bold"),text="Medicine ID",fg="black").place(x=0,y=135)
    mfgIDDs=Label(where,font=("Liberation Sans",9,"bold"),text="Manufacturer ID",fg="black").place(x=0,y=155)
    invIDDs=Label(where,font=("Liberation Sans",9,"bold"),text="Inventory ID",fg="black").place(x=0,y=175)
    AvlNmDs=Label(where,font=("Liberation Sans",9,"bold"),text="Available Amount",fg="black").place(x=0,y=195)
    PriceDs=Label(where,font=("Liberation Sans",20,"normal"),text="Rs.",fg="black").place(x=0,y=215)
    mfgText=Label(where,font=("Liberation Sans",9,"normal"),text="Not Available",fg="black").place(x=150,y=55)
    typText=Label(where,font=("Liberation Sans",9,"normal"),text="Not Available",fg="black").place(x=150,y=75)
    mfgDtTx=Label(where,font=("Liberation Sans",9,"normal"),text="Not Available",fg="black").place(x=150,y=95)
    expDtTx=Label(where,font=("Liberation Sans",9,"normal"),text="Not Available",fg="black").place(x=150,y=115)
    medIDTx=Label(where,font=("Liberation Sans",9,"normal"),text="N/A",fg="black").place(x=150,y=135)
    mfgIDTx=Label(where,font=("Liberation Sans",9,"normal"),text="N/A",fg="black").place(x=150,y=155)
    invIDTx=Label(where,font=("Liberation Sans",9,"normal"),text="N/A",fg="black").place(x=150,y=175)
    AvlNmTx=Label(where,font=("Liberation Sans",9,"normal"),text="N/A",fg="black").place(x=150,y=195)
    PriceTx=Label(where,font=("Liberation Sans",20,"normal"),text="N/A",fg="black").place(x=45,y=215)

def displayIDNotFound(where,RequestID):
    Current=Frame(where,width=370,height=250,relief="raise")
    Current.place(x=900,y=445)
    medName=Label(Current,font=("Liberation Sans",20,"normal"),text="Invalid Product!",fg="green").place(x=0,y=0)
    AvlStat=Label(Current,font=("Liberation Sans",9,"bold"),text="PRODUCT NOT FOUND",fg="red").place(x=0,y=35)
    mfgDesc=Label(Current,font=("Liberation Sans",9,"bold"),text="Manufacturer Name",fg="black").place(x=0,y=55)
    typDesc=Label(Current,font=("Liberation Sans",9,"bold"),text="Product Type",fg="black").place(x=0,y=75)
    mfgDtDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Manufacturing Date",fg="black").place(x=0,y=95)
    expDtDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Expiry Date",fg="black").place(x=0,y=115)
    medIDDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Medicine ID",fg="black").place(x=0,y=135)
    mfgIDDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Manufacturer ID",fg="black").place(x=0,y=155)
    invIDDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Inventory ID",fg="black").place(x=0,y=175)
    AvlNmDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Available Amount",fg="black").place(x=0,y=195)
    PriceDs=Label(Current,font=("Liberation Sans",20,"normal"),text="Rs.",fg="black").place(x=0,y=215)
    mfgText=Label(Current,font=("Liberation Sans",9,"normal"),text="Not Available",fg="black").place(x=150,y=55)
    typText=Label(Current,font=("Liberation Sans",9,"normal"),text="Not Available",fg="black").place(x=150,y=75)
    mfgDtTx=Label(Current,font=("Liberation Sans",9,"normal"),text="Not Available",fg="black").place(x=150,y=95)
    expDtTx=Label(Current,font=("Liberation Sans",9,"normal"),text="Not Available",fg="black").place(x=150,y=115)
    medIDTx=Label(Current,font=("Liberation Sans",9,"normal"),text=RequestID,fg="black").place(x=150,y=135)
    mfgIDTx=Label(Current,font=("Liberation Sans",9,"normal"),text="N/A",fg="black").place(x=150,y=155)
    invIDTx=Label(Current,font=("Liberation Sans",9,"normal"),text="N/A",fg="black").place(x=150,y=175)
    AvlNmTx=Label(Current,font=("Liberation Sans",9,"normal"),text="N/A",fg="black").place(x=150,y=195)
    PriceTx=Label(Current,font=("Liberation Sans",20,"normal"),text="N/A",fg="black").place(x=45,y=215)

def displayIDAvlStock(where,RequestID,medNam,typNam,mfgDat,expDat,mfgrID,inveID,stkLim,mfgNam,medPri):
    def finalisePay():
        receiveDat.makePurch(medNam,medPri,RequestID)
        msgbox.showinfo("Purchase Successful","You purchased "+medNam+" from "+mfgNam+" for Rs. "+str(medPri)+". Your order will reach you within 5 working days.")
        print("We actually reach here!")

    Current=Frame(where,width=370,height=250,relief="raise")
    Current.place(x=900,y=445)
    medName=Label(Current,font=("Liberation Sans",20,"normal"),text=medNam,fg="green").place(x=0,y=0)
    AvlStat=Label(Current,font=("Liberation Sans",9,"bold"),text="AVAILABLE FOR PURCHASE",fg="green").place(x=0,y=35)
    mfgDesc=Label(Current,font=("Liberation Sans",9,"bold"),text="Manufacturer Name",fg="black").place(x=0,y=55)
    typDesc=Label(Current,font=("Liberation Sans",9,"bold"),text="Product Type",fg="black").place(x=0,y=75)
    mfgDtDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Manufacturing Date",fg="black").place(x=0,y=95)
    expDtDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Expiry Date",fg="black").place(x=0,y=115)
    medIDDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Medicine ID",fg="black").place(x=0,y=135)
    mfgIDDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Manufacturer ID",fg="black").place(x=0,y=155)
    invIDDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Inventory ID",fg="black").place(x=0,y=175)
    AvlNmDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Available Amount",fg="black").place(x=0,y=195)
    PriceDs=Label(Current,font=("Liberation Sans",20,"normal"),text="Rs.",fg="black").place(x=0,y=215)
    mfgText=Label(Current,font=("Liberation Sans",9,"normal"),text=mfgNam,fg="black").place(x=150,y=55)
    typText=Label(Current,font=("Liberation Sans",9,"normal"),text=typNam,fg="black").place(x=150,y=75)
    mfgDtTx=Label(Current,font=("Liberation Sans",9,"normal"),text=mfgDat,fg="black").place(x=150,y=95)
    expDtTx=Label(Current,font=("Liberation Sans",9,"normal"),text=expDat,fg="black").place(x=150,y=115)
    medIDTx=Label(Current,font=("Liberation Sans",9,"normal"),text=RequestID,fg="black").place(x=150,y=135)
    mfgIDTx=Label(Current,font=("Liberation Sans",9,"normal"),text=mfgrID,fg="black").place(x=150,y=155)
    invIDTx=Label(Current,font=("Liberation Sans",9,"normal"),text=inveID,fg="black").place(x=150,y=175)
    AvlNmTx=Label(Current,font=("Liberation Sans",9,"normal"),text=stkLim,fg="black").place(x=150,y=195)
    PriceTx=Label(Current,font=("Liberation Sans",20,"normal"),text=medPri,fg="black").place(x=45,y=215)
    PurcBtn=Button(Current,text="PURCHASE",font=("Liberation Sans",10,"bold"),bg="green",bd=0,fg="white",command=finalisePay,height=1).place(x=150,y=220)

def displayIDNotStock(where,RequestID,medNam,typNam,mfgDat,expDat,mfgrID,mfgNam,medPri):
    Current=Frame(where,width=370,height=250,relief="raise")
    Current.place(x=900,y=445)
    medName=Label(Current,font=("Liberation Sans",20,"normal"),text=medNam,fg="green").place(x=0,y=0)
    AvlStat=Label(Current,font=("Liberation Sans",9,"bold"),text="OUT OF STOCK",fg="red").place(x=0,y=35)
    mfgDesc=Label(Current,font=("Liberation Sans",9,"bold"),text="Manufacturer Name",fg="black").place(x=0,y=55)
    typDesc=Label(Current,font=("Liberation Sans",9,"bold"),text="Product Type",fg="black").place(x=0,y=75)
    mfgDtDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Manufacturing Date",fg="black").place(x=0,y=95)
    expDtDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Expiry Date",fg="black").place(x=0,y=115)
    medIDDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Medicine ID",fg="black").place(x=0,y=135)
    mfgIDDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Manufacturer ID",fg="black").place(x=0,y=155)
    invIDDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Inventory ID",fg="black").place(x=0,y=175)
    AvlNmDs=Label(Current,font=("Liberation Sans",9,"bold"),text="Available Amount",fg="black").place(x=0,y=195)
    PriceDs=Label(Current,font=("Liberation Sans",20,"normal"),text="Rs.",fg="black").place(x=0,y=215)
    mfgText=Label(Current,font=("Liberation Sans",9,"normal"),text=mfgNam,fg="black").place(x=150,y=55)
    typText=Label(Current,font=("Liberation Sans",9,"normal"),text=typNam,fg="black").place(x=150,y=75)
    mfgDtTx=Label(Current,font=("Liberation Sans",9,"normal"),text=mfgDat,fg="black").place(x=150,y=95)
    expDtTx=Label(Current,font=("Liberation Sans",9,"normal"),text=expDat,fg="black").place(x=150,y=115)
    medIDTx=Label(Current,font=("Liberation Sans",9,"normal"),text=RequestID,fg="black").place(x=150,y=135)
    mfgIDTx=Label(Current,font=("Liberation Sans",9,"normal"),text=mfgrID,fg="black").place(x=150,y=155)
    invIDTx=Label(Current,font=("Liberation Sans",9,"normal"),text="Not Available",fg="black").place(x=150,y=175)
    AvlNmTx=Label(Current,font=("Liberation Sans",9,"normal"),text="N/A",fg="black").place(x=150,y=195)
    PriceTx=Label(Current,font=("Liberation Sans",20,"normal"),text=medPri,fg="black").place(x=45,y=215)

def drawPurchase(where):
    def fetchInputs():
        RequestID=MedIDBox.get()
        if RequestID not in receiveDat.getIDfromMeds():
            displayIDNotFound(where,RequestID)
        if RequestID in receiveDat.getIDfromMeds():
            if RequestID not in receiveDat.getIDfromWare():
                medNam=receiveDat.getMedNam(RequestID)
                typNam=receiveDat.getTypNam(RequestID)
                mfgDat=receiveDat.getMfgDat(RequestID)
                expDat=receiveDat.getExpDat(RequestID)
                mfgrID=receiveDat.getMfgrID(RequestID)
                #inveID=receiveDat.getInveID(RequestID)
                #stkLim=receiveDat.getStkLim(RequestID)
                mfgNam=receiveDat.getMfgNam(RequestID)
                medPri=receiveDat.getMedPri(RequestID)
                print(medNam,typNam,mfgDat,expDat,mfgrID,mfgNam,medPri)
                displayIDNotStock(where,RequestID,medNam,typNam,mfgDat,expDat,mfgrID,mfgNam,medPri)
        if RequestID in receiveDat.getIDfromMeds():
            if RequestID in receiveDat.getIDfromWare():
                medNam=receiveDat.getMedNam(RequestID)
                typNam=receiveDat.getTypNam(RequestID)
                mfgDat=receiveDat.getMfgDat(RequestID)
                expDat=receiveDat.getExpDat(RequestID)
                mfgrID=receiveDat.getMfgrID(RequestID)
                inveID=receiveDat.getInveID(RequestID)
                stkLim=receiveDat.getStkLim(RequestID)
                mfgNam=receiveDat.getMfgNam(RequestID)
                medPri=receiveDat.getMedPri(RequestID)
                print(medNam,typNam,mfgDat,expDat,mfgrID,inveID,stkLim,mfgNam,medPri)
                displayIDAvlStock(where,RequestID,medNam,typNam,mfgDat,expDat,mfgrID,inveID,stkLim,mfgNam,medPri)
    Workspace=Frame(where,width=370,height=250,relief="raise")
    Workspace.place(x=900,y=445)
    MedIDTex=Label(where,font=("Liberation Sans",9,"bold"),text="Enter your product ID",fg="black").place(x=900,y=420)
    MedIDBox=Entry(where,font=("Liberation Sans",9,"normal"),width=25,fg="black")
    MedIDBox.place(x=1040,y=419)
    DetailBt=Button(where,font=("Liberation Sans",4,"bold"),text="GO",bd=0,fg="white",bg="green",command=fetchInputs).place(x=1235,y=419)
    drawPurcInit(Workspace)

def ProdCatalog(where,user):
    UparBar=Frame(where,width=1280,height=58,bd=0,relief="raise",bg="white")
    TopBond=Frame(where,width=1280,height=2,bd=0,relief="raise",bg="green")
    WorkSpc=Frame(where,width=1280,height=640,bd=0,relief="sunken")
    StatBar=Frame(where,width=1280,height=20,bd=0,relief="raise",bg="green")
    UparBar.pack(side=TOP)
    TopBond.pack(side=TOP)
    StatBar.pack(side=BOTTOM)
    WorkSpc.pack(side=LEFT)
    drawMedTable(where)
    drawWarTable(where)
    drawOptPlace(where,user)
    drawPurchase(where)

def LoginScreen(where):
    def GetUsrAndPwd():
        UserName=UsrNamBox.get()
        PassWord=PwdNamBox.get()
        try:
            TryToExe="select StorePass from TestUserCreds where StoreUser='"+UserName+"'"
            curs.execute(TryToExe)
            VerifySt=curs.fetchall()
            if UserName not in receiveDat.getUserList():
                msgbox.showinfo("Login Failed","The entered username does not exist in the database. You might want to request access from the administrator.")
            else:
                if (PassWord==VerifySt[0][0]):
                    msgbox.showinfo("Login Successful","Welcome to PharmaDB Store "+UserName+"!")
                    BackOne.destroy()
                    BackTwo.destroy()
                    ConArea.destroy()
                    print(UserName, "has logged in!")
                    ProdCatalog(where,UserName)
                else:
                    msgbox.showinfo("Login Failed","The entered password is wrong. Correct your entry and try again.")
                    print("Login failed!")
        except Exception as e:
            msgbox.showinfo("Login Failed","The application could not contact the database. "+str(e))
    BackOne=Frame(where,width=1280,height=250,bd=0,relief="raise",bg="green")
    BackTwo=Frame(where,width=1280,height=270,bd=0,relief="raise",bg="green")
    ConArea=Frame(where,width=1280,height=200,bd=0,relief="sunken")
    BackOne.pack(side=TOP)
    BackTwo.pack(side=BOTTOM)
    ConArea.pack(side=LEFT)
    Welcome=Label(ConArea,font=("Liberation Sans",20,"normal"),fg="green",text="PharmaDB Store").place(x=200,y=50)
    LoginTe=Label(ConArea,font=("Liberation Sans",20,"normal"),fg="green",text="Login Now").place(x=700,y=50)
    Describ=Label(ConArea,text="PharmaDB is a dsitributed repository of pharmaceutical products available across the globe giving you the opportunity of handling purchase of medicines on-the-go and putting your products on sale without any hassles. Welcome to PharmaDB!",wraplength=450,font=('Liberation Sans',9,'normal'),fg="black",justify=LEFT)
    UsrNamTex=Label(ConArea,font=("Liberation Sans",9,"normal"),fg="black",text="Username").place(x=700,y=90)
    UsrNamBox=Entry(ConArea,font=("Liberation Sans",9,"normal"),width=20)
    PwdNamTex=Label(ConArea,font=("Liberation Sans",9,"normal"),fg="black",text="Password").place(x=700,y=115)
    PwdNamBox=Entry(ConArea,font=("Liberation Sans",9,"normal"),width=20)
    LogNowBtn=Button(ConArea,text="LOGIN",font=("Liberation Sans",10,"bold"),bg="green",fg="white",command=GetUsrAndPwd,width=12,height=2)
    LogNowBtn.place(x=930,y=90)
    UsrNamBox.place(x=770,y=90)
    PwdNamBox.place(x=770,y=115)
    Describ.place(x=200,y=90)