        ################################           library
from tkinter import *
# from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
        ################################        class
class PharmacyMangementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1270x700+0+0")
        ############### add medicine variable####
        self.addmed_var=StringVar()
        self.refMed_var=StringVar()
#################################################
        lbltitle=Label(self.root,text="Pharmacy Management System",
                            bd=15,relief=RIDGE,bg='SpringGreen4',fg='white',font=('times new roman',50,'bold'),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)
        #################################          image
        img1=Image.config('D:\python\projects\imp\PH.png')
        img1=img1.resize((80,80),Image.ANTIALIAS)
        # self.photoimg1=ImageTk.PhotoImage(img1)
        btn1=Button(self.root,image=self.photoimg1,borderwidth=0)
        btn1.place(x=50,y=15)
        ########################  MAIN    DATA  FRAME        ####
        dataframe=Frame(self.root,bd=6,relief=RIDGE,padx=20,bg='linen')
        dataframe.place(x=0,y=120,width=1270,height=350)
        #########################     left frame
        dataframeleft=LabelFrame(dataframe,bd=2,relief=RIDGE,padx=20,
                         text='MEDICINE INFORMATION',bg='linen',fg='tan4',font=('arial',12,'bold'))
        dataframeleft.place(x=0,y=0,width=740,height=340)
