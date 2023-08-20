import mysql.connector
import os
import cv2
import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Attendance management system using facial recognition")

        # This part is image labels setting start
        # first header image
        img = Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\banner2.png")
        img = img.resize((1280, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1280, height=130)

        # background image
        bg1 = Image.open(r"D:\projects\Attendance_Management_System_Using_Face_Recognition-main\Images_GUI\bg-reg.png")
        bg1 = bg1.resize((1200, 520), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=180, width=1280, height=500)

        # title section
        title_lb1 = Label(bg_img, text="Face recognition System", font=("verdana", 20, "bold"), bg="navyblue",fg="white")
        title_lb1.place(x=0, y=0, width=1280, height=40)


        std_b1_1 = Button(bg_img, command=self.face_recog, text="Face_recongnization", cursor="hand2",font=("tahoma", 12, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=255, y=330, width=180, height=35)

    # =====================Attendance===================
    def mark_attendance(self, n,r,i):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])


            if ((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, present")


    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(user='root', password='root', host='localhost', database='face_recognizer', port=3306)
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_ID=" + str(id))
                n = cursor.fetchone()
                n = "+".join(n)

                cursor.execute("select Roll_No from student where Student_ID=" + str(id))
                r = cursor.fetchone()
                r = "+".join(r)

                cursor.execute("select Student_ID from student where Student_ID=" + str(id))
                i = cursor.fetchone()
                i = "+".join(i)


                if confidence > 77:
                    cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(n,r,i)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)

                coord=[x,y,w,y]

            return coord


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(1)


        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)

            cv2.imshow("Welcome",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()