"""
By Samuel Buzas
Application UI
"""

import tkinter as tk
#From https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application
class ApplicationUI(tk.Frame):
    """
    Documentation is my passion
    """
    def __init__(self, *args, **kwargs):
        """
        Documentation is my passion
        """
        tk.Frame.__init__(self, *args, **kwargs)
        form1 = Form1(self)
        form2 = Form2(self)
        form3 = Form3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)


        form1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        form2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        form3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Form 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Form 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Form 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")


        self.create_window()

    def create_window(self):

        pass

    def destroy_window(self):

        pass


    def create_login(self):
        """
        Documentation is my passion
        """
        pass
    def on_button_pressed(self):
        """
        Documentation is my passion
        """
        pass

# From https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application
class Form(tk.Frame):
    """
    Documentation is my passion
    """
    def __init__(self, *args, **kwargs):
        """
        Documentation is my passion
        """
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        """
        Documentation is my passion
        """
        self.lift()
