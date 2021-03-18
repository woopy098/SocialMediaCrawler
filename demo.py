import Database as Database
import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import simpledialog
import mysql.connector

db = Database.Database()
myFont = ('Arial', 15, 'bold')
myFont1 = ('broadway', 15, 'bold')


def showdata():
    f = open("Database.py", "r")
    print(f.read())
    print("\nData Shown\n")


def search():
    e = simpledialog.askstring(title="Data Crawled",
                               prompt="What do you want to search?:")
    x = db.search(e)
    i = 0
    for i in x:
        for j in range(len(i)):
            e = Entry(root, width=30, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, i[j])
        i += 1


def plotting():
    print("Bar chart")


def crawltwitter():
    # T = tk.Text(root, height=2, width=30)
    # T.pack()
    # T.insert(tk.END, "Just a text Widget\nin two lines\n")
    # tk.mainloop()
    print("Twitter usage")


def crawlreddit():
    print("Reddit usage")


root = Tk(className=' Crawler Data for Reddit & Twitter')
root.geometry("550x350")
myFont = font.Font(family='Arial', size=15, weight='bold')
myFont1 = font.Font(family='broadway', size=15, weight='bold')
frame = tk.Frame(root)
frame.pack()

w = Label(frame,
          text="Welcome to the Crawler Data GUI",
          font="50")
w['font'] = myFont1
w.pack(side=tk.TOP)

button0 = tk.Button(frame,
                    text="Search",
                    fg="black",
                    command=search)
button0['font'] = myFont
button0.pack(side=tk.TOP,
             padx=5,
             pady=5)

button1 = tk.Button(frame, text="Exit",
                    fg="red",
                    command=quit)
button1['font'] = myFont
button1.pack(side=tk.BOTTOM,
             padx=5,
             pady=5)

button2 = tk.Button(frame, text="Plot",
                    fg="black",
                    command=plotting)
button2['font'] = myFont
button2.pack(side=tk.BOTTOM,
             padx=5,
             pady=5)

button3 = tk.Button(frame,
                    text="Crawl Data from Reddit",
                    fg="black",
                    command=crawlreddit)
button3['font'] = myFont
button3.pack(side=tk.BOTTOM,
             padx=5,
             pady=5)

slogan = tk.Button(frame,
                   text="Crawl Data from Twitter",
                   command=crawltwitter)
slogan['font'] = myFont
slogan.pack(side=tk.BOTTOM,
            padx=5,
            pady=5)

button4 = tk.Button(frame,
                    text="Show Data",
                    command=showdata)
button4['font'] = myFont
button4.pack(side=tk.TOP, padx=5, pady=5)

root.mainloop()
