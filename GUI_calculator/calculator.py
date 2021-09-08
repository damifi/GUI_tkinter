import tkinter

#main window of the application
root = tkinter.Tk()
#Title of the window
root.title("Calculator")

#as this is a single step calculator, I only need to keep track of one variable 
#as the result is computed immediately
firstValue = None


#entry field for the numbers and operands with parent window = root
entryField = tkinter.Entry(root, width = 30)

#grid of the entry field. Start in row=col=0, span over 3 columns and pad x and y axis by 10
entryField.grid(row=0, column=0, columnspan=3,padx = 10, pady=10)

def button_press(number):
    """This function is called when a button from 0 to 9 is pressed and adds its value to the entryField"""
    value= entryField.get()
    entryField.delete(0, "end")
    entryField.insert(0, value + str(number))

def clear():
    """Function to clear the entryField. Called when clear button is pressed."""
    entryField.delete(0, "end")


def add():
    """Function to add two numbers"""
    #get the current value of the entry field as the first value
    firstValue = entryField.get()
    #global number represents the first value of the entry field and therefore the first number of the computation
    global globalNumber
    #op defines what operand is pressed and therefore the operand with which the two numbers computed
    global op
    globalNumber = int(firstValue)
    op = "+"
    entryField.delete(0,"end")

def sub():
    """Function to implement substract when buttonSub is pressed."""
    firstValue = entryField.get()
    global globalNumber
    global op
    globalNumber = int(firstValue)
    op = "-"
    entryField.delete(0,"end")

def mult():
    """Function to implement multiplication when buttonMult is pressed."""
    firstValue = entryField.get()
    global globalNumber
    global op
    globalNumber = int(firstValue)
    op = "x"
    entryField.delete(0,"end")

def div():
    """Function to implement division when buttonDiv is pressed."""
    firstValue = entryField.get()
    global globalNumber
    global op
    globalNumber = int(firstValue)
    op = "/"
    entryField.delete(0,"end")
    
def equal():
    """Function to implement the evaluation of two numbers when buttonEqual is pressed."""
    secondValue = int(entryField.get())
    entryField.delete(0, "end")

    if(op == "+"):
        entryField.insert(0, globalNumber + secondValue)

    if(op == "-"):
        entryField.insert(0, globalNumber - secondValue)

    if(op == "x"):
        entryField.insert(0, globalNumber * secondValue)

    if(op == "/"):
        entryField.insert(0, globalNumber / secondValue)    



#create buttons for the calculator. They are not drawn in the window yet.
button0 = tkinter.Button(root, text="0", padx = 40, pady = 20, command = lambda: button_press(0))
button1 = tkinter.Button(root, text="1", padx = 40, pady = 20, command = lambda: button_press(1))
button2 = tkinter.Button(root, text="2", padx = 40, pady = 20, command = lambda: button_press(2))
button3 = tkinter.Button(root, text="3", padx = 40, pady = 20, command = lambda: button_press(3))
button4 = tkinter.Button(root, text="4", padx = 40, pady = 20, command = lambda: button_press(4))
button5 = tkinter.Button(root, text="5", padx = 40, pady = 20, command = lambda: button_press(5))
button6 = tkinter.Button(root, text="6", padx = 40, pady = 20, command = lambda: button_press(6))
button7 = tkinter.Button(root, text="7", padx = 40, pady = 20, command = lambda: button_press(7))
button8 = tkinter.Button(root, text="8", padx = 40, pady = 20, command = lambda: button_press(8))
button9 = tkinter.Button(root, text="9", padx = 40, pady = 20, command = lambda: button_press(9))

buttonClear = tkinter.Button(root, text = "clear", padx = 28, pady = 20, command = clear)
buttonAdd = tkinter.Button(root, text = "+", padx = 40, pady = 20, command = add)
buttonSub = tkinter.Button(root, text = "-", padx = 40, pady = 20, command = sub)
buttonMult = tkinter.Button(root, text = "x", padx = 40, pady = 20, command = mult)
buttonDiv = tkinter.Button(root, text="/", padx = 40, pady = 20, command = div)

buttonEqual = tkinter.Button(root, text = "equal", padx = 31, pady = 20, command = equal)


buttonComma = tkinter.Button(root, text=",", padx = 41, pady = 20, command = None)

#draw the buttons in the root window
button0.grid(row=4, column = 1)
button1.grid(row=3, column = 0)
button2.grid(row=3, column = 1)
button3.grid(row=3, column = 2)
button4.grid(row=2, column = 0)
button5.grid(row=2, column = 1)
button6.grid(row=2, column = 2)
button7.grid(row=1, column = 0)
button8.grid(row=1, column = 1)
button9.grid(row=1, column = 2)

buttonEqual.grid(row=4, column=3)
buttonAdd.grid(row=3,column=3)
buttonSub.grid(row=2,column=3)
buttonMult.grid(row=1,column=3)

buttonComma.grid(row = 4, column=2)
buttonDiv.grid(row= 4, column=0)
buttonClear.grid(row=4, column=4)



#updates the window in while loop, blocks until window is closed
root.mainloop()