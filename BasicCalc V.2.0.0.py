from tkinter import *   # This imports everything from tkinter
from tkinter.font import *   # This imports everything from tkinter.font

def main():
    root = Tk()
    root.title("BasicCalc. V.2.0.0")
    root.resizable(False, False)
    root.counter = 0

# The following code defines lFont, eFont & bFont which respectively are used for the label, entry and the buttons

    lFont = Font(family="Carrier New", size=20)
    eFont = Font(family="Carrier New", size=30)
    bFont = Font(family="Carrier New", size=20)

# The following code defines and draws the entry named "mainField" onto the grid, this is where the number inputs
# are shown while inputting and before being moved to the "secondaryField".
# mainField also displays the answer to the calculation that is displayed in the secondaryField

    mainField = Entry(root, width=18, font=eFont)
    mainField.grid(row=1, column=0, columnspan=4)
    secondaryField = Entry(root, width=18, font=lFont)
    secondaryField.grid(row=0, column=0, columnspan=4)

# The following code handles the logic functions of the calculator
    # This function takes the number the user clicks on the numpad and inserts it into mainField

    def numpad_click(number):
        currentEntry = mainField.get()
        mainField.delete(0, END)
        mainField.insert(0, str(currentEntry) + str(number))

    # This function first defines the global variable "operator" as whatever function the user has wished to perform
    # on the calculator, operator is used later. Then it defines the global variable "n1" which stands for "number 1"
    # it takes the number 1 from whatever is written on the mainField by numpad_click() and stores it in n1
    # the function then clears the mainField in preparation for the second number input
    # finally the n1 is inserted onto the secondaryField to be displayed for the user

    def div():
        root.counter = 0
        global operator
        operator = "div"
        global n1
        n1 = str(mainField.get())
        mainField.delete(0, END)
        secondaryField.delete(0, END)
        secondaryField.insert(END, str(n1)+ " /")


    # This function operates on the same principle as div()

    def mul():
        root.counter = 0
        global operator
        operator = "mul"
        global n1
        n1 = str(mainField.get())
        mainField.delete(0, END)
        secondaryField.delete(0, END)
        secondaryField.insert(END, str(n1)+ " *")

    # This function operates on the same principle as div()

    def sub():
        root.counter = 0
        global operator
        operator = "sub"
        global n1
        n1 = str(mainField.get())
        mainField.delete(0, END)
        secondaryField.delete(0, END)
        secondaryField.insert(END, str(n1) + " -")

    # This function operates on the same principle as div()

    def add():
        root.counter = 0
        global operator
        operator = "add"
        global n1
        n1 = str(mainField.get())
        mainField.delete(0, END)
        secondaryField.delete(0, END)
        secondaryField.insert(END, str(n1) + " +")

    # This function clears whatever input is currently on the mainField

    def clear():
        root.counter +=1
        mainField.delete(0, END)
        if root.counter == 2:
            secondaryField.delete(0, END)


    # This function defines n2 (number2) as whatever is currently written on the mainField, then deleting whatever is
    # written there. Then it inserts n2 into the secondaryField so that the user to display.
    # Then the function checks an if statement that relies on the global variable operator which is defined by either
    # div(), mul(), sub() or add() as either "div", "mul", "sub" or "add" respectively
    # depending on what the operator has been defined as the function inserts the correct logic into the mainField
    # to display the correct answer


    def equal():
        n2 = str(mainField.get())
        mainField.delete(0, END)
        secondaryField.insert(END, " " + str(n2))
        if operator == "div":
            mainField.insert(0, float(n1) / float(n2))
        elif operator == "mul":
            mainField.insert(0, float(n1) / float(n2))
        elif operator == "sub":
            mainField.insert(0, float(n1) / float(n2))
        elif operator == "add":
            mainField.insert(0, float(n1) / float(n2))


    # This function defines variable "string" as whatever is written in the mainField. After the string is defined,
    # the function removes the last character from the string, then the function simply deletes whatever was written
    # on the mainField and then it inserts the new shortened string onto the mainField


    def backspace():
        string = mainField.get()
        string = string[:-1]
        mainField.delete(0, END)
        mainField.insert(END, string)


