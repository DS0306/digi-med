import mysql.connector as msc
#------------------------------------------------------UPDATE DOCTOR PROFILE-----------------------------------------------------------
def updateprofile(rs):
    mycon=msc.connect(host="localhost", user="root",database="project",password="abcd1234")
    mycursor=mycon.cursor()
    ch=input("to change the name press # otherwise press anykey to make no changes: ")
    if ch=='#':
        name=input("enter your new name: ")
    else:
        name=rs[0][1]
    ch=input("to change the fees press # otherwise press anykey to make no changes: ")
    if ch=='#':
        fees=int(input("enter your new fees: "))
    else:
        fees=rs[0][3]
    ch=input("to change the degree press # otherwise press anykey to make no changes: ")
    if ch=='#':
        degree=input("enter your updated degree: ")
    else:
        degree=rs[0][4]
    ch=input("to change the timings press # otherwise press anykey to make no changes: ")
    if ch=='#':
        time=input("enter your new timings: ")
    else:
        time=rs[0][5]
    ch=input("to change the hospitalname press # otherwise press anykey to make no changes: ")
    if ch=='#':
        hname=input("enter your new hospitalname: ")
    else:
        hname=rs[0][6]
    ch=input("to change the password press # otherwise press anykey to make no changes: ")
    if ch=='#':
        password=input("enter your new password: ")
    else:
        password=rs[0][8]
    ch=input("to change the phone number  press # otherwise press anykey to make no changes: ")
    if ch=='#':
        
        while True:
            Phone=input("enter your new phone number : ")
            if len(Phone)==10:
                 break
            else:
                print("PHONE NUMBER IS INCORRECT, TRY AGAIN")
    else:
        Phone=rs[0][9]
    ch=input("to change the emailid press # otherwise press anykey to make no changes: ")
    if ch=='#':
        while True:
            Email=input("ENTER YOUR EMAIL ID:")
            if "@" in Email:
                break
            else:
                print("INCORRECT EMAIL, TRY AGAIN")
    else:
        Email=rs[0][10]
    Q="update doctordetails set doctorname='{}', fees={}, degree='{}', timings='{}', hospitalname='{}', password='{}', phonenumber={}, emailid='{}' where doctorid={}". format(name,fees,degree,time,hname,password,Phone,Email,rs[0][0])
    mycursor.execute(Q)
    mycon.commit()
    print("DETAILS HAVE BEEN UPDATED")
#----------------------------------------------------DOCTOR LOGIN PROFILE-------------------------------------------------------------
def logind(char):
    if(char =='D'):
        userid=int(input('ENTER YOUR LOGIN ID : '))
        passw=input('ENTER PASSWORD : ')
        mycon=msc.connect(host="localhost", user="root", password="abcd1234", database="project")
        mycursor=mycon.cursor()
        Q="SELECT * FROM DOCTORDETAILS WHERE Doctorid='{}' and password='{}' ".format(userid,passw)
        mycursor.execute(Q)
        rs=mycursor.fetchall()
        if(rs==[]):
            print("YOUR ID AND PASSWORD ARE NOT MATCHED ")
        else:
            print("HELLO",rs[0][1].upper(), "WELCOME TO YOUR DASH BOARD NOW ENTER TO PROCEED FURTHER")
            input()
            while(True):
                print("PRESS 1. TO VIEW APPOINTMENT")
                print("PRESS 2. TO UPDATE PROFILE ")
                print("PRESS 3. LOGOUT ")
                ch=int(input("enter your choice:"))
                if ch==1:
                    mycon=msc.connect(host="localhost", user="root", database="project", password="abcd1234")
                    mycursor=mycon.cursor()
                    Q="select*from appointment where doctorid='{}'".format(userid)
                    mycursor.execute(Q)
                    rd=mycursor.fetchall()
                    if(rd==[]):
                        print("NO APPOINTMENT FOUND")
                    else:
                        for i in rd:
                            print(i)
                elif ch==2:
                    updateprofile(rs)
                elif ch==3:
                    print("THANK YOU FOR USING DIGIMED ")
                    return
                else:
                    print("wrong choice entered")
                    
            
            

        
