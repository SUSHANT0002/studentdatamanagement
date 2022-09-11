##############################imported libraries
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
import random
import pandas
##############################################main frame
root = Tk()
root.title('student management system')
root.geometry('1000x600+150+50')
root.configure(bg='ivory3')
root.iconbitmap('image.ico')
root.resizable(False,False)
##########################################################################1st frame with buttons
DataEntryFrame = Frame(root,bg='peach puff',relief=RIDGE,borderwidt=2,bd=5)
DataEntryFrame.place(width=570,height=500,x=20,y=50)

##############################################################################function for 1st frame addstudent
def addstudent():
    def submitadd():
       ID = IDval.get()
       sname = snameval.get()
       contact = contactval.get()
       email = emailval.get()
       address = addressval.get()
       gender = genderval.get()
       dob = dobval.get()
       addedtime = time.strftime('%H:%M:%S')
       addeddate = time.strftime('%d/%m/%Y')
       try:
           strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
           mycursor.execute(strr,(ID,sname,contact,email,address,gender,dob,addeddate,addedtime))
           con.commit()
           res = messagebox.askyesnocancel('Notification','ID{} sname{} added successfully . Do you  want to clean form '.format(ID,sname),parent=addroot)
           if (res == True):
               IDval.set('')
               snameval.set('')
               contactval.set('')
               emailval.set('')
               addressval.set('')
               genderval.set('')
               dobval.set('')
       except:
           messagebox.showerror('Notifications','ID already Exist try another Id',parent=addroot)
       strr = 'select * from studentdata'
       mycursor.execute(strr)
       datas = mycursor.fetchall()
       StudentTable.delete(*StudentTable.get_children())
       for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],]
            StudentTable.insert('',END,values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('400x450+220+140')
    addroot.title('ADD STUDENT')
    addroot.config(bg='LemonChiffon3')
    addroot.iconbitmap('image.ico')
    addroot.resizable(False,False)
##########################################################################lables in addroot
    ID=Label(addroot, text='1.Enter ID ', bd=5, font=('ariel', 13, "italic bold"), width=15, bg='alice blue'
                 ,activebackground='white', activeforeground='black',anchor='w')
    ID.place(x=0,y=10)
    sname = Label(addroot, text='2.Enter Name ', bd=5, font=('ariel', 13, "italic bold"), width=15, bg='alice blue'
                  , activebackground='white', activeforeground='black',anchor='w')
    sname.place(x=0, y=70)
    contact = Label(addroot, text='3.Enter Contact ', bd=5, font=('ariel', 13, "italic bold"), width=15, bg='alice blue'
                  , activebackground='white', activeforeground='black',anchor='w')
    contact.place(x=0, y=130)
    email = Label(addroot, text='4.Enter E-MAIL ', bd=5, font=('ariel', 13, "italic bold"), width=15,
                  bg='alice blue', activebackground='white', activeforeground='black', anchor='w')
    email.place(x=0, y=190)
    address = Label(addroot, text='5.Enter Address ', bd=5, font=('ariel',13, "italic bold"), width=15, bg= 'alice blue'
                  , activebackground='white', activeforeground='black',anchor='w')
    address.place(x=0, y=250)
    gender = Label(addroot, text='6.Enter Gender ', bd=5, font=('ariel', 13, "italic bold"), width=15, bg='alice blue'
                  , activebackground='white', activeforeground='black',anchor='w')
    gender.place(x=0, y=310)
    dob = Label(addroot, text='7.Enter D.O.B ', bd=5, font=('ariel', 13, "italic bold"), width=15, bg='alice blue'
                  , activebackground='white', activeforeground='black',anchor='w')
    dob.place(x=0, y=370)
    submitbtn = Button(addroot, text='S  U  B  M  I  T', bd=5, font=('times', 10, "italic bold"), width=25, bg='MediumPurple3',
                       activebackground='black', activeforeground='white',command=submitadd)
    submitbtn.place(x=100, y=410)
######################################################################################entry box for labels in addroot
    IDval=StringVar()
    snameval = StringVar()
    contactval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    ID = Entry(addroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3',textvariable=IDval)
    ID.place(x=180, y=15)
    sname = Entry(addroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3',textvariable=snameval)
    sname.place(x=180, y=75)
    contact = Entry(addroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3',textvariable=contactval)
    contact.place(x=180, y=135)
    email = Entry(addroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3',textvariable=emailval)
    email.place(x=180, y=195)
    address = Entry(addroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3',textvariable=addressval)
    address.place(x=180, y=255)
    gender = Entry(addroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3',textvariable=genderval)
    gender.place(x=180, y=315)
    dob = Entry(addroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3',textvariable=dobval)
    dob.place(x=180, y=375)
    addroot.mainloop()
##########################################################################function of 1st frame search button
def searchstudent():
    def submitsearch():
        ID = IDval.get()
        sname = snameval.get()
        contact = contactval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime('%d/%m/%Y')
        if   (ID !=''):
            strr = 'select * from studentdata where ID=%s '
            mycursor.execute(strr,(ID))
            datas = mycursor.fetchall()
            StudentTable.delete(*StudentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], ]
                StudentTable.insert('', END, values=vv)
        elif (sname != ''):
            strr = 'select * from studentdata where name=%s '
            mycursor.execute(strr, (sname))
            datas = mycursor.fetchall()
            StudentTable.delete(*StudentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], ]
                StudentTable.insert('', END, values=vv)
        elif (contact != ''):
            strr = 'select * from studentdata where mobile=%s '
            mycursor.execute(strr, (contact))
            datas = mycursor.fetchall()
            StudentTable.delete(*StudentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], ]
                StudentTable.insert('', END, values=vv)
        elif (email != ''):
            strr = 'select * from studentdata where email=%s '
            mycursor.execute(strr, email )
            datas = mycursor.fetchall()
            StudentTable.delete(*StudentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], ]
                StudentTable.insert('', END, values=vv)
        elif (address != ''):
            strr = 'select * from studentdata where address=%s '
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            StudentTable.delete(*StudentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], ]
                StudentTable.insert('', END, values=vv)
        elif (gender != ''):
            strr = 'select * from studentdata where gender=%s '
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            StudentTable.delete(*StudentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], ]
                StudentTable.insert('', END, values=vv)
        elif (dob != ''):
            strr = 'select * from studentdata where dob=%s '
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            StudentTable.delete(*StudentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], ]
                StudentTable.insert('', END, values=vv)
        elif (addeddate != ''):
            strr = 'select * from studentdata where addeddate=%s '
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            StudentTable.delete(*StudentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], ]
                StudentTable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('400x530+220+70')
    searchroot.title('SEARCH STUDENT')
    searchroot.config(bg='LemonChiffon3')
    searchroot.iconbitmap('image.ico')
    searchroot.resizable(False, False)
    ##########################################################################lables in searchroot
    ID = Label(searchroot, text='1.Enter ID ', bd=5, font=('ariel', 13, "italic bold"), width=15, bg='alice blue'
               , activebackground='white', activeforeground='black', anchor='w')
    ID.place(x=0, y=10)
    sname = Label(searchroot, text='2.Enter Name ', bd=5, font=('ariel', 13, "italic bold"), width=15,bg='alice blue'
    , activebackground='white', activeforeground='black', anchor='w')
    sname.place(x=0, y=70)
    contact = Label(searchroot, text='3.Enter Contact ', bd=5, font=('ariel', 13, "italic bold"), width=15,bg='alice blue'
                    , activebackground='white', activeforeground='black', anchor='w')
    contact.place(x=0, y=130)
    email = Label(searchroot, text='4.Enter E-MAIL ', bd=5, font=('ariel', 13, "italic bold"), width=13,
                  bg='alice blue', activebackground='white', activeforeground='black', anchor='w')
    email.place(x=0, y=190)
    address = Label(searchroot, text='5.Enter Address ', bd=5, font=('ariel', 13, "italic bold"), width=15, bg='alice blue'
                     , activebackground='white', activeforeground='black', anchor='w')
    address.place(x=0, y=250)
    gender = Label(searchroot, text='6.Enter Gender ', bd=5, font=('ariel', 13, "italic bold"), width=15,
                   bg='alice blue', activebackground='white', activeforeground='black', anchor='w')
    gender.place(x=0, y=310)
    dob = Label(searchroot, text='7.Enter D.O.B ', bd=5, font=('ariel', 13, "italic bold"), width=15,bg='alice blue'
                , activebackground='white', activeforeground='black', anchor='w')
    dob.place(x=0, y=370)
    date = Label(searchroot, text='8.Enter Date ', bd=5, font=('ariel', 13, "italic bold"), width=15, bg= 'alice blue'
                      , activebackground='white', activeforeground='black', anchor='w')
    date.place(x=0, y=430)
    searchbtn = Button(searchroot, text='S E A R C H', bd=5, font=('times', 10, "italic bold"), width=25,
                       bg='MediumPurple3',activebackground='black', activeforeground='white', command=submitsearch)
    searchbtn.place(x=100, y=495)
    ######################################################################################entry box for labels in searchroot
    IDval = StringVar()
    snameval = StringVar()
    contactval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval=StringVar()

    ID = Entry(searchroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=IDval)
    ID.place(x=180, y=15)
    sname = Entry(searchroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=snameval)
    sname.place(x=180, y=75)
    contact = Entry(searchroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=contactval)
    contact.place(x=180, y=135)
    email = Entry(searchroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=emailval)
    email.place(x=180, y=195)
    address = Entry(searchroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=addressval)
    address.place(x=180, y=255)
    gender = Entry(searchroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=genderval)
    gender.place(x=180, y=315)
    dob = Entry(searchroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=dobval)
    dob.place(x=180, y=375)
    date = Entry(searchroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=dateval)
    date.place(x=180, y=435)
    searchroot.mainloop()
