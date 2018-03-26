import tkinter as tk

LARGE_FONT = ("Verdana", 12)
#let me know if this code is useful, so far the configuration page pops
#up and lets you enter the server name
class ApplicationUI(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (ConfigurationPage, FormOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(ConfigurationPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def connect_to_sql_server(server_name):
    print(server_name)

class ConfigurationPage(tk.Frame): #Add more classes for more pages and then add them to the dictionary in the
                                    # Application UI class
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Configuration Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label2 = tk.Label(self, text="Server Name", font=LARGE_FONT)
        label2.pack(pady=5, padx=5)
        e = tk.Entry()
        e.pack()
        e.focus_set()
        button1 = tk.Button(self, text="Enter",
                            command=lambda: connect_to_sql_server(e.get()))
        button1.pack(pady=2, padx=2)


class FormOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Form", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


app = ApplicationUI()
app.mainloop()



