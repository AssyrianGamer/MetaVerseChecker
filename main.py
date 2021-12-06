#!/usr/bin/env python

"""main.py: This is the main function of the script. Ok fine - it's the only function! XD"""

__name__ = "MetaVerseChecker"
__author__ = "Andrew Kumar"
__copyright__ = "Copyright 2021, Andrew Kumar"
__credits__ = ["Andrew Kumar"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Andrew Kumar"
__email__ = "andrew.kumar@unsw.edu.au"
__status__ = "Production"

import os
# import PIL.Image
import time
import tkinter as tk

# from bs4 import BeautifulSoup
from datetime import date, datetime
from os import *
from PIL import ImageTk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from tkinter import font
from urllib.request import urlopen

root = tk.Tk()

# Set variables and values
fbUsername_var = tk.StringVar()
fbMetaScoreResult_var = tk.StringVar()
igUsername_var = tk.StringVar()
igMetaScoreResult_var = tk.StringVar()
twUsername_var = tk.StringVar()
twMetaScoreResult_var = tk.StringVar()
metaVersalTitleResult_var = tk.StringVar()

fbMetaVersalScore = 100
fbMetaVersalScoreResult_var = tk.IntVar()
fbMetaScoreResult_var.set(fbMetaVersalScore)

igMetaVersalScore = 100
igMetaVersalScoreResult_var = tk.IntVar()
igMetaScoreResult_var.set(igMetaVersalScore)

twMetaVersalScore = 100
twMetaVersalScoreResult_var = tk.IntVar()
twMetaScoreResult_var.set(twMetaVersalScore)

metaVersalScore = fbMetaVersalScore + igMetaVersalScore + twMetaVersalScore
metaVersalScoreResult_var = tk.IntVar()
metaVersalScoreResult_var.set(metaVersalScore)

metaVersalTitleResult_var.set("Cyber Master!") # You always start at Cyber Master! Osu!

# Set the amount of penalty points applied when a social media account is detected. Default 50.
metaVersalReducer = 50

status = tk.StringVar()
status.set("Loaded "+ __name__ + " v" + __version__ + ". Created by " + __author__)

today = datetime.now()

# Facebook check function
def facebook():
    fbname = fbUsername_var.get().lower()
    if fbname == "":
        print("Please enter a Facebook username.")
        status.set("Please enter a Facebook username.")
    elif " " in fbname:
        print("Please ensure the Facebook username is entered correctly.")
        status.set("Please ensure the Facebook username is entered correctly.")
    else:
        print("Checking Facebook!")
        status.set("Checking Facebook!")
        url = "https://www.facebook.com/" + fbname
        options = Options()
        # soup = BeautifulSoup(urlopen(url), features="html.parser")
        options.add_argument("--incognito") # Runs Chrome in stealth mode
        options.add_argument("--headless") # Runs Chrome in headless mode
        options.add_argument("--no-sandbox") # Bypass OS security model
        options.add_argument("--disable-extensions") # Disables all extentions
        options.add_argument("--disable-gpu") # Enables headless on windows platforms
        options.add_argument("-disable-infobars") # Disables browser prompts
        # options.add_argument("--disable-software-rasterizer") # redundant in headless mode
        # options.add_argument('start-maximized') # redundant in headless mode
        driver = webdriver.Chrome(options=options, executable_path='chromedriver')
        driver.get(url)
        fbUsernameResult = driver.title
        # print(fbUsernameResult)
        print("Looking up Facebook username " + fbname + "!")
        status.set("Looking up Facebook username " + fbname + "!")
        if "Page not found" in fbUsernameResult:
            print("You hide well...or maybe you don't exist?")
            status.set("You hide well...or maybe you don't exist?")
        elif fbUsernameResult == "Facebook":
            print("You hide well...or maybe you don't exist?")
            status.set("You hide well...or maybe you don't exist?")
        else:
            time.sleep(1.5)
            # webbrowser.open("https://www.facebook.com/" + fbname)
            fbUsernamePrintResult = fbUsernameResult.strip().split(" |", 1)[0]
            print("I found you on Facebook, " + fbUsernamePrintResult + "!")
            status.set("I found you on Facebook, " + fbUsernamePrintResult + "!")
            global fbScreenshotName
            fbScreenshotName ="Facebook - " + fbname + " - " + fbUsernamePrintResult + " - " + today.now().strftime("%Y%m%d%H%M") + ".png"
            print(fbScreenshotName)
            if os.path.exists(fbScreenshotName):
                print("Check for this user has been done within the last minute!")
                status.set("Check for this user has been done within the last minute!")
            else:
                fbImageCanvas.pack_forget()
                driver.save_screenshot(fbScreenshotName)
                driver.quit()
                # fbUsernameResult_var.set(fbUsernamePrintResult)
                fbMetaScore()
                metaScore()
                fbimg = PhotoImage(file=fbScreenshotName).subsample(1, 1)
                fbImageCanvas.create_image(160, 100, anchor=CENTER, image=fbimg)
                fbImageUpdate()

# Instagram check function
def instagram():
    igname = igUsername_var.get().lower()
    if igname == "":
        print("Please enter an Instagram username.")
        status.set("Please enter an Instagram username.")
    elif " " in igname:
        print("Please ensure the Instagram username is entered correctly.")
        status.set("Please ensure the Instagram username is entered correctly.")
    else:
        print("Checking Instagram!")
        status.set("Checking Instagram!")
        url = "https://www.instagram.com/" + igname
        options = Options()
        # soup = BeautifulSoup(urlopen(url), features="html.parser")
        options.add_argument("--incognito") # Runs Chrome in stealth mode
        options.add_argument("--headless") # Runs Chrome in headless mode
        options.add_argument("--no-sandbox") # Bypass OS security model
        options.add_argument("--disable-extensions") # Disables all extentions
        options.add_argument("--disable-gpu") # Enables headless on windows platforms
        options.add_argument("-disable-infobars") # Disables browser prompts
        # options.add_argument("--disable-software-rasterizer") # redundant in headless mode
        # options.add_argument('start-maximized') # redundant in headless mode
        driver = webdriver.Chrome(options=options, executable_path='chromedriver')
        driver.get(url)
        igUsernameResult = driver.title
        # print(igUsernameResult)
        print("Looking up Instagram username " + igname + "!")
        status.set("Looking up Instagram username " + igname + "!")
        if "Log in" in igUsernameResult:
            print("We have hit the Instagram soft ban! You will have to wait 5-10 minutes!")
            status.set("We have hit the Instagram soft ban! You will have to wait 5-10 minutes!")
        elif "Login" in igUsernameResult:
            print("We have hit the Instagram soft ban! You will have to wait 5-10 minutes!")
            status.set("We have hit the Instagram soft ban! You will have to wait 5-10 minutes!")
        elif "Page Not Found" in igUsernameResult:
            print("You hide well...or maybe you don't exist?")
            status.set("You hide well...or maybe you don't exist?")
        elif "(@" not in igUsernameResult:
            time.sleep(1.5)
            # webbrowser.open("https://www.instagram.com/" + igname)
            igUsernamePrintResult1 = igUsernameResult.strip().split(" • Instagram", 1)[0]
            print("I found you on Instagram, " + igUsernamePrintResult1 + "!")
            status.set("I found you on Instagram, " + igUsernamePrintResult1 + "!")
            igScreenshotName1 = "Instagram - " + igname + " - " + igUsernamePrintResult1 + " - " + today.now().strftime("%Y%m%d%H%M") + ".png"
            print(igScreenshotName1)
            if os.path.exists(igScreenshotName1):
                print("Check for this user has been done within the last minute!")
                status.set("Check for this user has been done within the last minute!")
            else:
                igImageCanvas.pack_forget()
                driver.save_screenshot(igScreenshotName1)
                driver.quit()
                # igUsernameResult_var.set(igUsernamePrintResult1)
                igMetaScore()
                metaScore()
                igImageUpdate()
        else:
            time.sleep(1.5)
            # webbrowser.open("https://www.instagram.com/" + igname)
            igUsernamePrintResult2 = igUsernameResult.strip().split(" (", 1)[0]
            print("I found you on Instagram, " + igUsernamePrintResult2 + "!")
            status.set("I found you on Instagram, " + igUsernamePrintResult2 + "!")
            igScreenshotName2 = "Instagram - " + igname + " - " + igUsernamePrintResult2 + " - " + today.now().strftime("%Y%m%d%H%M") + ".png"
            print(igScreenshotName2)
            if os.path.exists(igScreenshotName2):
                print("Check for this user has been done within the last minute!")
                status.set("Check for this user has been done within the last minute!")
            else:
                igImageCanvas.pack_forget()
                driver.save_screenshot(igScreenshotName2)
                driver.quit()
                # igUsernameResult_var.set(igUsernamePrintResult2)
                igMetaScore()
                metaScore()
                igImageUpdate()

# Twitter check function
def twitter():
    twname = twUsername_var.get().lower()
    if twname == "":
        print("Please enter a Twitter username.")
        status.set("Please enter a Twitter username.")
    elif " " in twname:
        print("Please ensure the Twitter username is entered correctly.")
        status.set("Please ensure the Twitter username is entered correctly.")
    else:
        print("Checking Twitter!")
        status.set("Checking Twitter!")
        url = "https://twitter.com/" + twname
        options = Options()
        # soup = BeautifulSoup(urlopen(url), features="html.parser")
        options.add_argument("--incognito") # Runs Chrome in stealth mode
        options.add_argument("--headless") # Runs Chrome in headless mode
        options.add_argument("--no-sandbox") # Bypass OS security model
        options.add_argument("--disable-extensions") # Disables all extentions
        options.add_argument("--disable-gpu") # Enables headless on windows platforms
        options.add_argument("-disable-infobars") # Disables browser prompts
        # options.add_argument("--disable-software-rasterizer") # redundant in headless mode
        # options.add_argument('start-maximized') # redundant in headless mode
        driver = webdriver.Chrome(options=options, executable_path='chromedriver')
        driver.get(url)
        twUsernameResult = driver.title
        # print(twUsernameResult)
        print("Looking up Twitter username " + twname + "!")
        status.set("Looking up Twitter username " + twname + "!")
        if "Page not found" in twUsernameResult:
            print("You hide well...or maybe you don't exist?")
            status.set("You hide well...or maybe you don't exist?")
        else:
            time.sleep(1.5)
            # webbrowser.open("https://www.twitter.com/" + twname)
            # twUsernamePrintResult = twUsernameResult.strip().split(" (", 1)[0]
            # print("I found you " + twUsernameResult.strip().split(" (", 1)[0] + "!")
            # status.set("I found you " + twUsernameResult.strip().split(" (", 1)[0] + "!")
            print("I found you on Twitter, " + twname + "!")
            status.set("I found you on Twitter, " + twname + "!")
            twScreenshotName = "Twitter - " + twname + " - " + today.now().strftime("%Y%m%d%H%M") + ".png"
            print(twScreenshotName)
            if os.path.exists(twScreenshotName):
                print("Check for this user has been done within the last minute!")
                status.set("Check for this user has been done within the last minute!")
            else:
                twImageCanvas.pack_forget()
                driver.save_screenshot(twScreenshotName)
                driver.quit()
                # twUsernameResult_var.set(twUsernamePrintResult)
                twMetaScore()
                metaScore()
                twImageUpdate()

# Menubar function - Reset
def menubarReset():
    fbUsername_var.set("")
    igUsername_var.set("")
    twUsername_var.set("")
    fbMetaVersalScore = 100
    igMetaVersalScore = 100
    twMetaVersalScore = 100
    fbMetaScoreResult_var.set(fbMetaVersalScore)
    igMetaScoreResult_var.set(igMetaVersalScore)
    twMetaScoreResult_var.set(twMetaVersalScore)
    metaVersalScoreResult_var.set(fbMetaVersalScore + igMetaVersalScore + twMetaVersalScore)
    metaVersalTitleResult_var.set("Cyber Master")
    status.set(__name__ + " details have been reset!")

# Menubar function - Help
def menubarHelp():
   filewin = Toplevel(root)
   filewin.attributes("-topmost", 1)
   filewin.iconbitmap("./logo-meta.ico")
   tk.Label(filewin, text=__name__ + " v" + __version__).pack()
   tk.Label(filewin, text="Created by " + __author__).pack()
   filewin.geometry(f'250x250+{center_x}+{center_y}')

# Score and title function
def metaScore():
    global metaVersalScore
    metaVersalScore = fbMetaVersalScore + igMetaVersalScore + twMetaVersalScore
    metaVersalScoreResult_var.set(metaVersalScore)
    if metaVersalScore >= 280:
        metaVersalTitleResult_var.set("Cyber Master!")
    elif metaVersalScore >= 250:
        metaVersalTitleResult_var.set("Cyber Knight!")
    elif metaVersalScore >= 200:
        metaVersalTitleResult_var.set("Cyber Padawan!")
    elif metaVersalScore >= 150:
        metaVersalTitleResult_var.set("I may have some social media.")
    elif metaVersalScore >= 100:
        metaVersalTitleResult_var.set("Ok, I have a few social media accounts.")
    elif metaVersalScore >= 50:
        metaVersalTitleResult_var.set("FINE! I have a social media addiction!")
    elif metaVersalScore <= 50:
        metaVersalTitleResult_var.set("Game over. Please insert coin.")

# Facebook score penalty function
def fbMetaScore():
    global fbMetaVersalScore
    if fbMetaVersalScore > 0:
        fbMetaVersalScore -= metaVersalReducer
    else:
        print("You really need to re-assess your social footprint!")
    fbMetaScoreResult_var.set(fbMetaVersalScore)
    return fbMetaVersalScore

def fbImageUpdate():
    fbImageCanvas.pack(side=RIGHT)

# Instagram score penalty function
def igMetaScore():
    global igMetaVersalScore
    if igMetaVersalScore > 0:
        igMetaVersalScore -= metaVersalReducer
    else:
        print("You really need to re-assess your social footprint!")
    igMetaScoreResult_var.set(igMetaVersalScore)
    return igMetaVersalScore

def igImageUpdate():
    igImageCanvas.pack(side=RIGHT)

# Twitter score penalty function
def twMetaScore():
    global twMetaVersalScore
    if twMetaVersalScore > 0:
        twMetaVersalScore -= metaVersalReducer
    else:
        print("You really need to re-assess your social footprint!")
    twMetaScoreResult_var.set(twMetaVersalScore)
    return twMetaVersalScore

def twImageUpdate():
    twImageCanvas.pack(side=RIGHT)

# Sets window title and always on top
root.title(__name__ + " - A social media tool")
root.attributes("-topmost", 2)
root.resizable(False, False)
root.iconbitmap("./logo-meta.ico")
menubar = Menu(root)
root.config(menu=menubar)

# Sets window size and positioning
window_width = 700
window_height = 900
# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
# Set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="New", command=)
# filemenu.add_command(label="Open", command=)
# filemenu.add_command(label="Save", command=)
# filemenu.add_command(label="Save as...", command=)
filemenu.add_command(label="Reset", command=menubarReset)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

# editmenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Edit", menu=editmenu)
# editmenu.add_command(label="Undo", command=)
# editmenu.add_separator()
# editmenu.add_command(label="Cut", command=)
# editmenu.add_command(label="Copy", command=)
# editmenu.add_command(label="Paste", command=)
# editmenu.add_command(label="Delete", command=)
# editmenu.add_command(label="Select All", command=)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
# helpmenu.add_command(label="Help Index", command=)
helpmenu.add_command(label="About...", command=menubarHelp)

# Score label frame
score = tk.LabelFrame(root, text="Current Score", width=150, height=100)
score.pack(fill=BOTH, expand=True, padx=10, pady=5)
fbFormScoreLabel = tk.Label(score, text="Facebook Score: ").place(x=0, y=0)
fbFormScoreResultLabel = tk.Label(score, textvariable=fbMetaScoreResult_var).place(x=10, y=20)
igFormScoreLabel = tk.Label(score, text="Instagram Score: ").place(x=0, y=40)
igFormScoreResultLabel = tk.Label(score, textvariable=igMetaScoreResult_var).place(x=10, y=60)
twFormScoreLabel = tk.Label(score, text="Twitter Score: ").place(x=0, y=80)
twFormScoreResultLabel = tk.Label(score, textvariable=twMetaScoreResult_var).place(x=10, y=100)
metaVersalScoreLabel = tk.Label(score, textvariable=metaVersalScoreResult_var, font=("Arial", 44)).place(x=window_width/2, y=80, anchor=S)
metaVersalTitleLabel = tk.Label(score, text="Title: ", textvariable=metaVersalTitleResult_var, font=("Arial", 10)).place(x=window_width/2, y=100, anchor=S)

# FB label frame
fb = tk.LabelFrame(root, text="Facebook Tool", width=150, height=75)
fb.pack(fill=BOTH, expand=True, padx=10, pady=5)

# FB username input
fbUsernameLabel = tk.Label(fb, text="Facebook username:").place(x=5, y=30)
fbUsernameEntry = tk.Entry(fb, textvariable=fbUsername_var, width="25").place(x=5, y=50)
fbUsernameButton = tk.Button(fb, text="Submit", command=facebook).place(x=5, y=80)
fbImageCanvas = Canvas(fb, width=300, height=150, borderwidth=2, relief="groove")
# fbImageCanvas.pack(side=RIGHT)
# fbimg = PhotoImage(file="Facebook - zuck - Mark Zuckerberg - 202111251123.png").subsample(1, 1)
# fbImageCanvas.create_image(160, 100, anchor=CENTER, image=fbimg)

# IG label frame
ig = tk.LabelFrame(root, text="Instagram Tool", width=150, height=75)
ig.pack(fill=BOTH, expand=True, padx=10, pady=5)

# IG username input
igUsernameLabel = tk.Label(ig, text="Instagram username:").place(x=5, y=30)
igUsernameEntry = tk.Entry(ig, textvariable=igUsername_var, width="25").place(x=5, y=50)
igUsernameButton = tk.Button(ig, text="Submit", command=instagram).place(x=5, y=80)
igImageCanvas = Canvas(ig, width=300, height=150, borderwidth=2, relief="groove")
# igImageCanvas.pack(side=RIGHT)
# igimg = PhotoImage(file="Instagram - zuck - Mark Zuckerberg - 202111251339.png").subsample(1, 1)
# igImageCanvas.create_image(430, 220, anchor=CENTER, image=igimg)

# TW label frame
tw = tk.LabelFrame(root, text="Twitter Tool", width=150, height=75)
tw.pack(fill=BOTH, expand=True, padx=10, pady=5)

# TW username input
twUsernameLabel = tk.Label(tw, text="Twitter username:").place(x=5, y=30)
twUsernameEntry = tk.Entry(tw, textvariable=twUsername_var, width="25").place(x=5, y=50)
twUsernameButton = tk.Button(tw, text="Submit", command=twitter).place(x=5, y=80)
twImageCanvas = Canvas(tw, width=300, height=150, borderwidth=2, relief="groove")
# twImageCanvas.pack(side=RIGHT)
# twimg = PhotoImage(file="Twitter - finkd - 202111251124.png").subsample(1, 1)
# twImageCanvas.create_image(350, 135, anchor=CENTER, image=twimg)

# Status bar
statusbarLabel = tk.Label(root, textvariable=status, text="Loaded "+ __name__ + " v" + __version__ + ". Created by " + __author__, bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbarLabel.pack(side=tk.BOTTOM, fill=tk.X)

# Keep the main window displayed
root.mainloop()