####################################################################function of 1st frame delete button
def deletestudent():
    cc = StudentTable.focus()
    content = StudentTable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata where ID=%s '
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','ID{} deleted successfully.....'.format(pp))

    strr = 'select *from studentdata '
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    StudentTable.delete(*StudentTable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], ]
        StudentTable.insert('', END, values=vv)
##########################################################################function of 1st update search button
def updatestudent():
    def update():
        ID = IDval.get()
        sname = snameval.get()
        contact = contactval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()
        strr = 'update studentdata set name=%s,mobile=%s ,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where ID=%s'
        mycursor.execute(strr,(sname,contact,email,address,gender,dob,date,time,ID))
        con.commit()
        messagebox.showinfo('Notification','ID{} updated successfully.....'.format(ID),parent=updateroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        StudentTable.delete(*StudentTable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], ]
            StudentTable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('400x570+220+80')
    updateroot.title('UPDATE STUDENT')
    updateroot.config(bg='LemonChiffon3')
    updateroot.iconbitmap('image.ico')
    updateroot.resizable(False, False)
    ##########################################################################lables in updateroot
    ID = Label(updateroot, text='1.Update ID ', bd=5, font=('ariel', 13, "italic bold"), width=15, bg='alice blue'
        , activebackground='white', activeforeground='black', anchor='w')
    ID.place(x=0, y=10)
    sname = Label(updateroot, text='2.Update Name ', bd=5, font=('ariel', 13, "italic bold"), width=15,bg='alice blue'
                 , activebackground='white', activeforeground='black', anchor='w')
    sname.place(x=0, y=70)
    contact = Label(updateroot, text='3.Update Contact ', bd=5, font=('ariel', 13, "italic bold"), width=15,bg='alice blue'
                    , activebackground='white', activeforeground='black', anchor='w')
    contact.place(x=0, y=130)
    email = Label(updateroot, text='4.Update E-MAIL ', bd=5, font=('ariel', 13, "italic bold"), width=15,
                  bg='alice blue', activebackground='white', activeforeground='black', anchor='w')
    email.place(x=0, y=190)
    address = Label(updateroot, text='5.Update Address ', bd=5, font=('ariel', 13, "italic bold"), width=15,bg='alice blue'
                    , activebackground='white', activeforeground='black', anchor='w')
    address.place(x=0, y=250)
    gender = Label(updateroot, text='6.Update Gender ', bd=5, font=('ariel', 13, "italic bold"), width=15,
                   bg='alice blue', activebackground='white', activeforeground='black', anchor='w')
    gender.place(x=0, y=310)
    dob = Label(updateroot, text='7.Update D.O.B ', bd=5, font=('ariel', 13, "italic bold"), width=15,bg='alice blue'
            , activebackground='white', activeforeground='black', anchor='w')
    dob.place(x=0, y=370)
    date = Label(updateroot, text='8.Update Date ', bd=5, font=('ariel', 13, "italic bold"), width=15,bg='alice blue'
                 , activebackground='white', activeforeground='black', anchor='w')
    date.place(x=0, y=430)
    time = Label(updateroot, text='9.Update Time ', bd=5, font=('ariel', 13, "italic bold"), width=15,bg= 'alice blue'
                 , activebackground='white', activeforeground='black', anchor='w')
    time.place(x=0, y=490)

    ######################################################################################entry box for labels in updateroot
    IDval = StringVar()
    snameval = StringVar()
    contactval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    ID = Entry(updateroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=IDval)
    ID.place(x=180, y=15)
    sname = Entry(updateroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=snameval)
    sname.place(x=180, y=75)
    contact = Entry(updateroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=contactval)
    contact.place(x=180, y=135)
    email = Entry(updateroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=emailval)
    email.place(x=180, y=195)
    address = Entry(updateroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=addressval)
    address.place(x=180, y=255)
    gender = Entry(updateroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=genderval)
    gender.place(x=180, y=315)
    dob = Entry(updateroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=dobval)
    dob.place(x=180, y=375)
    date = Entry(updateroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=dateval)
    date.place(x=180, y=435)
    time = Entry(updateroot, font=('ariel', 15, 'bold'), width=18, bg='ivory3', textvariable=timeval)
    time.place(x=180, y=495)
    updatebtn = Button(updateroot, text='U P D A T E', bd=5, font=('times', 10, "italic bold"), width=25,
                       bg='MediumPurple3', activebackground='black', activeforeground='white', command=update)
    updatebtn.place(x=100, y=530)
    cc = StudentTable.focus()
    content = StudentTable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        IDval.set(pp[0])
        snameval.set(pp[1])
        contactval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()
