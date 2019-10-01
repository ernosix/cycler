#!/usr/bin/python

from tkinter import *
from tkinter import ttk, font
from datetime import datetime, timedelta
#import pifacedigitalio


mode = 'HEAT'

# Creates a PiFace Digital object
#pfd = pifacedigitalio.PiFaceDigital()
# start first relay
#pfd.relays[0].value = 1


def quit(*args):
    root.destroy()


def show_time():
    global mode
    global endTime
    #global pfd
    # Get the time remaining until mode ends
    remainder = endTime - datetime.now()

    # If below 3:45 set text color yellow
    if int(remainder.total_seconds()) < 225:
        lbl.configure(foreground="yellow")

    # At 0:00 cycle modes
    if int(remainder.total_seconds()) < 1:
        if mode == 'HEAT':
            mode = 'COOL'
            lbl.configure(foreground="blue")
            # Turn off the first relay
            #pfd.relays[0].value = 0
        else:
            mode = 'HEAT'
            lbl.configure(foreground="red")
            # Turn on/set high the first relay
            #pfd.relays[0].value = 1
        endTime = datetime.now() + timedelta(minutes=8)

    # Show the time left
    remainder = remainder - timedelta(microseconds=remainder.microseconds)
    txt.set(remainder)

    # Loop
    root.after(1000, show_time)


# Use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("x", quit)
root.after(1000, show_time)

# Set the end date and time for the countdown loop (8 min)
endTime = datetime.now() + timedelta(minutes=8)

fnt = font.Font(family='Helvetica', size=280, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="red", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
