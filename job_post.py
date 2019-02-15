from tkinter import *
#job-seeker profile
root = Tk()
root.title("JOB POSTING")
root.geometry("500x700")

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
    sql = "INSERT INTO jobPost (c_name,YOE,Vac,Loc,skills,role,Sal,JPO,JLD,JD,Itype,Cweb) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (f"{c_namevalue.get()}", f"{NOYEvalue.get()}",f"{NOVvalue.get()}",f"{locationvalue.get()}",f"{skillsvalue.get()}",f"{rolevalue.get()}",f"{salaryvalue.get()}",f"{jpovalue.get()}",f"{jldvalue.get()}",f"{jdescvalue.get()}",f"{in_typevalue.get()}",f"{Cwebvalue.get()}")#fsting is imp

    mycursor.execute(sql, val)

    mydb.commit()  #it is importent bcoz bydefault is is not comment

    print(mycursor.rowcount, "record inserted.")



#making variable to hold value given by user(company)
c_namevalue = StringVar()  #1
NOYEvalue= StringVar()   #2
NOVvalue = StringVar()  #3
locationvalue = StringVar()  #4
skillsvalue = StringVar()   #5
rolevalue=StringVar()      #6
salaryvalue = StringVar()   #7
jpovalue = StringVar()   #8
jldvalue = StringVar()   #9
jdescvalue = StringVar()  # 10
in_typevalue = StringVar()  #11
Cwebvalue = StringVar()  #12




#0
c_name = Label(root,text="Company Name",font=10)  #maybe wann edit
c_name.grid(row =0,column=0,padx=10,pady=10)

c_namei = Entry(root,font=10,textvariable =c_namevalue)
c_namei.grid(row=0,column=1)
#1
NOYE = Label(root,text="Years of Experience",font=10)
NOYE.grid(row =1,column=0,padx=10,pady=10)

NOYEi = Entry(root,font=10,textvariable =NOYEvalue)
NOYEi.grid(row=1,column=1) #1
#2
NOV = Label(root,text="Vacancies",font=10)
NOV.grid(row =2,column=0,padx=10,pady=10)

NOVi = Entry(root,font=10,textvariable =NOVvalue)
NOVi.grid(row=2,column=1)
#3
location = Label(root,text="Location",font=10)
location.grid(row =3,column=0,padx=10,pady=10)

locationi = Entry(root,font=10,textvariable =locationvalue)
locationi.grid(row=3,column=1)
#4
skills= Label(root,text="Skills",font=10)
skills.grid(row =4,column=0,padx=10,pady=10)

skillsi = Entry(root,font=10,textvariable =skillsvalue)
skillsi.grid(row=4,column=1)
#5 (for what i.e what to do in company after hired)
role= Label(root,text="Role",font=10)
role.grid(row =5,column=0,padx=10,pady=10)

rolei = Entry(root,font=10,textvariable =rolevalue)
rolei.grid(row=5,column=1)
#6
salary= Label(root,text="Salary",font=10) #IT BPO BANKING MANUFACUTRER ETC (OTHER)
salary.grid(row =6,column=0,padx=10,pady=10)

salaryi = Entry(root,font=10,textvariable =salaryvalue)
salaryi.grid(row=6,column=1)

#7
jpo = Label(root,text="Job Posted On",font=10)  #give him calander
jpo.grid(row =7,column=0,padx=10,pady=10)

jpoi = Entry(root,font=10,textvariable =jpovalue)
jpoi.grid(row=7,column=1)

#8

jld= Label(root,text="Last Date",font=10)  #give him calander
jld.grid(row =8,column=0,padx=10,pady=10)

jldi = Entry(root,font=10,textvariable =jldvalue)
jldi.grid(row=8,column=1)

#9
jdesc = Label(root,text="Job Description",font=10)      #gender give them radio button
jdesc.grid(row =9,column=0,padx=10,pady=10)

jdesci = Entry(root,font=10,textvariable =jdescvalue)
jdesci.grid(row=9,column=1)
#10
in_type = Label(root,text="Industry Type",font=10)
in_type.grid(row =10,column=0,padx=10,pady=10)

in_typei = Entry(root,font=10,textvariable =in_typevalue)
in_typei.grid(row=10,column=1)
#11
Cweb = Label(root,text="Company Website",font=10)
Cweb.grid(row =11,column=0,padx=10,pady=10)

Cwebi = Entry(root,font=10,textvariable =Cwebvalue)
Cwebi.grid(row=11,column=1)
#12

submit = Button(root,text="submit",font="15",command= submitF)
submit.grid(row=12,column=1)






root.mainloop()

exit()