# The following code is defining and drawing the calculator buttons onto a grid

    numpad0 = Button(root, bg="white", activebackground="#A9A9A9", text="0", font=bFont, padx=29, pady=15,
                     command=lambda: numpad_click(0))
    numpad0.grid(row=6, column=1)
    numpad1 = Button(root, bg="white", activebackground="#A9A9A9", text="1", font=bFont, padx=29, pady=15,
                     command=lambda: numpad_click(1))
    numpad1.grid(row=5, column=0)
    numpad2 = Button(root, bg="white", activebackground="#A9A9A9", text="2", font=bFont, padx=29, pady=15,
                     command=lambda: numpad_click(2))
    numpad2.grid(row=5, column=1)
    numpad3 = Button(root, bg="white", activebackground="#A9A9A9", text="3", font=bFont, padx=29, pady=15,
                     command=lambda: numpad_click(3))
    numpad3.grid(row=5, column=2)
    numpad4 = Button(root, bg="white", activebackground="#A9A9A9", text="4", font=bFont, padx=29, pady=15,
                     command=lambda: numpad_click(4))
    numpad4.grid(row=4, column=0)
    numpad5 = Button(root, bg="white", activebackground="#A9A9A9", text="5", font=bFont, padx=29, pady=15,
                     command=lambda: numpad_click(5))
    numpad5.grid(row=4, column=1)
    numpad6 = Button(root, bg="white", activebackground="#A9A9A9", text="6", font=bFont, padx=29, pady=15,
                     command=lambda: numpad_click(6))
    numpad6.grid(row=4, column=2)
    numpad7 = Button(root, bg="white", activebackground="#A9A9A9", text="7", font=bFont, padx=29, pady=15,
                     command=lambda: numpad_click(7))
    numpad7.grid(row=3, column=0)
    numpad8 = Button(root, bg="white", activebackground="#A9A9A9", text="8", font=bFont, padx=29, pady=15,
                     command=lambda: numpad_click(8))
    numpad8.grid(row=3, column=1)
    numpad9 = Button(root, bg="white", activebackground="#A9A9A9", text="9", font=bFont, padx=29, pady=15,
                     command=lambda: numpad_click(9))
    numpad9.grid(row=3, column=2)
    bDecimal = Button(root, bg="white", activebackground="#A9A9A9", text=".", font=bFont, padx=33, pady=15,
                      )
    bDecimal.grid(row=6, column=0)
    bBackspace = Button(root, bg="white", activebackground="#A9A9A9", text="<-", font=bFont, padx=24, pady=15,
                        command=backspace)
    bBackspace.grid(row=6, column=2)
    bDiv = Button(root, bg="#E1E1E1",  activebackground="#A9A9A9", text="/", font=bFont, padx=34, pady=15, command=div)
    bDiv.grid(row=3, column=3)
    bMul = Button(root, bg="#E1E1E1",  activebackground="#A9A9A9", text="X", font=bFont, padx=29, pady=15, command=mul)
    bMul.grid(row=4, column=3)
    bSub = Button(root, bg="#E1E1E1",  activebackground="#A9A9A9", text="-", font=bFont, padx=33, pady=15, command=sub)
    bSub.grid(row=5, column=3)
    bAdd = Button(root, bg="#E1E1E1",  activebackground="#A9A9A9", text="+", font=bFont, padx=30, pady=15, command=add)
    bAdd.grid(row=6, column=3)
    bClear = Button(root, bg="#CD6A6A", activebackground="#A33737", text="C", font=bFont, padx=79, pady=15,
                    command=clear)
    bClear.grid(row=2, column=0, columnspan=2)
    bEqual = Button(root, bg="#5CB0C6", activebackground="#258199", text="=", font=bFont, padx=79, pady=15,
                    command=equal)
    bEqual.grid(row=2, column=2, columnspan=2)

    root.mainloop()   # This is looping the root until the user closes the window

main()

# Version: 2.0.0
# Author of BasicCalc: Stetussa
# www.github.com/Stetussa/Basic-Calc-Public
# Thanks for downloading and using BasicCalc!
