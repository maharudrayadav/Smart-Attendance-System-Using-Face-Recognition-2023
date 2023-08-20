from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.title("Attendance management system using facial recognition")

# This part is image labels setting start
        # first header image
        std_img_btn=Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\banner2.png")

        std_img_btn=std_img_btn.resize((1280, 130), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(std_img_btn)

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
        title_lb1 = Label(bg_img,text=" Face recognition attendance system",font=("verdana",20,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0,y=0,width=1280,height=40)

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # student button 1
        std_img_btn=Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\std1.jpg")
        std_img_btn=std_img_btn.resize((220,220),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=220,y=70,width=220,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=220,y=220,width=220,height=40)

        # Detect Face  button 2
        det_img_btn=Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((220,220),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=70,width=220,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Recognition",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=480,y=220,width=220,height=40)

        # Attendance System  button 3
        att_img_btn=Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\att.jpg")
        att_img_btn=att_img_btn.resize((220,220),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=740,y=70,width=220,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=740,y=220,width=220,height=40)


        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
        # Train   button 5
        tra_img_btn=Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\tra1.jpg")
        tra_img_btn=tra_img_btn.resize((220,220),Image.LANCZOS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=220,y=270,width=220,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Train Data",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=220,y=420,width=220,height=40)

        # Photo   button 6
        pho_img_btn=Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\dataset.jpg")
        pho_img_btn=pho_img_btn.resize((220,220),Image.LANCZOS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=480,y=270,width=220,height=180)

        pho_b1_1 = Button(bg_img,command=self.open_img,text="Data set",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=480,y=420,width=220,height=40)


        # exit   button 8
        exi_img_btn=Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\exi.jpg")
        exi_img_btn=exi_img_btn.resize((220,220),Image.LANCZOS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=740,y=270,width=220,height=180)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=740,y=420,width=220,height=40)


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
    obj=Face_Recognition_System(root)
    root.mainloop()
