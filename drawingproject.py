from time import sleep
import tkinter as tk
from tkinter import *
##### Functions
def clear():
    txtbar1.delete(0, tk.END) ## Removes text from all text boxes
    txtbar2.delete(0, tk.END)
    txtbar3.delete(0, tk.END)
    txtbar4.delete(0, tk.END)

    canvas.delete("all") #Gets rid of the graph

def graph():


    try:
        bar1 = float(txtbar1.get()) # Gets values for each bar from user input
        bar2 = float(txtbar2.get())
        bar3 = float(txtbar3.get())
        bar4 = float(txtbar4.get())
        if bar1 > 650 or bar2 > 650 or bar3 > 650 or bar4 > 650: #if bar is too big for canvas, this shrinks the graph
            toobig = max(bar1,bar2,bar3,bar4)
            toobig = toobig/100
            bar1 = bar1/toobig
            bar2=bar2/toobig
            bar3=bar3/toobig
            bar4=bar4/toobig

        canvas.create_rectangle(225,650,275,650-bar1, fill="red", tags="bar1") #Graphs each bar
        canvas.create_rectangle(300,650,350,650-bar2, fill="blue",tags="bar2")
        canvas.create_rectangle(375,650,425,650-bar3, fill="green", tags="bar3")
        canvas.create_rectangle(450,650,500,650-bar4, fill="yellow", tags="bar4")

        btngraph.config(text="Create Graph") #If user previously puts invalid input, this changes the button back to saying Create Graph
   

    
    except ValueError:
        btngraph.config(text="Invalid Input(s)") #Error message if user puts invalid input

###### Building window
root = Tk()
canvas = Canvas(root, width="750", height="750")
root.geometry("750x750")
root.resizable(width=False,height=False)
root.title("Bar Graph Maker")
###### Labels/Text Boxes/Buttons
lblbar1 = tk.Label(root, text="Bar 1 Value: ") ### All labels next to the bar inputs
lblbar2 = tk.Label(root,text="Bar 2 Value: ")
lblbar3 = tk.Label(root,text="Bar 3 Value: ")
lblbar4 = tk.Label(root,text="Bar 4 Value: ")

txtbar1 = tk.Entry(root) ## All text boxes for bar value inputs
txtbar2 = tk.Entry(root)
txtbar3 = tk.Entry(root)
txtbar4 = tk.Entry(root)

btnclear = tk.Button(text="Clear", command=clear) #Creates clear button
btngraph = tk.Button(text="Create Graph", command=graph)#Creates graph button
######### Positioning

lblbar1.pack(anchor=NW) #Puts labels in the top left corner of the window
lblbar2.pack(anchor=NW)
lblbar3.pack(anchor=NW)
lblbar4.pack(anchor=NW)

txtbar1.place(x=70) #Puts text boxes to the right of the labels
txtbar2.place(x=70, y=20) 
txtbar3.place(x=70, y=40)
txtbar4.place(x=70, y=60)

btngraph.place(y=80) #Puts buttons under the labels and text boxes
btnclear.place(y=80,x=100)
canvas.pack()
root.mainloop()