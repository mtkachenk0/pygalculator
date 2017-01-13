#! /usr/bin/python
# -*-coding: utf-8-*-

from Tkinter import END, Entry, Button, Tk
import math


class Calculator:
    div = '÷'.decode('utf-8')

    def __init__(self, master):
        master.title('Galculator')  # reference to linux galculator :D
        master.geometry()   # will grow dynamically depending on grid size;)
        self.e = Entry(master)
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.focus_set()  # Sets focus on the input text area

        self.expression = None

        # Generating Buttons
        Button(master, text="=", width=10, command=lambda: self.calculate()).grid(row=4, column=4, columnspan=2)
        Button(master, text='AC', width=3, command=lambda: self.purge()).grid(row=1, column=4)
        Button(master, text='C', width=3, command=lambda: self.remove_the_last()).grid(row=1, column=5)
        Button(master, text="+", width=3, command=lambda: self.append('+')).grid(row=4, column=3)
        Button(master, text="x", width=3, command=lambda: self.append('x')).grid(row=2, column=3)
        Button(master, text="-", width=3, command=lambda: self.append('-')).grid(row=3, column=3)
        Button(master, text="÷", width=3, command=lambda: self.append(self.div)).grid(row=1, column=3)
        Button(master, text="%", width=3, command=lambda: self.append('%')).grid(row=4, column=2)
        Button(master, text="7", width=3, command=lambda: self.append('7')).grid(row=1, column=0)
        Button(master, text="8", width=3, command=lambda: self.append(8)).grid(row=1, column=1)
        Button(master, text="9", width=3, command=lambda: self.append(9)).grid(row=1, column=2)
        Button(master, text="4", width=3, command=lambda: self.append(4)).grid(row=2, column=0)
        Button(master, text="5", width=3, command=lambda: self.append(5)).grid(row=2, column=1)
        Button(master, text="6", width=3, command=lambda: self.append(6)).grid(row=2, column=2)
        Button(master, text="1", width=3, command=lambda: self.append(1)).grid(row=3, column=0)
        Button(master, text="2", width=3, command=lambda: self.append(2)).grid(row=3, column=1)
        Button(master, text="3", width=3, command=lambda: self.append(3)).grid(row=3, column=2)
        Button(master, text="0", width=3, command=lambda: self.append(0)).grid(row=4, column=0)
        Button(master, text=".", width=3, command=lambda: self.append('.')).grid(row=4, column=1)
        Button(master, text="(", width=3, command=lambda: self.append('(')).grid(row=2, column=4)
        Button(master, text=")", width=3, command=lambda: self.append(')')).grid(row=2, column=5)
        Button(master, text="√", width=3, command=lambda: self.get_square_root()).grid(row=3, column=4)
        Button(master, text="x²", width=3, command=lambda: self.get_power()).grid(row=3, column=5)
        master.bind('<Return>', self._on_return_event)

    def append(self, arg):
        self.e.insert(END, arg)

    def mul_div_replace(self):
        self.expression = self.e.get().replace(self.div, '/').replace('x', '*')

    def calculate(self):
        self.mul_div_replace()
        try:
            value = eval(self.expression)
        except (SyntaxError, NameError):
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, value)

    def _on_return_event(self, event=None):
        return self.calculate()

    def get_square_root(self):
        self.mul_div_replace()
        try:
            value = eval(self.expression)  # evaluate the expression using the eval function
        except (SyntaxError, NameError):
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            sqrt_val = math.sqrt(value)
            self.e.delete(0, END)
            self.e.insert(0, sqrt_val)

    def get_power(self):
        self.mul_div_replace()
        try:
            value = eval(self.expression)  # evaluate the expression using the eval function
        except (SyntaxError, NameError):
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            power = math.pow(value, 2)
            self.e.delete(0, END)
            self.e.insert(0, int(power))

    def purge(self):
        self.e.delete(0, END)

    def remove_the_last(self):
        last_char = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, last_char)


if __name__ == '__main__':
    root = Tk()
    galculator = Calculator(root)
    root.mainloop()