#------------------------------------------------------------PATIENT LOGIN---------------------------------------------------------------
    elif(char=='P'):
        mycon=msc.connect(host="localhost", user="root", password="abcd1234", database="project")
        mycursor=mycon.cursor()
        while True:
            userid=int(input("enter your patientid:"))
            password=input("enter your password:")
            Q="select*from patientdetails where patientid={} and password='{}'".format(userid, password)
            mycursor.execute(Q)
            rs=mycursor.fetchall()
            if rs==[]:
                print("WRONG USER ID OR PASSWORD")
            else:
                break
        print("WELCOME",rs[0][2],"TO DIGIMED")
        while True:
            print("1. BOOK APPOINTMENT")
            print("2. UPDATE PROFILE")
            print("3. VIEW APPOINTMENT")
            print("4. LOGOUT")
            ch=int(input("ENTER YOUR CHOICE: "))
            if ch==1:
                print("press 'A' for myself")
                print("press 'B' for others")
                choice=input("ENTER YOUR CHOICE: ")
                bookappointment(choice,rs)
            elif ch==2:
                mycon=msc.connect(host="localhost", user="root",database="project",password="abcd1234")
                mycursor=mycon.cursor()
                ch=input("to change the name press # otherwise press anykey to make no changes: ")
                if ch=='#':
                    name=input("enter your new name: ")
                else:
                    name=rs[0][2]
                ch=input("to change the password press # otherwise press anykey to make no changes: ")
                if ch=='#':
                    password=input("enter your new password: ")
                else:
                    password=rs[0][1]
                ch=input("to change the phone number  press # otherwise press anykey to make no changes: ")
                if ch=='#':
                   
                    while True:
                        Phone=input("enter your new phone number : ")
                        if len(Phone)==10:
                            break
                        else:
                            print("PHONE NUMBER IS INCORRECT, TRY AGAIN")
                else:
                    Phone=rs[0][5]
                ch=input("to change the emailid press # otherwise press anykey to make no changes: ")
                if ch=='#':
                    while True:
                        Email=input("ENTER YOUR EMAIL ID:")
                        if "@" in Email:
                            break
                        else:
                            print("INCORRECT EMAIL, TRY AGAIN")
                else:
                    Email=rs[0][6]
                Q="update patientdetails set password='{}', patientname='{}', contactno={}, emailid='{}' where patientid={}". format(password,name,Phone, Email, rs[0][0])
                mycursor.execute(Q)
                mycon.commit()
                print("DETAILS HAVE BEEN UPDATED")
            elif ch==3:
                mycon=msc.connect(host="localhost", user="root", database="project", password="abcd1234")
                mycursor=mycon.cursor()
                Q="select*from appointment where patientname='{}'".format(rs[0][2])
                mycursor.execute(Q)
                rp=mycursor.fetchall()
                if rp==[]:
                    print("NO APPOINTMENT FOUND")
                else:
                    for i in rp:
                        print(i)
            elif ch==4:
                print("THANK YOU FOR USING DIGIMED")
                break
            else:
                print("WRONG CHOICE ENTERED")
           
            
#------------------------------------------------------SHOWING DEPARTMENTS-------------------------------------------------------------
import random
def showdept():
    print("CHOOSE DEPARTMENT FROM THE FOLLOWING MENU:")
    print("1. CARDIO")
    print("2. ORTHOPEDIC")
    print("3. DENTAL")
    print("4. OPTHOMALOGY")
    print("5. NEUROLOGY")
    print("6. PEDIATRIC")
    print("7. GENERAL")
