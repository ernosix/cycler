#!/usr/bin/python

from tkinter import *
from tkinter import ttk, font
#import pifacedigitalio
from datetime import datetime, timedelta

minutes = 7
seconds = 47


def quit(*args):
#    pifacedigital.relays[0].turn_off()
    root.destroy()


def show_time():
    global mode
    global endTime
    global foreground_color

    # Get the time remaining until mode ends
    remainder = endTime - datetime.now()

    # If below 3:45 set text color yellow
    if int(remainder.total_seconds()) < 225:
        foreground_color = "yellow"
        status_txt.set("CHANGING MODE")
    else:
        status_txt.set(mode + "ING MODE")

    # At 0:00 cycle modes
    if int(remainder.total_seconds()) < 1:
        if mode == 'HEAT':
            mode = 'COOL'
            foreground_color = "blue"
#            pifacedigital.relays[0].turn_off()
        else:
            mode = 'HEAT'
            foreground_color = "red"
#            pifacedigital.relays[0].turn_on()
        endTime = datetime.now() + timedelta(minutes=minutes, seconds=seconds)

    # Show the time left
    remainder = remainder - timedelta(microseconds=remainder.microseconds)
    time_left = str(remainder)
    time_left = time_left.replace(time_left[:2], '')
    txt.set(time_left)
    status.configure(foreground=foreground_color)
    lbl.configure(foreground=foreground_color)

    # Loop
    root.after(1000, show_time)


# Initialize PiFace, turn on relay 1
#pifacedigital = pifacedigitalio.PiFaceDigital()
#pifacedigital.relays[0].turn_on()

# Use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black', cursor='none')
root.bind("x", quit)
root.after(1000, show_time)

# Set the end date and time for the countdown loop
endTime = datetime.now() + timedelta(minutes=minutes, seconds=seconds)
mode = 'HEAT'
foreground_color = "red"
fnt = font.Font(family='Helvetica', size=380, weight='bold')
status_font = font.Font(family='Helvetica', size=120, weight='bold')
txt = StringVar()
status_txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="red", background="black")
lbl.place(relx=0.5, rely=0.4, anchor=CENTER)
status = ttk.Label(root, textvariable=status_txt, font=status_font, foreground="red", background="black")
status.place(relx=0.5, rely=0.8, anchor=CENTER)
root.mainloop()