######################################### ref no.
        reflabel=Label(dataframeleft,text='Refrance No.',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        reflabel.place(x=0,y=0,width=150,height=25)

        conn=mysql.connector.connect(host='localhost',username='root',password='sushant@12345678',database='studentmanagementsystem1')
        my_cursor=conn.cursor()
        my_cursor.execute('select Ref from pharma')
        reff=my_cursor.fetchall()

        ref_combo=ttk.Combobox(dataframeleft,width=20,font=('arial',10,'bold'),state='readonly')
        ref_combo['values']=reff
        ref_combo.current(0)
        ref_combo.place(x=155,y=0,width=200,height=25)
#######################################################
        complabel=Label(dataframeleft,text='Company Name ',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        complabel.place(x=0,y=35,width=150,height=25)
        compentry=Entry(dataframeleft,font=('arial',10,'bold'))
        compentry.place(x=155,y=35,width=200,height=25)
########################################################
        typlabel=Label(dataframeleft,text='Type of Medicine ',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        typlabel.place(x=0,y=70,width=150,height=25)
        typ_combo=ttk.Combobox(dataframeleft,width=20,font=('arial',10,'bold'),state='readonly')
        typ_combo['values']=('Tablet','Liquid','Capsule','Topical Medicine','Suppositorie','Drop','Inhaler','Injection','Implants')
        typ_combo.place(x=155,y=70,width=200,height=25)
        typ_combo.current(0)
########################################################
        medlabel=Label(dataframeleft,text='Medicine Name',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        medlabel.place(x=0,y=105,width=150,height=25)
        
        conn=mysql.connector.connect(host='localhost',username='root',password='sushant@12345678',database='studentmanagementsystem1')
        my_cursor=conn.cursor()
        my_cursor.execute('select MedName from pharma')
        med=my_cursor.fetchall()
        
        med_combo=ttk.Combobox(dataframeleft,width=20,font=('arial',10,'bold'),state='readonly')
        med_combo['values']=med
        med_combo.place(x=155,y=105,width=200,height=25)
        med_combo.current(0)
#########################################################
        lotlabel=Label(dataframeleft,text='Lot No. ',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        lotlabel.place(x=0,y=140,width=150,height=25)
        lotentry=Entry(dataframeleft,font=('arial',10,'bold'))
        lotentry.place(x=155,y=140,width=200,height=25)

        issulabel=Label(dataframeleft,text='Issue Date',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        issulabel.place(x=0,y=175,width=150,height=25)
        issuentry=Entry(dataframeleft,font=('arial',10,'bold'))
        issuentry.place(x=155,y=175,width=200,height=25)

        EXPlabel=Label(dataframeleft,text='EXP Date ',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        EXPlabel.place(x=0,y=210,width=150,height=25)
        EXPentry=Entry(dataframeleft,font=('arial',10,'bold'))
        EXPentry.place(x=155,y=210,width=200,height=25)

        useslabel=Label(dataframeleft,text='Uses ',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        useslabel.place(x=0,y=245,width=150,height=25)
        usesentry=Entry(dataframeleft,font=('arial',10,'bold'))
        usesentry.place(x=155,y=245,width=200,height=25)

        sidelabel=Label(dataframeleft,text='Side Effect ',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        sidelabel.place(x=0,y=280,width=150,height=25)
        sideentry=Entry(dataframeleft,font=('arial',10,'bold'))
        sideentry.place(x=155,y=280,width=200,height=25)

        warnlabel=Label(dataframeleft,text='Prec & Warning ',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        warnlabel.place(x=370,y=0,width=140,height=25)
        warnentry=Entry(dataframeleft,font=('arial',10,'bold'))
        warnentry.place(x=515,y=0,width=200,height=25)

        doselabel=Label(dataframeleft,text='Dosage ',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        doselabel.place(x=370,y=35,width=140,height=25)
        doseentry=Entry(dataframeleft,font=('arial',10,'bold'))
        doseentry.place(x=515,y=35,width=200,height=25)

        pricelabel=Label(dataframeleft,text='Tablet Price ',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        pricelabel.place(x=370,y=70,width=140,height=25)
        priceentry=Entry(dataframeleft,font=('arial',10,'bold'))
        priceentry.place(x=515,y=70,width=200,height=25)

        QTlabel=Label(dataframeleft,text='Product QT',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        QTlabel.place(x=370,y=105,width=140,height=25)
        QTentry=Entry(dataframeleft,font=('arial',10,'bold'))
        QTentry.place(x=515,y=105,width=200,height=25)

        ########################       right frame
        dataframeright=LabelFrame(dataframe,bd=2,relief=RIDGE,padx=20,bg='linen',
                         text=' ADD MEDICINE',fg='tan4',font=('arial',12,'bold'))
        dataframeright.place(x=760,y=0,width=450,height=340)
        
        doselabel=Label(dataframeright,text='Refrance No.',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        doselabel.place(x=0,y=0,width=150,height=25)
        doseentry=Entry(dataframeright,textvariable=self.refMed_var,font=('arial',10,'bold'))
        doseentry.place(x=155,y=0,width=200,height=25)

        pricelabel=Label(dataframeright,text='Medicine Name ',font=('arial',10,'bold'),bg="misty rose3",anchor='w')
        pricelabel.place(x=0,y=35,width=150,height=25)
        priceentry=Entry(dataframeright,textvariable=self.addmed_var,font=('arial',10,'bold'))
        priceentry.place(x=155,y=35,width=200,height=25)
        ######################      sub frame
        subframe=Frame(dataframeright,bd=5,relief=RIDGE,bg='white')
        subframe.place(x=0,y=70,width=250,height=220)
        
        #####################      scroll bar
        scrolls_x =ttk.Scrollbar(subframe,orient=HORIZONTAL)
        scrolls_x.pack(side=BOTTOM,fill=X)
        scrolls_y =ttk.Scrollbar(subframe,orient=VERTICAL)
        scrolls_y.pack(side=RIGHT,fill=Y)

        ########################    table tree view
        self.medicine_table=ttk.Treeview(subframe,column=('REF','MEDICINE'),xscrollcommand=scrolls_x.set,yscrollcommand=scrolls_y.set)
        self.medicine_table.heading('REF',text='REF')
        self.medicine_table.heading('MEDICINE',text='MEDICINE NAME')

        self.medicine_table['show']='headings'
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column('REF',width=100)
        self.medicine_table.column('MEDICINE',width=100)

        self.medicine_table.bind('<ButtonRelease-1>',self.MedGet_cursor)
        
        scrolls_x.config(command=self.medicine_table.xview)
        scrolls_y.config(command=self.medicine_table.xview)
        #################### button frame in right frame
        subframe=Frame(dataframeright,bd=5,relief=RIDGE,bg='black')
        subframe.place(x=255,y=170,width=159,height=120)
        ######################### buttons in button frame in right frame
        addbtn=Button(subframe,text='ADD',font=('arial',10,'bold'),bg='SpringGreen4',command=self.AddMed
                      ,fg='black',activebackground='black',activeforeground='gold')
        addbtn.place(x=0,y=0,width=150)

        updatebtn=Button(subframe,text='UPDATE',font=('arial',10,'bold'),bg='SpringGreen4',fg='black',activebackground='black',activeforeground='gold')
        updatebtn.place(x=0,y=27,width=150)

        deletebtn=Button(subframe,text='DELETE',font=('arial',10,'bold'),bg='red',fg='black',activebackground='black',activeforeground='gold')
        deletebtn.place(x=0,y=54,width=150)

        clearbtn=Button(subframe,text='CLEAR',font=('arial',10,'bold'),bg='SpringGreen4',fg='black',activebackground='black',activeforeground='gold')
        clearbtn.place(x=0,y=81,width=150)
        ################### button frame
        btnframe=Frame(self.root,bd=8,relief=RIDGE,bg='white')
        btnframe.place(x=0,y=468,width=1270,height=45)
        ########################### buttons in btn frame
        addbtn=Button(btnframe,text='ADD MEDICINE',font=('arial',10,'bold'),bg='SpringGreen4',fg='black',activebackground='black',activeforeground='gold')
        addbtn.place(x=0,y=0,width=150)
        updatebtn=Button(btnframe,text='UPDATE',font=('arial',10,'bold'),bg='SpringGreen4',fg='black',activebackground='black',activeforeground='gold')
        updatebtn.place(x=150,y=0,width=100)
        delbtn=Button(btnframe,text='DELETE',font=('arial',10,'bold'),bg='red',fg='black',activebackground='black',activeforeground='gold')
        delbtn.place(x=250,y=0,width=100)
        resetbtn=Button(btnframe,text='RESET',font=('arial',10,'bold'),bg='SpringGreen4',fg='black',activebackground='black',activeforeground='gold')
        resetbtn.place(x=350,y=0,width=100)
        exitbtn=Button(btnframe,text='EXIT',font=('arial',10,'bold'),bg='SpringGreen4',fg='black',activebackground='black',activeforeground='gold')
        exitbtn.place(x=450,y=0,width=100)       
        searchbtn=Button(btnframe,text='SEARCH',font=('arial',10,'bold'),bg='SpringGreen4',fg='black',activebackground='black',activeforeground='gold')
        searchbtn.place(x=954,y=0,width=150)
        showbtn=Button(btnframe,text='SHOW ALL',font=('arial',10,'bold'),bg='SpringGreen4',fg='black',activebackground='black',activeforeground='gold')
        showbtn.place(x=1104,y=0,width=150)   
        ###########################  Search 
        srchlablel=Label(btnframe,font=('arial',10,'bold'),text='SEARCH BY',bg='coral',fg='dark blue')
        srchlablel.place(x=550,y=1,height=27)
        srch_combo=ttk.Combobox(btnframe,width=12,font=('arial',10,'bold'),state='readonly')
        srch_combo['values']=('REF','MEDICINE NAME','LOT')
        srch_combo.place(x=631,y=1,height=27)
        srch_combo.current(0)    
        txtsrch=Entry(btnframe,font=('arial',10,'bold'),width=30)
        txtsrch.place(x=740,y=1,height=27)
        ######################  detail frame
        detailframe=Frame(self.root,bd=5,relief=RIDGE,bg='white')
        detailframe.place(x=0,y=510,width=1270,height=190)

        scrolls_x =ttk.Scrollbar(detailframe,orient=HORIZONTAL)
        scrolls_x.pack(side=BOTTOM,fill=X)
        scrolls_y =ttk.Scrollbar(detailframe,orient=VERTICAL)
        scrolls_y.pack(side=RIGHT,fill=Y)

        self.detailframe=ttk.Treeview(detailframe,column=('reg','companyname','type','tabletname','lotno','issuedate',
        'expdate','uses','sideeffect','warning','dosage','price','productqt'),xscrollcommand=scrolls_x.set,yscrollcommand=scrolls_y.set)
        
        scrolls_x.pack(side=BOTTOM,fill=X)
        scrolls_y.pack(side=RIGHT,fill=Y)

        scrolls_x.config(command=self.detailframe.xview)
        scrolls_y.config(command=self.detailframe.yview)

        self.detailframe['show']='headings'

        self.detailframe.heading('reg',text='Reafrance No')
        self.detailframe.heading('companyname',text='Company Name')
        self.detailframe.heading('type',text='Type of Medicine')
        self.detailframe.heading('tabletname',text='Tablet Name')
        self.detailframe.heading('lotno',text='Lot No.')
        self.detailframe.heading('issuedate',text='Issue Date')
        self.detailframe.heading('expdate',text='EXP Date')
        self.detailframe.heading('uses',text='Uses')
        self.detailframe.heading('sideeffect',text='Side Effect')
        self.detailframe.heading('warning',text='Prec & Warning')
        self.detailframe.heading('dosage',text='Dosage')
        self.detailframe.heading('price',text='Price')
        self.detailframe.heading('productqt',text='Product Qty')
        self.detailframe.pack(fill=BOTH,expand=1)
        
        self.detailframe.column('reg',width=100)
        self.detailframe.column('companyname',width=100)
        self.detailframe.column('type',width=100)
        self.detailframe.column('tabletname',width=100)
        self.detailframe.column('lotno',width=100)
        self.detailframe.column('issuedate',width=100)
        self.detailframe.column('expdate',width=100)
        self.detailframe.column('uses',width=100)
        self.detailframe.column('sideeffect',width=100)
        self.detailframe.column('warning',width=100)
        self.detailframe.column('dosage',width=100)
        self.detailframe.column('price',width=100)
        self.detailframe.column('productqt',width=100)
        self.fetch_dataMed()
############################################################### Add Medicine Funtionality
    def AddMed(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='sushant@12345678',database='studentmanagementsystem1')
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                                                                          self.refMed_var.get(),
                                                                          self.addmed_var.get()                                      
                                       ))
        conn.commit()
        self.fetch_dataMed()
        self.MedGet_cursor()
        conn.close()
        messagebox.showinfo("Notification","Medicine Added successfully")  

    def fetch_dataMed(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='sushant@12345678',
                                       database='studentmanagementsystem1')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close     
#########################################med get cursor    ############################
    def MedGet_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item
        row=content['values']
        self.refMed_var.set(row[0])    
        self.addmed_var.set(row[1])




if __name__ == "__main__":
    root=Tk()
    obj=PharmacyMangementSystem(root)
    root.mainloop()