#--------------------------------------------------------BOOK APPOINTMENT FOR PATIENT--------------------------------------------------
def bookappointment(choice,prs):
    pname=age=gender=contactno=None
    if(choice.lower()=='b'):
        pname=input("ENTER THE NAME OF THE PATIENT: ")
        age=int(input("ENTER AGE OF PATIENT:"))
        gender=input("ENTER GENDER: ")
        contactno=int(input("ENTER CONTACT NUMBER: "))
    if choice.lower()=='a':
        pname=prs[0][2]
        age=prs[0][3]
        gender=prs[0][4]
        contactno=prs[0][5]
    showdept()
    while True:
        ch=int(input("SELECT DEPARTMENT: "))
        if ch==1:
            dept="cardio"
            break
        elif ch==2:
            dept="orthopedic"
            break
        elif ch==3:
            dept="dental"
            break
        elif ch==4:
            dept="opthomalogy"
            break
        elif ch==5:
            dept="neurology"
            break
        elif ch==6:
            dept="pediatric"
            break
        elif ch==7:
            dept="general"
            break
        else:
            print("WRONG CHOICE ENTERED")
    mycon=msc.connect(user="root", host="localhost", database="project", password="abcd1234")
    mycursor=mycon.cursor()
    
    date=input("ENTER DATE IN THE FORMAT (DD-MM-YYYY): ")
    
    Q="select*from doctordetails where specialisation like'{}%'".format(dept)
    mycursor.execute(Q)
    rs=mycursor.fetchall()
    if rs==[]:
        print("NO DOCTOR FOUND")
    else:
        count=1
        if(len(rs)>1):
            print("WE HAVE FOUND MULTIPLE DOCTORS AND DETAILS ARE :")
            for x in rs:
                print("DETAILS OF DOCTOR ",count," ARE ")
                print("DOCTOR ID : ",x[0],"\t DOCTOR NAME :",x[1],"\t TIMINGS = ",x[5],"\t HOSPITAL : ",x[6])
                count+=1
                print()
            choice=input("ENTER THE DOCTOR ID ON THE BASIS OF THE ABOVE DATA: ")
            Q="select*from doctordetails where doctorid={}".format(choice)
            mycursor.execute(Q)
            rd=mycursor.fetchone()
            if len(rd)==0:
                print("WRONG DOCTOR ID YOU HAVE ENTERED ")
            else:
                doctorid=rd[0]
                doctorname=rd[1]
                timings=rd[5]
                hname=rd[6]
                appointmentid=random.randrange(1000,40000)
                Q="insert into appointment values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(appointmentid, doctorname, dept, hname, date, timings,
                                                                                                             pname, age, gender,contactno, doctorid)
                mycursor.execute(Q)
                print("YOUR APPOINTMENT SUCCESSFULLY COMPLETED, YOUR APPOINTMENT ID IS:",appointmentid)
                mycon.commit()
        else:
            doctorid=rs[0][0]
            doctorname=rs[0][1]
            timings=rs[0][5]
            hname=rs[0][6]
            appointmentid=random.randrange(1000,40000)
            Q="insert into appointment values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(appointmentid, doctorname, dept, hname, date, timings,
                                                                                                             pname, age, gender,contactno, doctorid)
            mycursor.execute(Q)
            print("YOUR APPOINTMENT SUCCESSFULLY COMPLETED, YOUR APPOINTMENT ID IS:",appointmentid)
            mycon.commit()
#----------------------------------------------------------PATIENT SIGN IN------------------------------------------------------------------       
    
#PATIENT REGISTRATION
def registrationP():
    mycon=msc.connect(host="localhost", user="root", password="abcd1234", database="project")
    if (mycon.is_connected()):
        print("connected")
        mycursor=mycon.cursor()
        Patientid=int(input("ENTER YOUR PATIENT ID:"))
        PatientName=input("ENTER YOUR FULL NAME:")
        Age=int(input("ENTER YOUR AGE:"))
        Gender=input("ENTER YOUR GENDER:")
        while True:
            Phone=input("ENTER YOUR PHONE NUMBER:")
            if len(Phone)==10:
                break
            else:
                print("PHONE NUMBER IS INCORRECT, TRY AGAIN")
        while True:
            Email=input("ENTER YOUR EMAIL ID:")
            if "@" in Email:
                break
            else:
                print("INCORRECT EMAIL, TRY AGAIN")
        Password=input("ENTER YOUR PASSWORD:")
        Retype=input("RETYPE YOUR PASWORD:")
        while True:
            if Password==Retype:
                print("RETYPE PASSWORD HAS BEEN MATCHED:")
                break
            else:
                print("RETYPE PASSWORD IS INCORRECT")
        Q="insert into patientdetails values ({},'{}','{}',{},'{}',{},'{}')".format(Patientid, Password, PatientName, Age, Gender, Phone, Email)                     
        mycursor.execute(Q)
        print("YOU HAVE BEEN SUCCESSFULLY REGISTERED:")
        mycon.commit()
        input("PRESS ENTER KEY TO LOGIN")
        logind('P')
    else:
        print("not connected")
