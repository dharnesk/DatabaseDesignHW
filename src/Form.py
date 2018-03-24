"""
Created by Samuel Buzas
Forms Parent Class
"""
from src.ApplicationUI import ApplicationUI
import tkinter as tk
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

    def none(self):
        """
        Documentation is my passion.
        """
        pass
