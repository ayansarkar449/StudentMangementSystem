from tkinter import *
from tkinter import ttk, messagebox,filedialog
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
import os
import time

class student:
    def __init__(self, root):
        self.root = root
        self.width = self.root.winfo_screenwidth() - 2
        self.height = self.root.winfo_screenheight() - 80
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        self.root.title("STUDENT")
        self.root.iconbitmap()

        # veriable
        self.V1 = StringVar()
        self.V2 = StringVar()
        self.V3 = StringVar()
        self.V4 = StringVar()
        self.V5 = StringVar()
        self.V6 = StringVar()
        self.V7 = StringVar()
        self.V8 = StringVar()
        self.V9 = StringVar()
        self.V10 = StringVar()
        self.V11 = StringVar()
        self.V12 = StringVar()
        self.V13 = StringVar()
        self.V14 = StringVar()
        self.V15 = StringVar()
        self.V16 = StringVar()

        ###################################     farme  ########################################################################
        # main fram, bg="#CBC3E3", bg="#8FBC8F"

        main_frame = Frame(self.root, bd=10, relief=RIDGE, width=self.width, height=self.height)
        main_frame.place(x=0, y=0, width=self.width, height=self.height)

        # inerfram1
        iner_frame1 = Frame(main_frame, bd=2, relief=RIDGE, width=self.width - 18, height=170)
        iner_frame1.place(x=0, y=0, width=self.width - 18, height=170)
        # inerfram2
        iner_frame2 = Frame(main_frame, bd=2, relief=RIDGE, width=self.width - 18, height=50)
        iner_frame2.place(x=0, y=170, width=self.width - 18, height=50)
        # inerfram3
        iner_frame3 = Frame(main_frame, bd=2, relief=RIDGE, width=self.width - 20,
                            height=self.height - (self.height // 5) - 70)
        iner_frame3.place(x=0, y=220, width=self.width - 18, height=self.height - 240)

        ##############################################  image  #######################################
        # image1
        self.image = ImageTk.PhotoImage(
            (Image.open("photo//9th.jpg")).resize(((self.width // 4) - 11, 160), Image.ANTIALIAS))
        self.my = Button(iner_frame1, command=lambda: self.fileee(), image=self.image, cursor="hand2")
        self.my.grid(row=0, column=0)
        # image 2
        self.image1 = ImageTk.PhotoImage(
            (Image.open("photo//8th.jpg")).resize(((self.width // 4) - 11, 160), Image.ANTIALIAS))
        self.my1 = Button(iner_frame1, command=self.fileee1, image=self.image1, cursor="hand2", pady=160)
        self.my1.grid(row=0, column=1)
        # image 3
        self.image2 = ImageTk.PhotoImage(
            (Image.open("photo//6th.jpg")).resize(((self.width // 4) - 11, 160), Image.ANTIALIAS))
        self.my2 = Button(iner_frame1, command=self.fileee2, image=self.image2, cursor="hand2", pady=160)
        self.my2.grid(row=0, column=2)
        # image 4
        self.image3 = ImageTk.PhotoImage(
            (Image.open("photo//10th.jpg")).resize(((self.width // 4) - 11, 160), Image.ANTIALIAS))
        self.my3 = Button(iner_frame1, command=self.fileee3, image=self.image2, cursor="hand2", pady=160)
        self.my3.grid(row=0, column=3)

        ########################    title     ######################
        title1 = Label(iner_frame2, text="STUDENT MANAGEMENT SYSTEM", font=("bold", 30), bg="green", fg="orange")
        title1.place(x=0, y=0, width=self.width - 122, height=46)

        self.label16 = Label(iner_frame2, font=("arial", 12, "bold"), bg="green",
                             fg="black")
        self.label16.place(x=self.width - 122, y=0, width=100, height=46)
        self.my_time()

        ########################### background image    #####################################
        self.image4 = ImageTk.PhotoImage(
            (Image.open("photo//10th.jpg")).resize((self.width - 24, self.height - 246), Image.ANTIALIAS))
        bbgmy4 = Label(iner_frame3, image=self.image4, pady=160, bd=2, relief=RIDGE)
        bbgmy4.place(x=0, y=0)

        ########################    right and left frame     ######################

        # left frame table
        left_frame = LabelFrame(bbgmy4, text="Register new student", bd=2, relief=RIDGE, font=("bold", 15),
                                bg="#CBC3E3",
                                fg="black")
        left_frame.place(x=30, y=60, width=(self.width - 60) // 3, height=600)

        my_fram1 = Frame(left_frame, bd=3, relief=RIDGE, bg="#8FBC8F", width=(self.width - 60) / 3, height=280)
        my_fram1.grid(row=0, column=0, sticky=W)

        my_fram2 = Frame(left_frame, bd=2, relief=RIDGE, bg="orange", width=(self.width - 80) / 3, height=30)
        my_fram2.grid(row=1, column=0, sticky=W)

        my_fram3 = Frame(left_frame, bd=2, relief=RIDGE, bg="white", width=(self.width - 60) / 3 - 5, height=305)
        my_fram3.grid(row=3, column=0, sticky=W)

        # self.label16 = Label(my_fram3, font=("arial", 12, "bold"), bg="green",
        # fg="black")
        # self.label16.grid()
        # self.my_time()

        # rightframeF

        right_frame = LabelFrame(bbgmy4, text="Student Details", bd=2, relief=RIDGE, font=("bold", 15), bg="#8FBC8F",
                                 fg="red")
        right_frame.place(x=40 + (self.width - 60) // 3, y=60, width=(self.width - 80) * 2 // 3, height=600)

        my_fram4 = Frame(right_frame, bd=2, relief=RIDGE, bg="orange", width=2 * (self.width - 88) / 3, height=50)
        my_fram4.place(x=0, y=0, width=2 * (self.width - 88) / 3, height=40)

        # inner fram4
        my_fram5 = Frame(right_frame, bd=4, relief=RIDGE, bg="#CBC3E3", width=2 * (self.width - 88) / 3, height=532)
        my_fram5.place(x=0, y=40, width=2 * (self.width - 88) / 3, height=533)

        ################### left table content   ############################

        label1 = Label(my_fram1, text="First Name: ", font=("arial", 12, "bold"), bg="#CBC3E3", fg="black")
        label1.grid(row=0, column=0, sticky=W)

        entry1 = ttk.Entry(my_fram1, textvariabl=self.V2, font=("arial", 12, "bold"), width=19)
        entry1.grid(row=0, column=1, padx=2, pady=2, sticky=W)
        # lastname
        label2 = Label(my_fram1, text="Last Name:", font=("arial", 12, "bold"), bg="#CBC3E3", fg="black")
        label2.grid(row=0, column=2, sticky=W)

        entry2 = ttk.Entry(my_fram1, textvariabl=self.V3, font=("arial", 12, "bold"), width=19)

        entry2.grid(row=0, column=3, padx=2, pady=2, sticky=W)
        # student_id_no
        label3 = Label(my_fram1, text="Student Id No:", font=("arial", 12, "bold"), bg="#CBC3E3",fg="black")
        label3.grid(row=1, column=0, sticky=W)

        entry3 = ttk.Entry(my_fram1, textvariabl=self.V1, font=("arial", 12, "bold"), width=19, state="readonly")
        entry3.grid(row=1, column=1, padx=2, pady=2, sticky=W)
        # roll_number
        label4 = Label(my_fram1, text="Roll Number:", font=("arial", 12, "bold"), bg="#CBC3E3", fg="black")
        label4.grid(row=1, column=2, sticky=W)

        entry4 = ttk.Entry(my_fram1, textvariabl=self.V4, font=("arial", 12, "bold"), width=19)
        entry4.grid(row=1, column=3, padx=2, pady=2, sticky=W)
        # dob
        label5 = Label(my_fram1, text="DOB: ", font=("arial", 12, "bold"), bg="#CBC3E3", fg="black")
        label5.grid(row=2, column=0, sticky=W)

        entry5 = ttk.Entry(my_fram1, textvariabl=self.V5, font=("arial", 12, "bold"), width=19)
        entry5.grid(row=2, column=1, padx=2, pady=2, sticky=W)
        # gender
        label6 = Label(my_fram1, text="Gender:  ", font=("arial", 12, "bold"), bg="#CBC3E3", fg="black")
        label6.grid(row=2, column=2, sticky=W)

        combo1 = ttk.Combobox(my_fram1, textvariabl=self.V6, font=("arial", 12, "bold"), width=17, state="readonly")
        combo1["value"] = ("", "M", "F", "Other")
        combo1.current(0)
        combo1.grid(row=2, column=3, padx=2, pady=2, sticky=W)
        # department
        label7 = Label(my_fram1, text="Department:", font=("arial", 12, "bold"), bg="#CBC3E3", fg="black")
        label7.grid(row=3, column=0, sticky=W)

        combo2 = ttk.Combobox(my_fram1, textvariabl=self.V7, font=("arial", 12, "bold"), width=17, state="readonly")
        combo2["value"] = (
            "", "Math", "Computer", "Botany", "Zoology", "Physics", "Chemistry", "English", "Bengali", "History",
            "Geography")
        combo2.current(0)
        combo2.grid(row=3, column=1, padx=2, pady=2, sticky=W)
        # Group
        label8 = Label(my_fram1, text="Group:", font=("arial", 12, "bold"), bg="#CBC3E3", fg="black")
        label8.grid(row=3, column=2, sticky=W)

        combo3 = ttk.Combobox(my_fram1, textvariabl=self.V8, font=("arial", 12, "bold"), width=17, state="readonly")
        combo3["value"] = ("", "A", "B", "C", "D")
        combo3.current(0)
        combo3.grid(row=3, column=3, padx=2, pady=2, sticky=W)
        # year
        label9 = Label(my_fram1, text="Year:", font=("arial", 12, "bold"), bg="#CBC3E3", fg="black")
        label9.grid(row=4, column=0, sticky=W)

        combo4 = ttk.Combobox(my_fram1, textvariabl=self.V9, font=("arial", 12, "bold"), width=17, state="readonly")
        combo4["value"] = ("2021-22", "2020-21", "2019-20")
        combo4.current(0)
        combo4.grid(row=4, column=1, padx=2, pady=2, sticky=W)
        # sem
        label10 = Label(my_fram1, text="Semester:", font=("arial", 12, "bold"), bg="#CBC3E3", fg="black")
        label10.grid(row=4, column=2, sticky=W)

        combo5 = ttk.Combobox(my_fram1, textvariabl=self.V10, font=("arial", 12, "bold"), width=17,
                              state="readonly")
        combo5["value"] = ("", "2nd", "1st")
        combo5.current(0)
        combo5.grid(row=4, column=3, padx=2, pady=2, sticky=W)
        # email
        label11 = Label(my_fram1, text="Email Id:", font=("arial", 12, "bold"), bg="#CBC3E3", fg="black")
        label11.grid(row=5, column=0, sticky=W)
        entry6 = ttk.Entry(my_fram1, textvariabl=self.V11, font=("arial", 12, "bold"), width=19)
        entry6.grid(row=5, column=1, padx=2, pady=2, sticky=W)
        # Phone
        label12 = Label(my_fram1, text="Phone Number:", font=("arial", 12, "bold"), bg="#CBC3E3",
                        fg="black")
        label12.grid(row=5, column=2, sticky=W)

        entry7 = ttk.Entry(my_fram1, textvariabl=self.V12, font=("arial", 12, "bold"), width=19)
        entry7.grid(row=5, column=3, padx=2, pady=2, sticky=W)
        # adress
        label13 = Label(my_fram1, text="Address:", font=("arial", 12, "bold"), bg="#CBC3E3", fg="black")
        label13.grid(row=6, column=0, sticky=W)

        entry8 = ttk.Entry(my_fram1, textvariabl=self.V13, font=("arial", 12, "bold"), width=19)
        entry8.grid(row=6, column=1, padx=2, pady=2, sticky=W)
        # teacher name
        label14 = Label(my_fram1, text="Teacher Name:  ", font=("arial", 12, "bold"), bg="#CBC3E3",
                        fg="black")
        label14.grid(row=6, column=2, sticky=W)

        entry9 = ttk.Entry(my_fram1, textvariabl=self.V14, font=("arial", 12, "bold"), width=19)
        entry9.grid(row=6, column=3, sticky=W)

        ##############################  right frame content     #############
        # label1
        label15 = Label(my_fram4, text="Search by:", width=(2 * (self.width - 88) // 150), font=("arial", 12, "bold"),
                        bg="black", fg="white")
        label15.grid(row=0, column=0, padx=2, pady=2, sticky=W)
        # combo
        combo6 = ttk.Combobox(my_fram4, textvariabl=self.V15, font=("arial", 12, "bold"),
                              width=(2 * (self.width - 88) // 150),
                              state="readonly")
        combo6["value"] = (
            "", "Student_Id", "First_Name", "Last_Name", "Roll_Number ", "DOB", "Gender",
            "Department",
            "Course", "Year", "Semester", "Email_Id", "Phone_Number", "Address", "Teacher_Name")
        combo6.current(0)
        combo6.grid(row=0, column=1, padx=2, pady=2, sticky=W)
        # entry
        entry7 = ttk.Entry(my_fram4, textvariabl=self.V16, font=("arial", 12, "bold"),
                           width=(2 * (self.width - 88) // 150) - 1)
        entry7.grid(row=0, column=2, padx=2, pady=2, sticky=W)

        # scrollbar
        self.scroll_x = ttk.Scrollbar(my_fram5, orient=HORIZONTAL)
        self.scroll_y = ttk.Scrollbar(my_fram5, orient=VERTICAL)
        # table
        self.student_tabel = ttk.Treeview(my_fram5, column=("Student Id No",
                                                            "First Name", "Last Name", "Roll Number", "DOB", "Gender",
                                                            "Department",
                                                            "Group",
                                                            "Year", "Semester", "Email Id", "Phone Number", "Address",
                                                            "Teacher Name"), xscrollcommand=self.scroll_x.set,
                                          yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.student_tabel.xview)
        self.scroll_y.config(command=self.student_tabel.yview)
        # show table heading
        self.student_tabel.heading("Student Id No", text="Student Id No")
        self.student_tabel.heading("First Name", text="First Name")
        self.student_tabel.heading("Last Name", text="Last Name")
        self.student_tabel.heading("Roll Number", text="Roll Number")
        self.student_tabel.heading("DOB", text="DOB")
        self.student_tabel.heading("Gender", text="Gender")
        self.student_tabel.heading("Department", text="Department")
        self.student_tabel.heading("Group", text="Group")
        self.student_tabel.heading("Year", text="Year")
        self.student_tabel.heading("Semester", text="Semester")
        self.student_tabel.heading("Email Id", text="Email Id")
        self.student_tabel.heading("Phone Number", text="Phone Number")
        self.student_tabel.heading("Address", text="Address")
        self.student_tabel.heading("Teacher Name", text="Teacher Name")
        # table content showing
        self.student_tabel["show"] = "headings"
        # table width set
        self.student_tabel.column("First Name", width=100)
        self.student_tabel.column("Last Name", width=100)
        self.student_tabel.column("Student Id No", width=100)
        self.student_tabel.column("Roll Number", width=100)
        self.student_tabel.column("DOB", width=100)
        self.student_tabel.column("Gender", width=100)
        self.student_tabel.column("Department", width=100)
        self.student_tabel.column("Group", width=100)
        self.student_tabel.column("Year", width=100)
        self.student_tabel.column("Semester", width=100)
        self.student_tabel.column("Email Id", width=100)
        self.student_tabel.column("Phone Number", width=100)
        self.student_tabel.column("Address", width=100)
        self.student_tabel.column("Teacher Name", width=100)

        self.student_tabel.pack(fill=BOTH, expand=2)
        self.student_tabel.bind("<ButtonRelease>", self.get_cursor)

        self.show_data()

        ########################### button ##########

        ###left

        button1 = Button(my_fram2, text="Save", command=self.add_data, height=2, width=11, font=("arial", 12, "bold"),
                         bg="blue",
                         fg="white")
        button1.grid(row=0, column=0, padx=2, pady=2, sticky=W)

        button2 = Button(my_fram2, text="Update", command=self.update, height=2, width=11, font=("arial", 12, "bold"),
                         bg="blue",
                         fg="white")
        button2.grid(row=0, column=1, padx=2, pady=2, sticky=W)

        button3 = Button(my_fram2, text="Delete", command=self.delete, height=2, width=10, font=("arial", 12, "bold"),
                         bg="blue",
                         fg="white")
        button3.grid(row=0, column=2, padx=2, pady=2, sticky=W)

        button4 = Button(my_fram2, text="Refresh", command=self.refresh, height=2, width=11, font=("arial", 12, "bold"),
                         bg="blue",
                         fg="white")
        button4.grid(row=0, column=3, padx=2, pady=1, sticky=W)

        button7 = Button(my_fram2, text="Exit", command=self.exit, height=2, width=11, font=("arial", 12, "bold"),
                         bg="blue",
                         fg="white")
        button7.grid(row=0, column=4, padx=2, pady=2, sticky=W)

        # right
        button5 = Button(my_fram4, command=self.search, text="Search", width=(2 * (self.width - 88) // 150),
                         font=("arial", 12, "bold"), bg="blue",
                         fg="white")
        button5.grid(row=0, column=3, padx=2, pady=2, sticky=W)
        # Button2
        button6 = Button(my_fram4, command=self.search_all, text="Search All", width=(2 * (self.width - 88) // 150),
                         font=("arial", 12, "bold"),
                         bg="blue", fg="white")
        button6.grid(row=0, column=4, padx=2, pady=2, sticky=W)

    def search_all(self):
        self.V15.set("")
        self.V16.set("")
        self.show_data()

    def search(self):
        if self.V15.get() == "" :
            messagebox.showerror("Error please select something")
        elif self.V16.get() == "":
            messagebox.showerror(" please type something")
        else:
            try:
                db = mysql.connector.connect(host='localhost',
                                             user='root1',
                                             password='1234',
                                             database='student_management_system'
                                             )
                my_cu = db.cursor()
                my_cu.execute(
                    "SELECT * FROM student_data WHERE " + str(self.V15.get()) + " LIKE '%" + str(self.V16.get()) + "%'")
                data = my_cu.fetchall()
                if len(data) != 0:
                    self.student_tabel.delete(*self.student_tabel.get_children())
                    for i in data:
                        self.student_tabel.insert("", END, values=i)

                db.commit()
                db.close()

            except Exception as es:
                messagebox.showerror("error", f"{es}")

    def refresh(self):
        for i in range(1,15):
            eval(f"self.V{i}.set(\"\")")


    def delete(self):
        if self.V1.get() == "" or self.V2.get() == "" or self.V3.get() == "":
            messagebox.showerror("Error,Filds can not be empty")
        else:
            try:
                data = messagebox.askyesno("Do you want to delete?", parent=self.root)
                if data > 0:
                    db = mysql.connector.connect(host='localhost',
                                                 user='root1',
                                                 password='1234',
                                                 database='student_management_system'

                                                 )
                    my_cu = db.cursor()
                    my_cu.execute("DELETE FROM student_data  WHERE Student_Id = %s", (self.V1.get(),))
                else:
                    if not data:
                        return
                db.commit()
                self.show_data()
                self.refresh()
                db.close()
                messagebox.showinfo("Remove successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f"{es}")

    def update(self):
        if self.V1.get() == "" or self.V2.get() == "" or self.V3.get() == "":
            messagebox.showerror("Error,Filds can not be empty")
        else:
            try:
                data = messagebox.askyesno("Do you want to update?", parent=self.root)
                if data > 0:
                    db = mysql.connector.connect(host='localhost',
                                                 user='root1',
                                                 password='1234',
                                                 database='student_management_system'

                                                 )
                    id =self.V1.get()
                    name=self.V2.get()
                    lname =self.V3.get()
                    id1=id[0:4]+name[0]+lname[0]+id[6:]
                    my_cu=db.cursor()
                    my_cu.execute("UPDATE student_data SET Student_Id = %s, First_Name =%s , Last_Name = %s, Roll_Number = %s, DOB = %s,"
                                  "Gender = %s, Department = %s, Group1 = %s, Year = %s, Semester = %s, Email_Id = %s, "
                                  "Phone_Number = %s, Address = %s, Teacher_Name = %s WHERE Student_Id = %s", (
                                      id1,
                                      self.V2.get(),
                                      self.V3.get(),
                                      self.V4.get(),
                                      self.V5.get(),
                                      self.V6.get(),
                                      self.V7.get(),
                                      self.V8.get(),
                                      self.V9.get(),
                                      self.V10.get(),
                                      self.V11.get(),
                                      self.V12.get(),
                                      self.V13.get(),
                                      self.V14.get(),
                                      self.V1.get()

                                  ))
                else:
                    if not data:
                        return
                db.commit()
                self.show_data()
                self.V1.set(id1)

                db.close()

                messagebox.showinfo("UPDATE successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f"{es}")

    def get_cursor(self, event=""):
        cursor_row = self.student_tabel.focus()
        content = self.student_tabel.item(cursor_row)
        data = content["values"]
        for i in range(1,15):
            eval(f"self.V{i}.set({data}[{i}-1])")
        """  self.V1.set(data[0])
        self.V2.set(data[1])
        self.V3.set(data[2])
        self.V4.set(data[3])
        self.V5.set(data[4])
        self.V6.set(data[5])
        self.V7.set(data[6])
        self.V8.set(data[7])
        self.V9.set(data[8])
        self.V10.set(data[9])
        self.V11.set(data[10])
        self.V12.set(data[11])
        self.V13.set(data[12])
        self.V14.set(data[13])"""

    def show_data(self):
        db = mysql.connector.connect(host='localhost',
                                     user='root1',
                                     password='1234',
                                     database='student_management_system'

                                     )
        my_cu = db.cursor()
        my_cu.execute("SELECT * FROM student_data")
        data = my_cu.fetchall()
        if len(data) != 0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in data:
                self.student_tabel.insert("", END, values=i)
            db.commit()
        db.close()

    def add_data(self):
        if self.V2.get() == "" or self.V3.get() == "":
            messagebox.showerror("Error,Filds can not be empty")
        else:
            try:
                data = messagebox.askyesno("Do you want to save it?", parent=self.root)
                if data > 0:
                    db = mysql.connector.connect(host='localhost',
                                                 user='root1',
                                                 password='1234',
                                                 database='student_management_system'

                                                 )
                    my_cu = db.cursor()
                    my_cu.execute("INSERT INTO student_data (First_Name, Last_Name, Roll_Number , DOB, Gender , Department , Group1 , Year , Semester , Email_Id ,Phone_Number , Address, Teacher_Name) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (
                                   self.V2.get(),
                                   self.V3.get(),
                                   self.V4.get(),
                                   self.V5.get(),
                                   self.V6.get(),
                                   self.V7.get(),
                                   self.V8.get(),
                                   self.V9.get(),
                                   self.V10.get(),
                                   self.V11.get(),
                                   self.V12.get(),
                                   self.V13.get(),
                                   self.V14.get()
                                   ))
                else:
                    if not data:
                        return
                db.commit()
                self.show_data()
                db.close()
                messagebox.showinfo("Students successfully register", parent=self.root)
            except Exception as es:
                messagebox.showerror("error", f"{es}")

    def exit(self):
        data = messagebox.askyesno("Do you want to leave?")
        if data > 0:
            self.root.destroy()

    def my_time(self):
        time = datetime.now().strftime("%H:%M:%S \n %a %b %d")
        self.label16.config(text=time)
        self.label16.after(1000, self.my_time)

    ##3##### open image
    def fileee(self):
        filer = filedialog.askopenfilename(initialdir=os.getcwd(), title="open images",
                                           filetypes=(("JPG File", "*.jpg"), ("All Files", "*.*")))
        x = Image.open(filer)
        y = x.resize(((self.width // 4) - 11, 160), Image.ANTIALIAS)
        self.funimage = ImageTk.PhotoImage(y)
        self.my.config(image=self.funimage)

    def fileee1(self):
        filer = filedialog.askopenfilename(initialdir=os.getcwd(), title="open images",
                                           filetypes=(("JPG File", "*.jpg"), ("All Files", "*.*")))
        x = Image.open(filer)
        y = x.resize(((self.width // 4) - 11, 160), Image.ANTIALIAS)
        self.funimage1 = ImageTk.PhotoImage(y)
        self.my1.config(image=self.funimage1)

    def fileee2(self):
        filer = filedialog.askopenfilename(initialdir=os.getcwd(), title="open images",
                                           filetypes=(("JPG File", "*.jpg"), ("All Files", "*.*")))
        x = Image.open(filer)
        y = x.resize(((self.width // 4) - 11, 160), Image.ANTIALIAS)
        self.funimage2 = ImageTk.PhotoImage(y)
        self.my2.config(image=self.funimage2)

    def fileee3(self):
        filer = filedialog.askopenfilename(initialdir=os.getcwd(), title="open images",
                                           filetypes=(("JPG File", "*.jpg"), ("All Files", "*.*")))
        x = Image.open(filer)
        y = x.resize(((self.width // 4) - 11, 160), Image.ANTIALIAS)
        self.funimage3 = ImageTk.PhotoImage(y)
        self.my3.config(image=self.funimage3)


if __name__ == "__main__":
    root = Tk()
    student(root)
    root.mainloop()