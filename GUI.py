# others
import numpy as np
# tkinter
from tkinter.ttk import Treeview
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox, ttk
from tkinter import *
from tkinter import simpledialog
# matplotlib
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# User Defined Modules
from Database import Database
from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler


class GUI:
    def __init__(self, db, reddit, twitter):
        self.myFont = ('Arial', 15, 'bold')
        self.myFont1 = ('broadway', 15, 'bold')
        self.db = db
        self.reddit = reddit
        self.twitter = twitter
        self.root = Tk(className=' Crawler Data for Reddit & Twitter')
        self.root.geometry("800x500")
        self.wrapper1 = LabelFrame(self.root, text="Crawl Data")
        self.wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.style = ttk.Style()
        self.trv = ttk.Treeview(wrapper1,
                                columns=(1, 2, 3, 4, 5, 6),
                                show="headings",
                                height="20")
        self.trv.pack()
        self.trv.heading(1, text="ID")
        self.trv.heading(2, text="type")
        self.trv.heading(3, text="user")
        self.trv.heading(4, text="text")
        self.trv.heading(5, text="likes")
        self.trv.heading(6, text="dates & times")
        self.w = Label(frame,
                       text="Welcome to the Crawler Data GUI",
                       font="50")
        self.w['font'] = self.myFont1
        self.w.pack(side=tk.TOP)
        self.button0 = tk.Button(frame,
                                 text="Search",
                                 fg="black",
                                 command=search)
        self.button0['font'] = myFont
        self.button0.pack(side=tk.TOP,
                          padx=5,
                          pady=5)
        self.button1 = tk.Button(frame,
                    text="Exit",
                    fg="red",
                    command=quit)
        self.button1['font'] = myFont
        self.button1.pack(side=tk.BOTTOM,
                padx=5,
                pady=5)
        self.button2 = tk.Button(frame,
                            text="Plot",
                            fg="black",
                            command=plotting)
        self.button2['font'] = myFont
        self.button2.pack(side=tk.BOTTOM,
                    padx=5,
                    pady=5)
        self.button3 = tk.Button(frame,
                            text="Crawl Data",
                            fg="black",
                            command=crawldata)
        self.button3['font'] = myFont
        self.button3.pack(side=tk.BOTTOM,
                    padx=5,
                    pady=5)
    # Refresh function: To refresh the table

    def refresh(self):
        for i in trv.get_children():
            trv.delete(i)
        # print("table")
    # Update function: To update table after the search function

    def update(self, rows):
        for i in rows:
            trv.insert('', 'end', values=i)
    # Search function: To search the keyword

    def search(self):
        e = simpledialog.askstring(title="Data Crawled",
                                   prompt="What do you want to search?:")
        self.refresh()
        x = self.db.search(e)
        self.update(x)

    # window function: To open new window when plotting the graph
    # def window():
    #   newWindow = Toplevel(root)
    #   newWindow.title("Graph")
    #   newWindow.geometry("300x300")

    # plotting function: To plot the graph
    def plotting(self):
        a_dictionary = {"a": 1, "b": 2, "c": 3}
        keys = a_dictionary.keys()
        values = a_dictionary.values()
        matplotlib.pyplot.bar(keys, values)
        # new_dict = {}
        # for value in word_dict.values():
        #     if value in word_dict:
        #        new_dict += 1
        #    else:
        #        new_dict = 1
        #    y = new_dict[value]
        #    x = word_dict[value]
        # print(new_dict)
        # pyplot.plot(x, y)
        # pyplot.show()

    # crawldata function: To start the crawling of data from the website

    def crawldata(self):
        self.db.createTable()
        self.reddit.crawl()
        self.twitter.crawl()
        messagebox.showinfo("Popup", "Crawl Done")
