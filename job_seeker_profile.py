from tkinter import *
#job-seeker profile
root = Tk()

root.title("JOB-SEEKER PROFILE")

root.geometry("500x700")

def submitf():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="job portal"
    )

    mycursor = mydb.cursor()

    #val = ("John", "passofjohn")
    sql = "INSERT INTO profilejs (name,email,phone_no,location,key_skill,experience,education,IT_skill,date_of_birth,gender,address,martialS,language)" \
          " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (f"{namevalue.get()}", f"{emailvalue.get()}",f"{phone_novalue.get()}",f"{languagevalue.get()}",f"{key_skillvalue.get()}",f"{experiencevalue.get()}",f"{educationvalue.get()}",f"{IT_skillvalue.get()}",f"{dobvalue.get()}",f"{gendervalue.get()}",f"{addressvalue.get()}",f"{marital_stvalue.get()}",f"{languagevalue.get()}")#fsting is imp

    mycursor.execute(sql, val)

    mydb.commit()  #it is importent bcoz bydefault is is not comment

    print(mycursor.rowcount, "record inserted.")


namevalue = StringVar()     #Value holder for strings variables.
emailvalue = StringVar() # here value holder name is passwordvalue i.e a variable
phone_novalue = StringVar()
locationvalue = StringVar()
key_skillvalue = StringVar()
experiencevalue = StringVar()
educationvalue = StringVar()
IT_skillvalue = StringVar()
dobvalue = StringVar()
gendervalue = StringVar()
addressvalue = StringVar()
marital_stvalue = StringVar()
languagevalue = StringVar()



#0
name = Label(root,text="Name",font=10)  #maybe wann edit
name.grid(row =0,column=0,padx=10,pady=10)

namei = Entry(root,font=10,textvariable = namevalue)
namei.grid(row=0,column=1)
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
key_skill = Label(root,text="Key Skill",font=10)
key_skill.grid(row =4,column=0,padx=10,pady=10)

key_skilli = Entry(root,font=10,textvariable =key_skillvalue)
key_skilli.grid(row=4,column=1)
#5
experience = Label(root,text="Experience",font=10)
experience.grid(row =5,column=0,padx=10,pady=10)

experiencei = Entry(root,font=10,textvariable =experiencevalue)
experiencei.grid(row=5,column=1)
#6
education = Label(root,text="Education",font=10) #10 12 diploma degree (passing year) specialization
education.grid(row =6,column=0,padx=10,pady=10)

educationi = Entry(root,font=10,textvariable =educationvalue)
educationi.grid(row=6,column=1)
#7
IT_skill = Label(root,text="IT Skill",font=10)
IT_skill.grid(row =7,column=0,padx=10,pady=10)

IT_skilli = Entry(root,font=10,textvariable = IT_skillvalue)
IT_skilli.grid(row=7,column=1)
#8
dob = Label(root,text="Date Of Birth",font=10)  #give him calander
dob.grid(row =8,column=0,padx=10,pady=10)

dobi = Entry(root,font=10,textvariable = dobvalue)
dobi.grid(row=8,column=1)
#9
gender = Label(root,text="Gender",font=10)      #gender give them radio button
gender.grid(row =9,column=0,padx=10,pady=10)

genderi = Entry(root,font=10,textvariable = gendervalue)
genderi.grid(row=9,column=1)
#10
address = Label(root,text="Address",font=10)
address.grid(row =10,column=0,padx=10,pady=10)

addressi = Entry(root,font=10,textvariable = addressvalue)
addressi.grid(row=10,column=1)
#11
marital_st = Label(root,text="Marital Status",font=10)   #give radio button
marital_st.grid(row =11,column=0,padx=10,pady=10)

marital_sti = Entry(root,font=10,textvariable = marital_stvalue)
marital_sti.grid(row=11,column=1)
#12
language = Label(root,text="Language",font=10)  #give checkbox
language.grid(row =12,column=0,padx=10,pady=10)

languagei = Entry(root,font=10,textvariable = languagevalue)
languagei.grid(row=12,column=1)

# button 13
submit = Button(root,text="Submit",font="15",command=submitf) #command is take function name that execute after clicking on button
submit.grid(row=13,column=1,pady=10)




root.mainloop()
