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
import matplotlib.pyplot as plt

# User Defined Modules
from Database import Database
from RedditCrawler import RedditCrawler
from TwitterCrawler import TwitterCrawler
from socialMediaObjectCreator import socialMedia


class GUI:
    """
    A class to represent the GUI

    ...
    Attributes
    ----------
    self.root : Object
        Work to create the window with title 'Crawler Data for Reddit & Twitter'
    self.frame : Object
        Work like a container to organize and group widgets
    self.pack : Object
        Work as to organize widget depend on the option place in the brackets
    self.button : Object
        Work to create a button to communicate between the GUI and the user
    self.trv : Object
        Work to create a space like a table with header

    Methods
    -------
    refresh()
        help to refresh the data after displaying it in the table
    update()
        help to continue update table after using the search function
    search()
        help to search for the keyword in the crawled data
    plotting()
        help to plot the graph for analysis
    crawldata()
        help to integrate between user to crawl data from Reddit and Twitter

    """

    def __init__(self, db, reddit, twitter):
        """
        Construct all the necessary attributes for GUI:

        Parameters
        ----------
        db: object
            database object containing the social media
        reddit: object
            reddit object to crawl Reddit data
        twitter: object
            twitter object to crawl Twitter data
        """
        self.graph = socialMedia
        self.myFont = ('Arial', 15, 'bold')
        self.myFont1 = ('broadway', 15, 'bold')
        self.db = db
        self.redditObject = socialMedia(self.db, "reddit")
        self.twitterObject = socialMedia(self.db, "twitter")
        self.reddit = reddit
        self.twitter = twitter
        self.root = Tk(className=' Crawler Data for Reddit & Twitter')
        self.root.geometry("800x500")
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.w = Label(self.frame,
                       text="Welcome to the Crawler Data GUI",
                       font="50")
        self.w['font'] = self.myFont1
        self.w.pack(side=tk.TOP)

        self.button0 = tk.Button(self.frame,
                                 text="Search",
                                 fg="black",
                                 command=self.search)
        self.button0['font'] = self.myFont
        self.button0.pack(side=tk.TOP,
                          padx=5,
                          pady=5)

        self.wrapper1 = LabelFrame(self.root, text="Crawl Data")
        self.wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
        self.trv = ttk.Treeview(self.wrapper1,
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

        self.button1 = tk.Button(self.frame,
                                 text="Exit",
                                 fg="red",
                                 command=quit)
        self.button1['font'] = self.myFont
        self.button1.pack(side=tk.BOTTOM,
                          padx=5,
                          pady=5)

        self.button2 = tk.Button(self.frame,
                                 text="Plot",
                                 fg="black",
                                 command=self.plotting)
        self.button2['font'] = self.myFont
        self.button2.pack(side=tk.BOTTOM,
                          padx=5,
                          pady=5)

        self.button3 = tk.Button(self.frame,
                                 text="Crawl Data",
                                 fg="black",
                                 command=self.crawldata)
        self.button3['font'] = self.myFont
        self.button3.pack(side=tk.BOTTOM,
                          padx=5,
                          pady=5)

    # Refresh function: To refresh the table
    def refresh(self):
        """
        To refresh the table after search function

        """
        for i in self.trv.get_children():
            self.trv.delete(i)
        # print("table")

    # Update function: To update table after the search function
    def update(self, rows):
        """
        Updating the table after searching the keyword

        Parameter
        ---------
        rows: the rows needed after searching keyword

        Returns
        -------
            Data being displayed in the table
        """
        for i in rows:
            self.trv.insert('', 'end', values=i)

    # Search function: To search the keyword
    def search(self):
        """
        Searching the keyword in the crawled data

        Returns
        -------
            Post or tweet with the keyword will displayed on the table

        """
        e = simpledialog.askstring(title="Data Crawled",
                                   prompt="What do you want to search?:")
        self.refresh()
        x = self.db.search(e)
        self.update(x)

    # plotting function: To plot the graph
    def plotting(self):
        """
        Plotting the graph using the crawled data for analysis

        Returns
        -------
            A bar chart displaying Reddit and Twitter crawled data

        """
        key = list(self.redditObject.getCrimeScore().keys())
        index = np.arange(len(key))
        index1 = [x + 0.4 for x in index]
        rvalue = list(self.redditObject.getCrimeScore().values())
        tvalue = list(self.twitterObject.getCrimeScore().values())
        p1 = plt.bar(index, rvalue, width=0.4, tick_label="reddit", color='r')
        p2 = plt.bar(index1, tvalue, width=0.4,
                     tick_label="twitter", color='b')
        plt.ylabel('Frequency')
        plt.xlabel('Crimes')
        plt.xticks([r + 0.2 for r in range(len(key))], key)
        plt.title('Keyword Category in the News')
        plt.legend((p1[0], p2[0]), ('Reddit: '+self.redditObject.getSentiment(),
                                    'Twitter: ' + self.twitterObject.getSentiment()))
        plt.show()
        print("Plot")

    # crawldata function: To start the crawling of data from the website
    def crawldata(self):
        """
        Crawling data for Reddit and Twitter

        returns
        -------
            A popup window saying Crawl done after crawling done for Reddit and Twitter

        """
        self.db.createTable()
        self.reddit.crawl(self.db)
        self.twitter.crawl(self.db)
        self.redditObject = socialMedia(self.db, "reddit")
        self.twitterObject = socialMedia(self.db, "twitter")
        messagebox.showinfo("Popup", "Crawl Done")
