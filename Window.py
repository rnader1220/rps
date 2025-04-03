
import tkinter as tk
import random

class Window:

    def __init__ (self):
        self.window = tk.Tk()
        self.window.geometry("800x400")
        self.window.title("Mr. Nader RPS")
        self.replay_resp = tk.IntVar()
        self.name_entry = tk.StringVar()
        self.elements = {}

    def loop(self):
        self.window.mainloop()

    def wait(self, varname):
        self.window.waitvar(varname)

    def addImage(self, image, caption, row, col, width=1):
        key = random.random()
        element = tk.Label(self.window, text=caption, image=image, compound='top')
        element.grid(row = row, column = col, columnspan=width, padx=20, pady=10)
        self.elements[key] = element
        return key

    def addLabel(self, content, row, col, width=1) :
        key = random.random()
        element = tk.Label(self.window, text=content)
        element.grid(row = row, column = col, columnspan=width, padx=20, pady=10)
        self.elements[key] = element
        return key

    # just in case I can differentiate later
    def addText(self, content, row, col, width=1):
        key = random.random()
        element = tk.Label(self.window, text=content)
        element.grid(row = row, column = col, columnspan=width, padx=20, pady=10)
        self.elements[key] = element
        return key

    def addTextInput(self, textvariable, row, col, width=1) :
        key = random.random()
        element = tk.Entry(self.window, textvariable=textvariable)
        element.grid(row = row, column = col, columnspan=width, padx=20, pady=10)
        self.elements[key] = element
        return key
    
    def addSubmit(self, caption, command, row, col, width=1) :
        key = random.random()
        element = tk.Button(self.window, text=caption, command=command)
        element.grid(row = row, column = col, columnspan=width, padx=20, pady=10)
        self.elements[key] = element
        return key
    
    def addRadio(self, caption, variable, value, command, row, col, width=1, image=None) :
        key = random.random()
        element = tk.Radiobutton( \
            self.window, \
            variable=variable, \
            value=value, \
            text=caption, \
            image=image, \
            compound='top', \
            indicatoron=False, \
            command=command)
        element.grid(column=col, row=row, padx=20, pady=10)
        self.elements[key] = element
        return key

    def getVariable(self, type) :
        match type.lower():
            case 'string':
                return tk.StringVar()
            case 'int':
                return tk.IntVar()

    def kill(self, key):
        element = self.elements.pop(key)
        element.destroy()        
    