from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("My Button Increaser")

global counter
counter = 0

def raiseCounter():
    global counter
    counter += 1
    testLabel.config(text = f"The counter is currently at {counter}")


testLabel = Label(master=window, text=f"The counter is currently at {counter}")
testLabel.pack()
testBtn = Button(text = "raise the counter", command = raiseCounter, fg = "darkgreen", bg = "white")
testBtn.pack()

window.mainloop()