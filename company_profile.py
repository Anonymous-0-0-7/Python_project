from tkinter import *
#job-seeker profile
root = Tk()

root.geometry("500x700")
root.title("Company Profile")
def submitF():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="job portal"
    )

    mycursor = mydb.cursor()

    #val = ("John", "passofjohn")
    sql = "INSERT INTO profilecjp (companyName,email,phone_no,location,YOE,official_Web,company_type) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (f"{c_namevalue.get()}", f"{emailvalue.get()}",f"{phone_novalue.get()}",f"{locationvalue.get()}",f"{yoevalue.get()}",f"{official_wvalue.get()}",f"{c_typevalue.get()}") #fsting is imp

    mycursor.execute(sql, val)

    mydb.commit()  #it is importent bcoz bydefault is is not comment

    print(mycursor.rowcount, "record inserted.")



#making variable to hold value given by user(company)
c_namevalue = StringVar()
emailvalue = StringVar()
phone_novalue = StringVar()
locationvalue = StringVar()
yoevalue = StringVar()
official_wvalue = StringVar()
c_typevalue = StringVar()





#0
c_name = Label(root,text="Company Name",font=10)  #maybe wann edit
c_name.grid(row =0,column=0,padx=10,pady=10)

c_namei = Entry(root,font=10,textvariable =c_namevalue)
c_namei.grid(row=0,column=1)
#1
email = Label(root,text="Email",font=10)
email.grid(row =1,column=0,padx=10,pady=10)

emaili = Entry(root,font=10,textvariable =emailvalue)
emaili.grid(row=1,column=1) #1
#2
phone_no = Label(root,text="Phone_no",font=10)
phone_no.grid(row =2,column=0,padx=10,pady=10)

phone_noi = Entry(root,font=10,textvariable =phone_novalue)
phone_noi.grid(row=2,column=1)
#3
location = Label(root,text="Location",font=10)
location.grid(row =3,column=0,padx=10,pady=10)

locationi = Entry(root,font=10,textvariable =locationvalue)
locationi.grid(row=3,column=1)
#4
yoe = Label(root,text="Year Of Established",font=10)
yoe.grid(row =4,column=0,padx=10,pady=10)

yoei = Entry(root,font=10,textvariable =yoevalue)
yoei.grid(row=4,column=1)
#5
official_w = Label(root,text="Official Website",font=10)
official_w.grid(row =5,column=0,padx=10,pady=10)

official_wi = Entry(root,font=10,textvariable =official_wvalue)
official_wi.grid(row=5,column=1)
#6
c_type = Label(root,text="Company Type",font=10) #IT BPO BANKING MANUFACUTRER ETC (OTHER)
c_type.grid(row =6,column=0,padx=10,pady=10)

c_type = Entry(root,font=10,textvariable =c_typevalue)
c_type.grid(row=6,column=1)

#7
submit = Button(root,text="submit",font="15",command= submitF)
submit.grid(row=7,column=1)

root.mainloop()
exit()