##########################################################################function of 1st frame show button
def showstudent():
    strr = 'select *from studentdata '
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    StudentTable.delete(*StudentTable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], ]
        StudentTable.insert('', END, values=vv)


##########################################################################function of 1st frame exportdata button
def exportdata():
    ff = filedialog.asksaveasfilename()
    gg = StudentTable.get_children()
    ID,sname,contact,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = StudentTable.item(i)
        pp = content['values']
        ID.append(pp[0]),sname.append(pp[1]),contact.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Sname','Mobile','Email','Address','Gender','DOB','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(ID,sname,contact,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification','student data is saved{}'.format(paths))

##########################################################################function of 1st frame exit button
def exitprofile():
    res = messagebox.askyesnocancel('NOTIFICATION','Do you want to exit ?')
    if(res==True):
        root.destroy()
################################################################################################buttons in 1st frame
studentaddbtn = Button(DataEntryFrame, text='1.Add Student', bd=5, font=('calibri', 20, "bold"), width=20, bg='thistle'
                       ,command=addstudent,activebackground='white', activeforeground='black',anchor='w')
studentaddbtn.pack(side=TOP,expand=True)

Searchbtn = Button(DataEntryFrame, text='2.Search Student', bd=5, font=('calibri', 20, "bold"), width=20, bg='thistle'
                   ,command=searchstudent,activebackground='white', activeforeground='black',anchor='w')
Searchbtn.pack(side=TOP,expand=True)

Deletebtn = Button(DataEntryFrame, text='3.Delete Student', bd=5, font=('calibri', 20, "bold"), width=20, bg='thistle'
                   ,command=deletestudent,activebackground='white', activeforeground='black',anchor='w')
Deletebtn.pack(side=TOP,expand=True)

Updatebtn = Button(DataEntryFrame, text='4.Update Student', bd=5, font=('calibri', 20, "bold"), width=20, bg='thistle'
                   ,command=updatestudent,activebackground='white', activeforeground='black',anchor='w')
Updatebtn.pack(side=TOP,expand=True)

showbtn = Button(DataEntryFrame, text='5.Show All', bd=5, font=('calibri', 20, "bold"), width=20, bg='thistle'
                 ,command=showstudent,activebackground='white', activeforeground='black',anchor='w')
showbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame, text='6.Export Data', bd=5, font=('calibri', 20, "bold"), width=20, bg='thistle'
                  ,command=exportdata,activebackground='white', activeforeground='black',anchor='w')
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame, text='7.E X I T', bd=5, font=('calibri', 20, "bold"), width=20, bg='thistle'
                ,command=exitprofile,activebackground='white', activeforeground='black',anchor='w')
