import requests
import json
from tkinter import *

window = Tk()

# creating the Box
window.title("Covid-19")

# Determining the size of the Box


# Including labels
lbl = Label(window,
			text ="Total active cases:-......",font=("Arial",20))
lbl1 = Label(window,
			text ="Total confirmed cases:-...",font=("Arial",20))

lbl.grid(column = 1, row = 0)
lbl1.grid(column = 1, row = 1)
lbl2 = Label(window, text ="")
lbl2.grid(column = 1, row = 3)


def clicked():
	# Opening the url and loading the
	# json data using json Library
	url = "https://api.covid19india.org/data.json"
	page = requests.get(url)
	data = json.loads(page.text)
	
	lbl.configure(text ="Total active cases:-"
				+ data["statewise"][0]["active"],font=("Arial",20))
	
	lbl1.configure(text ="Total Confirmed cases:-"
				+ data["statewise"][0]["confirmed"],font=("Arial",20))
	
	lbl2.configure(text ="Data refreshed",font=("Arial",20))

btn = Button(window, text ="Refresh", command = clicked,font=("Arial",20))
btn.grid(column = 2, row = 0)

window.mainloop()
