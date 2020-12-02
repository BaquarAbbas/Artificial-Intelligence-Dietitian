from tkinter import *
from tkinter import messagebox
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def getMeal():
    global prediction
    global e
    df = pd.read_csv('Diet.csv', encoding='cp1252')

    # print(df.head())

    X_train = df.loc[:, 'Gender':'Exercise']
    Y_train = df.loc[:, 'Diet']

    # The actual decision tree classifier
    tree = DecisionTreeClassifier(max_leaf_nodes=5, random_state=0)

    # Train the model
    tree.fit(X_train, Y_train)

    if Gender == 'Male':
        G = 1
    else:
        G = 2
    if Exercise == 'Sedentary':
        e = 1
    elif Exercise == 'Lightly Active':
        e = 2
    elif Exercise == 'Moderate':
        e = 3
    elif Exercise == 'Very Active':
        e = 4
    elif Exercise == 'SuperActive':
        e = 5
    prediction = tree.predict([[G, Age, e]])

    # print('Printing the prediction: ')

    # print(prediction)


def getDiet():
    global cal
    global txt2
    global Name
    global Gender
    global Exercise
    global Age
    global Height
    global Weight
    global b2
    global L3
    global cal

    Name = e1.get()
    if len(Name) == 0:
        messageBox()

    if var_chk.get() == 1:
        Gender = "Male"
    else:
        Gender = "Female"
    Age = spin.get()
    Height = e2.get()
    if len(Height) == 0:
        messageBox()
    Weight = e3.get()
    if len(Weight) == 0:
        messageBox()
    Exercise = c.get()
    if len(Exercise) == 0 or Exercise == "Select":
        messageBox()

    if Gender == 'Male':
        cal = float()
        cal = 88.362 + (13.397 * float(Weight)) + (4.799 * float(Height)) - (5.677 * float(Age))
        # print(cal)
    elif Gender == 'Female':
        cal = float()
        cal = 447.593 + (9.247 * float(Weight)) + (3.098 * float(Height)) - (4.330 * float(Age))

    if Exercise == 'Sedentary':
        cal = cal * 1.2

    elif Exercise == 'Lightly Active':
        cal = cal * 1.375

    elif Exercise == 'Moderate':
        cal = cal * 1.55

    elif Exercise == 'Very Active':
        cal = cal * 1.725

    elif Exercise == 'SuperActive':
        cal = cal * 1.9

    L4 = Label(f2, width=35, text='Your Calories ', font=('Montserrat', 15, 'bold'), bg="#9AD4D6")
    L4.grid(row=0)
    txt1 = Text(f2, width=45, height=7, wrap=WORD, relief=SUNKEN)
    txt1.insert(0.0, '\n')
    txt1.insert(0.0, "Calories: " + str(cal) + '\n')
    txt1.insert(0.0, "Exercise: " + Exercise + '\n')
    txt1.insert(0.0, 'Weight: ' + Weight + 'Kgs' + '\n')
    txt1.insert(0.0, 'Height: ' + Height + 'cms' + '\n')
    txt1.insert(0.0, 'Age: ' + Age + 'Years' + '\n')
    txt1.insert(0.0, 'Gender: ' + Gender + '\n')
    txt1.insert(0.0, 'Name: ' + Name + '\n')
    txt1.grid(row=1)

    getMeal()

    L3 = Label(f3, width=35, text='Your Meal Plan ', font=('Montserrat', 15, 'bold'), bg="#9AD4D6")
    L3.grid(row=2)

    txt2 = Text(f3, width=55, height=5, wrap=WORD, relief=SUNKEN)
    txt2.insert(0.0, 'Meal Plan ' + prediction + '\n')
    txt2.grid(row=3)

    b2 = Button(f3, text="Reset", bg='#101935', fg='#F2FDFF', font=('Proxima Nova', 12), command=reset)
    b2.grid(row=4)


def messageBox():
    messagebox.showwarning("warning", "Please Enter Your Deatils")
    reset()