exitbtn.pack(side=TOP,expand=True)

##########################################################################################################2nd frame showing data
ShowDataFrame = Frame(root,bg='blanched almond',relief=RIDGE,borderwidth=3,bd=5)
ShowDataFrame.place(width=504,height=500,x=490,y=50)
##################################################################################showing data functions and labels in tree form
style = ttk.Style()
style.configure('Treeview.Heading',font=('ariel',15,'bold'),foreground='rosy brown')
style.configure('Treeview',font=('ariel',15,'bold'),foreground='olive drab',bg='LightSalmon2')

scrolls_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scrolls_y = Scrollbar(ShowDataFrame,orient=VERTICAL)

StudentTable = Treeview(ShowDataFrame,columns=('Id','Name','Contact','E-mail','Address','Gender','D.O.B',
                'Added Date','Added Time'),xscrollcommand=scrolls_x.set,yscrollcommand=scrolls_y.set)
StudentTable.heading('Id',text='Id')
StudentTable.heading('Name',text='Name')
StudentTable.heading('Contact',text='Contact')
StudentTable.heading('E-mail',text='E-mail')
StudentTable.heading('Address',text='Address')
StudentTable.heading('Gender',text='Gender')
StudentTable.heading('D.O.B',text='D.O.B')
StudentTable.heading('Added Date',text='Added Date')
StudentTable.heading('Added Time',text='Added Time')
StudentTable['show'] = 'headings'
StudentTable.column('Id',width=100)
StudentTable.column('Name',width=300)
StudentTable.column('Contact',width=150)
StudentTable.column('E-mail',width=300)
StudentTable.column('Address',width=300)
StudentTable.column('Gender',width=100)
StudentTable.column('D.O.B',width=100)
StudentTable.column('Added Date',width=100)
StudentTable.column('Added Time',width=100)

