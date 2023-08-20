import math
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
from tkinter import messagebox
from register import Register
import mysql.connector

# --------------------------
from train import Train
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Sign in")
        self.root.state('zoomed')
        self.root.config(bg="#021e2f")


        # Background colr
        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        # Frame
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text="LOG IN", font=("times new roman", 30, "bold"), bg="white", fg="navyblue")
        title.place(x=250, y=50)

        #variable
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        email = Label(login_frame, text="Email", font=("times new roman", 18, "bold"), bg="white", fg="navyblue").place(x=250, y=150)
        self.txtuser = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txtuser.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text="Password", font=("times new roman", 18, "bold"), bg="white", fg="navyblue").place(x=250, y=250)
        self.txtpwd = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txtpwd.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, cursor="hand2", command=self.reg, text="Sign up ", font=("times new roman", 14), bg="white", bd=0, fg="navyblue").place(x=250, y=330)

        btn_forgetpwd = Button(login_frame, cursor="hand2", command=self.forget_pwd, text="Forgot password?", font=("times new roman", 14), bg="white", bd=0, fg="navyblue").place(x=500, y=330)

        btn_login = Button(login_frame, text="Log in", command=self.login, font=("times new roman", 20, "bold"), fg="white", cursor="hand2", bg="navyblue").place(x=250, y=380, width=180, height=40)




        # Clock
        now = datetime.now()
        # dd/mm/YY
        dt_string = now.strftime("%d/%m/%Y - %H:%M:%S")
        self.lbl = Label(self.root, text=dt_string, font=("times new roman", 20, ), fg="white", compound=BOTTOM, bg="#081923", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)

        self.working()


    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)

        # For Clock Image
        bg = Image.open("D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\clock_new4.png")
        bg = bg.resize((300, 300), Image.LANCZOS)
        clock.paste(bg, (50, 50))


        origin = 200, 200
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill="#DF005E", width=4)

        # For Clock hand ( Min Line) Image
        draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))), fill="white", width=3)

        # For Clock hand ( Second Line) Image
        draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))), fill="yellow", width=2)

        # For circle in clock
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")

        clock.save("clock_new4.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h/12)*360
        min_ = (m/60)*360
        sec_ = (s/60)*360

        # print(h, m, s)
        # print(hr, min_, sec_)
        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="clock_new4.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        self.new_window.state('zoomed')

    #  THis function is for open login frame
    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All fields required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Face Recognition Management System")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(user='root', password='root',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid email and password!")
            else:
                open_min=messagebox.askyesno("Admin","Succesful! Do yo want continue")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Choose a security question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please enter your answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please enter a new password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(user='root', password='root',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer!",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been reset, Please login with a new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(user='root', password='root',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please enter a valid email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget MK")
                self.root2.geometry("350x450+80+120")
                l=Label(self.root2,text="Forgot password",font=("times new roman",25,"bold"),fg="#fff",bg="#002B53")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select a security question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=45,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Date of birth","Nick Name","Favorite books")
                self.combo_security.current(0)
                self.combo_security.place(x=45,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=45,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=45,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="new password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=45,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=45,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset pass",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=45,y=300,width=270,height=35)


            

# =====================main program Face deteion system====================

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.title("Attendance management system using facial recognition")
        
# This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\banner2.png")
        img=img.resize((1280,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1280,height=130)

        # backgorund image 
        bg1=Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\bg4.jpg")
        bg1=bg1.resize((1280,500),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=145,width=1280,height=500)


        #title section
        title_lb1 = Label(bg_img,text="Face recognition attendance system",font=("verdana",20,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0,y=0,width=1280,height=40)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn = Image.open(
            r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\std1.jpg")
        std_img_btn = std_img_btn.resize((220, 220), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.student_pannels, image=self.std_img1, cursor="hand2")
        std_b1.place(x=220, y=70, width=220, height=180)

        std_b1_1 = Button(bg_img, command=self.student_pannels, text="Student", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=220, y=220, width=220, height=40)

        # Detect Face  button 2
        det_img_btn = Image.open(
            r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\det1.jpg")
        det_img_btn = det_img_btn.resize((220, 220), Image.LANCZOS)
        self.det_img1 = ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img, command=self.face_rec, image=self.det_img1, cursor="hand2", )
        det_b1.place(x=480, y=70, width=220, height=180)

        det_b1_1 = Button(bg_img, command=self.face_rec, text="Recognition", cursor="hand2",font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        det_b1_1.place(x=480, y=220, width=220, height=40)

        # Attendance System  button 3
        att_img_btn = Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\att.jpg")
        att_img_btn = att_img_btn.resize((220, 220), Image.LANCZOS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img, command=self.attendance_pannel, image=self.att_img1, cursor="hand2", )
        att_b1.place(x=740, y=70, width=220, height=180)

        att_b1_1 = Button(bg_img, command=self.attendance_pannel, text="Attendance", cursor="hand2",font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        att_b1_1.place(x=740, y=220, width=220, height=40)

        tra_img_btn = Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\tra1.jpg")
        tra_img_btn = tra_img_btn.resize((220, 220), Image.LANCZOS)
        self.tra_img1 = ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img, command=self.train_pannels, image=self.tra_img1, cursor="hand2", )
        tra_b1.place(x=220, y=270, width=220, height=180)

        tra_b1_1 = Button(bg_img, command=self.train_pannels, text="Train Data", cursor="hand2",font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        tra_b1_1.place(x=220, y=420, width=220, height=40)

        # Photo   button 6
        pho_img_btn = Image.open( r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\dataset.jpg")
        pho_img_btn = pho_img_btn.resize((220, 220), Image.LANCZOS)
        self.pho_img1 = ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img, command=self.open_img, image=self.pho_img1, cursor="hand2", )
        pho_b1.place(x=480, y=270, width=220, height=180)

        pho_b1_1 = Button(bg_img, command=self.open_img, text="Data set", cursor="hand2", font=("tahoma", 15, "bold"),bg="white", fg="navyblue")
        pho_b1_1.place(x=480, y=420, width=220, height=40)

        # exit   button 8
        exi_img_btn = Image.open( r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\exi.jpg")
        exi_img_btn = exi_img_btn.resize((220, 220), Image.LANCZOS)
        self.exi_img1 = ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img, command=self.Close, image=self.exi_img1, cursor="hand2", )
        exi_b1.place(x=740, y=270, width=220, height=180)

        exi_b1_1 = Button(bg_img, command=self.Close, text="Exit", cursor="hand2", font=("tahoma", 15, "bold"),bg="white", fg="navyblue")
        exi_b1_1.place(x=740, y=420, width=220, height=40)
# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        self.new_window.state('zoomed')

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        self.new_window.state('zoomed')
        
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        self.new_window.state('zoomed')

    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        self.new_window.state('zoomed')


    def Close(self):
        root.destroy()


if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()
    