def mainWindow():
    global screen1
    global L1
    global L2
    global L3
    global L4
    global f1
    global f2
    global f3
    global l1
    global l2
    global l3
    global l4
    global l5
    global l6
    global l7
    global e1
    global e2
    global e3
    global rd1
    global rd2
    global txt1
    global txt2
    global spin
    global droplist
    screen1 = Tk()
    screen1.title("Dietitian")
    screen1.geometry("850x525")
    screen1.iconbitmap('diet1.ico')
    screen1.configure(bg="#9AD4D6")
    screen1.resizable(FALSE, FALSE)

    L1 = Label(screen1, height=1, width=53, font=("Berlin Sans FB", 24), text="Dietitian Application", compound=LEFT,
               fg="#494949", bg="#9AD4D6")
    L1.grid(row=1, column=1)
    # User Details
    f1 = Frame(screen1, bg="#9AD4D6", padx=40, pady=40)
    L2 = Label(f1, text='Fill Your Details', font=('Montserrat', 16, 'bold'), bg="#9AD4D6", fg="#0C0910")
    L2.grid(row=0)
    l1 = Label(f1, text='Name:', font=('Proxima Nova', 14), bg="#9AD4D6")
    l2 = Label(f1, text='Gender:', font=('Proxima Nova', 14), bg="#9AD4D6")
    l3 = Label(f1, text='Age:', font=('Proxima Nova', 14), bg="#9AD4D6")
    l4 = Label(f1, text='Height', font=('Proxima Nova', 14), bg="#9AD4D6")
    l5 = Label(f1, text='Weight', font=('Proxima Nova', 14), bg="#9AD4D6")
    l6 = Label(f1, text='Exercise', font=('Proxima Nova', 14), bg="#9AD4D6")

    e1 = Entry(f1, relief=SUNKEN)
    e2 = Entry(f1, relief=SUNKEN)
    e3 = Entry(f1, relief=SUNKEN)

    spin = Spinbox(f1, from_=18, to=60)

    global var_chk
    var_chk = IntVar()
    rd1 = Radiobutton(f1, text='Male', variable=var_chk, value=1, bg="#9AD4D6")
    rd2 = Radiobutton(f1, text='Female', variable=var_chk, value=2, bg="#9AD4D6")

    list1 = ['Sedentary', 'Lightly Active', 'Moderate', 'Very Active', 'SuperActive']
    global c
    c = StringVar()
    droplist = OptionMenu(f1, c, *list1)
    droplist.config(width=15)
    c.set('Select')

    b1 = Button(f1, text="Submit", bg='#101935', fg='#F2FDFF', font=('Proxima Nova', 12), command=getDiet)

    l1.grid(row=1)
    l2.grid(row=2)
    l3.grid(row=3)
    l4.grid(row=4)
    l5.grid(row=5)
    l6.grid(row=6)

    e1.grid(row=1, column=1, padx='2')
    e2.grid(row=4, column=1, padx='2')
    e3.grid(row=5, column=1, padx='2')

    spin.grid(row=3, column=1)

    rd1.grid(row=2, column=1, sticky=W, padx='2')
    rd2.grid(row=2, column=1, sticky=E)

    droplist.grid(row=6, column=1)
    b1.grid(row=7, column=1)

    f1.grid(row=2, column=1, sticky=W)

    f2 = Frame(screen1, relief=SUNKEN, bg="#9AD4D6")
    L4 = Label(f2, width=35, text='Please Fill The Details As Given Below ', font=('Montserrat', 16, 'bold'),
               bg="#9AD4D6")
    L4.grid(row=0)

    txt1 = Text(f2, width=45, height=7, wrap=WORD, relief=SUNKEN)
    txt1.insert(0.0, 'SuperActive:twice/day')
    txt1.insert(0.0, 'VeryActive:6-7day/week' + '\n')
    txt1.insert(0.0, 'Moderate:3-5day/week' + '\n')
    txt1.insert(0.0, 'LightlyActive:1-3day/week' + '\n')
    txt1.insert(0.0, 'Sedentary:No Exercise' + '\n')
    # txt1.insert(0.0, "" + '\n')
    txt1.insert(0.0, 'Please Enter Height In Cms' + '\n')
    txt1.insert(0.0, 'Please Enter Weight In Kgs' + '\n')

    txt1.grid(row=1)

    f2.grid(row=2, column=1, padx=(300, 10))

    f3 = Frame(screen1, bg="#9AD4D6")

    f3.grid(row=3, column=1, padx=(300, 10))
    screen1.mainloop()


def reset():
    e1.delete(0, END)
    rd1.deselect()
    rd2.deselect()
    e2.delete(0, END)
    e3.delete(0, END)
    spin.delete(0, END)
    c.set('Select')
    L4 = Label(f2, width=35, text='Please Fill The Details As Given Below ', font=('Montserrat', 16, 'bold'),
               bg="#9AD4D6")
    L4.grid(row=0)

    txt1 = Text(f2, width=45, height=7, wrap=WORD, relief=SUNKEN)
    txt1.insert(0.0, 'SuperActive:twice/day')
    txt1.insert(0.0, 'VeryActive:6-7day/week' + '\n')
    txt1.insert(0.0, 'Moderate:3-5day/week' + '\n')
    txt1.insert(0.0, 'LightlyActive:1-3day/week' + '\n')
    txt1.insert(0.0, 'Sedentary:No Exercise' + '\n')
    # txt1.insert(0.0, "" + '\n')
    txt1.insert(0.0, 'Please Enter Height In Cms' + '\n')
    txt1.insert(0.0, 'Please Enter Weight In Kgs' + '\n')
    txt1.grid(row=1)

    try:
        txt2.destroy()
    except:
        pass

    L3 = Label(f3, width=35, text='', font=('Montserrat', 16, 'bold'), bg="#9AD4D6")
    L3.grid(row=2)

    try:
        b2.destroy()
    except:
        pass


mainWindow()