StudentTable.pack(fill=BOTH,expand=True)

scrolls_x.pack(side=BOTTOM,fill=X)
scrolls_y.pack(side=RIGHT,fill=Y)
scrolls_x.config(command=StudentTable.xview)
scrolls_y.config(command=StudentTable.yview)
#######################################################slider animation
ss = 'STUDENT DATA BASE '
AnimatedLabel = Label(root,text=ss,font=('ariel',20,'italic bold'),bg="black",relief=RIDGE,borderwidth=3,bd=5,fg='white')
AnimatedLabel.place(x=270,y=0,width=380,height=40)


####################################################################slider text color
colors=['grey']
def Animatedcolor():
    fg = random.choice(colors)
    AnimatedLabel.config(fg=fg)
    AnimatedLabel.after(20,Animatedcolor)
# def Tick():
#     global count,text
#     if(count>=len(ss)):
#         count =0
#         text = ""
#         AnimatedLabel.configure(text=text)
#     else:
#         text =text+ss[count]
#         AnimatedLabel.configure(text=text)
#         count +=1
#     AnimatedLabel.after(150, Tick)
#
# count = 0
# text = ''
# Tick()
Animatedcolor()
####################################################################clock
Clock = Label(root,font=('times',10,'bold'),borderwidth=3,fg='black',relief=RIDGE,bg='white' )
Clock.place(x=10,y=5,width=150,height=40)

def vel():
    time_string = time.strftime('%H:%M:%S')
    date_string = time.strftime('%d/%m/%Y')
    Clock.after(100,vel)
    Clock.config(text = 'Date:'+date_string+'\n'+'Time:'+time_string,anchor='w' )

vel()
########################################################################################connect data button
def connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passval.get()

        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is Incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int,name varchar(20),contact varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database created and Now you are connected to the database', parent=dbroot)
        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database',parent=dbroot)
        dbroot.destroy()


    dbroot = Toplevel()
    dbroot.geometry('300x130+500+200')
    dbroot.grab_set()
    dbroot.iconbitmap('image.ico')
    dbroot.title('LOGIN')
    dbroot.config(bg='cornsilk2')
    dbroot.resizable(False,False)
    ########inside db root box
    idlable1 = Label(dbroot,text='Enter host ',bg='cornsilk2',font=('times',13,'bold'),width=8,anchor='w',bd=4)
    idlable1.place(x=0,y=10)

    userlable1 = Label(dbroot, text='User Name ', bg='cornsilk2', font=('times', 13, 'bold'), width=8,anchor='w',bd=4)
    userlable1.place(x=0, y=40)

    passwordlable1 = Label(dbroot, text='Password', bg='cornsilk2', font=('times', 13, 'bold'), width=8,bd=4,anchor='w')
    passwordlable1.place(x=0, y=70)
##################################### entries of dbroot
    hostval = StringVar()
    userval = StringVar()
    passval = StringVar()


    entry1 = Entry(dbroot,font=('ariel',14,'bold'),width=16,bg='peach puff',textvariable=hostval)
    entry1.place(x=108,y=10)

    entry2 = Entry(dbroot, font=('time', 14, 'bold'), width=16,bg='peach puff',textvariable= userval)
    entry2.place(x=108, y=40)

    entry3 = Entry(dbroot, font=('time', 14, 'bold'), width=16,bg='peach puff',textvariable= passval)
    entry3.place(x=108, y=70)

    submitbtn = Button(dbroot,text='S U B M I T',bd=5,font=('ariel',10,"italic bold"),width=15,bg='cornsilk2',command=submitdb,activebackground='black',activeforeground='white')
    submitbtn.place(x=90,y=97)

    dbroot.mainloop()
##############################################################################connect to data button command connects dbroot
connectbtn = Button(root,text="Log In To Database ~> ",bg='gold',bd=7,activeforeground='white',font=('ariel',8,'bold'),activebackground='black',command=connectdb)
connectbtn.place(x=750,y=550,width=150,height=40)

root.mainloop()