#------------------------------------------------------DOCTOR SIGN IN---------------------------------------------------------------------
#DOCTOR REGISTRATION
def registrationD():
    mycon=msc.connect(host="localhost", user="root", password="abcd1234", database="project")
    if (mycon.is_connected()):
        mycursor=mycon.cursor()
        Doctorid=int(input("ENTER YOUR REGISTERED DOCTOR ID:"))
        Doctorname=input("ENTER YOUR FULL NAME:")
        Specialisation=input("ENTER YOUR SPECIALISATION:")
        Fees=int(input("ENTER YOUR FEES:"))
        Degree=input("ENTER YOUR DEGREE:")
        Timings=input("ENTER YOUR TIMINGS:")
        Hospitalname=input("ENTER HOSPITAL NAME:")
        Gender=input("ENTER YOUR GENDER:")
        while True:
            Phone=input("ENTER YOUR PHONE NUMBER:")
            if len(Phone)==10:
                break
            else:
                print("PHONE NUMBER IS INCORRECT, TRY AGAIN")
        while True:
            Email=input("ENTER YOUR EMAIL ID:")
            if "@" in Email:
                break
            else:
                print("INCORRECT EMAIL, TRY AGAIN")
        Password=input("ENTER YOUR PASSWORD:")
        Retype=input("RETYPE YOUR PASWORD:")
        while True:
            if Password==Retype:
                print("RETYPE PASSWORD HAS BEEN MATCHED:")
                break
            else:
                print("RETYPE PASSWORD IS INCORRECT")
        Q="insert into doctordetails values ({},'{}','{}',{},'{}','{}','{}','{}','{}',{},'{}')".format(Doctorid, Doctorname, Specialisation, Fees, Degree, Timings, Hospitalname, Gender, Password, Phone, Email)                     
        mycursor.execute(Q)
        print("YOU HAVE BEEN SUCCESSFULLY REGISTERED:")
        mycon.commit()
        input("PRESS ENTER KEY TO LOGIN")
        logind('D')
    else:
        print("not connected")
#-------------------------------------------------------------MAIN MENU------------------------------------------------------------------- 
print("**************************************************WELCOME TO DIGIMED************************************************")
print("PRESS 1 FOR DOCTOR")
print("PRESS 2 FOR PATIENT")
choice=int(input("ENTER YOUR CHOICE:"))
if choice==1:
    print("-----------------------------------------------WELCOME TO DOCTOR PORTAL-----------------------------------------------------")
    print("PRESS 1 TO LOG IN")
    print("PRESS 2 TO SIGN UP FOR NEW USER")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        logind('D')
    elif choice==2:
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print("\t\t\tDOCTOR REGISTRATION PORTAL")
        print("--------------------------------------------------------------------------------------------------------------------------------")
        registrationD()
    else:
        print("INVALID CHOICE ENTERED")
elif(choice==2):
    print("----------------------------------------------WELCOME TO PATIENT PORTAL------------------------------------------------------")
    print("PRESS 1 TO LOG IN")
    print("PRESS 2 TO SIGN UP")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        logind('P')
    elif choice==2:
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("-------------------------------------------PATIENT REGISTRATION PORTAL------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------------------------------------")
        registrationP()
    else:
        print("INVALID CHOICE ENTERED")

   
    
    
