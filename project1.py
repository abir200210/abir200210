#classroom management#
import mysql.connector as ms
mydb=ms.connect(host="abir",user="root",password="1234",database="cemk")
mycur=mydb.cursor()


def ad_task():
    print("Admin Menu")
    print("")
    print("1.Register new student")
    print("2.Register new teacher")
    print("3.Delete ex student")
    print("4.Delete ex teacher")
    print("5.Logout")
    ad_choice=int(input("Enter your choice admin="))
    if(ad_choice==1):
        s_name=input("Enter student's name=")
        roll_no=input("Enter student's roll=")
        mail_id=input("Enter student's mail=")
        contact=input("Enter contact number of student=")
        data_add1=(s_name,roll_no,mail_id,contact)
        mycur.execute("""INSERT INTO STUDENT(S_NAME,ROLL_NO,MAIL_ID,CONTACT) VALUES (%s,%s,%s,%s )""",data_add1)
        print(s_name+" is added as a new student in college")
        mydb.commit()

        
    elif(ad_choice==2):
        t_name=input("Enter teacher's name=")
        id_no=input("Enter teacher' id=")
        mail_id=input("Enter teacher's mail id=")
        contact=input("Enter teacher's contact number=")
        data_add2=(t_name,id_no,mail_id,contact)
        mycur.execute("""INSERT INTO TEACHER(T_NAME,ID_NO,MAIL_ID,CONTACT) VALUES (%s,%s,%s,%s)""",data_add2)
        print("Mr. "+t_name+" is added as a new professor")
        mydb.commit()


    elif(ad_choice==3):
        s_name=input("Enter student's name=")
        mail_id=input("Enter student's mail id=")
        data_rmv1=(s_name,mail_id)
        mycur.execute("""DELETE FROM STUDENT WHERE S_NAME=%s AND MAIL_ID=%s""",data_rmv1)
        print(s_name+" has been removed successfully")
        mydb.commit()

        
    elif(ad_choice==4):
        t_name=input("Enter teacher's name=")
        id_no=input("Enter id number of student=")
        data_rmv2=(t_name,id_no)
        mycur.execute("""DELETE FROM TEACHER WHERE T_NAME=%S AND ID_NO=%s""",data_rmv2)
        print("Prof.",t_name,"is removed successfully")
        mydb.commit()
    elif(ad_choice==5):
        print("Have a nice day")

def ad_check():
    username=input("Enter admin's username=")
    password=input("Enter admin's password=")
    if(username=='cemk'):
        if(password=='cemk1234'):
            ad_task()
        else:
            print("Invalid credentials")
    else:
        print("Login unsuccessful for admin")

def t_task():
    print("Teacher's menu")
    print("")
    print("1.Inserting subject's marks")
    print("2.Updating marks")
    t_choice=int(input("Enter your choice="))
    if(t_choice==1):
        name=input("Enter student's name=")
        sub1=int(input("Enter sub1 marks="))
        sub2=int(input("Enter sub2 marks="))
        sub3=int(input("Enter sub3 marks="))
        sub4=int(input("Enter sub4 marks="))
        sub_val=(name,sub1,sub2,sub3,sub4)
        mycur.execute("""INSERT INTO RESULT(NAME,SUB1,SUB2,SUB3,SUB4) VALUES (%s,%d,%d,%d,%d)""",sub_val)
        print(s_name+"'s data added successfully")
        mydb.commit()

def t_check():
    username=input("Enter teacher's username=")
    password=input("Enter teacher's password=")
    if(username=='tcemk'):
        if(password=='tcemk1234'):
            t_task()
        else:
            print("Invalid credentials")
    else:
        print("Login unsuccessful for teacher")


def s_task():
    print("Student' menu")
    print("Students are allowed only to view their reults")
    s_name=input("Enter student'name=")
    roll_no=input("enter student' roll=")
    s_vals=(s_name,roll_no)
    mycur.execute("""SELECT * FROM STUDENT WHRERE S_NAME=%s AND ROLL_NO=%s""",s_vals)
    mydb.commit()


def s_check():
    username=input("Enter student's username=")
    password=input("Enter student's password=")
    if(username=='scemk'):
        if(password=='scemk1234'):
            s_task()
        else:
            print("Invalid credentials")
    print("Login unsuccessful")
            


def main():
    while 1:
        print("College Of Engineering And Management,Kolaghat welcomes you all")
        print("")
        print("1.Login as an adminisrator")
        print("2.Login as a teacher")
        print("3.Login as a student")
        print("")
        user_choice=int(input("Enter your choice(1-3)="))
        if(user_choice==1):
            print("Welcome admin!")
            print("")
            ad_check()
        elif(user_choice==2):
            t_check()
            print("")
        elif(user_choice==3):
            print("Welcome student")
            print("")
            s_check()
        else:
            print("Enter choice between 1-3")
            print("")
main()
